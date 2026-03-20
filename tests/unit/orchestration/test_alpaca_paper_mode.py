from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.runtime.service import RuntimeStateService


def _write_runtime_artifacts(tmp_path: Path, *, predicted_return: float = 0.012) -> tuple[Path, Path]:
    predictions_path = tmp_path / "predictions.json"
    market_path = tmp_path / "market.json"
    generated_at = datetime(2026, 3, 18, 15, 0, tzinfo=timezone.utc)
    predictions_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.95,
                    "predicted_return": predicted_return,
                    "confidence": 0.84,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                }
            ]
        ),
        encoding="utf-8",
    )
    market_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "last_price": 100.0,
                    "vwap": 99.4,
                    "spread_bps": 1.0,
                    "volume": 1_500_000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "timestamp": generated_at.isoformat(),
                }
            ]
        ),
        encoding="utf-8",
    )
    return predictions_path, market_path


class _FakeTradingClient:
    def __init__(self) -> None:
        self.account = SimpleNamespace(status="ACTIVE", buying_power="25000", portfolio_value="25100")
        self.orders: list[object] = []
        self.positions: list[object] = []

    def get_account(self):
        return self.account

    def submit_order(self, order_data):
        return SimpleNamespace(
            id="submitted-order-1",
            client_order_id=getattr(order_data, "client_order_id", None),
            symbol=getattr(order_data, "symbol"),
            side=getattr(order_data, "side", None),
            qty=getattr(order_data, "qty", None),
            status="accepted",
            submitted_at=datetime.now(timezone.utc),
            filled_at=None,
            filled_qty="0",
            filled_avg_price=None,
            order_class=getattr(order_data, "order_class", None),
            limit_price=None,
            stop_price=None,
            legs=[],
        )

    def get_orders(self, filter=None):
        return list(self.orders)

    def get_all_positions(self):
        return list(self.positions)

    def close_position(self, symbol_or_asset_id, close_options=None):
        return SimpleNamespace(
            id=f"close-{symbol_or_asset_id}",
            client_order_id=None,
            symbol=symbol_or_asset_id,
            side=SimpleNamespace(value="sell"),
            qty="5",
            status=SimpleNamespace(value="accepted"),
            submitted_at=datetime.now(timezone.utc),
            filled_at=None,
            filled_qty="0",
            filled_avg_price=None,
            order_class=None,
            legs=[],
        )


def test_alpaca_paper_mode_preflight_failure_aborts_before_session_execution(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.broker_mode = "alpaca_paper_api"
    settings.broker.alpaca_api_key = ""
    settings.broker.alpaca_secret_key = ""
    predictions_path, market_path = _write_runtime_artifacts(tmp_path)

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=RuntimeStateService(settings=settings),
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.status == "failed"
    assert result.health_status.ok is False
    assert "preflight" in result.health_status.summary.lower()


def test_alpaca_paper_mode_reconcile_restores_bot_owned_state_without_duplicate_entry(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.broker_mode = "alpaca_paper_api"
    settings.broker.alpaca_api_key = "key"
    settings.broker.alpaca_secret_key = "secret"
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.02)
    runtime_service = RuntimeStateService(settings=settings)
    fake_client = _FakeTradingClient()
    fake_client.orders = [
        SimpleNamespace(
            id="alpaca-parent-1",
            client_order_id="SCALPING-AAPL-BUY-202603181500",
            symbol="AAPL",
            side=SimpleNamespace(value="buy"),
            qty="5",
            filled_qty="5",
            filled_avg_price="100.0",
            status=SimpleNamespace(value="filled"),
            submitted_at=datetime(2026, 3, 18, 15, 0, tzinfo=timezone.utc),
            filled_at=datetime(2026, 3, 18, 15, 0, tzinfo=timezone.utc),
            order_class=SimpleNamespace(value="bracket"),
            legs=[],
        )
    ]
    fake_client.positions = [
        SimpleNamespace(
            symbol="AAPL",
            qty="5",
            avg_entry_price="100.0",
            current_price="101.0",
            unrealized_pl="5.0",
        )
    ]
    broker = AlpacaPaperBroker(
        settings=settings,
        runtime_store=runtime_service.store,
        trading_client_factory=lambda _settings: fake_client,
    )
    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
        broker=broker,
        broker_mode="alpaca_paper_api",
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.trade_count == 0
    assert "duplicate_position" in result.rejection_reasons
    assert runtime_service.store.active_position_symbols() == {"AAPL"}
    assert runtime_service.store.foreign_position_symbols() == set()
