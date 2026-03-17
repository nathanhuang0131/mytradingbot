"""Core enumerations used across the trading platform."""

from __future__ import annotations

from enum import Enum


class RuntimeMode(str, Enum):
    """Supported operator-visible runtime modes."""

    DRY_RUN = "dry_run"
    PAPER = "paper"
    LIVE = "live"


class StrategyName(str, Enum):
    """Canonical user-facing strategy names."""

    SCALPING = "scalping"
    INTRADAY = "intraday"
    SHORT_TERM = "short_term"
    LONG_TERM = "long_term"


class DiagnosticsLevel(str, Enum):
    """Severity levels for operator diagnostics."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
