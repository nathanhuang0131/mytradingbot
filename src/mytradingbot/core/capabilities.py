"""Central capability detection for the phased platform rollout."""

from __future__ import annotations

import importlib.util
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from mytradingbot.core.settings import AppSettings

CapabilityStatus = Literal["enabled", "blocked", "partial"]


class PhaseCapability(BaseModel):
    """Operator-facing status for a single rollout phase."""

    name: str
    status: CapabilityStatus
    summary: str
    guidance: list[str] = Field(default_factory=list)
    works_without_pyqlib: bool = False
    works_without_alpaca_credentials: bool = False


class CapabilitySnapshot(BaseModel):
    """Current repo capability view for UI and CLI surfaces."""

    pyqlib_available: bool
    alpaca_sdk_available: bool
    alpaca_credentials_configured: bool
    phase_1: PhaseCapability
    phase_2: PhaseCapability
    phase_3: PhaseCapability
    phase_4: PhaseCapability


class CapabilityService:
    """Evaluate which rollout phases are operational or blocked."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        pyqlib_available: bool | None = None,
        alpaca_sdk_available: bool | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.pyqlib_available = (
            self._is_module_available("qlib")
            if pyqlib_available is None
            else pyqlib_available
        )
        self.alpaca_sdk_available = (
            self._is_module_available("alpaca")
            if alpaca_sdk_available is None
            else alpaca_sdk_available
        )

    def detect(self) -> CapabilitySnapshot:
        alpaca_credentials_configured = bool(
            self.settings.broker.alpaca_api_key and self.settings.broker.alpaca_secret_key
        )
        phase_1 = self._phase_one_status()
        phase_2 = self._phase_two_status(alpaca_credentials_configured)
        phase_3 = self._phase_three_status()
        phase_4 = self._phase_four_status(alpaca_credentials_configured)
        return CapabilitySnapshot(
            pyqlib_available=self.pyqlib_available,
            alpaca_sdk_available=self.alpaca_sdk_available,
            alpaca_credentials_configured=alpaca_credentials_configured,
            phase_1=phase_1,
            phase_2=phase_2,
            phase_3=phase_3,
            phase_4=phase_4,
        )

    def _phase_one_status(self) -> PhaseCapability:
        predictions_ready = self.settings.prediction_artifact_path().exists()
        snapshot_ready = self.settings.market_snapshot_artifact_path().exists()
        if predictions_ready and snapshot_ready:
            return PhaseCapability(
                name="Phase 1",
                status="enabled",
                summary="Paper trading artifacts are present.",
                works_without_pyqlib=True,
                works_without_alpaca_credentials=True,
            )
        return PhaseCapability(
            name="Phase 1",
            status="partial",
            summary="Paper trading remains available, but runtime artifacts must be supplied or refreshed.",
            guidance=[
                "Provide explicit prediction and market snapshot artifacts for paper sessions, or complete the phase-2/3 pipeline.",
            ],
            works_without_pyqlib=True,
            works_without_alpaca_credentials=True,
        )

    def _phase_two_status(self, alpaca_credentials_configured: bool) -> PhaseCapability:
        if not self.alpaca_sdk_available:
            return PhaseCapability(
                name="Phase 2",
                status="blocked",
                summary="Repo-local Alpaca data download/update is unavailable because alpaca-py is not installed.",
                guidance=[
                    "Install mytradingbot-next[broker] to enable Alpaca historical downloads.",
                ],
            )
        if not alpaca_credentials_configured:
            return PhaseCapability(
                name="Phase 2",
                status="blocked",
                summary="Repo-local Alpaca data download/update is blocked until Alpaca credentials are configured.",
                guidance=[
                    "Set broker.alpaca_api_key and broker.alpaca_secret_key in environment variables or .env.",
                ],
            )
        raw_exists = any(self._iter_data_files(self.settings.paths.raw_data_dir / "alpaca"))
        normalized_exists = any(self._iter_data_files(self.settings.paths.normalized_data_dir))
        if raw_exists and normalized_exists:
            return PhaseCapability(
                name="Phase 2",
                status="enabled",
                summary="Repo-local Alpaca download, normalize, and snapshot data is present.",
            )
        return PhaseCapability(
            name="Phase 2",
            status="partial",
            summary="Alpaca data pipeline is configured but repo-local parquet artifacts have not been built yet.",
            guidance=[
                "Run the repo-local download/update and normalization workflow to populate parquet data under the repo data directory.",
            ],
        )

    def _phase_three_status(self) -> PhaseCapability:
        if not self.pyqlib_available:
            return PhaseCapability(
                name="Phase 3",
                status="blocked",
                summary="Qlib dataset build, training, and prediction refresh are unavailable because pyqlib is not installed.",
                guidance=[
                    "Install mytradingbot-next[qlib] so pyqlib is available before running dataset build, training, or prediction refresh.",
                ],
            )
        dataset_ready = self.settings.qlib_dataset_artifact_path().exists()
        model_ready = self.settings.qlib_model_artifact_path().exists()
        predictions_ready = self.settings.prediction_artifact_path().exists()
        if dataset_ready and model_ready and predictions_ready:
            return PhaseCapability(
                name="Phase 3",
                status="enabled",
                summary="Qlib dataset, model, and prediction artifacts are available.",
            )
        return PhaseCapability(
            name="Phase 3",
            status="partial",
            summary="Qlib is installed, but dataset/model/prediction artifacts are incomplete.",
            guidance=[
                "Run repo-local qlib dataset build, training, and prediction refresh in order.",
            ],
        )

    def _phase_four_status(self, alpaca_credentials_configured: bool) -> PhaseCapability:
        if not self.settings.runtime.live_trading_enabled:
            return PhaseCapability(
                name="Phase 4",
                status="blocked",
                summary="Live trading remains guarded and validation-only in this phase.",
                guidance=[
                    "Enable live trading explicitly in configuration only after broker persistence and preflight checks are in place.",
                ],
            )
        status: CapabilityStatus = "partial" if alpaca_credentials_configured else "blocked"
        guidance = []
        if not alpaca_credentials_configured:
            guidance.append("Configure Alpaca credentials before enabling live execution preflights.")
        guidance.append("Phase 4 remains scaffolded; no real live order submission is active yet.")
        return PhaseCapability(
            name="Phase 4",
            status=status,
            summary="Live trading scaffolding is visible, but real submission remains disabled.",
            guidance=guidance,
        )

    @staticmethod
    def _is_module_available(module_name: str) -> bool:
        return importlib.util.find_spec(module_name) is not None

    @staticmethod
    def _iter_data_files(path: Path):
        if not path.exists():
            return []
        return path.rglob("*.parquet")
