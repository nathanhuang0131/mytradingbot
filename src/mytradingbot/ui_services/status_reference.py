"""Profile-aware status-reference payloads for Streamlit."""

from __future__ import annotations

import csv

from pydantic import BaseModel, Field

from mytradingbot.core.models import SessionSummary
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.runtime.models import PaperTradingSessionReport
from mytradingbot.session_setup.storage import SetupWizardStorage
from mytradingbot.ui_services.descriptive_sections import DescriptiveSection, describe_item


class TradingTrackActivity(BaseModel):
    """Recent ledger activity shown in the status reference page."""

    timestamp: str
    symbol: str
    outcome: str
    signal_source: str | None = None
    predicted_return: float | None = None
    rejection_reason: str | None = None


class TradingTrackPayload(BaseModel):
    """Readable summary of current and saved trading activity."""

    description: str
    current_session: SessionSummary | None = None
    latest_saved_session: PaperTradingSessionReport | None = None
    recent_activity: list[TradingTrackActivity] = Field(default_factory=list)


class StatusReferencePayload(BaseModel):
    """Payload consumed by the Status Reference page."""

    profile_names: list[str] = Field(default_factory=list)
    default_profile_name: str | None = None
    selected_profile_name: str | None = None
    sections: list[DescriptiveSection] = Field(default_factory=list)
    trading_track: TradingTrackPayload


