from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd

from mytradingbot.universe.models import UniverseAssetRecord
from mytradingbot.universe.ranking import filter_assets, rank_assets_by_liquidity


def test_filter_assets_excludes_inactive_etf_and_structurally_awkward_symbols() -> None:
    assets = [
        UniverseAssetRecord(symbol="AAPL", name="Apple Inc", exchange="NASDAQ", status="active", tradable=True),
        UniverseAssetRecord(symbol="SPY", name="SPDR S&P 500 ETF", exchange="ARCA", status="active", tradable=True),
        UniverseAssetRecord(symbol="TQQQ", name="ProShares UltraPro QQQ", exchange="NASDAQ", status="active", tradable=True),
        UniverseAssetRecord(symbol="ABCW", name="ABC Warrant", exchange="NYSE", status="active", tradable=True),
        UniverseAssetRecord(symbol="ZZZ", name="Inactive Common", exchange="NYSE", status="inactive", tradable=True),
    ]

    filtered = filter_assets(assets, include_etfs=False)

    assert [asset.symbol for asset in filtered] == ["AAPL"]


def test_rank_assets_by_average_dollar_volume_is_deterministic() -> None:
    lookback_start = datetime(2026, 2, 2, tzinfo=timezone.utc)
    lookback_end = datetime(2026, 2, 3, tzinfo=timezone.utc)
    assets = [
        UniverseAssetRecord(symbol="AAA", name="AAA Inc", exchange="NYSE", status="active", tradable=True),
        UniverseAssetRecord(symbol="BBB", name="BBB Inc", exchange="NYSE", status="active", tradable=True),
    ]
    bars_by_symbol = {
        "AAA": pd.DataFrame(
            [
                {"timestamp": pd.Timestamp("2026-02-02T00:00:00Z"), "close": 10.0, "volume": 800_000},
                {"timestamp": pd.Timestamp("2026-02-03T00:00:00Z"), "close": 11.0, "volume": 900_000},
            ]
        ),
        "BBB": pd.DataFrame(
            [
                {"timestamp": pd.Timestamp("2026-02-02T00:00:00Z"), "close": 40.0, "volume": 700_000},
                {"timestamp": pd.Timestamp("2026-02-03T00:00:00Z"), "close": 41.0, "volume": 710_000},
            ]
        ),
    }

    ranked = rank_assets_by_liquidity(
        assets=assets,
        bars_by_symbol=bars_by_symbol,
        lookback_start=lookback_start,
        lookback_end=lookback_end,
        minimum_price=5.0,
        minimum_average_volume=500_000,
        minimum_coverage_ratio=0.5,
        top_n=2,
    )

    assert [row.symbol for row in ranked] == ["BBB", "AAA"]
    assert ranked[0].rank == 1
    assert ranked[1].rank == 2
