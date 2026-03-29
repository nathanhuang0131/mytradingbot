"""Scalping strategy implementation."""

from __future__ import annotations

import logging
import math

from mytradingbot.core.models import (
    BracketPlan,
    CandidateCostEstimate,
    CandidateQualitySnapshot,
    ExitPlan,
    HigherTimeframeTrend,
    MicrostructureProxySignal,
    SignalBundle,
    StrategyDecision,
)
from mytradingbot.core.settings import AppSettings
from mytradingbot.signals.microstructure import microstructure_relation_for_direction
from mytradingbot.strategies.base import BaseStrategy

logger = logging.getLogger(__name__)

# The quality score intentionally favors edge-after-cost and signal quality over raw
# throughput. These weights are deterministic so the operator can compare runs
# cleanly, and they avoid double-counting qlib raw score because the current adapter
# already maps predicted_return directly from score.
PREDICTED_RETURN_WEIGHT = 0.17
CONFIDENCE_WEIGHT = 0.12
EDGE_AFTER_COST_WEIGHT = 0.30
SPREAD_QUALITY_WEIGHT = 0.08
LIQUIDITY_WEIGHT = 0.10
TREND_ALIGNMENT_WEIGHT = 0.10
MICROSTRUCTURE_WEIGHT = 0.08
REWARD_RISK_WEIGHT = 0.05