class StatusReferenceService:
    """Build readable profile and trading-status payloads for Streamlit."""

    def __init__(
        self,
        platform_service: TradingPlatformService,
        *,
        storage: SetupWizardStorage | None = None,
    ) -> None:
        self.platform_service = platform_service
        self.storage = storage or SetupWizardStorage(settings=self.platform_service.settings)

    def get_payload(self, profile_name: str | None = None) -> StatusReferencePayload:
        profiles = self.storage.list_profiles()
        profile_names = [profile.profile_name for profile in profiles]
        default_profile_name = profile_names[0] if profile_names else None
        selected_profile_name = profile_name or default_profile_name

        sections: list[DescriptiveSection] = []
        if selected_profile_name is not None:
            profile = self.storage.load_profile(selected_profile_name)
            latest_config = self.storage.load_latest_session_config(profile.profile_slug)
            if latest_config is not None:
                sections = self._build_sections(profile.profile_name, latest_config)

        return StatusReferencePayload(
            profile_names=profile_names,
            default_profile_name=default_profile_name,
            selected_profile_name=selected_profile_name,
            sections=sections,
            trading_track=self._build_trading_track(),
        )

    def _build_sections(self, profile_name: str, config) -> list[DescriptiveSection]:
        settings = self.platform_service.settings
        prediction_status = self.platform_service.get_prediction_status()
        market_status = self.platform_service.runtime_state_service.market_snapshot_status(
            market_snapshot_path=self.platform_service.market_data_service.market_snapshot_path
        )

        return [
            DescriptiveSection(
                title="Profile & Session",
                description="The saved profile currently selected and the top-level session choices attached to it.",
                items=[
                    describe_item("profile.profile_name", profile_name),
                    describe_item("strategy.preset_name", config.preset_name),
                    describe_item("strategy.strategy_name", config.strategy.strategy_name),
                    describe_item("strategy.run_type", config.strategy.run_type.value),
                    describe_item("strategy.broker_mode", config.strategy.broker_mode),
                    describe_item("strategy.session_mode", config.strategy.session_mode),
                ],
            ),
            DescriptiveSection(
                title="Universe",
                description="The saved symbol-universe settings that define how this profile chooses its active symbols.",
                items=[
                    describe_item("universe.selection_mode", config.universe.selection_mode),
                    describe_item("universe.target_symbol_count", config.universe.target_symbol_count),
                    describe_item("universe.min_price", config.universe.min_price),
                    describe_item("universe.min_average_volume", config.universe.min_average_volume),
                    describe_item("universe.include_etfs", config.universe.include_etfs),
                    describe_item("universe.active_symbol_count", config.universe.active_symbol_count),
                    describe_item("universe.active_symbols_path", config.active_symbols_path),
                ],
            ),
            DescriptiveSection(
                title="Refresh Policy",
                description="How the runtime keeps market, dataset, and prediction artifacts fresh for this profile.",
                items=[
                    describe_item("refresh.auto_refresh_market_snapshot", config.refresh.auto_refresh_market_snapshot),
                    describe_item("refresh.auto_refresh_predictions", config.refresh.auto_refresh_predictions),
                    describe_item("refresh.auto_refresh_dataset", config.refresh.auto_refresh_dataset),
                    describe_item("refresh.loop_interval_seconds", config.refresh.loop_interval_seconds),
                    describe_item("refresh.market_refresh_interval_seconds", config.refresh.market_refresh_interval_seconds),
                    describe_item("refresh.prediction_refresh_interval_seconds", config.refresh.prediction_refresh_interval_seconds),
                    describe_item("refresh.dataset_refresh_interval_seconds", config.refresh.dataset_refresh_interval_seconds),
                    describe_item("refresh.stale_input_behavior", config.refresh.stale_input_behavior),
                ],
            ),
            DescriptiveSection(
                title="Alpha & Model",
                description="The qlib forecast gating and ranking settings that shape the candidate list for this profile.",
                items=[
                    describe_item("alpha.use_latest_trained_model", config.alpha.use_latest_trained_model),
                    describe_item("alpha.side_mode", config.alpha.side_mode),
                    describe_item("alpha.refresh_predictions_before_run", config.alpha.refresh_predictions_before_run),
                    describe_item("alpha.candidate_count", config.alpha.candidate_count),
                    describe_item("alpha.long_threshold", config.alpha.long_threshold),
                    describe_item("alpha.short_threshold", config.alpha.short_threshold),
                    describe_item("alpha.predicted_return_threshold", config.alpha.predicted_return_threshold),
                    describe_item("alpha.confidence_threshold", config.alpha.confidence_threshold),
                    describe_item("alpha.model_artifact_path", config.alpha.model_artifact_path),
                ],
            ),
            DescriptiveSection(
                title="Risk Controls",
                description="The exposure, cooldown, and protection limits saved for this profile.",
                items=[
                    describe_item("risk.max_positions", config.risk.max_positions),
                    describe_item("risk.max_dollars_per_trade", config.risk.max_dollars_per_trade),
                    describe_item("risk.max_daily_loss_percent", config.risk.max_daily_loss_percent),
                    describe_item("risk.same_symbol_protection", config.risk.same_symbol_protection),
                    describe_item("risk.max_positions_long", config.risk.max_positions_long),
                    describe_item("risk.max_positions_short", config.risk.max_positions_short),
                    describe_item("risk.cooldown_minutes", config.risk.cooldown_minutes),
                    describe_item("risk.block_foreign_manual_exposure", config.risk.block_foreign_manual_exposure),
                    describe_item("risk.shortability_gate_policy", config.risk.shortability_gate_policy),
                    describe_item("risk.reversal_policy", config.risk.reversal_policy),
                    describe_item("risk.regime_gating_enabled", config.risk.regime_gating_enabled),
                ],
            ),
            DescriptiveSection(
                title="Execution & Brackets",
                description="The saved order-routing and bracket-planning settings applied when this profile trades.",
                items=[
                    describe_item("execution.order_type", config.execution.order_type),
                    describe_item("execution.bracket_enabled", config.execution.bracket_enabled),
                    describe_item("execution.take_profit_percent", config.execution.take_profit_percent),
                    describe_item("execution.stop_loss_percent", config.execution.stop_loss_percent),
                    describe_item("execution.sizing_mode", config.execution.sizing_mode),
                    describe_item("execution.quantity", config.execution.quantity),
                    describe_item("execution.penny_normalization", config.execution.penny_normalization),
                    describe_item("execution.market_open_only", config.execution.market_open_only),
                    describe_item("execution.allow_after_hours_submission", config.execution.allow_after_hours_submission),
                    describe_item("execution.smoke_order_behavior", config.execution.smoke_order_behavior),
                ],
            ),
            DescriptiveSection(
                title="Artifact Readiness",
                description="The current repo-local runtime artifact state that determines whether a session can proceed cleanly.",
                items=[
                    describe_item(
                        "artifacts.predictions_ready",
                        "Ready" if prediction_status.is_ready else f"{prediction_status.reason or 'Unavailable'}",
                        label="Prediction artifact",
                        description="The readiness state of the current qlib prediction artifact.",
                        effect="If predictions are stale or missing, trading and forecast review become unreliable or blocked.",
                    ),
                    describe_item(
                        "artifacts.predictions_age",
                        prediction_status.freshness_minutes,
                        label="Prediction artifact age",
                        description="How old the current prediction artifact is, measured in minutes when available.",
                        effect="Helps explain whether the forecast is still fresh enough for runtime decisions.",
                    ),
                    describe_item(
                        "artifacts.market_snapshot_ready",
                        "Ready" if market_status.is_ready else f"{market_status.reason or 'Unavailable'}",
                        label="Market snapshot",
                        description="The readiness state of the current market snapshot artifact.",
                        effect="If the snapshot is stale or missing, the runtime blocks or risks acting on outdated market structure.",
                    ),
                    describe_item(
                        "artifacts.market_snapshot_age",
                        market_status.freshness_minutes,
                        label="Market snapshot age",
                        description="How old the current market snapshot artifact is, measured in minutes when available.",
                        effect="Helps explain whether price and microstructure inputs are fresh enough for trading.",
                    ),
                    describe_item(
                        "artifacts.model_path",
                        settings.qlib_model_artifact_path(),
                        label="Model artifact path",
                        description="The repo-local model file used by the qlib workflow unless a custom override is selected.",
                        effect="Shows which trained model artifact the platform is using for prediction refresh.",
                    ),
                    describe_item(
                        "artifacts.dataset_path",
                        settings.qlib_dataset_artifact_path(),
                        label="Dataset artifact path",
                        description="The repo-local dataset artifact used as the qlib prediction input.",
                        effect="Shows where the current feature dataset lives for training and refresh operations.",
                    ),
                ],
            ),
        ]

    def _build_trading_track(self) -> TradingTrackPayload:
        return TradingTrackPayload(
            description=(
                "Current-session data comes from this live Streamlit app session when available. "
                "Saved history comes from the latest repo-local paper-session and signal ledger artifacts."
            ),
            current_session=(
                self.platform_service.last_session_result.session_summary
                if self.platform_service.last_session_result is not None
                else None
            ),
            latest_saved_session=self._latest_saved_session(),
            recent_activity=self._recent_activity(),
        )

    def _latest_saved_session(self) -> PaperTradingSessionReport | None:
        report_files = sorted(
            self.platform_service.settings.paths.reports_paper_trading_dir.glob("*_paper_session.json"),
            key=lambda path: path.stat().st_mtime,
            reverse=True,
        )
        for path in report_files:
            try:
                return PaperTradingSessionReport.model_validate_json(path.read_text(encoding="utf-8"))
            except Exception:
                continue
        return None

    def _recent_activity(self, limit: int = 10) -> list[TradingTrackActivity]:
        ledger_path = self.platform_service.settings.paths.ledger_dir / "signal_outcomes.csv"
        if not ledger_path.exists():
            return []
        rows: list[TradingTrackActivity] = []
        with ledger_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                rows.append(
                    TradingTrackActivity(
                        timestamp=row.get("timestamp", ""),
                        symbol=row.get("symbol", ""),
                        outcome=row.get("final_decision_status", ""),
                        signal_source=row.get("signal_source"),
                        predicted_return=(
                            float(row["predicted_return"])
                            if row.get("predicted_return")
                            else None
                        ),
                        rejection_reason=row.get("rejection_reason_code") or None,
                    )
                )
        return sorted(rows, key=lambda item: item.timestamp, reverse=True)[:limit]
