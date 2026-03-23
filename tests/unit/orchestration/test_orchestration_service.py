from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.models import MarketDataPipelineResult
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.models import QlibOperationResult
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


def _set_mtime(path: Path, *, minutes_ago: int) -> None:
    timestamp = (datetime.now(timezone.utc) - timedelta(minutes=minutes_ago)).timestamp()
    os.utime(path, (timestamp, timestamp))


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


def test_run_session_blocks_stale_snapshot_when_auto_refresh_disabled(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.012)
    _set_mtime(market_path, minutes_ago=settings.freshness.market_snapshot_max_age_minutes + 5)
    runtime_service = RuntimeStateService(settings=settings)
    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        auto_refresh_inputs=False,
    )

    assert result.session_summary.status == "failed"
    assert result.decision_pipeline_readiness is not None
    assert result.decision_pipeline_readiness.market_snapshot_ready is False
    assert result.decision_pipeline_readiness.decision_pipeline_ready is False
    assert result.decision_pipeline_readiness.decision_block_reason == "stale_market_snapshot"
    report = runtime_service.store.list_session_reports()[-1]
    assert report.market_snapshot_ready is False
    assert report.decision_block_reason == "stale_market_snapshot"


def test_run_session_blocks_stale_predictions_when_auto_refresh_disabled(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.012)
    _set_mtime(predictions_path, minutes_ago=settings.freshness.predictions_max_age_minutes + 5)
    runtime_service = RuntimeStateService(settings=settings)
    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        auto_refresh_inputs=False,
    )

    assert result.session_summary.status == "failed"
    assert result.decision_pipeline_readiness is not None
    assert result.decision_pipeline_readiness.predictions_ready is False
    assert result.decision_pipeline_readiness.decision_pipeline_ready is False
    assert result.decision_pipeline_readiness.decision_block_reason == "stale_predictions"


def test_run_session_auto_refreshes_inputs_and_restores_readiness(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.012)
    _set_mtime(predictions_path, minutes_ago=settings.freshness.predictions_max_age_minutes + 5)
    _set_mtime(market_path, minutes_ago=settings.freshness.market_snapshot_max_age_minutes + 5)
    runtime_service = RuntimeStateService(settings=settings)
    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    def fake_download_market_data(**kwargs):
        source_path = settings.market_snapshot_artifact_path()
        source_path.parent.mkdir(parents=True, exist_ok=True)
        source_path.write_text(
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
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                    }
                ]
            ),
            encoding="utf-8",
        )
        return MarketDataPipelineResult(ok=True, message="market data refreshed")

    def fake_build_dataset(**kwargs):
        dataset_path = settings.qlib_dataset_artifact_path()
        dataset_path.parent.mkdir(parents=True, exist_ok=True)
        dataset_path.write_text("dataset_refreshed", encoding="utf-8")
        return QlibOperationResult(ok=True, message="dataset refreshed")

    def fake_refresh_predictions(**kwargs):
        predictions_path.write_text(
            json.dumps(
                [
                    {
                        "symbol": "AAPL",
                        "score": 0.95,
                        "predicted_return": 0.012,
                        "confidence": 0.84,
                        "rank": 1,
                        "direction": "long",
                        "horizon": "intraday",
                        "generated_at": datetime.now(timezone.utc).isoformat(),
                    }
                ]
            ),
            encoding="utf-8",
        )
        return QlibOperationResult(ok=True, message="predictions refreshed")

    service.download_market_data = fake_download_market_data
    service.build_dataset = fake_build_dataset
    service.refresh_predictions = fake_refresh_predictions

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        auto_refresh_inputs=True,
        symbols=["AAPL"],
    )

    assert result.session_summary.status == "completed"
    assert result.session_summary.trade_count == 1
    assert result.decision_pipeline_readiness is not None
    assert result.decision_pipeline_readiness.decision_pipeline_ready is True
    assert result.decision_pipeline_readiness.decision_block_reason is None
    assert "market_refresh:market data refreshed" in result.decision_pipeline_readiness.refresh_actions
    assert "prediction_refresh:predictions refreshed" in result.decision_pipeline_readiness.refresh_actions
