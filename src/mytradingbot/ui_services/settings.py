"""Settings UI services."""

from __future__ import annotations

import logging

from mytradingbot.core.settings import AppSettings

logger = logging.getLogger(__name__)


class SettingsService:
    """Expose application settings to the UI."""

    def __init__(self, settings: AppSettings) -> None:
        self.settings = settings

    def get_settings_payload(self) -> dict:
        return self.settings.model_dump(mode="json")
