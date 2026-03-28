"""Helpers for applying resolved wizard configs to runtime execution."""

from __future__ import annotations

from mytradingbot.core.settings import AppSettings
from mytradingbot.core.models import QlibPrediction
from mytradingbot.session_setup.models import ResolvedSessionConfig


def apply_resolved_config_to_settings(
    settings: AppSettings,
    config: ResolvedSessionConfig,
) -> AppSettings:
    resolved = settings.model_copy(deep=True)
    resolved.broker.broker_mode = config.strategy.broker_mode
    resolved.runtime_safety.auto_refresh_inputs_in_loop = (
        config.refresh.auto_refresh_market_snapshot
        or config.refresh.auto_refresh_predictions
        or config.refresh.auto_refresh_dataset
    )
    resolved.runtime_safety.market_refresh_interval_seconds = (
        config.refresh.market_refresh_interval_seconds
    )
    resolved.runtime_safety.prediction_refresh_interval_seconds = (
        config.refresh.prediction_refresh_interval_seconds
    )
    resolved.runtime_safety.dataset_refresh_interval_seconds = (
        config.refresh.dataset_refresh_interval_seconds
    )
    resolved.freshness.market_snapshot_max_age_minutes = (
        config.refresh.market_snapshot_max_age_minutes
    )
    resolved.freshness.predictions_max_age_minutes = (
        config.refresh.predictions_max_age_minutes
    )
    resolved.scalping.max_position_notional = config.risk.max_dollars_per_trade
    resolved.scalping.predicted_return_threshold = config.alpha.predicted_return_threshold
    resolved.scalping.confidence_threshold = config.alpha.confidence_threshold
    resolved.scalping.top_n_per_cycle = config.alpha.top_n_per_cycle
    resolved.scalping.edge_after_cost_min_buffer = config.alpha.edge_after_cost_min_buffer
    resolved.scalping.cooldown_minutes = config.risk.cooldown_minutes
    resolved.scalping.higher_timeframe_filter_enabled = config.risk.higher_timeframe_filter_enabled
    resolved.scalping.higher_timeframe_source_timeframe = (
        config.risk.higher_timeframe_source_timeframe
    )
    resolved.scalping.higher_timeframe_fast_ma_length = (
        config.risk.higher_timeframe_fast_ma_length
    )
    resolved.scalping.higher_timeframe_slow_ma_length = (
        config.risk.higher_timeframe_slow_ma_length
    )
    resolved.scalping.enable_pseudo_order_book_gate = not config.risk.disable_pseudo_order_book_gate
    resolved.scalping.stop_loss_buffer_bps = config.execution.stop_loss_percent * 100
    return resolved


def filter_predictions_for_config(
    predictions: list[QlibPrediction],
    config: ResolvedSessionConfig,
) -> list[QlibPrediction]:
    side_mode = config.alpha.side_mode
    long_threshold = max(0.0, config.alpha.long_threshold)
    short_threshold = max(0.0, config.alpha.short_threshold)
    filtered: list[QlibPrediction] = []
    for prediction in predictions:
        if side_mode == "long_only" and prediction.direction != "long":
            continue
        if side_mode == "short_only" and prediction.direction != "short":
            continue
        if prediction.direction == "long" and prediction.predicted_return < long_threshold:
            continue
        if prediction.direction == "short" and abs(prediction.predicted_return) < short_threshold:
            continue
        filtered.append(prediction)
    if config.alpha.candidate_count > 0:
        return filtered[: config.alpha.candidate_count]
    return filtered
