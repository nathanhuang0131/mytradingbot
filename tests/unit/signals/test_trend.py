from __future__ import annotations

import pandas as pd

from mytradingbot.signals.trend import build_higher_timeframe_trend


def _frame(closes: list[float], vwaps: list[float]) -> pd.DataFrame:
    timestamps = pd.date_range("2026-03-28 00:00:00+00:00", periods=len(closes), freq="15min")
    return pd.DataFrame(
        {
            "timestamp": timestamps,
            "close": closes,
            "vwap": vwaps,
        }
    )


def test_higher_timeframe_trend_reports_bullish_alignment() -> None:
    trend = build_higher_timeframe_trend(
        _frame(
            closes=[100.0, 100.5, 101.0, 101.4, 101.8, 102.2, 102.6, 103.0, 103.4, 103.8],
            vwaps=[99.9, 100.2, 100.6, 100.9, 101.2, 101.5, 101.9, 102.3, 102.7, 103.1],
        ),
        source_timeframe="15m",
        fast_ma_length=5,
        slow_ma_length=10,
    )

    assert trend.state == "bullish"
    assert trend.long_allowed is True
    assert trend.short_allowed is False


def test_higher_timeframe_trend_reports_bearish_alignment() -> None:
    trend = build_higher_timeframe_trend(
        _frame(
            closes=[103.8, 103.4, 103.0, 102.6, 102.2, 101.8, 101.4, 101.0, 100.6, 100.2],
            vwaps=[103.9, 103.5, 103.1, 102.7, 102.3, 101.9, 101.5, 101.1, 100.7, 100.3],
        ),
        source_timeframe="15m",
        fast_ma_length=5,
        slow_ma_length=10,
    )

    assert trend.state == "bearish"
    assert trend.long_allowed is False
    assert trend.short_allowed is True


def test_higher_timeframe_trend_reports_unavailable_when_history_is_too_short() -> None:
    trend = build_higher_timeframe_trend(
        _frame(
            closes=[100.0, 100.4, 100.8],
            vwaps=[99.8, 100.1, 100.5],
        ),
        source_timeframe="15m",
        fast_ma_length=5,
        slow_ma_length=10,
    )

    assert trend.state == "unavailable"
    assert trend.long_allowed is False
    assert trend.short_allowed is False
