"""UI service payloads for the setup wizard page."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from pydantic import BaseModel, Field

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.session_setup.models import ResolvedSessionConfig, SetupWizardState, UserProfile
from mytradingbot.session_setup.runtime import apply_resolved_config_to_settings
from mytradingbot.session_setup.service import SetupWizardService


class SetupWizardProfileCard(BaseModel):
    profile_name: str
    profile_slug: str
    last_used_at: str | None = None
    last_preset_name: str | None = None
    latest_session_config_path: str | None = None


class SetupWizardPayload(BaseModel):
    profiles: list[SetupWizardProfileCard] = Field(default_factory=list)
    profile_names: list[str] = Field(default_factory=list)
    preset_names: list[str] = Field(default_factory=list)
    recommended_defaults: dict[str, object] = Field(default_factory=dict)
    available_strategies: list[str] = Field(default_factory=list)
    broker_modes: list[str] = Field(default_factory=lambda: ["local_paper", "alpaca_paper_api"])
    session_modes: list[str] = Field(default_factory=lambda: ["single_run", "bounded_smoke", "loop"])


class SetupWizardActionResult(BaseModel):
    ok: bool
    message: str
    resolved_config: ResolvedSessionConfig
    profile_path: str
    session_config_path: str
    active_symbols_path: str
    launched_command: list[str] = Field(default_factory=list)
    stdout_log_path: str | None = None
    stderr_log_path: str | None = None
    process_id: int | None = None
    session_summary: dict | None = None


class SetupWizardUIService:
    def __init__(
        self,
        platform_service: TradingPlatformService,
        *,
        wizard_service: SetupWizardService | None = None,
    ) -> None:
        self.platform_service = platform_service
        self.wizard_service = wizard_service or SetupWizardService(
            settings=self.platform_service.settings
        )

    def get_payload(self) -> SetupWizardPayload:
        profiles = self.wizard_service.list_profiles()
        return SetupWizardPayload(
            profiles=[
                SetupWizardProfileCard(
                    profile_name=profile.profile_name,
                    profile_slug=profile.profile_slug,
                    last_used_at=profile.last_used_at.isoformat() if profile.last_used_at else None,
                    last_preset_name=profile.last_preset_name,
                    latest_session_config_path=profile.latest_session_config_path,
                )
                for profile in profiles
            ],
            profile_names=[profile.profile_name for profile in profiles],
            preset_names=list(self.wizard_service.presets.keys()),
            recommended_defaults=self.wizard_service.recommended_defaults,
            available_strategies=self.platform_service.get_strategy_names(),
        )

    def initialize_wizard(
        self,
        *,
        profile_name: str,
        source_mode: str,
        existing_profile_name: str | None = None,
    ) -> SetupWizardState:
        return self.wizard_service.initialize_wizard(
            profile_name=profile_name,
            source_mode=source_mode,
            existing_profile_name=existing_profile_name,
        )

    def apply_preset(self, state: SetupWizardState, preset_name: str) -> SetupWizardState:
        return self.wizard_service.apply_preset(state, preset_name)  # type: ignore[arg-type]

    def save_and_exit(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
    ) -> SetupWizardActionResult:
        resolved = self.wizard_service.finalize_setup(state, generated_symbols=generated_symbols)
        return SetupWizardActionResult(
            ok=True,
            message="Profile and latest session configuration saved.",
            profile_path=resolved.profile_path,
            session_config_path=resolved.latest_session_config_path,
            active_symbols_path=resolved.active_symbols_path,
            resolved_config=resolved,
        )

    def start_session(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
        smoke_only: bool = False,
    ) -> SetupWizardActionResult:
        resolved = self.wizard_service.finalize_setup(state, generated_symbols=generated_symbols)
        if resolved.strategy.session_mode == "loop" and not smoke_only:
            return self._launch_loop_subprocess(resolved)

        runtime_service = self._build_runtime_service(resolved)
        result = runtime_service.run_session(
            strategy_name=resolved.strategy.strategy_name,
            mode=RuntimeMode(resolved.strategy.run_type.value),
            auto_refresh_inputs=self._auto_refresh_enabled(resolved),
            symbols_file=Path(resolved.active_symbols_path),
            refresh_timeframes=[runtime_service.settings.data.snapshot_timeframe],
            session_config=resolved,
        )
        return SetupWizardActionResult(
            ok=result.session_summary.status == "completed",
            message="Session started from the setup wizard.",
            profile_path=resolved.profile_path,
            session_config_path=resolved.latest_session_config_path,
            active_symbols_path=resolved.active_symbols_path,
            resolved_config=resolved,
            session_summary=result.session_summary.model_dump(mode="json"),
        )

    def preview_generated_symbols(self, state: SetupWizardState) -> list[str]:
        return self.wizard_service.resolve_generated_symbols(state)

    def review_flags(self, state: SetupWizardState) -> dict[str, list[str]]:
        return self.wizard_service.build_review_flags(state)

    def _build_runtime_service(self, config: ResolvedSessionConfig) -> TradingPlatformService:
        settings = apply_resolved_config_to_settings(
            self.platform_service.settings,
            config,
        )
        return TradingPlatformService(settings=settings, broker_mode=config.strategy.broker_mode)

    @staticmethod
    def _auto_refresh_enabled(config: ResolvedSessionConfig) -> bool:
        return (
            config.refresh.auto_refresh_market_snapshot
            or config.refresh.auto_refresh_predictions
            or config.refresh.auto_refresh_dataset
        )

    def _launch_loop_subprocess(self, config: ResolvedSessionConfig) -> SetupWizardActionResult:
        repo_root = self.platform_service.settings.paths.repo_root
        stdout_log = self.platform_service.settings.paths.logs_dir / f"{config.profile_slug}_wizard_stdout.log"
        stderr_log = self.platform_service.settings.paths.logs_dir / f"{config.profile_slug}_wizard_stderr.log"
        command = [
            sys.executable,
            str(self.platform_service.settings.paths.scripts_dir / "run_paper_trading.py"),
            "--session-config",
            config.latest_session_config_path,
            "--verbose",
        ]
        creationflags = 0
        for flag_name in ("CREATE_NEW_PROCESS_GROUP", "DETACHED_PROCESS"):
            creationflags |= int(getattr(subprocess, flag_name, 0))
        with stdout_log.open("w", encoding="utf-8") as stdout_handle, stderr_log.open(
            "w",
            encoding="utf-8",
        ) as stderr_handle:
            process = subprocess.Popen(  # noqa: S603
                command,
                cwd=str(repo_root),
                stdout=stdout_handle,
                stderr=stderr_handle,
                creationflags=creationflags,
            )
        pid_path = self.platform_service.settings.paths.runtime_dir / f"{config.profile_slug}_wizard_session.pid"
        pid_path.write_text(str(process.pid), encoding="utf-8")
        return SetupWizardActionResult(
            ok=True,
            message="Wizard launched the supervised loop in the background.",
            profile_path=config.profile_path,
            session_config_path=config.latest_session_config_path,
            active_symbols_path=config.active_symbols_path,
            resolved_config=config,
            launched_command=command,
            stdout_log_path=str(stdout_log),
            stderr_log_path=str(stderr_log),
            process_id=process.pid,
        )
