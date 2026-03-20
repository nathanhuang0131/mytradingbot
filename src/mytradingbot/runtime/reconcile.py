"""Ownership classification helpers for broker-backed paper reconciliation."""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Iterable

from mytradingbot.runtime.models import OwnershipClass


CLIENT_ORDER_ID_PATTERN = re.compile(r"^[A-Z_]+-[A-Z0-9.\-]+-(BUY|SELL)-\d{12}$")


@dataclass(frozen=True)
class OwnershipClassifier:
    """Classify broker account state into bot-owned or read-only exposure."""

    known_client_order_ids: set[str]
    known_order_ids: set[str]

    def classify_order(self, order, *, parent_ownership: OwnershipClass | None = None) -> OwnershipClass:
        if parent_ownership == "bot_owned":
            return "bot_owned"
        order_id = getattr(order, "id", None)
        if order_id is not None and str(order_id) in self.known_order_ids:
            return "bot_owned"
        client_order_id = getattr(order, "client_order_id", None)
        if client_order_id:
            text = str(client_order_id).upper()
            if text in {value.upper() for value in self.known_client_order_ids}:
                return "bot_owned"
            if CLIENT_ORDER_ID_PATTERN.match(text):
                return "bot_owned"
            return "foreign"
        return "unknown"

    def classify_position(self, *, symbol: str, bot_owned_symbols: Iterable[str]) -> OwnershipClass:
        return "bot_owned" if symbol in set(bot_owned_symbols) else "foreign"

    @staticmethod
    def management_class(ownership_class: OwnershipClass) -> OwnershipClass:
        return "foreign" if ownership_class == "unknown" else ownership_class
