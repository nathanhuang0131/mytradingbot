from __future__ import annotations

import json
import os
import pickle
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.models import MarketDataPipelineResult
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.adapter import FEATURE_COLUMNS, PyQlibWorkflowAdapter
from mytradingbot.qlib_engine.models import QlibOperationResult
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.runtime.models import OrderLifecycleRecord
from mytradingbot.runtime.service import RuntimeStateService
from mytradingbot.session_setup.service import SetupWizardService


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
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bullish",
                        "long_allowed": True,
                        "short_allowed": False,
                        "reason": "close_above_vwap_and_fast_above_slow",
                    },
                    "timestamp": generated_at.isoformat(),
                }
            ]
        ),
        encoding="utf-8",
    )
    return predictions_path, market_path


def _write_dual_direction_artifacts(tmp_path: Path) -> tuple[Path, Path]:
    predictions_path = tmp_path / "predictions_dual.json"
    market_path = tmp_path / "market_dual.json"
    generated_at = datetime(2026, 3, 18, 15, 0, tzinfo=timezone.utc)
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
                    "generated_at": generated_at.isoformat(),
                },
                {
                    "symbol": "MSFT",
                    "score": -0.95,
                    "predicted_return": -0.012,
                    "confidence": 0.84,
                    "rank": 2,
                    "direction": "short",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                },
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
                        "reason": "close_above_vwap_and_fast_above_slow",
                    },
                    "timestamp": generated_at.isoformat(),
                },
                {
                    "symbol": "MSFT",
                    "last_price": 100.0,
                    "vwap": 100.6,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": -0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bearish",
                        "long_allowed": False,
                        "short_allowed": True,
                        "reason": "close_below_vwap_and_fast_below_slow",
                    },
                    "timestamp": generated_at.isoformat(),
                },
            ]
        ),
        encoding="utf-8",
    )
    return predictions_path, market_path


class _PredictableModel:
    def __init__(self, scores: dict[str, float]) -> None:
        self.scores = scores

    def predict(self, dataset, segment: str = "predict"):
        latest_rows = dataset.sort_values("datetime").groupby("instrument").tail(1)
        index = []
        values = []
        for row in latest_rows.itertuples(index=False):
            index.append((row.datetime, row.instrument))
            values.append(float(self.scores[row.instrument]))
        return pd.Series(
            values,
            index=pd.MultiIndex.from_tuples(index, names=["datetime", "instrument"]),
        )


