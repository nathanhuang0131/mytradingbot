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
    data_dir: Path
    docs_dir: Path
    logs_dir: Path
    models_dir: Path
    reports_dir: Path
    scripts_dir: Path
    tests_dir: Path

    @classmethod
    def discover(cls) -> "RepoPaths":
        repo_root = Path(__file__).resolve().parents[3]
        return cls(
            repo_root=repo_root,
            src_dir=repo_root / "src",
            configs_dir=repo_root / "configs",
            data_dir=repo_root / "data",
            docs_dir=repo_root / "docs",
            logs_dir=repo_root / "logs",
            models_dir=repo_root / "models",
            reports_dir=repo_root / "reports",
            scripts_dir=repo_root / "scripts",
            tests_dir=repo_root / "tests",
        )

    def ensure_runtime_directories(self) -> None:
        """Create the mutable runtime directories the app relies on."""

        for path in (self.data_dir, self.logs_dir, self.models_dir, self.reports_dir):
            path.mkdir(parents=True, exist_ok=True)
