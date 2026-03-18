from __future__ import annotations

import json
from pathlib import Path
from datetime import datetime, timedelta, timezone

import pandas as pd

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.qlib_engine.service import QlibWorkflowService


def test_missing_pyqlib_blocks_refresh_with_explicit_guidance(tmp_path) -> None:
    service = QlibWorkflowService(
        pyqlib_available=False,
        predictions_path=tmp_path / "latest.json",
    )

    result = service.refresh_predictions()

    assert not result.ok
    assert any("pyqlib" in line.lower() for line in result.guidance)


def test_missing_prediction_artifact_fails_clearly(tmp_path) -> None:
    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=tmp_path / "latest.json",
    )

    result = service.load_predictions()

    assert not result.ok
    assert "refresh" in result.message.lower()


def test_stale_prediction_artifact_is_reported(tmp_path) -> None:
    artifact_path = tmp_path / "latest.json"
    artifact_path.write_text("[]", encoding="utf-8")
    old_time = datetime.now(timezone.utc) - timedelta(minutes=90)
    timestamp = old_time.timestamp()

    import os

    os.utime(artifact_path, (timestamp, timestamp))

    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=artifact_path,
        freshness_threshold_minutes=30,
    )

    result = service.get_runtime_prediction_status()

    assert not result.is_ready
    assert result.reason == "stale"


def test_prediction_artifact_loads_typed_predictions(tmp_path) -> None:
    artifact_path = tmp_path / "latest.json"
    artifact_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.87,
                    "predicted_return": 0.014,
                    "confidence": 0.82,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                }
            ]
        ),
        encoding="utf-8",
    )

    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=artifact_path,
    )

    result = service.load_predictions()

    assert result.ok
    assert result.predictions[0].symbol == "AAPL"


class _FakeQlibAdapter:
    def build_dataset(self, frame: pd.DataFrame, artifact_path: Path) -> Path:
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(artifact_path, index=False)
        return artifact_path

    def train_model(self, frame: pd.DataFrame, artifact_path: Path, strategy_name: str) -> Path:
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        artifact_path.write_text(
            json.dumps({"strategy": strategy_name, "rows": len(frame)}),
            encoding="utf-8",
        )
        return artifact_path

    def generate_predictions(
        self,
        frame: pd.DataFrame,
        model_path: Path,
        output_path: Path,
        strategy_name: str,
    ) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        latest_rows = frame.sort_values("datetime").groupby("instrument").tail(1)
        payload = []
        for rank, row in enumerate(latest_rows.itertuples(index=False), start=1):
            payload.append(
                {
                    "symbol": row.instrument,
                    "score": float(row.feature_return_1),
                    "predicted_return": float(row.label),
                    "confidence": 0.75,
                    "rank": rank,
                    "direction": "long" if float(row.label) >= 0 else "short",
                    "horizon": strategy_name,
                }
            )
        output_path.write_text(json.dumps(payload), encoding="utf-8")
        return output_path


def _write_normalized_bars(root: Path, timeframe: str = "1m") -> None:
    normalized_path = root / "data" / "normalized" / "bars" / timeframe
    normalized_path.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        [
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp("2026-01-02T14:30:00Z"),
                "timeframe": timeframe,
                "open": 100.0,
                "high": 101.0,
                "low": 99.5,
                "close": 100.5,
                "volume": 1_000,
                "trade_count": 100,
                "vwap": 100.3,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            },
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp("2026-01-02T14:31:00Z"),
                "timeframe": timeframe,
                "open": 100.5,
                "high": 101.2,
                "low": 100.2,
                "close": 101.1,
                "volume": 1_100,
                "trade_count": 110,
                "vwap": 100.7,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            },
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp("2026-01-02T14:32:00Z"),
                "timeframe": timeframe,
                "open": 101.1,
                "high": 101.4,
                "low": 100.8,
                "close": 101.3,
                "volume": 1_200,
                "trade_count": 120,
                "vwap": 101.0,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            },
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp("2026-01-02T14:33:00Z"),
                "timeframe": timeframe,
                "open": 101.3,
                "high": 101.6,
                "low": 101.0,
                "close": 101.7,
                "volume": 1_300,
                "trade_count": 130,
                "vwap": 101.4,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            },
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp("2026-01-02T14:34:00Z"),
                "timeframe": timeframe,
                "open": 101.7,
                "high": 102.0,
                "low": 101.5,
                "close": 102.0,
                "volume": 1_350,
                "trade_count": 140,
                "vwap": 101.8,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            },
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp("2026-01-02T14:35:00Z"),
                "timeframe": timeframe,
                "open": 102.0,
                "high": 102.2,
                "low": 101.8,
                "close": 102.1,
                "volume": 1_400,
                "trade_count": 145,
                "vwap": 102.0,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            },
        ]
    ).to_parquet(normalized_path / "AAPL.parquet", index=False)


def test_build_train_and_refresh_use_repo_local_normalized_data(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    _write_normalized_bars(tmp_path)
    service = QlibWorkflowService(
        settings=settings,
        pyqlib_available=True,
        workflow_adapter=_FakeQlibAdapter(),
    )

    build_result = service.build_dataset(strategy_name="scalping")
    train_result = service.train_models(strategy_name="scalping")
    refresh_result = service.refresh_predictions(strategy_name="scalping")

    assert build_result.ok
    assert settings.qlib_dataset_artifact_path().exists()
    assert train_result.ok
    assert settings.qlib_model_artifact_path().exists()
    assert refresh_result.ok
    assert settings.prediction_artifact_path().exists()


def test_build_dataset_fails_clearly_when_normalized_data_is_missing(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    service = QlibWorkflowService(
        settings=settings,
        pyqlib_available=True,
        workflow_adapter=_FakeQlibAdapter(),
    )

    result = service.build_dataset(strategy_name="scalping")

    assert not result.ok
    assert "normalized" in result.message.lower()


def test_qlib_service_does_not_reference_demo_get_data_path() -> None:
    source = Path("src/mytradingbot/qlib_engine/service.py").read_text(encoding="utf-8")

    assert "get_data" not in source


def test_prediction_artifact_with_utf8_bom_loads_cleanly(tmp_path) -> None:
    artifact_path = tmp_path / "latest.json"
    artifact_path.write_text(
        "\ufeff"
        + json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.87,
                    "predicted_return": 0.014,
                    "confidence": 0.82,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                }
            ]
        ),
        encoding="utf-8",
    )

    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=artifact_path,
    )

    result = service.load_predictions()

    assert result.ok
    assert result.predictions[0].symbol == "AAPL"
