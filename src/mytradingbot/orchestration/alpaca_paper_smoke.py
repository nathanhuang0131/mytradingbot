"""One-shot Alpaca paper submission smoke workflow."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import utc_now
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.runtime.models import BrokerMode
from mytradingbot.runtime.service import RuntimeStateService

logger = logging.getLogger(__name__)

SmokeSide = Literal["long", "short"]


class AlpacaPaperSmokeResult(BaseModel):
    """Structured result for a one-shot Alpaca paper submission smoke."""

    ok: bool
    submitted: bool
    symbol: str
    side: SmokeSide
    strategy: str
    broker_mode: BrokerMode = "alpaca_paper_api"
    session_id: str | None = None
    run_id: str | None = None
    client_order_id: str | None = None
    broker_order_id: str | None = None
    broker_order_status: str | None = None
    bot_owned_classified: bool = False
    ownership_classification: str | None = None
    session_report_path: str | None = None
    decision_audit_path: str | None = None
    predictions_artifact_path: str
    market_snapshot_artifact_path: str
    cancel_after_submit: bool = True
    canceled_after_submit: bool = False
    cancel_message: str | None = None
    rejection_reasons: list[str] = Field(default_factory=list)
    decision_block_reason: str | None = None


class AlpacaPaperSmokeService:
    """Run a bounded one-shot Alpaca paper bracket submission smoke."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()
        self.settings.broker.broker_mode = "alpaca_paper_api"

    def run(
        self,
        *,
        symbol: str,
        side: SmokeSide,
        strategy_name: str = "scalping",
        cancel_after_submit: bool = True,
    ) -> AlpacaPaperSmokeResult:
        smoke_dir = self._build_smoke_directory(symbol=symbol, side=side)
        try:
            reference_price = self._lookup_reference_price(symbol)
            predictions_path, market_snapshot_path = self._write_runtime_artifacts(
                smoke_dir=smoke_dir,
                symbol=symbol,
                side=side,
                reference_price=reference_price,
            )
        except Exception as exc:
            return AlpacaPaperSmokeResult(
                ok=False,
                submitted=False,
                symbol=symbol,
                side=side,
                strategy=strategy_name,
                predictions_artifact_path=str(smoke_dir / "predictions.json"),
                market_snapshot_artifact_path=str(smoke_dir / "market_snapshot.json"),
                cancel_after_submit=cancel_after_submit,
                rejection_reasons=[f"reference_price_lookup_failed:{exc}"],
                decision_block_reason="reference_price_lookup_failed",
            )

        runtime_state_service = RuntimeStateService(settings=self.settings)
        service = TradingPlatformService(
            settings=self.settings,
            qlib_service=QlibWorkflowService(
                settings=self.settings,
                predictions_path=predictions_path,
            ),
            market_data_service=MarketDataService(
                settings=self.settings,
                market_snapshot_path=market_snapshot_path,
            ),
            runtime_state_service=runtime_state_service,
            broker_mode="alpaca_paper_api",
        )

        session_result = service.run_session(
            strategy_name=strategy_name,
            mode=RuntimeMode.PAPER,
            auto_refresh_inputs=False,
            symbols=[symbol],
            intent_metadata_overrides={"entry_order_type": "limit", "smoke_submission": True},
        )
        session_id = session_result.session_summary.session_id
        session_report_path = (
            self.settings.paths.reports_paper_trading_dir
            / f"{session_id}_paper_session.md"
        )
        decision_audit_path = (
            self.settings.paths.reports_signals_dir
            / f"{session_id}_decision_audit.json"
        )

        order = session_result.orders[0] if session_result.orders else None
        client_order_id = (
            order.client_order_id
            if order is not None
            else self._extract_client_order_id(decision_audit_path)
        )
        cancel_message = None
        canceled_after_submit = False

        if order is not None and cancel_after_submit:
            cancel_message, canceled_after_submit = self._cancel_if_possible(
                service=service,
                order_id=order.order_id,
            )

        service.broker.reconcile_runtime_state(strategy_name=strategy_name)
        order_record = self._lookup_order_record(
            runtime_state_service=runtime_state_service,
            order_id=order.order_id if order is not None else None,
            client_order_id=client_order_id,
        )

        return AlpacaPaperSmokeResult(
            ok=order is not None,
            submitted=order is not None,
            symbol=symbol,
            side=side,
            strategy=strategy_name,
            session_id=session_result.session_summary.session_id,
            run_id=self._read_session_run_id(session_report_path),
            client_order_id=client_order_id,
            broker_order_id=order.order_id if order is not None else None,
            broker_order_status=(
                order_record.status if order_record is not None else (order.status if order is not None else None)
            ),
            bot_owned_classified=bool(
                order_record is not None and order_record.ownership_class == "bot_owned"
            ),
            ownership_classification=(
                order_record.ownership_class if order_record is not None else None
            ),
            session_report_path=str(session_report_path),
            decision_audit_path=str(decision_audit_path),
            predictions_artifact_path=str(predictions_path),
            market_snapshot_artifact_path=str(market_snapshot_path),
            cancel_after_submit=cancel_after_submit,
            canceled_after_submit=canceled_after_submit,
            cancel_message=cancel_message,
            rejection_reasons=session_result.rejection_reasons,
            decision_block_reason=(
                session_result.decision_pipeline_readiness.decision_block_reason
                if session_result.decision_pipeline_readiness is not None
                else None
            ),
        )

    def _build_smoke_directory(self, *, symbol: str, side: SmokeSide) -> Path:
        timestamp = utc_now().strftime("%Y%m%d%H%M%S")
        smoke_dir = self.settings.paths.runtime_dir / "alpaca_paper_smoke" / f"{timestamp}_{symbol}_{side}"
        smoke_dir.mkdir(parents=True, exist_ok=True)
        return smoke_dir

    def _write_runtime_artifacts(
        self,
        *,
        smoke_dir: Path,
        symbol: str,
        side: SmokeSide,
        reference_price: float,
    ) -> tuple[Path, Path]:
        now = utc_now()
        direction = "long" if side == "long" else "short"
        predicted_return = 0.0055 if side == "long" else -0.0055
        market_snapshot = {
            "symbol": symbol,
            "last_price": round(reference_price, 4),
            "vwap": round(reference_price * (0.997 if side == "long" else 1.003), 4),
            "spread_bps": 1.0,
            "volume": 1_500_000,
            "liquidity_score": 0.55,
            "liquidity_stress": 0.2,
            "order_book_imbalance": 0.2 if side == "long" else -0.2,
            "liquidity_sweep_detected": False,
            "volatility_regime": "normal",
            "timestamp": now.isoformat(),
        }
        prediction = {
            "symbol": symbol,
            "score": 0.91,
            "predicted_return": predicted_return,
            "confidence": 0.61,
            "rank": 1,
            "direction": direction,
            "horizon": "intraday",
            "generated_at": now.isoformat(),
        }
        predictions_path = smoke_dir / "predictions.json"
        market_snapshot_path = smoke_dir / "market_snapshot.json"
        predictions_path.write_text(json.dumps([prediction], indent=2), encoding="utf-8")
        market_snapshot_path.write_text(json.dumps([market_snapshot], indent=2), encoding="utf-8")
        return predictions_path, market_snapshot_path

    def _lookup_reference_price(self, symbol: str) -> float:
        from alpaca.data.historical import StockHistoricalDataClient
        from alpaca.data.requests import StockLatestTradeRequest

        client = StockHistoricalDataClient(
            api_key=self.settings.broker.alpaca_api_key,
            secret_key=self.settings.broker.alpaca_secret_key,
        )
        response = client.get_stock_latest_trade(
            StockLatestTradeRequest(symbol_or_symbols=[symbol])
        )
        trade = response.get(symbol)
        if trade is None or getattr(trade, "price", None) in (None, 0):
            raise ValueError(f"No latest trade price available for {symbol}.")
        return float(trade.price)

    @staticmethod
    def _extract_client_order_id(decision_audit_path: Path) -> str | None:
        if not decision_audit_path.exists():
            return None
        try:
            payload = json.loads(decision_audit_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None
        if not payload:
            return None
        notes = payload[0].get("notes", [])
        for note in notes:
            if isinstance(note, str) and note.startswith("client_order_id="):
                return note.split("=", 1)[1]
        return None

    def _cancel_if_possible(
        self,
        *,
        service: TradingPlatformService,
        order_id: str,
    ) -> tuple[str, bool]:
        broker = service.broker
        client = getattr(broker, "client", None)
        cancel_order = getattr(client, "cancel_order_by_id", None)
        get_order = getattr(client, "get_order_by_id", None)
        if not callable(cancel_order):
            return ("cancel_order_by_id unavailable on Alpaca client", False)
        try:
            cancel_order(order_id)
            status = None
            if callable(get_order):
                refreshed = get_order(order_id)
                status = getattr(getattr(refreshed, "status", None), "value", getattr(refreshed, "status", None))
            return (f"cancel_requested status={status}" if status else "cancel_requested", True)
        except Exception as exc:  # pragma: no cover - broker-dependent
            logger.warning("Alpaca paper smoke cancel failed for %s: %s", order_id, exc)
            return (f"cancel_failed:{exc}", False)

    @staticmethod
    def _lookup_order_record(
        *,
        runtime_state_service: RuntimeStateService,
        order_id: str | None,
        client_order_id: str | None,
    ):
        for record in reversed(runtime_state_service.store.list_order_records()):
            if order_id and record.order_id == order_id:
                return record
            if client_order_id and record.client_order_id == client_order_id:
                return record
        return None

    @staticmethod
    def _read_session_run_id(session_report_path: Path) -> str | None:
        if not session_report_path.with_suffix(".json").exists():
            return None
        try:
            payload = json.loads(session_report_path.with_suffix(".json").read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return None
        return str(payload.get("run_id")) if payload.get("run_id") is not None else None
