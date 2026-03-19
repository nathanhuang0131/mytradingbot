"""Typed models for liquid-universe generation."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class UniverseAssetRecord(BaseModel):
    """Tradability metadata for a candidate symbol."""

    symbol: str
    name: str = ""
    exchange: str = ""
    asset_class: str = "us_equity"
    status: str = "active"
    tradable: bool = True
    marginable: bool | None = None
    shortable: bool | None = None
    easy_to_borrow: bool | None = None
    fractionable: bool | None = None
    attributes: list[str] = Field(default_factory=list)


class UniverseLiquidityRow(BaseModel):
    """Ranked liquid-universe row persisted to repo-local artifacts."""

    symbol: str
    exchange: str
    asset_class: str = "us_equity"
    status: str
    tradable: bool
    marginable: bool | None = None
    shortable: bool | None = None
    easy_to_borrow: bool | None = None
    avg_close: float
    avg_volume: float
    avg_dollar_volume: float
    median_dollar_volume: float
    bars_used: int
    completeness_ratio: float
    rank: int
    lookback_start: datetime
    lookback_end: datetime
    generated_at: datetime


class TopLiquidityUniverseResult(BaseModel):
    """Service result for universe generation."""

    ok: bool
    message: str
    rows: list[UniverseLiquidityRow] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