class ScalpingStrategy(BaseStrategy):
    """Scalping strategy with modular qlib and microstructure filters."""

    name = "scalping"

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()
        self.predicted_return_threshold = self.settings.scalping.predicted_return_threshold
        self.confidence_threshold = self.settings.scalping.confidence_threshold
        self.edge_after_cost_min_buffer = self.settings.scalping.edge_after_cost_min_buffer
        self.max_spread_bps = self.settings.scalping.max_spread_bps
        self.min_liquidity_score = self.settings.scalping.min_liquidity_score
        self.max_liquidity_stress = self.settings.scalping.max_liquidity_stress
        self.flatten_near_close_minutes = self.settings.scalping.flatten_near_close_minutes
        self.higher_timeframe_filter_enabled = (
            self.settings.scalping.higher_timeframe_filter_enabled
        )
        self.pseudo_order_book_gate_enabled = self.settings.scalping.enable_pseudo_order_book_gate
        self.microstructure_proxy_mode = self.settings.scalping.microstructure_proxy_mode
        self.microstructure_proxy_min_alignment_score = (
            self.settings.scalping.microstructure_proxy_min_alignment_score
        )
        self.timeout_seconds = self.settings.scalping.max_holding_seconds

    def evaluate(self, signal: SignalBundle) -> StrategyDecision:
        passed_filters: list[str] = []
        failed_filters: list[str] = []

        self._validate_signal_payload(signal, failed_filters)
        if failed_filters:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason=failed_filters[0],
                failed_filters=failed_filters,
                passed_filters=passed_filters,
            )

        trend = self._resolve_higher_timeframe_trend(signal)
        cost_estimate = self._estimate_candidate_cost(signal)
        microstructure = self._resolve_microstructure_proxy(signal)
        quality = self._build_quality_snapshot(
            signal,
            trend=trend,
            microstructure=microstructure,
            cost_estimate=cost_estimate,
            bracket_plan=None,
        )

        self._apply_qlib_signal_gate(signal, passed_filters, failed_filters)
        self._check_thresholds(signal, cost_estimate, passed_filters, failed_filters)
        self._check_market_structure(
            signal,
            trend,
            microstructure,
            passed_filters,
            failed_filters,
        )
        self._check_session_logic(signal, passed_filters, failed_filters)

        if failed_filters:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason=failed_filters[0],
                failed_filters=failed_filters,
                passed_filters=passed_filters,
                quality=quality.model_copy(update={"top_n_eligible": False}),
            )

        bracket_plan = self._build_bracket_plan(signal)
        quality = self._build_quality_snapshot(
            signal,
            trend=trend,
            microstructure=microstructure,
            cost_estimate=cost_estimate,
            bracket_plan=bracket_plan,
        )
        if bracket_plan is None:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason="fee_adjusted_expectancy",
                failed_filters=["fee_adjusted_expectancy"],
                passed_filters=passed_filters,
                quality=quality.model_copy(update={"top_n_eligible": False}),
            )

        intent = self._intent_from_signal(
            signal,
            quantity=bracket_plan.planned_quantity,
            metadata={
                "adaptive_target_size": bracket_plan.planned_quantity,
                "flatten_near_close": True,
                "timeout_seconds": self.timeout_seconds,
            },
        )
        intent.exit_plan = self._build_exit_plan(signal)
        intent.bracket_plan = bracket_plan
        passed_filters.extend(
            [
                "adaptive_target_sizing",
                "take_profit",
                "stop_loss",
                "timeout_exit",
                "fee_adjusted_expectancy",
                "bracket_plan_valid",
            ]
        )

        return StrategyDecision.approve(
            strategy_name=self.name,
            symbol=signal.symbol,
            intent=intent,
            passed_filters=passed_filters,
            quality=quality.model_copy(update={"top_n_eligible": True}),
        )

    def _apply_qlib_signal_gate(
        self,
        signal: SignalBundle,
        passed_filters: list[str],
        failed_filters: list[str],
    ) -> None:
        direction = signal.prediction.direction
        predicted_return = signal.prediction.predicted_return
        if (direction == "long" and predicted_return <= 0) or (
            direction == "short" and predicted_return >= 0
        ):
            failed_filters.append("qlib_signal_gating")
            return
        passed_filters.append("qlib_signal_gating")

    def _check_thresholds(
        self,
        signal: SignalBundle,
        cost_estimate: CandidateCostEstimate,
        passed_filters: list[str],
        failed_filters: list[str],
    ) -> None:
        if abs(signal.prediction.predicted_return) < self.predicted_return_threshold:
            failed_filters.append("predicted_return_threshold")
        else:
            passed_filters.append("predicted_return_threshold")

        if signal.prediction.confidence < self.confidence_threshold:
            failed_filters.append("confidence_threshold")
        else:
            passed_filters.append("confidence_threshold")

        if cost_estimate.expected_edge_after_cost < self.edge_after_cost_min_buffer:
            failed_filters.append("edge_after_cost_buffer")
        else:
            passed_filters.append("edge_after_cost_buffer")

    def _check_market_structure(
        self,
        signal: SignalBundle,
        trend: HigherTimeframeTrend,
        microstructure: MicrostructureProxySignal,
        passed_filters: list[str],
        failed_filters: list[str],
    ) -> None:
        is_long = signal.prediction.direction == "long"
        if (is_long and signal.market.last_price < signal.market.vwap) or (
            not is_long and signal.market.last_price > signal.market.vwap
        ):
            failed_filters.append("vwap_relationship")
        else:
            passed_filters.append("vwap_relationship")

        if self.higher_timeframe_filter_enabled:
            aligned = trend.long_allowed if is_long else trend.short_allowed
            if not aligned:
                failed_filters.append("higher_timeframe_trend_alignment")
            else:
                passed_filters.append("higher_timeframe_trend_alignment")
        else:
            passed_filters.append("higher_timeframe_trend_filter_disabled")

        alignment_score, relation = microstructure_relation_for_direction(
            microstructure,
            signal.prediction.direction,
        )
        if self.microstructure_proxy_mode == "confirmation_gate":
            if relation in {"unavailable", "neutral"}:
                passed_filters.append("microstructure_proxy_unavailable")
            elif alignment_score < self.microstructure_proxy_min_alignment_score:
                failed_filters.append("microstructure_proxy_alignment")
            else:
                passed_filters.append("microstructure_proxy_alignment")
        elif self.microstructure_proxy_mode == "soft_rank":
            passed_filters.append("microstructure_proxy_soft_rank")
        else:
            passed_filters.append("microstructure_proxy_off")

        if signal.market.spread_bps > self.max_spread_bps:
            failed_filters.append("spread_filter")
        else:
            passed_filters.append("spread_filter")

        if signal.market.liquidity_score < self.min_liquidity_score:
            failed_filters.append("liquidity_filter")
        else:
            passed_filters.append("liquidity_filter")

        if signal.market.liquidity_stress > self.max_liquidity_stress:
            failed_filters.append("liquidity_stress_filter")
        else:
            passed_filters.append("liquidity_stress_filter")

        if self.pseudo_order_book_gate_enabled:
            imbalance = signal.market.order_book_imbalance
            if (is_long and imbalance < 0) or (not is_long and imbalance > 0):
                failed_filters.append("pseudo_order_book_pressure_alignment")
            else:
                passed_filters.append("pseudo_order_book_pressure_alignment")
        else:
            passed_filters.append("pseudo_order_book_gate_disabled")

        if signal.market.liquidity_sweep_detected:
            failed_filters.append("liquidity_sweep_detection")
        else:
            passed_filters.append("liquidity_sweep_detection")

        if signal.market.volatility_regime == "high":
            failed_filters.append("intraday_volatility_regime")
        else:
            passed_filters.append("intraday_volatility_regime")

    def _check_session_logic(
        self,
        signal: SignalBundle,
        passed_filters: list[str],
        failed_filters: list[str],
    ) -> None:
        if signal.metadata.get("position_exists", False):
            failed_filters.append("duplicate_position")
        else:
            passed_filters.append("duplicate_position")

        if signal.metadata.get("cooldown_active", False):
            failed_filters.append("cooldown_logic")
        else:
            passed_filters.append("cooldown_logic")

        minutes_to_close = int(signal.metadata.get("minutes_to_close", 999))
        if minutes_to_close <= self.flatten_near_close_minutes:
            failed_filters.append("flatten_near_close_logic")
        else:
            passed_filters.append("flatten_near_close_logic")

    def _adaptive_quantity(self, signal: SignalBundle, *, risk_per_share: float) -> float:
        raw_signal_size = (
            abs(signal.prediction.predicted_return)
            * 1000
            * signal.prediction.confidence
            * signal.market.liquidity_score
        )
        risk_budget_size = (
            self.settings.scalping.risk_budget_per_trade / risk_per_share
            if risk_per_share > 0
            else 0.0
        )
        notional_cap_size = self.settings.scalping.max_position_notional / signal.market.last_price
        liquidity_cap_size = max(1.0, signal.market.volume * 0.00002)
        return max(
            0.0,
            min(raw_signal_size, risk_budget_size, notional_cap_size, liquidity_cap_size),
        )

    def _build_exit_plan(self, signal: SignalBundle) -> ExitPlan:
        entry = signal.market.last_price
        take_profit_delta, stop_loss_delta = self._target_deltas(signal)
        if signal.prediction.direction == "long":
            take_profit = entry * (1 + take_profit_delta)
            stop_loss = entry * (1 - stop_loss_delta)
        else:
            take_profit = entry * (1 - take_profit_delta)
            stop_loss = entry * (1 + stop_loss_delta)

        return ExitPlan(
            take_profit=round(take_profit, 4),
            stop_loss=round(stop_loss, 4),
            timeout_seconds=self.timeout_seconds,
            flatten_near_close=True,
        )

    def _build_bracket_plan(self, signal: SignalBundle) -> BracketPlan | None:
        entry = signal.market.last_price
        take_profit_delta, stop_loss_delta = self._target_deltas(signal)
        is_long = signal.prediction.direction == "long"

        if is_long:
            take_profit = entry * (1 + take_profit_delta)
            stop_loss = entry * (1 - stop_loss_delta)
        else:
            take_profit = entry * (1 - take_profit_delta)
            stop_loss = entry * (1 + stop_loss_delta)

        risk_per_share = abs(entry - stop_loss)
        gross_reward_per_share = abs(take_profit - entry)
        if risk_per_share <= 0 or gross_reward_per_share <= 0:
            return None

        planned_quantity = self._adaptive_quantity(signal, risk_per_share=risk_per_share)
        if planned_quantity < 1:
            return None

        estimated_fee_per_share = self.settings.scalping.estimated_fee_per_share
        estimated_slippage_per_share = (
            entry * self.settings.scalping.estimated_slippage_bps / 10_000
        )
        base_plan = BracketPlan(
            planned_entry_price=round(entry, 4),
            planned_stop_loss_price=round(stop_loss, 4),
            planned_take_profit_price=round(take_profit, 4),
            planned_quantity=planned_quantity,
            risk_per_share=risk_per_share,
            gross_reward_per_share=gross_reward_per_share,
            estimated_fees=0.0,
            estimated_slippage=0.0,
            estimated_fee_per_share=estimated_fee_per_share,
            estimated_slippage_per_share=estimated_slippage_per_share,
            estimated_fixed_fees=self.settings.scalping.estimated_fixed_fees,
            net_reward_per_share=0.0,
            reward_risk_ratio=0.0,
            expected_net_profit=0.0,
            time_in_force="day",
            exit_reason_metadata={
                "take_profit": "take_profit",
                "stop_loss": "stop_loss",
                "near_close_flatten": "near_close_flatten",
                "timeout": "timeout_exit",
            },
        ).with_quantity(planned_quantity)

        if base_plan.net_reward_per_share < self.settings.scalping.minimum_net_reward_per_share:
            return None
        if base_plan.reward_risk_ratio < self.settings.scalping.minimum_reward_risk_ratio:
            return None
        if base_plan.expected_net_profit <= 0:
            return None

        return base_plan

    def _target_deltas(self, signal: SignalBundle) -> tuple[float, float]:
        volatility_multiplier = {"low": 0.8, "normal": 1.0, "high": 1.2}[
            signal.market.volatility_regime
        ]
        base_take_profit = max(
            0.003,
            min(0.02, abs(signal.prediction.predicted_return) * 0.75),
        )
        base_stop_loss = max(
            self.settings.scalping.stop_loss_buffer_bps / 10_000,
            (signal.market.spread_bps / 10_000) * 2,
            base_take_profit / self.settings.scalping.take_profit_multiplier,
        )
        return (
            base_take_profit * volatility_multiplier,
            base_stop_loss * volatility_multiplier,
        )

    def _validate_signal_payload(
        self,
        signal: SignalBundle,
        failed_filters: list[str],
    ) -> None:
        if not self._is_positive_number(signal.market.last_price):
            failed_filters.append("invalid_signal_payload:last_price_unavailable")
        if not self._is_positive_number(signal.market.vwap):
            failed_filters.append("invalid_signal_payload:vwap_unavailable")
        if not self._is_non_negative_number(signal.market.spread_bps):
            failed_filters.append("invalid_signal_payload:spread_proxy_invalid")
        if not self._is_non_negative_number(signal.market.liquidity_score):
            failed_filters.append("invalid_signal_payload:liquidity_score_invalid")
        if not self._is_non_negative_number(signal.market.liquidity_stress):
            failed_filters.append("invalid_signal_payload:liquidity_stress_invalid")

        normalized_minutes_to_close = self._normalize_minutes_to_close(
            signal.metadata.get("minutes_to_close")
        )
        if normalized_minutes_to_close is None:
            failed_filters.append("invalid_signal_payload:minutes_to_close_invalid")
        else:
            signal.metadata["minutes_to_close"] = normalized_minutes_to_close

    def _resolve_higher_timeframe_trend(self, signal: SignalBundle) -> HigherTimeframeTrend:
        raw_trend = signal.metadata.get("higher_timeframe_trend") or signal.market.higher_timeframe_trend
        if isinstance(raw_trend, HigherTimeframeTrend):
            return raw_trend
        if isinstance(raw_trend, dict):
            return HigherTimeframeTrend.model_validate(raw_trend)
        return HigherTimeframeTrend(
            source_timeframe=self.settings.scalping.higher_timeframe_source_timeframe,
            fast_ma_length=self.settings.scalping.higher_timeframe_fast_ma_length,
            slow_ma_length=self.settings.scalping.higher_timeframe_slow_ma_length,
            state="unavailable",
            long_allowed=False,
            short_allowed=False,
            reason="higher_timeframe_trend_missing",
        )

    @staticmethod
    def _resolve_microstructure_proxy(signal: SignalBundle) -> MicrostructureProxySignal:
        raw_proxy = signal.metadata.get("microstructure_proxy") or signal.market.microstructure_proxy
        if isinstance(raw_proxy, MicrostructureProxySignal):
            return raw_proxy
        if isinstance(raw_proxy, dict):
            return MicrostructureProxySignal.model_validate(raw_proxy)
        return MicrostructureProxySignal(
            state="unavailable",
            score=0.0,
            directional_pressure=0.0,
            relative_volume=0.0,
            range_expansion=0.0,
            vwap_bias=0.0,
            wick_bias=0.0,
            persistence=0.0,
            reason="microstructure_proxy_missing",
        )

    def _estimate_candidate_cost(self, signal: SignalBundle) -> CandidateCostEstimate:
        price = max(signal.market.last_price, 0.01)
        gross_predicted_return = abs(signal.prediction.predicted_return)
        estimated_spread_cost = signal.market.spread_bps / 10_000
        estimated_slippage_cost = self.settings.scalping.estimated_slippage_bps / 10_000
        estimated_fee_cost = self.settings.scalping.estimated_fee_per_share / price
        regulatory_per_share = (
            (self.settings.broker_fees.sec_sell_rate_per_dollar * price)
            + self.settings.broker_fees.taf_sell_per_share
            + self.settings.broker_fees.cat_per_share
        )
        estimated_regulatory_fee_cost = regulatory_per_share / price
        estimated_total_cost = (
            estimated_spread_cost
            + estimated_slippage_cost
            + estimated_fee_cost
            + estimated_regulatory_fee_cost
        )
        return CandidateCostEstimate(
            gross_predicted_return=gross_predicted_return,
            estimated_spread_cost=estimated_spread_cost,
            estimated_slippage_cost=estimated_slippage_cost,
            estimated_fee_cost=estimated_fee_cost,
            estimated_regulatory_fee_cost=estimated_regulatory_fee_cost,
            estimated_total_cost=estimated_total_cost,
            expected_edge_after_cost=gross_predicted_return - estimated_total_cost,
        )

    def _build_quality_snapshot(
        self,
        signal: SignalBundle,
        *,
        trend: HigherTimeframeTrend,
        microstructure: MicrostructureProxySignal,
        cost_estimate: CandidateCostEstimate,
        bracket_plan: BracketPlan | None,
    ) -> CandidateQualitySnapshot:
        predicted_return_component = min(
            1.0,
            abs(signal.prediction.predicted_return)
            / max(self.predicted_return_threshold * 4, 0.001),
        )
        confidence_component = max(0.0, min(1.0, signal.prediction.confidence))
        edge_component = min(
            1.0,
            max(cost_estimate.expected_edge_after_cost, 0.0)
            / max(self.edge_after_cost_min_buffer * 4, 0.001),
        )
        spread_quality_component = max(
            0.0,
            1.0 - (signal.market.spread_bps / max(self.max_spread_bps, 0.01)),
        )
        liquidity_component = max(0.0, min(1.0, signal.market.liquidity_score))
        direction = signal.prediction.direction
        if not self.higher_timeframe_filter_enabled:
            trend_component = 1.0
        elif direction == "long":
            trend_component = 1.0 if trend.long_allowed else 0.0
        else:
            trend_component = 1.0 if trend.short_allowed else 0.0
        alignment_score, relation = microstructure_relation_for_direction(
            microstructure,
            direction,
        )
        if relation == "unavailable":
            microstructure_component = 0.5
        else:
            microstructure_component = max(0.0, min(1.0, (alignment_score + 1.0) / 2))
        reward_risk_ratio = bracket_plan.reward_risk_ratio if bracket_plan is not None else None
        reward_risk_component = 0.0
        if reward_risk_ratio is not None and self.settings.scalping.minimum_reward_risk_ratio > 0:
            reward_risk_component = min(
                1.0,
                reward_risk_ratio / (self.settings.scalping.minimum_reward_risk_ratio * 2),
            )
        quality_score = (
            (predicted_return_component * PREDICTED_RETURN_WEIGHT)
            + (confidence_component * CONFIDENCE_WEIGHT)
            + (edge_component * EDGE_AFTER_COST_WEIGHT)
            + (spread_quality_component * SPREAD_QUALITY_WEIGHT)
            + (liquidity_component * LIQUIDITY_WEIGHT)
            + (trend_component * TREND_ALIGNMENT_WEIGHT)
            + (microstructure_component * MICROSTRUCTURE_WEIGHT)
            + (reward_risk_component * REWARD_RISK_WEIGHT)
        )
        return CandidateQualitySnapshot(
            quality_score=quality_score,
            expected_edge_after_cost=cost_estimate.expected_edge_after_cost,
            cost_estimate=cost_estimate,
            trend=trend,
            microstructure=microstructure,
            microstructure_relation=relation,
            predicted_return_component=predicted_return_component,
            confidence_component=confidence_component,
            edge_component=edge_component,
            spread_quality_component=spread_quality_component,
            liquidity_component=liquidity_component,
            trend_component=trend_component,
            microstructure_component=microstructure_component,
            reward_risk_component=reward_risk_component,
            reward_risk_ratio=reward_risk_ratio,
            expected_net_profit=(
                bracket_plan.expected_net_profit if bracket_plan is not None else None
            ),
        )

    @staticmethod
    def _is_positive_number(value: float | int) -> bool:
        try:
            numeric = float(value)
        except (TypeError, ValueError):
            return False
        return math.isfinite(numeric) and numeric > 0

    @staticmethod
    def _is_non_negative_number(value: float | int) -> bool:
        try:
            numeric = float(value)
        except (TypeError, ValueError):
            return False
        return math.isfinite(numeric) and numeric >= 0

    @staticmethod
    def _normalize_minutes_to_close(value: object) -> int | None:
        if value is None:
            return 999
        if isinstance(value, bool):
            return None
        if isinstance(value, (int, float)):
            numeric = float(value)
            if not math.isfinite(numeric) or numeric < 0:
                return None
            return int(numeric)
        if isinstance(value, str):
            stripped = value.strip()
            if not stripped:
                return None
            try:
                numeric = float(stripped)
            except ValueError:
                return None
            if not math.isfinite(numeric) or numeric < 0:
                return None
            return int(numeric)
        return None
