from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.runtime.models import OrderLifecycleRecord
from mytradingbot.runtime.service import RuntimeStateService


def _write_runtime_artifacts(tmp_path, *, predicted_return: float = 0.012) -> tuple[Path, Path]:
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
                    "volume": 1500000,
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


def test_run_session_writes_decision_audit_even_when_no_trade(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.001)
    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=RuntimeStateService(settings=settings),
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.trade_count == 0
    audit_path = settings.paths.reports_signals_dir / f"{result.session_summary.session_id}_decision_audit.json"
    session_path = settings.paths.reports_paper_trading_dir / f"{result.session_summary.session_id}_paper_session.json"
    assert audit_path.exists()
    assert session_path.exists()
    audit_payload = json.loads(audit_path.read_text(encoding="utf-8"))
    assert audit_payload[0]["signal_source"] == "qlib_candidate_only"
    assert audit_payload[0]["final_decision_status"] == "rejected"


def test_run_session_blocks_duplicate_client_order_after_restart(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.012)
    runtime_service = RuntimeStateService(settings=settings)
    market_payload = json.loads(market_path.read_text(encoding="utf-8"))
    signal_timestamp = datetime.fromisoformat(market_payload[0]["timestamp"])
    expected_client_order_id = f"SCALPING-AAPL-BUY-{signal_timestamp.strftime('%Y%m%d%H%M')}"
    runtime_service.store.record_order(
        OrderLifecycleRecord(
            order_id="existing-order",
            session_id="seed-session",
            run_id="seed-run",
            strategy="scalping",
            mode=RuntimeMode.PAPER,
            symbol="AAPL",
            side="buy",
            quantity=2,
            client_order_id=expected_client_order_id,
            status="filled",
            submitted_at=datetime.now(timezone.utc),
            avg_fill_price=100.0,
            metadata={},
        )
    )
    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.trade_count == 0
    assert "execution_guard_blocked" in result.rejection_reasons
