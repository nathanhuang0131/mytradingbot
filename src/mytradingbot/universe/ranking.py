"""Deterministic liquidity ranking for tradable common-equity universes."""

from __future__ import annotations

from datetime import datetime

import pandas as pd

from mytradingbot.universe.models import UniverseAssetRecord, UniverseLiquidityRow


_STRUCTURAL_EXCLUSION_MARKERS = (" ETF", " FUND", " TRUST", " WARRANT", " RIGHT", " UNIT", " PFD")
_ETF_SPONSOR_MARKERS = (
    "ISHARES",
    "VANGUARD",
    "PROSHARES",
    "DIREXION",
    "SPDR",
    "INVESCO",
    "FRANKLIN",
    "GLOBAL X",
    "SCHWAB",
    "ARK ",
)


def filter_assets(
    assets: list[UniverseAssetRecord],
    *,
    include_etfs: bool,
) -> list[UniverseAssetRecord]:
    """Filter assets down to active tradable common-equity candidates."""

    filtered: list[UniverseAssetRecord] = []
    for asset in assets:
        if asset.status.lower() != "active":
            continue
        if not asset.tradable:
            continue
        if asset.asset_class.lower() != "us_equity":
            continue
        name_upper = asset.name.upper()
        if not include_etfs and (
            "ETF" in name_upper
            or "FUND" in name_upper
            or any(marker in name_upper for marker in _ETF_SPONSOR_MARKERS)
        ):
            continue
        if any(marker in name_upper for marker in _STRUCTURAL_EXCLUSION_MARKERS):
            continue
        symbol_upper = asset.symbol.upper()
        if any(token in symbol_upper for token in ("/", "-", ".", "+")):
            continue
        filtered.append(asset)
    return sorted(filtered, key=lambda asset: asset.symbol)


def rank_assets_by_liquidity(
    *,
    assets: list[UniverseAssetRecord],
    bars_by_symbol: dict[str, pd.DataFrame],
    lookback_start: datetime,
    lookback_end: datetime,
    minimum_price: float,
    minimum_average_volume: float,
    minimum_coverage_ratio: float,
    top_n: int,
) -> list[UniverseLiquidityRow]:
    """Rank filtered assets by average dollar volume with deterministic tie-breaks."""

    rows: list[UniverseLiquidityRow] = []
    expected_bars = max(1, len(pd.date_range(lookback_start, lookback_end, freq="B")))
    for asset in assets:
        frame = bars_by_symbol.get(asset.symbol, pd.DataFrame()).copy()
        if frame.empty:
            continue
        frame["timestamp"] = pd.to_datetime(frame["timestamp"], utc=True)
        frame = frame.dropna(subset=["close", "volume"])
        if frame.empty:
            continue
        frame["dollar_volume"] = frame["close"] * frame["volume"]
        avg_close = float(frame["close"].mean())
        avg_volume = float(frame["volume"].mean())
        avg_dollar_volume = float(frame["dollar_volume"].mean())
        median_dollar_volume = float(frame["dollar_volume"].median())
        bars_used = int(len(frame))
        completeness_ratio = min(1.0, bars_used / expected_bars)
        if avg_close < minimum_price:
            continue
        if avg_volume < minimum_average_volume:
            continue
        if completeness_ratio < minimum_coverage_ratio:
            continue
        rows.append(
            UniverseLiquidityRow(
                symbol=asset.symbol,
                exchange=asset.exchange,
                asset_class=asset.asset_class,
                status=asset.status,
                tradable=asset.tradable,
                marginable=asset.marginable,
                shortable=asset.shortable,
                easy_to_borrow=asset.easy_to_borrow,
                avg_close=avg_close,
                avg_volume=avg_volume,
                avg_dollar_volume=avg_dollar_volume,
                median_dollar_volume=median_dollar_volume,
                bars_used=bars_used,
                completeness_ratio=completeness_ratio,
                rank=0,
                lookback_start=lookback_start,
                lookback_end=lookback_end,
                generated_at=lookback_end,
            )
        )

    rows = sorted(
        rows,
        key=lambda row: (
            -row.avg_dollar_volume,
            -row.avg_volume,
            -row.avg_close,
            row.symbol,
        ),
    )[:top_n]
    return [row.model_copy(update={"rank": rank}) for rank, row in enumerate(rows, start=1)]
