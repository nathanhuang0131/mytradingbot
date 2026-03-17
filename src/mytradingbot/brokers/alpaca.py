"""Alpaca live broker scaffold for validation-only phase 1 behavior."""

from __future__ import annotations

import logging

from pydantic import BaseModel

logger = logging.getLogger(__name__)


class BrokerCapabilityStatus(BaseModel):
    """Capability status for a broker adapter surface."""

    is_enabled: bool
    message: str


class AlpacaBrokerScaffold:
    """Validation-only live broker scaffold."""

    def get_live_capability_status(self) -> BrokerCapabilityStatus:
        return BrokerCapabilityStatus(
            is_enabled=False,
            message="Live Alpaca order submission is disabled in phase 1.",
        )
