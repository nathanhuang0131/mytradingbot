"""Logging helpers for consistent application setup."""

from __future__ import annotations

import logging


def configure_logging(level: str = "INFO") -> None:
    """Configure the root logger with a simple, repeatable format."""

    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