def _write_generated_dual_direction_artifacts(tmp_path: Path, monkeypatch) -> tuple[Path, Path]:
    predictions_path = tmp_path / "predictions_generated.json"
    market_path = tmp_path / "market_generated.json"
    model_path = tmp_path / "model.pkl"
    generated_at = datetime(2026, 3, 18, 15, 0, tzinfo=timezone.utc)
    frame = pd.DataFrame(
        [
            {
                "datetime": pd.Timestamp(generated_at),
                "instrument": "AAPL",
                **{column: 0.1 for column in FEATURE_COLUMNS},
            },
            {
                "datetime": pd.Timestamp(generated_at),
                "instrument": "MSFT",
                **{column: 0.2 for column in FEATURE_COLUMNS},
            },
        ]
    )
    model_path.write_bytes(
        pickle.dumps(_PredictableModel({"AAPL": 0.008, "MSFT": -0.009}))
    )

    monkeypatch.setattr(
        PyQlibWorkflowAdapter,
        "_build_dataset_object",
        lambda self, frame, include_label=False, segment_name="predict": frame,
    )
    adapter = PyQlibWorkflowAdapter()
    adapter.generate_predictions(frame, model_path, predictions_path, "scalping")

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
                        "reason": "close_above_vwap_and_fast_above_slow",
                    },
                    "timestamp": generated_at.isoformat(),
                },
                {
                    "symbol": "MSFT",
                    "last_price": 100.0,
                    "vwap": 100.6,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": -0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bearish",
                        "long_allowed": False,
                        "short_allowed": True,
                        "reason": "close_below_vwap_and_fast_below_slow",
                    },
                    "timestamp": generated_at.isoformat(),
                },
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
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.0004)
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
    assert audit_payload[0]["signal_source"] == "qlib_plus_rules"
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
                            "higher_timeframe_trend": {
                                "source_timeframe": "15m",
                                "fast_ma_length": 5,
                                "slow_ma_length": 10,
                                "state": "bullish",
                                "long_allowed": True,
                                "short_allowed": False,
                                "reason": "close_above_vwap_and_fast_above_slow",
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


def test_run_session_honors_long_only_session_config(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_dual_direction_artifacts(tmp_path)
    runtime_service = RuntimeStateService(settings=settings)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state = wizard_service.apply_preset(state, "Scalping - Alpaca Paper Long Only")
    resolved_config = wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        session_config=resolved_config,
        symbols_file=Path(resolved_config.active_symbols_path),
    )

    assert all(attempt.symbol != "MSFT" for attempt in result.trade_attempts)
    assert any(attempt.symbol == "AAPL" for attempt in result.trade_attempts)


def test_run_session_honors_saved_scalping_predicted_return_threshold(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_runtime_artifacts(tmp_path, predicted_return=0.012)
    runtime_service = RuntimeStateService(settings=settings)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.alpha.predicted_return_threshold = 0.02
    resolved_config = wizard_service.finalize_setup(state, generated_symbols=["AAPL"])

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        session_config=resolved_config,
        symbols_file=Path(resolved_config.active_symbols_path),
    )

    assert result.session_summary.trade_count == 0
    assert "predicted_return_threshold" in result.rejection_reasons


def test_run_session_candidate_count_prefers_stronger_short_signal_by_absolute_score(
    tmp_path,
    monkeypatch,
) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path, market_path = _write_generated_dual_direction_artifacts(
        tmp_path,
        monkeypatch,
    )
    runtime_service = RuntimeStateService(settings=settings)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.alpha.side_mode = "both"
    state.alpha.candidate_count = 1
    state.alpha.predicted_return_threshold = 0.0
    state.alpha.confidence_threshold = 0.0
    resolved_config = wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        session_config=resolved_config,
        symbols_file=Path(resolved_config.active_symbols_path),
    )

    assert len(result.trade_attempts) == 1
    assert result.trade_attempts[0].symbol == "MSFT"
    assert result.trade_attempts[0].strategy_outcome is not None
    assert result.trade_attempts[0].strategy_outcome.intent is not None
    assert result.trade_attempts[0].strategy_outcome.intent.side == "sell"


def test_run_session_applies_top_n_selection_after_hard_filters(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path = tmp_path / "predictions_top_n.json"
    market_path = tmp_path / "market_top_n.json"
    generated_at = datetime(2026, 3, 28, 1, 0, tzinfo=timezone.utc)
    predictions_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.009,
                    "predicted_return": 0.009,
                    "confidence": 0.9,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                },
                {
                    "symbol": "MSFT",
                    "score": 0.008,
                    "predicted_return": 0.008,
                    "confidence": 0.85,
                    "rank": 2,
                    "direction": "long",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                },
                {
                    "symbol": "NVDA",
                    "score": 0.0075,
                    "predicted_return": 0.0075,
                    "confidence": 0.88,
                    "rank": 3,
                    "direction": "long",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                },
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
                    "liquidity_score": 0.95,
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
                },
                {
                    "symbol": "MSFT",
                    "last_price": 100.0,
                    "vwap": 99.5,
                    "spread_bps": 1.1,
                    "volume": 1400000,
                    "liquidity_score": 0.82,
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
                },
                {
                    "symbol": "NVDA",
                    "last_price": 100.0,
                    "vwap": 99.8,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.95,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bearish",
                        "long_allowed": False,
                        "short_allowed": True,
                        "reason": "close_below_vwap_and_fast_below_slow"
                    },
                    "timestamp": generated_at.isoformat(),
                },
            ]
        ),
        encoding="utf-8",
    )

    runtime_service = RuntimeStateService(settings=settings)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.alpha.side_mode = "both"
    state.alpha.candidate_count = 3
    state.alpha.top_n_per_cycle = 1
    state.alpha.predicted_return_threshold = 0.0
    state.alpha.confidence_threshold = 0.0
    state.risk.higher_timeframe_filter_enabled = True
    resolved_config = wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT", "NVDA"])

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        session_config=resolved_config,
        symbols_file=Path(resolved_config.active_symbols_path),
    )

    assert result.session_summary.trade_count == 1
    audit_path = settings.paths.reports_signals_dir / f"{result.session_summary.session_id}_decision_audit.json"
    audit_payload = json.loads(audit_path.read_text(encoding="utf-8"))
    assert any(
        row["symbol"] == "MSFT"
        and row["final_rejection_reason_detail"] == "top_n_selection_cutoff"
        for row in audit_payload
    )
    assert any(
        row["symbol"] == "NVDA"
        and row["final_rejection_reason_detail"] == "higher_timeframe_trend_alignment"
        for row in audit_payload
    )


