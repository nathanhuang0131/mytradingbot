"""Persistence helpers for setup-wizard profiles and resolved configs."""

from __future__ import annotations

import json
from pathlib import Path

from mytradingbot.core.settings import AppSettings
from mytradingbot.session_setup.models import ResolvedSessionConfig, UserProfile, slugify_profile_name


class SetupWizardStorage:
    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()
        self.settings.ensure_runtime_directories()

    def list_profiles(self) -> list[UserProfile]:
        profiles: list[UserProfile] = []
        for path in sorted(self.settings.paths.user_profiles_dir.glob("*.json")):
            try:
                profiles.append(UserProfile.model_validate_json(path.read_text(encoding="utf-8")))
            except Exception:
                continue
        return sorted(
            profiles,
            key=lambda item: item.last_used_at or item.updated_at,
            reverse=True,
        )

    def profile_path(self, profile_slug: str) -> Path:
        return self.settings.paths.user_profiles_dir / f"{profile_slug}.json"

    def session_config_path(self, profile_slug: str) -> Path:
        return self.settings.paths.session_profiles_dir / f"{profile_slug}_latest.json"

    def active_symbols_path(self, profile_slug: str) -> Path:
        return self.settings.paths.active_universes_dir / f"{profile_slug}_active_symbols.json"

    def load_profile(self, profile_name_or_slug: str) -> UserProfile:
        profile_slug = slugify_profile_name(profile_name_or_slug)
        path = self.profile_path(profile_slug)
        return UserProfile.model_validate_json(path.read_text(encoding="utf-8"))

    def save_profile(self, profile: UserProfile) -> Path:
        path = self.profile_path(profile.profile_slug)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(profile.model_dump_json(indent=2), encoding="utf-8")
        return path

    def load_latest_session_config(self, profile_slug: str) -> ResolvedSessionConfig | None:
        path = self.session_config_path(profile_slug)
        if not path.exists():
            return None
        return ResolvedSessionConfig.model_validate_json(path.read_text(encoding="utf-8"))

    def save_latest_session_config(self, config: ResolvedSessionConfig) -> Path:
        path = self.session_config_path(config.profile_slug)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(config.model_dump_json(indent=2), encoding="utf-8")
        return path

    def read_active_symbols(self, profile_slug: str) -> list[str]:
        path = self.active_symbols_path(profile_slug)
        if not path.exists():
            return []
        payload = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(payload, list):
            return [str(symbol).strip().upper() for symbol in payload if str(symbol).strip()]
        return []

    def write_active_symbols(self, *, profile_slug: str, symbols: list[str]) -> Path:
        path = self.active_symbols_path(profile_slug)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(list(symbols), indent=2), encoding="utf-8")
        return path
