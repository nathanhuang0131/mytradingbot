from __future__ import annotations

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.reset import LocalPaperStateResetService


def test_local_paper_reset_requires_explicit_confirmation(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    state_path = settings.paths.state_dir / settings.runtime_safety.sqlite_filename
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.write_text("sqlite-placeholder", encoding="utf-8")

    result = LocalPaperStateResetService(settings=settings).reset(confirm=False)

    assert not result.ok
    assert state_path.exists()
    assert result.archive_dir is None


def test_local_paper_reset_archives_only_repo_local_runtime_and_analytics_scope(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.ensure_runtime_directories()

    reset_targets = [
        settings.paths.state_dir / settings.runtime_safety.sqlite_filename,
        settings.paths.ledger_dir / "signal_outcomes.csv",
        settings.paths.reports_analytics_dir / "pnl_summary.md",
        settings.paths.reports_signals_dir / "latest_decision_audit.md",
        settings.paths.reports_paper_trading_dir / "latest_session.md",
        settings.paths.logs_dir / "paper_trading_loop.log",
    ]
    protected_targets = [
        settings.paths.raw_data_dir / "alpaca" / "bars" / "1m" / "AAPL.parquet",
        settings.paths.qlib_dir / "dataset.parquet",
        settings.paths.universe_dir / "latest_top_liquidity_universe.json",
        settings.paths.repo_root / "README.md",
    ]

    for path in reset_targets + protected_targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists():
            path.write_text(f"fixture:{path.name}", encoding="utf-8")

    result = LocalPaperStateResetService(settings=settings).reset(confirm=True)

    assert result.ok
    assert result.archive_dir is not None
    for path in reset_targets:
        assert not path.exists()
    for path in protected_targets:
        assert path.exists()

    archived_names = {
        action.relative_path
        for action in result.actions
        if action.action == "archived"
    }
    assert "data/state/institutional_runtime.sqlite3" in archived_names
    assert "reports/analytics/pnl_summary.md" in archived_names
    assert "logs/paper_trading_loop.log" in archived_names
