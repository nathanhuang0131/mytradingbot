"""Scalping strategy implementation."""

from __future__ import annotations

import logging

from mytradingbot.core.models import BracketPlan, ExitPlan, SignalBundle, StrategyDecision
from mytradingbot.core.settings import AppSettings
from mytradingbot.strategies.base import BaseStrategy

logger = logging.getLogger(__name__)


class ScalpingStrategy(BaseStrategy):
    """Scalping strategy with modular qlib and microstructure filters."""

    name = "scalping"

    max_spread_bps = 5.0
    min_liquidity_score = 0.5
    max_liquidity_stress = 0.7
    flatten_near_close_minutes = 10
    timeout_seconds = 900

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()
        self.predicted_return_threshold = self.settings.scalping.predicted_return_threshold
        self.confidence_threshold = self.settings.scalping.confidence_threshold
        self.timeout_seconds = self.settings.scalping.max_holding_seconds

    def evaluate(self, signal: SignalBundle) -> StrategyDecision:
        passed_filters: list[str] = []
        failed_filters: list[str] = []

        self._apply_qlib_signal_gate(signal, passed_filters, failed_filters)
        self._check_thresholds(signal, passed_filters, failed_filters)
        self._check_market_structure(signal, passed_filters, failed_filters)
        self._check_session_logic(signal, passed_filters, failed_filters)

        if failed_filters:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason=failed_filters[0],
                failed_filters=failed_filters,
                passed_filters=passed_filters,
            )

        bracket_plan = self._build_bracket_plan(signal)
        if bracket_plan is None:
            return StrategyDecision.reject(
                strategy_name=self.name,
                symbol=signal.symbol,
                reason="fee_adjusted_expectancy",
                failed_filters=["fee_adjusted_expectancy"],
                passed_filters=passed_filters,
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

    def _check_market_structure(
        self,
        signal: SignalBundle,
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

        if (is_long and signal.market.order_book_imbalance < 0) or (
            not is_long and signal.market.order_book_imbalance > 0
        ):
            failed_filters.append("order_book_imbalance")
        else:
            passed_filters.append("order_book_imbalance")

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

        if int(signal.metadata.get("minutes_to_close", 999)) <= self.flatten_near_close_minutes:
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
        return max(0.0, min(raw_signal_size, risk_budget_size, notional_cap_size, liquidity_cap_size))

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
        volatility_multiplier = {"low": 0.8, "normal": 1.0, "high": 1.2}[signal.market.volatility_regime]
        base_take_profit = max(0.003, min(0.02, abs(signal.prediction.predicted_return) * 0.75))
        base_stop_loss = max(
            self.settings.scalping.stop_loss_buffer_bps / 10_000,
            (signal.market.spread_bps / 10_000) * 2,
            base_take_profit / self.settings.scalping.take_profit_multiplier,
        )
        return base_take_profit * volatility_multiplier, base_stop_loss * volatility_multiplier
