from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pandas as pd

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.universe.models import UniverseAssetRecord
from mytradingbot.universe.service import AlpacaAssetProvider, TopLiquidityUniverseService
from mytradingbot.universe.storage import UniverseStorage


class FakeAssetProvider:
    def list_assets(self, *, asset_class: str, include_etfs: bool) -> list[UniverseAssetRecord]:
        return [
            UniverseAssetRecord(symbol="AAA", name="AAA Inc", exchange="NYSE", status="active", tradable=True),
            UniverseAssetRecord(symbol="BBB", name="BBB Inc", exchange="NYSE", status="active", tradable=True),
            UniverseAssetRecord(symbol="ETF1", name="Test ETF", exchange="ARCA", status="active", tradable=True),
        ]


class FakeBarsProvider:
    def fetch_daily_bars(self, symbols: list[str], *, start_at: datetime, end_at: datetime) -> dict[str, pd.DataFrame]:
        del start_at, end_at
        return {
            "AAA": pd.DataFrame(
                [
                    {"timestamp": pd.Timestamp("2026-02-02T00:00:00Z"), "close": 20.0, "volume": 600_000},
                    {"timestamp": pd.Timestamp("2026-02-03T00:00:00Z"), "close": 21.0, "volume": 610_000},
                ]
            ),
            "BBB": pd.DataFrame(
                [
                    {"timestamp": pd.Timestamp("2026-02-02T00:00:00Z"), "close": 50.0, "volume": 800_000},
                    {"timestamp": pd.Timestamp("2026-02-03T00:00:00Z"), "close": 49.0, "volume": 820_000},
                ]
            ),
            "ETF1": pd.DataFrame(
                [
                    {"timestamp": pd.Timestamp("2026-02-02T00:00:00Z"), "close": 100.0, "volume": 10_000_000},
                    {"timestamp": pd.Timestamp("2026-02-03T00:00:00Z"), "close": 101.0, "volume": 10_000_000},
                ]
            ),
        }


def test_universe_service_generates_repo_local_artifacts(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    storage = UniverseStorage(settings=settings)
    service = TopLiquidityUniverseService(
        settings=settings,
        storage=storage,
        asset_provider=FakeAssetProvider(),
        bars_provider=FakeBarsProvider(),
    )

    result = service.generate_top_liquidity_universe(
        top_n=2,
        lookback_days=2,
        minimum_price=5.0,
        minimum_average_volume=500_000,
        include_etfs=False,
        generated_at=datetime(2026, 2, 3, tzinfo=timezone.utc),
    )

    assert result.ok
    assert [row.symbol for row in result.rows] == ["BBB", "AAA"]
    assert settings.paths.universe_dir.joinpath("top_liquidity_universe_2.json").exists()
    assert settings.paths.universe_dir.joinpath("latest_top_liquidity_universe.json").exists()
    assert settings.paths.reports_universe_dir.joinpath("top_liquidity_universe_report.md").exists()


def test_universe_storage_loads_symbols_from_latest_json(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    storage = UniverseStorage(settings=settings)
    generated_at = datetime.now(timezone.utc)
    payload = [
        {
            "symbol": "AAA",
            "exchange": "NYSE",
            "status": "active",
            "tradable": True,
            "avg_close": 20.0,
            "avg_volume": 600_000,
            "avg_dollar_volume": 12_000_000,
            "rank": 1,
            "lookback_start": (generated_at - timedelta(days=30)).isoformat(),
            "lookback_end": generated_at.isoformat(),
            "bars_used": 20,
            "generated_at": generated_at.isoformat(),
        }
    ]
    settings.paths.universe_dir.mkdir(parents=True, exist_ok=True)
    settings.paths.universe_dir.joinpath("latest_top_liquidity_universe.json").write_text(
        __import__("json").dumps(payload),
        encoding="utf-8",
    )

    assert storage.load_symbols(settings.paths.universe_dir / "latest_top_liquidity_universe.json") == ["AAA"]


def test_alpaca_asset_provider_normalizes_enum_values() -> None:
    class _EnumLike:
        def __init__(self, value: str) -> None:
            self.value = value

    assert AlpacaAssetProvider._enum_text(_EnumLike("us_equity")) == "us_equity"
