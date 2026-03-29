from __future__ import annotations

import argparse
import logging

from mytradingbot.universe.service import TopLiquidityUniverseService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate the repo-local top-liquidity universe.")
    parser.add_argument("--top-n", type=int, default=800)
    parser.add_argument("--lookback-days", type=int, default=30)
    parser.add_argument("--min-price", type=float, default=5.0)
    parser.add_argument("--min-avg-volume", type=float, default=500000)
    parser.add_argument("--asset-class", default="us_equity")
    parser.add_argument("--include-etfs", default="false")
    parser.add_argument("--output-prefix", default="top_liquidity_universe")
    parser.add_argument("--verbose", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    if args.verbose:
        logging.getLogger("urllib3").setLevel(logging.WARNING)
        logging.getLogger("alpaca").setLevel(logging.INFO)
    result = TopLiquidityUniverseService().generate_top_liquidity_universe(
        top_n=args.top_n,
        lookback_days=args.lookback_days,
        minimum_price=args.min_price,
        minimum_average_volume=args.min_avg_volume,
        asset_class=args.asset_class,
        include_etfs=str(args.include_etfs).lower() in {"1", "true", "yes", "on"},
        output_prefix=args.output_prefix,
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
