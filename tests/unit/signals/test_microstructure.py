from __future__ import annotations

import pandas as pd

from mytradingbot.signals.microstructure import build_microstructure_proxy


def _frame(
    *,
    opens: list[float],
    highs: list[float],
    lows: list[float],
    closes: list[float],
    volumes: list[float],
    vwaps: list[float],
) -> pd.DataFrame:
    periods = len(closes)
    return pd.DataFrame(
        {
            "timestamp": pd.date_range("2026-03-28 01:00:00+00:00", periods=periods, freq="1min"),
            "symbol": ["AAPL"] * periods,
            "open": opens,
            "high": highs,
            "low": lows,
            "close": closes,
            "volume": volumes,
            "vwap": vwaps,
        }
    )


def test_build_microstructure_proxy_reports_bullish_pressure() -> None:
    frame = _frame(
        opens=[100.0, 100.1, 100.2, 100.35, 100.55],
        highs=[100.2, 100.35, 100.5, 100.75, 101.05],
        lows=[99.95, 100.0, 100.1, 100.28, 100.48],
        closes=[100.12, 100.28, 100.42, 100.68, 100.98],
        volumes=[900_000, 950_000, 1_000_000, 1_250_000, 1_650_000],
        vwaps=[100.02, 100.08, 100.18, 100.32, 100.52],
    )

    proxy = build_microstructure_proxy(frame)

    assert proxy.state == "bullish"
    assert proxy.score > 0.25
    assert proxy.directional_pressure > 0
    assert proxy.vwap_bias > 0
    assert proxy.persistence > 0


def test_build_microstructure_proxy_reports_bearish_pressure() -> None:
    frame = _frame(
        opens=[100.9, 100.75, 100.55, 100.28, 100.02],
        highs=[101.0, 100.82, 100.62, 100.34, 100.08],
        lows=[100.65, 100.45, 100.18, 99.92, 99.55],
        closes=[100.72, 100.5, 100.24, 99.98, 99.62],
        volumes=[900_000, 1_000_000, 1_080_000, 1_280_000, 1_700_000],
        vwaps=[100.85, 100.7, 100.48, 100.18, 99.9],
    )

    proxy = build_microstructure_proxy(frame)

    assert proxy.state == "bearish"
    assert proxy.score < -0.25
    assert proxy.directional_pressure < 0
    assert proxy.vwap_bias < 0
    assert proxy.persistence < 0


def test_build_microstructure_proxy_reports_neutral_for_mixed_structure() -> None:
    frame = _frame(
        opens=[100.0, 100.05, 100.1, 100.08, 100.12],
        highs=[100.18, 100.2, 100.24, 100.22, 100.28],
        lows=[99.92, 99.96, 99.98, 99.95, 99.99],
        closes=[100.04, 100.08, 100.02, 100.1, 100.11],
        volumes=[1_000_000, 1_010_000, 990_000, 1_005_000, 1_000_000],
        vwaps=[100.03, 100.06, 100.05, 100.07, 100.09],
    )

    proxy = build_microstructure_proxy(frame)

    assert proxy.state == "neutral"
    assert abs(proxy.score) < 0.2


def test_build_microstructure_proxy_returns_unavailable_when_required_inputs_are_missing() -> None:
    frame = pd.DataFrame(
        {
            "timestamp": pd.date_range("2026-03-28 01:00:00+00:00", periods=3, freq="1min"),
            "symbol": ["AAPL"] * 3,
            "close": [100.0, 100.1, 100.2],
            "volume": [1_000_000, 1_100_000, 1_200_000],
        }
    )

    proxy = build_microstructure_proxy(frame)

    assert proxy.state == "unavailable"
    assert proxy.score == 0.0
    assert proxy.reason == "missing_required_columns"
