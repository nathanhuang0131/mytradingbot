from __future__ import annotations

import argparse

from mytradingbot.reporting.trading_universe_audit import TradingUniverseAuditService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate a markdown trading universe audit from overnight loop artifacts."
    )
    parser.add_argument(
        "--profile-slug",
        help="Optional profile slug to anchor the audit to a specific saved session profile.",
    )
    parser.add_argument(
        "--lookback-hours",
        type=int,
        default=12,
        help="How many hours of loop sessions to include, anchored to the latest completed session.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report_path = TradingUniverseAuditService().generate(
        profile_slug=args.profile_slug,
        lookback_hours=args.lookback_hours,
    )
    print(report_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
