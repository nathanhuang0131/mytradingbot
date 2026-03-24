"""Repository-relative path discovery helpers."""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict


class RepoPaths(BaseModel):
    """Repository-relative filesystem locations used by the app."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    repo_root: Path
    src_dir: Path
    configs_dir: Path
    user_profiles_dir: Path
    data_dir: Path
    raw_data_dir: Path
    normalized_data_dir: Path
    snapshots_dir: Path
    qlib_dir: Path
    runtime_dir: Path
    session_profiles_dir: Path
    active_universes_dir: Path
    universe_dir: Path
    ledger_dir: Path
    state_dir: Path
    docs_dir: Path
    logs_dir: Path
    models_dir: Path
    reports_dir: Path
    reports_data_dir: Path
    reports_universe_dir: Path
    reports_training_dir: Path
    reports_pipeline_dir: Path
    reports_signals_dir: Path
    reports_paper_trading_dir: Path
    reports_analytics_dir: Path
    scripts_dir: Path
    tests_dir: Path

    @classmethod
    def discover(cls) -> "RepoPaths":
        repo_root = Path(__file__).resolve().parents[3]
        return cls.for_root(repo_root)

    @classmethod
    def for_root(cls, repo_root: Path) -> "RepoPaths":
        return cls(
            repo_root=repo_root,
            src_dir=repo_root / "src",
            configs_dir=repo_root / "configs",
            user_profiles_dir=repo_root / "configs" / "user_profiles",
            data_dir=repo_root / "data",
            raw_data_dir=repo_root / "data" / "raw",
            normalized_data_dir=repo_root / "data" / "normalized",
            snapshots_dir=repo_root / "data" / "snapshots",
            qlib_dir=repo_root / "data" / "qlib",
            runtime_dir=repo_root / "data" / "runtime",
            session_profiles_dir=repo_root / "data" / "runtime" / "session_profiles",
            active_universes_dir=repo_root / "data" / "runtime" / "active_universes",
            universe_dir=repo_root / "data" / "universe",
            ledger_dir=repo_root / "data" / "ledger",
            state_dir=repo_root / "data" / "state",
            docs_dir=repo_root / "docs",
            logs_dir=repo_root / "logs",
            models_dir=repo_root / "models",
            reports_dir=repo_root / "reports",
            reports_data_dir=repo_root / "reports" / "data",
            reports_universe_dir=repo_root / "reports" / "universe",
            reports_training_dir=repo_root / "reports" / "training",
            reports_pipeline_dir=repo_root / "reports" / "pipeline",
            reports_signals_dir=repo_root / "reports" / "signals",
            reports_paper_trading_dir=repo_root / "reports" / "paper_trading",
            reports_analytics_dir=repo_root / "reports" / "analytics",
            scripts_dir=repo_root / "scripts",
            tests_dir=repo_root / "tests",
        )

    def ensure_runtime_directories(self) -> None:
        """Create the mutable runtime directories the app relies on."""

        for path in (
            self.data_dir,
            self.user_profiles_dir,
            self.raw_data_dir,
            self.normalized_data_dir,
            self.snapshots_dir,
            self.qlib_dir,
            self.runtime_dir,
            self.session_profiles_dir,
            self.active_universes_dir,
            self.universe_dir,
            self.ledger_dir,
            self.state_dir,
            self.logs_dir,
            self.models_dir,
            self.reports_dir,
            self.reports_data_dir,
            self.reports_universe_dir,
            self.reports_training_dir,
            self.reports_pipeline_dir,
            self.reports_signals_dir,
            self.reports_paper_trading_dir,
            self.reports_analytics_dir,
        ):
            path.mkdir(parents=True, exist_ok=True)
