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
from mytradingbot.orchestration.paper_loop import PaperTradingLoopService
from mytradingbot.qlib_engine.models import QlibOperationResult
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
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bullish",
                        "long_allowed": True,
                        "short_allowed": False,
                        "reason": "close_above_vwap_and_fast_above_slow"
                    },
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


def test_paper_loop_runner_is_restart_safe_and_prevents_duplicate_entries(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.012)

    loop_service = PaperTradingLoopService(
        settings=settings,
        predictions_path=predictions_path,
        market_snapshot_path=market_path,
    )
    result = loop_service.run(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        interval_seconds=0,
        max_cycles=2,
    )

    store = RuntimeStateService(settings=settings).store

    assert result.cycle_count == 2
    assert result.cycles[0].trade_count == 1
    assert result.cycles[1].startup_open_positions == 1
    assert result.cycles[1].startup_open_brackets == 1
    assert result.cycles[1].trade_count == 0
    assert "duplicate_position" in result.cycles[1].rejection_reasons
    assert len(store.list_orders()) == 1

    restarted = PaperTradingLoopService(
        settings=settings,
        predictions_path=predictions_path,
        market_snapshot_path=market_path,
    ).run(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        interval_seconds=0,
        max_cycles=1,
    )

    assert restarted.cycles[0].startup_open_positions == 1
    assert restarted.cycles[0].startup_open_brackets == 1
    assert len(RuntimeStateService(settings=settings).store.list_orders()) == 1


def test_paper_loop_auto_refreshes_inputs_and_reports_ready_state(tmp_path) -> None:
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
                        "higher_timeframe_trend": {
                            "source_timeframe": "15m",
                            "fast_ma_length": 5,
                            "slow_ma_length": 10,
                            "state": "bullish",
                            "long_allowed": True,
                            "short_allowed": False,
                            "reason": "close_above_vwap_and_fast_above_slow"
                        },
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

    loop_service = PaperTradingLoopService(
        settings=settings,
        predictions_path=predictions_path,
        market_snapshot_path=market_path,
        symbols=["AAPL"],
        auto_refresh_inputs=True,
        platform_factory=lambda: service,
        runtime_state_service=runtime_service,
    )
    result = loop_service.run(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        interval_seconds=0,
        max_cycles=1,
    )

    assert result.ok
    assert result.cycle_count == 1
    assert result.cycles[0].trade_count == 1
    assert result.cycles[0].decision_pipeline_ready is True
    assert result.cycles[0].decision_block_reason is None
