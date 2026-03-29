"""Safe reset/archive helpers for repo-local local paper runtime state."""

from __future__ import annotations

import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field

from mytradingbot.core.settings import AppSettings


class LocalPaperResetAction(BaseModel):
    """Single reset action performed for a repo-local local paper artifact."""

    action: Literal["archived", "skipped"]
    relative_path: str
    archived_path: str | None = None
    reason: str | None = None


class LocalPaperResetResult(BaseModel):
    """Structured result for a local paper state reset run."""

    ok: bool
    message: str
    archive_dir: str | None = None
    actions: list[LocalPaperResetAction] = Field(default_factory=list)


class LocalPaperStateResetService:
    """Archive only repo-local local paper runtime state and analytics artifacts."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()

    def reset(self, *, confirm: bool) -> LocalPaperResetResult:
        if not confirm:
            return LocalPaperResetResult(
                ok=False,
                message="Refusing to reset local paper state without --yes.",
            )

        candidates = self._collect_candidates()
        if not candidates:
            return LocalPaperResetResult(
                ok=True,
                message="No repo-local local paper runtime or analytics artifacts matched the reset scope.",
                actions=[],
            )

        archive_root = self._archive_root()
        actions: list[LocalPaperResetAction] = []
        for path in candidates:
            relative_path = self._relative_path(path)
            destination = archive_root / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(path), str(destination))
            actions.append(
                LocalPaperResetAction(
                    action="archived",
                    relative_path=relative_path,
                    archived_path=str(destination),
                )
            )

        self.settings.ensure_runtime_directories()
        return LocalPaperResetResult(
            ok=True,
            message=(
                "Archived repo-local local paper runtime state and analytics artifacts. "
                "Market data, qlib artifacts, universe files, and external broker state were untouched."
            ),
            archive_dir=str(archive_root),
            actions=actions,
        )

    def _archive_root(self) -> Path:
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        archive_root = self.settings.paths.state_dir / "reset_archives" / timestamp
        archive_root.mkdir(parents=True, exist_ok=True)
        return archive_root

    def _collect_candidates(self) -> list[Path]:
        repo_root = self.settings.paths.repo_root.resolve()
        state_db = self.settings.paths.state_dir / self.settings.runtime_safety.sqlite_filename
        candidates: list[Path] = [
            state_db,
            state_db.with_suffix(state_db.suffix + "-wal"),
            state_db.with_suffix(state_db.suffix + "-shm"),
            self.settings.paths.ledger_dir / "signal_outcomes.csv",
            self.settings.paths.ledger_dir / "incidents.csv",
        ]
        candidates.extend(self.settings.paths.logs_dir.glob("paper_trading_loop.log*"))
        for directory in (
            self.settings.paths.reports_signals_dir,
            self.settings.paths.reports_paper_trading_dir,
            self.settings.paths.reports_analytics_dir,
        ):
            if directory.exists():
                candidates.extend(path for path in directory.rglob("*") if path.is_file())

        unique_paths: list[Path] = []
        seen: set[Path] = set()
        for candidate in sorted({path.resolve() for path in candidates if path.exists() and path.is_file()}):
            if not candidate.is_relative_to(repo_root):
                continue
            if candidate in seen:
                continue
            seen.add(candidate)
            unique_paths.append(candidate)
        return unique_paths

    def _relative_path(self, path: Path) -> str:
        return path.resolve().relative_to(self.settings.paths.repo_root.resolve()).as_posix()
