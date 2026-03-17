"""Core exception types for explicit runtime failures."""

from __future__ import annotations


class TradingBotError(Exception):
    """Base exception for platform-specific failures."""


class ConfigurationError(TradingBotError):
    """Raised when application configuration is invalid."""


class ArtifactUnavailableError(TradingBotError):
    """Raised when a required runtime artifact is missing or stale."""
