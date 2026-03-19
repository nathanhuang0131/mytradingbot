from __future__ import annotations

import argparse
import logging
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.orchestration.institutional import InstitutionalPipelineService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the canonical institutional one-command pipeline.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--symbols", nargs="*", default=None)
    parser.add_argument("--symbols-file", type=Path, default=None)
    parser.add_argument("--timeframes", nargs="*", default=["1m", "5m", "15m", "1d"])
    parser.add_argument("--skip-train", action="store_true")
    parser.add_argument("--skip-maintenance", action="store_true")
    parser.add_argument("--skip-validation", action="store_true")
    parser.add_argument("--mode", choices=["dry_run", "paper"], default="paper")
    parser.add_argument("--use-top-liquidity-universe", action="store_true")
    parser.add_argument("--top-n", type=int, default=800)
    parser.add_argument("--min-eligible-symbols", type=int, default=None)
    parser.add_argument("--verbose", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    result = InstitutionalPipelineService().run(
        strategy_name=args.strategy,
        mode=RuntimeMode(args.mode),
        symbols=args.symbols,
        symbols_file=args.symbols_file,
        timeframes=args.timeframes,
        use_top_liquidity_universe=args.use_top_liquidity_universe,
        top_n=args.top_n,
        min_eligible_symbols=args.min_eligible_symbols,
        skip_train=args.skip_train,
        skip_maintenance=args.skip_maintenance,
        skip_validation=args.skip_validation,
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
