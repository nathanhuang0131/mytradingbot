from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.orchestration.paper_loop import PaperTradingLoopService
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
                    "timestamp": generated_at.isoformat(),
                }
            ]
        ),
        encoding="utf-8",
    )
    return predictions_path, market_path


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
