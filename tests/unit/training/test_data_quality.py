from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pandas as pd

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings, TrainingSettings
from mytradingbot.data.storage import ParquetBarStore
from mytradingbot.training.data_quality import TrainingDataQualityChecker


def _write_normalized_symbol(store: ParquetBarStore, *, symbol: str, timeframe: str, timestamps: list[str]) -> None:
    frame = pd.DataFrame(
        [
            {
                "symbol": symbol,
                "timestamp": pd.Timestamp(ts),
                "timeframe": timeframe,
                "open": 100.0 + index,
                "high": 101.0 + index,
                "low": 99.0 + index,
                "close": 100.5 + index,
                "volume": 1_000_000,
                "trade_count": 100,
                "vwap": 100.2 + index,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            }
            for index, ts in enumerate(timestamps)
        ]
    )
    store.write_normalized_bars(symbol, timeframe, frame)


def test_training_quality_flags_insufficient_coverage(tmp_path) -> None:
    settings = AppSettings(
        paths=RepoPaths.for_root(tmp_path),
        training=TrainingSettings(
            minimum_eligible_symbols=1,
            timeframe_minimum_trading_days={"1d": 3, "1m": 1, "5m": 1, "15m": 1},
            timeframe_preferred_trading_days={"1d": 3, "1m": 1, "5m": 1, "15m": 1},
            timeframe_minimum_coverage_ratio={"1d": 0.8, "1m": 0.8, "5m": 0.8, "15m": 0.8},
        ),
    )
    store = ParquetBarStore(settings=settings)
    _write_normalized_symbol(
        store,
        symbol="AAPL",
        timeframe="1d",
        timestamps=["2026-01-02T00:00:00Z"],
    )
    checker = TrainingDataQualityChecker(settings=settings, store=store)

    report = checker.evaluate(symbols=["AAPL"], timeframes=["1d"])

    assert not report.ok
    assert report.timeframe_summaries[0].symbols_passing_quality == 0
    assert report.eligible_symbols == []


def test_training_quality_override_allows_smaller_eligible_floor(tmp_path) -> None:
    settings = AppSettings(
        paths=RepoPaths.for_root(tmp_path),
        training=TrainingSettings(
            minimum_eligible_symbols=150,
            timeframe_minimum_trading_days={"1d": 3, "1m": 1, "5m": 1, "15m": 1},
            timeframe_preferred_trading_days={"1d": 3, "1m": 1, "5m": 1, "15m": 1},
            timeframe_minimum_coverage_ratio={"1d": 0.8, "1m": 0.8, "5m": 0.8, "15m": 0.8},
        ),
    )
    store = ParquetBarStore(settings=settings)
    now = datetime.now(timezone.utc)
    recent_timestamps = [
        (now - timedelta(days=offset)).replace(hour=0, minute=0, second=0, microsecond=0).isoformat().replace("+00:00", "Z")
        for offset in (2, 1, 0)
    ]
    for symbol in ("AAPL", "MSFT"):
        _write_normalized_symbol(
            store,
            symbol=symbol,
            timeframe="1d",
            timestamps=recent_timestamps,
        )
    checker = TrainingDataQualityChecker(settings=settings, store=store)

    report = checker.evaluate(
        symbols=["AAPL", "MSFT"],
        timeframes=["1d"],
        minimum_eligible_symbols=2,
    )

    assert report.ok
    assert report.timeframe_summaries[0].symbols_requested == 2
    assert report.timeframe_summaries[0].symbols_passing_quality == 2
    assert report.eligible_symbols == ["AAPL", "MSFT"]
