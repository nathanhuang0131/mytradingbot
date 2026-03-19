"""Service for generating a deterministic top-liquidity universe."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import Protocol

import pandas as pd

from mytradingbot.core.settings import AppSettings
from mytradingbot.universe.models import TopLiquidityUniverseResult, UniverseAssetRecord
from mytradingbot.universe.ranking import filter_assets, rank_assets_by_liquidity
from mytradingbot.universe.storage import UniverseStorage


class AssetProvider(Protocol):
    def list_assets(self, *, asset_class: str, include_etfs: bool) -> list[UniverseAssetRecord]:
        """Return candidate assets for universe generation."""


class DailyBarsProvider(Protocol):
    def fetch_daily_bars(
        self,
        symbols: list[str],
        *,
        start_at: datetime,
        end_at: datetime,
    ) -> dict[str, pd.DataFrame]:
        """Return daily bars keyed by symbol."""


class AlpacaAssetProvider:
    """Asset discovery adapter using Alpaca trading metadata."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()

    def list_assets(self, *, asset_class: str, include_etfs: bool) -> list[UniverseAssetRecord]:
        from alpaca.trading.client import TradingClient
        from alpaca.trading.enums import AssetClass, AssetStatus
        from alpaca.trading.requests import GetAssetsRequest

        client = TradingClient(
            api_key=self.settings.broker.alpaca_api_key,
            secret_key=self.settings.broker.alpaca_secret_key,
            paper=True,
        )
        request = GetAssetsRequest(
            status=AssetStatus.ACTIVE,
            asset_class=AssetClass.US_EQUITY if asset_class == "us_equity" else None,
        )
        assets = client.get_all_assets(request)
        rows: list[UniverseAssetRecord] = []
        for asset in assets:
            rows.append(
                UniverseAssetRecord(
                    symbol=str(asset.symbol),
                    name=str(getattr(asset, "name", "")),
                    exchange=self._enum_text(getattr(asset, "exchange", "")),
                    asset_class=self._enum_text(getattr(asset, "asset_class", asset_class)),
                    status=self._enum_text(getattr(asset, "status", "active")),
                    tradable=bool(getattr(asset, "tradable", True)),
                    marginable=getattr(asset, "marginable", None),
                    shortable=getattr(asset, "shortable", None),
                    easy_to_borrow=getattr(asset, "easy_to_borrow", None),
                    fractionable=getattr(asset, "fractionable", None),
                )
            )
        return rows

    @staticmethod
    def _enum_text(value) -> str:
        if hasattr(value, "value"):
            return str(value.value)
        return str(value)


class AlpacaDailyBarsProvider:
    """Daily-bar adapter reusing the repo's Alpaca historical provider boundary."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        from mytradingbot.data.providers.alpaca_provider import AlpacaHistoricalProvider
        from mytradingbot.data.models import MarketDataRequest

        self.settings = settings or AppSettings()
        self._provider = AlpacaHistoricalProvider(settings=self.settings)
        self._request_type = MarketDataRequest
        self._provider.settings.data.symbol_chunk_size = max(
            self._provider.settings.data.symbol_chunk_size,
            200,
        )

    def fetch_daily_bars(
        self,
        symbols: list[str],
        *,
        start_at: datetime,
        end_at: datetime,
    ) -> dict[str, pd.DataFrame]:
        return self._provider.fetch_bars(
            self._request_type(
                symbols=symbols,
                timeframe="1d",
                start_at=start_at,
                end_at=end_at,
                provider="alpaca",
                adjustment=self.settings.broker.alpaca_adjustment,
                feed=self.settings.broker.alpaca_data_feed,
                limit=self.settings.data.request_page_limit,
            )
        )


class TopLiquidityUniverseService:
    """Generate and persist a ranked liquid stock universe."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        storage: UniverseStorage | None = None,
        asset_provider: AssetProvider | None = None,
        bars_provider: DailyBarsProvider | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.storage = storage or UniverseStorage(settings=self.settings)
        self.asset_provider = asset_provider or AlpacaAssetProvider(settings=self.settings)
        self.bars_provider = bars_provider or AlpacaDailyBarsProvider(settings=self.settings)

    def generate_top_liquidity_universe(
        self,
        *,
        top_n: int | None = None,
        lookback_days: int | None = None,
        minimum_price: float | None = None,
        minimum_average_volume: float | None = None,
        asset_class: str | None = None,
        include_etfs: bool | None = None,
        output_prefix: str = "top_liquidity_universe",
        generated_at: datetime | None = None,
    ) -> TopLiquidityUniverseResult:
        generated_at = generated_at or datetime.now(timezone.utc)
        lookback_days = lookback_days or self.settings.universe.lookback_days
        lookback_start = generated_at - timedelta(days=lookback_days)
        top_n = top_n or self.settings.universe.top_n
        minimum_price = minimum_price or self.settings.universe.minimum_price
        minimum_average_volume = minimum_average_volume or self.settings.universe.minimum_average_volume
        asset_class = asset_class or self.settings.universe.asset_class
        include_etfs = include_etfs if include_etfs is not None else self.settings.universe.include_etfs

        if not (self.settings.broker.alpaca_api_key and self.settings.broker.alpaca_secret_key):
            return TopLiquidityUniverseResult(
                ok=False,
                message="Alpaca credentials are required to generate the top liquidity universe.",
            )

        assets = filter_assets(
            self.asset_provider.list_assets(asset_class=asset_class, include_etfs=include_etfs),
            include_etfs=include_etfs,
        )
        if not assets:
            return TopLiquidityUniverseResult(ok=False, message="No candidate assets passed the universe filters.")

        bars_by_symbol = self.bars_provider.fetch_daily_bars(
            [asset.symbol for asset in assets],
            start_at=lookback_start,
            end_at=generated_at,
        )
        ranked = rank_assets_by_liquidity(
            assets=assets,
            bars_by_symbol=bars_by_symbol,
            lookback_start=lookback_start,
            lookback_end=generated_at,
            minimum_price=minimum_price,
            minimum_average_volume=minimum_average_volume,
            minimum_coverage_ratio=self.settings.universe.minimum_coverage_ratio,
            top_n=top_n,
        )
        if not ranked:
            return TopLiquidityUniverseResult(
                ok=False,
                message="No symbols passed the liquidity ranking filters.",
            )

        artifacts = self.storage.write(rows=ranked, output_prefix=output_prefix)
        return TopLiquidityUniverseResult(
            ok=True,
            message=f"Generated top liquidity universe with {len(ranked)} symbols.",
            rows=ranked,
            artifacts=artifacts,
        )
