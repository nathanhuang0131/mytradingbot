from __future__ import annotations

import argparse
import logging
from pathlib import Path

from mytradingbot.training.service import AlphaRobustTrainingService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Check alpha-robust training data quality.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--symbols", nargs="*", default=None)
    parser.add_argument("--symbols-file", type=Path, default=None)
    parser.add_argument("--timeframes", nargs="*", default=["1m", "5m", "15m", "1d"])
    parser.add_argument("--min-eligible-symbols", type=int, default=None)
    parser.add_argument("--verbose", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    service = AlphaRobustTrainingService()
    symbols = service.ensure_universe(
        symbols=args.symbols,
        symbols_file=args.symbols_file,
    )
    result = service.run_quality_check(
        symbols=symbols,
        timeframes=args.timeframes,
        minimum_eligible_symbols=args.min_eligible_symbols,
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
