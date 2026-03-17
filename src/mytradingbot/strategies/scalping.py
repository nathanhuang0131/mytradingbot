"""Scalping strategy implementation."""

from __future__ import annotations

import logging

from mytradingbot.core.models import ExitPlan, SignalBundle, StrategyDecision
from mytradingbot.strategies.base import BaseStrategy

logger = logging.getLogger(__name__)


class ScalpingStrategy(BaseStrategy):
    """Scalping strategy with modular qlib and microstructure filters."""

    name = "scalping"

    predicted_return_threshold = 0.005
    confidence_threshold = 0.6
    max_spread_bps = 5.0
    min_liquidity_score = 0.5
    max_liquidity_stress = 0.7
    flatten_near_close_minutes = 10
    timeout_seconds = 900

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

        quantity = self._adaptive_quantity(signal)
        intent = self._intent_from_signal(
            signal,
            quantity=quantity,
            metadata={
                "adaptive_target_size": quantity,
                "flatten_near_close": True,
                "timeout_seconds": self.timeout_seconds,
            },
        )
        intent.exit_plan = self._build_exit_plan(signal)
        passed_filters.extend(
            ["adaptive_target_sizing", "take_profit", "stop_loss", "timeout_exit"]
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
        if signal.metadata.get("cooldown_active", False):
            failed_filters.append("cooldown_logic")
        else:
            passed_filters.append("cooldown_logic")

        if int(signal.metadata.get("minutes_to_close", 999)) <= self.flatten_near_close_minutes:
            failed_filters.append("flatten_near_close_logic")
        else:
            passed_filters.append("flatten_near_close_logic")

    def _adaptive_quantity(self, signal: SignalBundle) -> int:
        raw_size = (
            abs(signal.prediction.predicted_return)
            * 1000
            * signal.prediction.confidence
            * signal.market.liquidity_score
        )
        return max(1, min(10, int(round(raw_size))))

    def _build_exit_plan(self, signal: SignalBundle) -> ExitPlan:
        entry = signal.market.last_price
        take_profit_delta = max(0.003, min(0.02, abs(signal.prediction.predicted_return) * 0.75))
        stop_loss_delta = max(0.002, take_profit_delta / 2)
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
