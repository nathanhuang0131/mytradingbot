"""Qlib adapter boundary for availability checks and artifact loading."""

from __future__ import annotations

import importlib.util
import json
import logging
import time
from pathlib import Path

from mytradingbot.core.models import ArtifactStatus, QlibPrediction
from mytradingbot.core.settings import AppSettings
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
    ) -> None:
        self.settings = settings or AppSettings()
        self.pyqlib_available = (
            self._detect_pyqlib() if pyqlib_available is None else pyqlib_available
        )
        self.predictions_path = predictions_path or self.settings.prediction_artifact_path()
        self.freshness_threshold_minutes = freshness_threshold_minutes

    def _detect_pyqlib(self) -> bool:
        return importlib.util.find_spec("qlib") is not None

    def build_dataset(self) -> QlibOperationResult:
        if not self.pyqlib_available:
            return self._missing_pyqlib_result("dataset build")
        return QlibOperationResult(
            ok=False,
            message="Qlib dataset build scaffolding is present but no concrete workflow is configured yet.",
            guidance=[
                "Add a concrete qlib dataset workflow configuration before running dataset builds.",
            ],
        )

    def train_models(self) -> QlibOperationResult:
        if not self.pyqlib_available:
            return self._missing_pyqlib_result("model training")
        return QlibOperationResult(
            ok=False,
            message="Qlib training scaffolding is present but no concrete workflow is configured yet.",
            guidance=[
                "Add a concrete qlib training workflow configuration before running training.",
            ],
        )

    def refresh_predictions(self) -> QlibOperationResult:
        if not self.pyqlib_available:
            return self._missing_pyqlib_result("prediction refresh")
        return QlibOperationResult(
            ok=False,
            message="Qlib prediction refresh requires a configured workflow artifact writer.",
            guidance=[
                "Install mytradingbot-next[qlib] and wire a qlib workflow that writes predictions to the configured artifact path.",
            ],
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
