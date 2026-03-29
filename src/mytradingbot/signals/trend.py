"""Higher-timeframe trend helpers for directional confirmation."""

from __future__ import annotations

import math

import pandas as pd

from mytradingbot.core.models import HigherTimeframeTrend


def build_higher_timeframe_trend(
    frame: pd.DataFrame,
    *,
    source_timeframe: str,
    fast_ma_length: int,
    slow_ma_length: int,
) -> HigherTimeframeTrend:
    """Build a simple directional trend state from higher-timeframe bars."""

    if frame.empty or len(frame.index) < max(fast_ma_length, slow_ma_length):
        return HigherTimeframeTrend(
            source_timeframe=source_timeframe,
            fast_ma_length=fast_ma_length,
            slow_ma_length=slow_ma_length,
            state="unavailable",
            long_allowed=False,
            short_allowed=False,
            reason="insufficient_history",
        )

    ordered = frame.sort_values("timestamp").reset_index(drop=True).copy()
    ordered["close"] = pd.to_numeric(ordered["close"], errors="coerce")
    ordered["vwap"] = pd.to_numeric(ordered["vwap"], errors="coerce")
    ordered = ordered.dropna(subset=["close", "vwap"])
    if ordered.empty or len(ordered.index) < max(fast_ma_length, slow_ma_length):
        return HigherTimeframeTrend(
            source_timeframe=source_timeframe,
            fast_ma_length=fast_ma_length,
            slow_ma_length=slow_ma_length,
            state="unavailable",
            long_allowed=False,
            short_allowed=False,
            reason="invalid_higher_timeframe_payload",
        )

    close_series = ordered["close"]
    vwap_series = ordered["vwap"]
    fast_ema = close_series.ewm(span=fast_ma_length, adjust=False).mean()
    slow_ema = close_series.ewm(span=slow_ma_length, adjust=False).mean()
    latest_close = float(close_series.iloc[-1])
    latest_vwap = float(vwap_series.iloc[-1])
    latest_fast = float(fast_ema.iloc[-1])
    latest_slow = float(slow_ema.iloc[-1])
    prior_slow = float(slow_ema.iloc[-2]) if len(slow_ema.index) >= 2 else latest_slow
    slow_slope_bps = 0.0
    if prior_slow > 0 and math.isfinite(prior_slow):
        slow_slope_bps = ((latest_slow - prior_slow) / prior_slow) * 10_000

    above_vwap = latest_close >= latest_vwap
    below_vwap = latest_close <= latest_vwap
    fast_above_slow = latest_fast >= latest_slow
    fast_below_slow = latest_fast <= latest_slow
    slope_up = slow_slope_bps >= 0
    slope_down = slow_slope_bps <= 0

    bullish = above_vwap and fast_above_slow and slope_up
    bearish = below_vwap and fast_below_slow and slope_down
    if bullish:
        state = "bullish"
        reason = "close_above_vwap_and_fast_above_slow"
    elif bearish:
        state = "bearish"
        reason = "close_below_vwap_and_fast_below_slow"
    else:
        state = "neutral"
        failure_parts: list[str] = []
        if not above_vwap and not below_vwap:
            failure_parts.append("close_equals_vwap")
        elif latest_close < latest_vwap:
            failure_parts.append("close_below_vwap")
        elif latest_close > latest_vwap:
            failure_parts.append("close_above_vwap")
        if latest_fast < latest_slow:
            failure_parts.append("fast_below_slow")
        elif latest_fast > latest_slow:
            failure_parts.append("fast_above_slow")
        if slow_slope_bps < 0:
            failure_parts.append("slow_slope_down")
        elif slow_slope_bps > 0:
            failure_parts.append("slow_slope_up")
        reason = "_and_".join(failure_parts) if failure_parts else "mixed_trend"

    return HigherTimeframeTrend(
        source_timeframe=source_timeframe,
        fast_ma_length=fast_ma_length,
        slow_ma_length=slow_ma_length,
        state=state,
        long_allowed=bullish,
        short_allowed=bearish,
        reason=reason,
        latest_close=latest_close,
        latest_vwap=latest_vwap,
        fast_ma=latest_fast,
        slow_ma=latest_slow,
        slow_ma_slope_bps=slow_slope_bps,
    )
