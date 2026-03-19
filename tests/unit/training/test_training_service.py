from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone
from pathlib import Path

import pandas as pd

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings, QlibSettings, TrainingSettings
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.training.service import AlphaRobustTrainingService


class _FakeQlibAdapter:
    def build_dataset(self, frame: pd.DataFrame, artifact_path: Path) -> Path:
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(artifact_path, index=False)
        return artifact_path

    def train_model(self, frame: pd.DataFrame, artifact_path: Path, strategy_name: str) -> Path:
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        artifact_path.write_text(json.dumps({"strategy": strategy_name, "rows": len(frame)}), encoding="utf-8")
        return artifact_path

    def generate_predictions(self, frame: pd.DataFrame, model_path: Path, output_path: Path, strategy_name: str) -> Path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        latest_rows = frame.sort_values("datetime").groupby("instrument").tail(1)
        payload = [
            {
                "symbol": row.instrument,
                "score": float(row.feature_return_1),
                "predicted_return": float(row.label),
                "confidence": 0.75,
                "rank": index,
                "direction": "long" if float(row.label) >= 0 else "short",
                "horizon": strategy_name,
            }
            for index, row in enumerate(latest_rows.itertuples(index=False), start=1)
        ]
        output_path.write_text(json.dumps(payload), encoding="utf-8")
        return output_path


def test_alpha_robust_training_service_writes_quality_and_manifest_artifacts(tmp_path) -> None:
    settings = AppSettings(
        paths=RepoPaths.for_root(tmp_path),
        qlib=QlibSettings(label_horizon_bars=1),
        training=TrainingSettings(
            minimum_eligible_symbols=1,
            timeframe_minimum_trading_days={"1d": 3, "1m": 1, "5m": 1, "15m": 1},
            timeframe_preferred_trading_days={"1d": 3, "1m": 1, "5m": 1, "15m": 1},
            timeframe_minimum_coverage_ratio={"1d": 0.5, "1m": 0.8, "5m": 0.8, "15m": 0.8},
        ),
    )
    normalized_path = settings.paths.normalized_data_dir / "bars" / "1d"
    normalized_path.mkdir(parents=True, exist_ok=True)
    end_date = datetime.now(timezone.utc)
    pd.DataFrame(
        [
            {
                "symbol": "AAPL",
                "timestamp": pd.Timestamp((end_date - timedelta(days=offset)).isoformat()),
                "timeframe": "1d",
                "open": 100.0 + offset,
                "high": 101.0 + offset,
                "low": 99.0 + offset,
                "close": 100.5 + offset,
                "volume": 1_000_000,
                "trade_count": 100,
                "vwap": 100.2 + offset,
                "provider": "alpaca",
                "adjustment": "raw",
                "feed": "iex",
            }
            for offset in range(8, 0, -1)
        ]
    ).to_parquet(normalized_path / "AAPL.parquet", index=False)
    service = AlphaRobustTrainingService(
        settings=settings,
        qlib_service=QlibWorkflowService(
            settings=settings,
            pyqlib_available=True,
            workflow_adapter=_FakeQlibAdapter(),
        ),
    )

    result = service.run_alpha_robust_training(
        strategy_name="long_term",
        symbols=["AAPL"],
        timeframes=["1d"],
        min_eligible_symbols=1,
        skip_download=True,
    )

    assert result.ok
    assert settings.paths.reports_training_dir.joinpath("training_data_quality_report.md").exists()
    assert settings.paths.data_dir.joinpath("registry", "latest_training_manifest.json").exists()
