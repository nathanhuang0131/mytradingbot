"""Training data quality checks for alpha-robust workflows."""

from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from mytradingbot.core.settings import AppSettings
from mytradingbot.data.schema import DataSchemaError, validate_canonical_bar_frame
from mytradingbot.data.storage import ParquetBarStore
from mytradingbot.training.models import (
    SymbolTimeframeQuality,
    TimeframeQualitySummary,
    TrainingDataQualityReport,
)


_BARS_PER_TRADING_DAY = {"1m": 390, "5m": 78, "15m": 26, "1d": 1}


class TrainingDataQualityChecker:
    """Assess normalized parquet readiness for robust model training."""

    def __init__(self, settings: AppSettings | None = None, *, store: ParquetBarStore | None = None) -> None:
        self.settings = settings or AppSettings()
        self.store = store or ParquetBarStore(settings=self.settings)

    def evaluate(self, *, symbols: list[str], timeframes: list[str]) -> TrainingDataQualityReport:
        timeframe_summaries: list[TimeframeQualitySummary] = []
        eligible_by_timeframe: list[set[str]] = []
        for timeframe in timeframes:
            details: list[SymbolTimeframeQuality] = []
            for symbol in symbols:
                details.append(self._evaluate_symbol(symbol=symbol, timeframe=timeframe))
            passing = [detail for detail in details if detail.passes]
            coverage_failures = [detail for detail in details if detail.failure_reason == "coverage"]
            freshness_failures = [detail for detail in details if detail.failure_reason == "stale"]
            schema_failures = [detail for detail in details if detail.failure_reason == "schema"]
            lookback_achieved = max(
                [
                    detail.unique_trading_days
                    for detail in details
                    if detail.passes
                ]
                or [0]
            )
            summary = TimeframeQualitySummary(
                timeframe=timeframe,
                symbols_requested=len(symbols),
                symbols_with_any_bars=len([detail for detail in details if detail.row_count > 0]),
                symbols_passing_quality=len(passing),
                symbols_failing_coverage=len(coverage_failures),
                symbols_failing_freshness=len(freshness_failures),
                symbols_failing_schema=len(schema_failures),
                median_coverage_ratio=float(pd.Series([detail.coverage_ratio for detail in details]).median() or 0.0),
                lookback_window_days_achieved=lookback_achieved,
                sufficiency_pass=lookback_achieved >= self.settings.training.timeframe_minimum_trading_days[timeframe]
                and len(passing) >= self.settings.training.minimum_eligible_symbols,
                symbol_details=details,
            )
            timeframe_summaries.append(summary)
            eligible_by_timeframe.append({detail.symbol for detail in passing})

        eligible_symbols = sorted(set.intersection(*eligible_by_timeframe)) if eligible_by_timeframe else []
        ok = all(summary.sufficiency_pass for summary in timeframe_summaries) and len(eligible_symbols) >= self.settings.training.minimum_eligible_symbols
        message = (
            "Training data passed multi-timeframe sufficiency checks."
            if ok
            else "Training data failed multi-timeframe sufficiency checks."
        )
        return TrainingDataQualityReport(
            ok=ok,
            message=message,
            generated_at=datetime.now(timezone.utc),
            timeframes=timeframes,
            timeframe_summaries=timeframe_summaries,
            requested_symbols=symbols,
            eligible_symbols=eligible_symbols,
        )

    def _evaluate_symbol(self, *, symbol: str, timeframe: str) -> SymbolTimeframeQuality:
        frame = self.store.read_normalized_bars(symbol, timeframe)
        if frame.empty:
            return SymbolTimeframeQuality(
                symbol=symbol,
                timeframe=timeframe,
                row_count=0,
                passes=False,
                failure_reason="coverage",
            )

        try:
            validate_canonical_bar_frame(frame)
            schema_ok = True
            failure_reason = None
        except DataSchemaError:
            schema_ok = False
            failure_reason = "schema"

        timestamps = pd.to_datetime(frame["timestamp"], utc=True)
        unique_days = int(timestamps.dt.normalize().nunique())
        expected_rows = max(1, unique_days * _BARS_PER_TRADING_DAY[timeframe])
        row_count = len(frame)
        duplicate_ratio = float(frame.duplicated(subset=["symbol", "timeframe", "timestamp"]).mean())
        coverage_ratio = min(1.0, row_count / expected_rows)
        last_timestamp = timestamps.max().to_pydatetime()
        first_timestamp = timestamps.min().to_pydatetime()
        age_hours = (datetime.now(timezone.utc) - last_timestamp).total_seconds() / 3600
        stale_limit_hours = 48 if timeframe == "1d" else 24
        stale = age_hours > stale_limit_hours
        coverage_threshold = self.settings.training.timeframe_minimum_coverage_ratio[timeframe]
        interval_alignment_ok = self._interval_alignment_ok(timestamps, timeframe)
        passes = schema_ok and interval_alignment_ok and not stale and coverage_ratio >= coverage_threshold and unique_days >= self.settings.training.timeframe_minimum_trading_days[timeframe]
        if failure_reason is None:
            if stale:
                failure_reason = "stale"
            elif coverage_ratio < coverage_threshold or unique_days < self.settings.training.timeframe_minimum_trading_days[timeframe]:
                failure_reason = "coverage"
            elif not interval_alignment_ok:
                failure_reason = "coverage"

        return SymbolTimeframeQuality(
            symbol=symbol,
            timeframe=timeframe,
            row_count=row_count,
            first_timestamp=first_timestamp,
            last_timestamp=last_timestamp,
            unique_trading_days=unique_days,
            coverage_ratio=coverage_ratio,
            duplicate_ratio=duplicate_ratio,
            stale=stale,
            schema_ok=schema_ok,
            interval_alignment_ok=interval_alignment_ok,
            passes=passes,
            failure_reason=failure_reason,
        )

    @staticmethod
    def _interval_alignment_ok(timestamps: pd.Series, timeframe: str) -> bool:
        if timeframe == "1d" or len(timestamps) < 2:
            return True
        deltas = timestamps.sort_values().diff().dropna().dt.total_seconds().astype(int)
        expected = {"1m": 60, "5m": 300, "15m": 900}[timeframe]
        return bool(((deltas % expected) == 0).all())