def test_run_session_microstructure_proxy_can_break_quality_ties_for_top_n(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    predictions_path = tmp_path / "predictions_microstructure.json"
    market_path = tmp_path / "market_microstructure.json"
    generated_at = datetime(2026, 3, 28, 1, 0, tzinfo=timezone.utc)
    predictions_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.008,
                    "predicted_return": 0.008,
                    "confidence": 0.88,
                    "rank": 2,
                    "direction": "long",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                },
                {
                    "symbol": "MSFT",
                    "score": 0.008,
                    "predicted_return": 0.008,
                    "confidence": 0.88,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                    "generated_at": generated_at.isoformat(),
                },
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
                    "liquidity_score": 0.95,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "microstructure_proxy": {
                        "state": "bullish",
                        "score": 0.72,
                        "directional_pressure": 0.74,
                        "relative_volume": 0.82,
                        "range_expansion": 0.48,
                        "vwap_bias": 0.52,
                        "wick_bias": 0.18,
                        "persistence": 0.65,
                        "reason": "price_volume_vwap_alignment"
                    },
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
                },
                {
                    "symbol": "MSFT",
                    "last_price": 100.0,
                    "vwap": 99.4,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.95,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "microstructure_proxy": {
                        "state": "bearish",
                        "score": -0.72,
                        "directional_pressure": -0.74,
                        "relative_volume": 0.82,
                        "range_expansion": 0.48,
                        "vwap_bias": -0.52,
                        "wick_bias": -0.18,
                        "persistence": -0.65,
                        "reason": "price_volume_vwap_alignment"
                    },
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
                },
            ]
        ),
        encoding="utf-8",
    )

    runtime_service = RuntimeStateService(settings=settings)
    wizard_service = SetupWizardService(settings=settings)
    state = wizard_service.initialize_wizard(profile_name="Alice Trader", source_mode="create_new")
    state.alpha.side_mode = "both"
    state.alpha.candidate_count = 2
    state.alpha.top_n_per_cycle = 1
    state.alpha.predicted_return_threshold = 0.0
    state.alpha.confidence_threshold = 0.0
    state.risk.higher_timeframe_filter_enabled = True
    state.risk.microstructure_proxy_mode = "soft_rank"
    resolved_config = wizard_service.finalize_setup(state, generated_symbols=["AAPL", "MSFT"])

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(settings=settings, predictions_path=predictions_path),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
        runtime_state_service=runtime_service,
    )

    result = service.run_session(
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        session_config=resolved_config,
        symbols_file=Path(resolved_config.active_symbols_path),
    )

    assert result.session_summary.trade_count == 1
    audit_path = settings.paths.reports_signals_dir / f"{result.session_summary.session_id}_decision_audit.json"
    audit_payload = json.loads(audit_path.read_text(encoding="utf-8"))
    assert any(
        row["symbol"] == "AAPL" and row["final_decision_status"].startswith("accepted")
        for row in audit_payload
    )
    assert any(
        row["symbol"] == "MSFT"
        and row["final_rejection_reason_detail"] == "top_n_selection_cutoff"
        for row in audit_payload
    )
