from __future__ import annotations

import argparse
import time
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.orchestration.institutional import InstitutionalPipelineService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run supervised institutional paper-trading cycles.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--symbols", nargs="*", default=None)
    parser.add_argument("--symbols-file", type=Path, default=None)
    parser.add_argument("--timeframes", nargs="*", default=["1m", "5m", "15m", "1d"])
    parser.add_argument("--interval-seconds", type=int, default=60)
    parser.add_argument("--cycles", type=int, default=1, help="Set 0 for continuous supervised execution.")
    parser.add_argument("--use-top-liquidity-universe", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    service = InstitutionalPipelineService()
    cycle = 0
    while True:
        cycle += 1
        result = service.run(
            strategy_name=args.strategy,
            mode=RuntimeMode.PAPER,
            symbols=args.symbols,
            symbols_file=args.symbols_file,
            timeframes=args.timeframes,
            use_top_liquidity_universe=args.use_top_liquidity_universe,
        )
        print(result.model_dump_json(indent=2))
        if args.cycles and cycle >= args.cycles:
            return 0 if result.ok else 1
        time.sleep(args.interval_seconds)


if __name__ == "__main__":
    raise SystemExit(main())
