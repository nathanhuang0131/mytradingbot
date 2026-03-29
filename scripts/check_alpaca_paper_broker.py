from __future__ import annotations

import argparse
import json

from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.store import RuntimeStateStore


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Probe Alpaca paper Trading API connectivity and bot-owned exposure visibility."
    )
    parser.add_argument("--list-orders", action="store_true")
    parser.add_argument("--strategy", default="scalping")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    settings = AppSettings()
    settings.broker.broker_mode = "alpaca_paper_api"
    store = RuntimeStateStore(settings=settings)
    broker = AlpacaPaperBroker(settings=settings, runtime_store=store)

    preflight = broker.preflight()
    payload: dict[str, object] = {
        "broker_mode": settings.broker.broker_mode,
        "ownership_policy": settings.broker.ownership_policy,
        "api_base_url": settings.broker.alpaca_base_url,
        "external_broker_submission_enabled": settings.broker.resolved_external_submission_enabled(),
        "preflight_ok": preflight.ok,
        "preflight_message": preflight.message,
        "preflight_metadata": preflight.metadata,
    }
    if not preflight.ok:
        print(json.dumps(payload, indent=2))
        return 1

    account = broker.client.get_account()
    reconciliation = broker.reconcile_runtime_state(strategy_name=args.strategy)
    payload.update(
        {
            "account_status": str(getattr(account, "status", "")),
            "buying_power": str(getattr(account, "buying_power", "")),
            "portfolio_value": str(getattr(account, "portfolio_value", "")),
            "bot_owned_open_orders": reconciliation.bot_owned_order_count,
            "bot_owned_open_positions": reconciliation.bot_owned_position_count,
            "foreign_open_orders": reconciliation.foreign_order_count,
            "foreign_open_positions": reconciliation.foreign_position_count,
        }
    )
    if args.list_orders:
        payload["recent_bot_owned_orders"] = [
            {
                "order_id": record.order_id,
                "symbol": record.symbol,
                "status": record.status,
                "client_order_id": record.client_order_id,
            }
            for record in store.list_order_records()[-5:]
            if record.broker_mode == "alpaca_paper_api"
        ]
        payload["recent_foreign_orders"] = [
            {
                "order_id": record.order_id,
                "symbol": record.symbol,
                "status": record.status,
                "ownership_class": record.ownership_class,
                "client_order_id": record.client_order_id,
            }
            for record in store.list_observed_orders()[-5:]
        ]

    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
