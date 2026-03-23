from __future__ import annotations

import argparse
import json
import logging

from mytradingbot.core.settings import AppSettings
from mytradingbot.orchestration.alpaca_paper_smoke import AlpacaPaperSmokeService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Submit one bounded Alpaca paper bracket order smoke through the repo."
    )
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", choices=["long", "short"], required=True)
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--leave-open", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        force=True,
    )
    settings = AppSettings()
    settings.broker.broker_mode = "alpaca_paper_api"
    logging.getLogger(__name__).info(
        "alpaca_paper_smoke_start broker_mode=%s api_base_url=%s external_broker_submission_enabled=%s ownership_mode=%s",
        settings.broker.broker_mode,
        settings.broker.alpaca_base_url,
        settings.broker.resolved_external_submission_enabled(),
        settings.broker.ownership_policy,
    )
    result = AlpacaPaperSmokeService(settings=settings).run(
        symbol=args.symbol.upper(),
        side=args.side,
        strategy_name=args.strategy,
        cancel_after_submit=not args.leave_open,
    )
    print(json.dumps(result.model_dump(mode="json"), indent=2))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
