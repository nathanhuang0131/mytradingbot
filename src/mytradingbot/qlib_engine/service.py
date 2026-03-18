"""Qlib adapter boundary for availability checks and artifact loading."""

from __future__ import annotations

import importlib.util
import json
import logging
import time
from pathlib import Path

import pandas as pd

from mytradingbot.core.models import ArtifactStatus, QlibPrediction
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.storage import ParquetBarStore
from mytradingbot.qlib_engine.adapter import PyQlibWorkflowAdapter, QlibWorkflowAdapter
from mytradingbot.qlib_engine.dataset import build_feature_dataset
from mytradingbot.qlib_engine.models import PredictionLoadResult, QlibOperationResult

logger = logging.getLogger(__name__)


class QlibWorkflowService:
    """Provide qlib-dependent operations and runtime artifact access."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        pyqlib_available: bool | None = None,
        predictions_path: Path | None = None,
        freshness_threshold_minutes: int = 60,
        workflow_adapter: QlibWorkflowAdapter | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.pyqlib_available = (
            self._detect_pyqlib() if pyqlib_available is None else pyqlib_available
        )
        self.predictions_path = predictions_path or self.settings.prediction_artifact_path()
        self.freshness_threshold_minutes = freshness_threshold_minutes
        self.workflow_adapter = workflow_adapter or PyQlibWorkflowAdapter()
        self.store = ParquetBarStore(settings=self.settings)
        self._qlib_initialized = False

    def _detect_pyqlib(self) -> bool:
        return importlib.util.find_spec("qlib") is not None

    def build_dataset(self, strategy_name: str | None = None) -> QlibOperationResult:
        if not self.pyqlib_available:
            return self._missing_pyqlib_result("dataset build")
        self._initialize_pyqlib_runtime()

        normalized_dataset = self._load_feature_dataset(strategy_name=strategy_name)
        if normalized_dataset.empty:
            return QlibOperationResult(
                ok=False,
                message="Normalized repo-local parquet data is missing for the requested strategy/timeframe.",
                guidance=[
                    "Run the repo-local download/update and normalization workflow before building the qlib dataset.",
                ],
            )

        artifact_path = self.settings.qlib_dataset_artifact_path()
        try:
            dataset_path = self.workflow_adapter.build_dataset(normalized_dataset, artifact_path)
        except Exception as exc:
            logger.exception("Qlib dataset build failed.")
            return QlibOperationResult(
                ok=False,
                message=f"Qlib dataset build failed: {exc}",
                guidance=[
                    "Check normalized parquet schema compatibility and confirm pyqlib is installed correctly.",
                ],
            )

        return QlibOperationResult(
            ok=True,
            message="Qlib-ready dataset artifact built from repo-local normalized parquet data.",
            artifacts=[str(dataset_path)],
            metadata={"rows": len(normalized_dataset)},
        )

    def train_models(self, strategy_name: str | None = None) -> QlibOperationResult:
        if not self.pyqlib_available:
            return self._missing_pyqlib_result("model training")
        self._initialize_pyqlib_runtime()

        dataset = self._read_dataset_artifact()
        if dataset.empty:
            return QlibOperationResult(
                ok=False,
                message="Qlib dataset artifact is missing or empty.",
                guidance=[
                    "Run the qlib dataset build workflow before training models.",
                ],
            )

        strategy = strategy_name or self.settings.strategies.default_strategy.value
        model_path = self.settings.qlib_model_artifact_path()
        try:
            trained_model_path = self.workflow_adapter.train_model(dataset, model_path, strategy)
        except Exception as exc:
            logger.exception("Qlib model training failed.")
            return QlibOperationResult(
                ok=False,
                message=f"Qlib model training failed: {exc}",
                guidance=[
                    "Confirm pyqlib and its model dependencies are installed, then rebuild the dataset if needed.",
                ],
            )

        return QlibOperationResult(
            ok=True,
            message="Qlib model training completed from the repo-local dataset artifact.",
            artifacts=[str(trained_model_path)],
            metadata={"rows": int(dataset['label'].notna().sum()) if 'label' in dataset.columns else 0},
        )

    def refresh_predictions(self, strategy_name: str | None = None) -> QlibOperationResult:
        if not self.pyqlib_available:
            return self._missing_pyqlib_result("prediction refresh")
        self._initialize_pyqlib_runtime()

        dataset = self._read_dataset_artifact()
        if dataset.empty:
            return QlibOperationResult(
                ok=False,
                message="Qlib dataset artifact is missing or empty.",
                guidance=[
                    "Run qlib dataset build before refreshing predictions.",
                ],
            )

        model_path = self.settings.qlib_model_artifact_path()
        if not model_path.exists():
            return QlibOperationResult(
                ok=False,
                message="Trained qlib model artifact is missing.",
                guidance=[
                    "Run qlib training before refreshing predictions.",
                ],
            )

        strategy = strategy_name or self.settings.strategies.default_strategy.value
        try:
            output_path = self.workflow_adapter.generate_predictions(
                dataset,
                model_path,
                self.predictions_path,
                strategy,
            )
        except Exception as exc:
            logger.exception("Prediction refresh failed.")
            return QlibOperationResult(
                ok=False,
                message=f"Prediction refresh failed: {exc}",
                guidance=[
                    "Check the trained model artifact and rebuild the dataset if schema or feature columns changed.",
                ],
            )

        return QlibOperationResult(
            ok=True,
            message="Predictions refreshed from the repo-local qlib workflow artifacts.",
            artifacts=[str(output_path)],
        )

    def get_runtime_prediction_status(self) -> ArtifactStatus:
        if not self.predictions_path.exists():
            return ArtifactStatus.missing(
                "predictions",
                guidance=[
                    "Run the prediction refresh workflow to create the runtime predictions artifact.",
                ],
            )

        freshness_minutes = int(
            (self._now_timestamp() - self.predictions_path.stat().st_mtime) / 60
        )
        if freshness_minutes > self.freshness_threshold_minutes:
            return ArtifactStatus.stale(
                "predictions",
                freshness_minutes=freshness_minutes,
                guidance=[
                    "Refresh predictions before running dry-run or paper trading sessions.",
                ],
            )

        return ArtifactStatus.ready("predictions", freshness_minutes=freshness_minutes)

    def load_predictions(self) -> PredictionLoadResult:
        status = self.get_runtime_prediction_status()
        if not status.is_ready:
            guidance = status.guidance or ["Refresh predictions before retrying."]
            return PredictionLoadResult(
                ok=False,
                message=guidance[0],
                status=status,
                predictions=[],
            )

        try:
            raw_payload = json.loads(
                self.predictions_path.read_text(encoding="utf-8-sig")
            )
        except json.JSONDecodeError as exc:
            logger.exception("Prediction artifact is not valid JSON.")
            invalid_status = ArtifactStatus.unavailable(
                "predictions",
                guidance=[
                    "Fix or regenerate the predictions artifact because it is not valid JSON.",
                ],
            )
            return PredictionLoadResult(
                ok=False,
                message=f"Prediction artifact is invalid: {exc}",
                status=invalid_status,
                predictions=[],
            )

        predictions = [QlibPrediction.model_validate(item) for item in raw_payload]
        return PredictionLoadResult(
            ok=True,
            message=f"Loaded {len(predictions)} predictions.",
            status=status,
            predictions=predictions,
        )

    def _missing_pyqlib_result(self, action_name: str) -> QlibOperationResult:
        return QlibOperationResult(
            ok=False,
            message=f"Cannot run {action_name} because pyqlib is not installed.",
            guidance=[
                "Install mytradingbot-next[qlib] to enable qlib workflows.",
                "The dashboard can still load, but dataset, training, and prediction refresh actions require pyqlib.",
            ],
        )

    @staticmethod
    def _now_timestamp() -> float:
        return time.time()

    def _load_feature_dataset(self, *, strategy_name: str | None) -> pd.DataFrame:
        strategy = strategy_name or self.settings.strategies.default_strategy.value
        return build_feature_dataset(
            settings=self.settings,
            strategy_name=strategy,
            store=self.store,
        )

    def _read_dataset_artifact(self) -> pd.DataFrame:
        dataset_path = self.settings.qlib_dataset_artifact_path()
        if not dataset_path.exists():
            return pd.DataFrame()
        return pd.read_parquet(dataset_path)

    def _initialize_pyqlib_runtime(self) -> None:
        if self._qlib_initialized or not self.pyqlib_available:
            return
        import qlib

        self.settings.paths.qlib_dir.mkdir(parents=True, exist_ok=True)
        qlib.init(
            default_conf="client",
            provider_uri=str(self.settings.paths.qlib_dir),
            region="us",
        )
        self._qlib_initialized = True
