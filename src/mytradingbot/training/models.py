"""Typed models for alpha-robust training quality and orchestration."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class SymbolTimeframeQuality(BaseModel):
    symbol: str
    timeframe: str
    row_count: int
    first_timestamp: datetime | None = None
    last_timestamp: datetime | None = None
    unique_trading_days: int = 0
    coverage_ratio: float = 0.0
    duplicate_ratio: float = 0.0
    stale: bool = False
    schema_ok: bool = True
    interval_alignment_ok: bool = True
    passes: bool = False
    failure_reason: str | None = None


class TimeframeQualitySummary(BaseModel):
    timeframe: str
    symbols_requested: int
    symbols_with_any_bars: int
    symbols_passing_quality: int
    symbols_failing_coverage: int
    symbols_failing_freshness: int
    symbols_failing_schema: int
    median_coverage_ratio: float = 0.0
    lookback_window_days_achieved: int = 0
    sufficiency_pass: bool = False
    symbol_details: list[SymbolTimeframeQuality] = Field(default_factory=list)


class ChronologicalSplit(BaseModel):
    train_start: datetime
    train_end: datetime
    valid_start: datetime
    valid_end: datetime
    test_start: datetime
    test_end: datetime
    prediction_horizon_bars: int
    label_definition: str


class TrainingDataQualityReport(BaseModel):
    ok: bool
    message: str
    generated_at: datetime
    timeframes: list[str]
    timeframe_summaries: list[TimeframeQualitySummary] = Field(default_factory=list)
    requested_symbols: list[str] = Field(default_factory=list)
    eligible_symbols: list[str] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)


class AlphaTrainingRunResult(BaseModel):
    ok: bool
    message: str
    eligible_symbols: list[str] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
    reports: list[str] = Field(default_factory=list)
    build_ok: bool = False
    train_ok: bool = False
    refresh_ok: bool = False
