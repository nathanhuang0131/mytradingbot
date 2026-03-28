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
from mytradingbot.ui_services.descriptive_sections import DescriptiveSection, describe_item


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


class SetupWizardReviewPayload(BaseModel):
    """Readable review payload for the wizard review step."""

    sections: list[DescriptiveSection] = Field(default_factory=list)
    defaults_section: DescriptiveSection
    customized_section: DescriptiveSection
    expected_actions: list[str] = Field(default_factory=list)


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

    def build_review_payload(
        self,
        state: SetupWizardState,
        *,
        generated_symbols: list[str] | None = None,
    ) -> SetupWizardReviewPayload:
        preview_symbols = self.wizard_service.preview_active_symbols(
            state.model_copy(deep=True),
            generated_symbols=generated_symbols,
        )
        flags = self.review_flags(state)
        sections = [
            DescriptiveSection(
                title="Profile & Session",
                description="The identity of the saved profile and the high-level session choices that will be persisted and launched.",
                items=[
                    describe_item("profile.profile_name", state.profile.profile_name),
                    describe_item("strategy.preset_name", state.strategy.preset_name),
                    describe_item("strategy.strategy_name", state.strategy.strategy_name),
                    describe_item("strategy.broker_mode", state.strategy.broker_mode),
                    describe_item("strategy.session_mode", state.strategy.session_mode),
                ],
            ),
            DescriptiveSection(
                title="Universe",
                description="How the active symbol universe will be resolved for this run and what files it will update.",
                items=[
                    describe_item("universe.selection_mode", state.universe.selection_mode),
                    describe_item("universe.target_symbol_count", state.universe.target_symbol_count),
                    describe_item("universe.min_price", state.universe.min_price),
                    describe_item("universe.min_average_volume", state.universe.min_average_volume),
                    describe_item("universe.include_etfs", state.universe.include_etfs),
                    describe_item("universe.active_symbol_count", len(preview_symbols)),
                    describe_item(
                        "universe.active_symbols_path",
                        self.wizard_service.storage.active_symbols_path(state.profile.profile_slug),
                    ),
                ],
            ),
            DescriptiveSection(
                title="Refresh Policy",
                description="The refresh behavior that keeps snapshots, datasets, and predictions up to date while the session runs.",
                items=[
                    describe_item("refresh.auto_refresh_market_snapshot", state.refresh.auto_refresh_market_snapshot),
                    describe_item("refresh.auto_refresh_predictions", state.refresh.auto_refresh_predictions),
                    describe_item("refresh.auto_refresh_dataset", state.refresh.auto_refresh_dataset),
                    describe_item("refresh.loop_interval_seconds", state.refresh.loop_interval_seconds),
                    describe_item("refresh.stale_input_behavior", state.refresh.stale_input_behavior),
                ],
            ),
            DescriptiveSection(
                title="Alpha & Model",
                description="The qlib ranking and gate settings that control how many symbols are considered and what strength they must show.",
                items=[
                    describe_item("alpha.side_mode", state.alpha.side_mode),
                    describe_item("alpha.candidate_count", state.alpha.candidate_count),
                    describe_item("alpha.top_n_per_cycle", state.alpha.top_n_per_cycle),
                    describe_item("alpha.long_threshold", state.alpha.long_threshold),
                    describe_item("alpha.short_threshold", state.alpha.short_threshold),
                    describe_item("alpha.predicted_return_threshold", state.alpha.predicted_return_threshold),
                    describe_item("alpha.confidence_threshold", state.alpha.confidence_threshold),
                    describe_item(
                        "alpha.edge_after_cost_min_buffer",
                        state.alpha.edge_after_cost_min_buffer,
                    ),
                ],
            ),
            DescriptiveSection(
                title="Risk Controls",
                description="The position limits and protections that constrain how much the profile can put at risk.",
                items=[
                    describe_item("risk.max_positions", state.risk.max_positions),
                    describe_item("risk.max_dollars_per_trade", state.risk.max_dollars_per_trade),
                    describe_item("risk.max_daily_loss_percent", state.risk.max_daily_loss_percent),
                    describe_item("risk.same_symbol_protection", state.risk.same_symbol_protection),
                    describe_item(
                        "risk.higher_timeframe_filter_enabled",
                        state.risk.higher_timeframe_filter_enabled,
                    ),
                    describe_item(
                        "risk.higher_timeframe_source_timeframe",
                        state.risk.higher_timeframe_source_timeframe,
                    ),
                    describe_item(
                        "risk.higher_timeframe_fast_ma_length",
                        state.risk.higher_timeframe_fast_ma_length,
                    ),
                    describe_item(
                        "risk.higher_timeframe_slow_ma_length",
                        state.risk.higher_timeframe_slow_ma_length,
                    ),
                    describe_item(
                        "risk.disable_pseudo_order_book_gate",
                        state.risk.disable_pseudo_order_book_gate,
                    ),
                ],
            ),
            DescriptiveSection(
                title="Execution & Brackets",
                description="The order and bracket settings that shape how approved trades are submitted and protected.",
                items=[
                    describe_item("execution.order_type", state.execution.order_type),
                    describe_item("execution.bracket_enabled", state.execution.bracket_enabled),
                    describe_item("execution.take_profit_percent", state.execution.take_profit_percent),
                    describe_item("execution.stop_loss_percent", state.execution.stop_loss_percent),
                    describe_item("execution.sizing_mode", state.execution.sizing_mode),
                    describe_item("execution.quantity", state.execution.quantity),
                ],
            ),
        ]
        return SetupWizardReviewPayload(
            sections=sections,
            defaults_section=DescriptiveSection(
                title="Recommended Defaults Currently Kept",
                description="These settings still match the recommended starting defaults for the guided workflow.",
                items=[
                    describe_item(
                        dotted_key,
                        self._resolve_dotted_value(state, dotted_key),
                        badge="Recommended default",
                    )
                    for dotted_key in flags["defaults"]
                ],
            ),
            customized_section=DescriptiveSection(
                title="Customized Settings",
                description="These settings differ from the recommended starting defaults and will directly change how the session behaves.",
                items=[
                    describe_item(
                        dotted_key,
                        self._resolve_dotted_value(state, dotted_key),
                        badge="Customized",
                    )
                    for dotted_key in flags["customized"]
                ],
            ),
            expected_actions=self.wizard_service.build_expected_actions(
                state,
                active_symbols=preview_symbols,
            ),
        )

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

    @staticmethod
    def _resolve_dotted_value(state: SetupWizardState, dotted_key: str):
        current = state
        for part in dotted_key.split("."):
            current = getattr(current, part)
        return current
