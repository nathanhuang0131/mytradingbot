from __future__ import annotations

import argparse
import logging
from pathlib import Path

from mytradingbot.training.service import AlphaRobustTrainingService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the institutional alpha-robust training workflow.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--top-n", type=int, default=800)
    parser.add_argument("--symbols", nargs="*", default=None)
    parser.add_argument("--symbols-file", type=Path, default=None)
    parser.add_argument("--timeframes", nargs="*", default=["1m", "5m", "15m", "1d"])
    parser.add_argument("--lookback-1m-days", type=int, default=90)
    parser.add_argument("--lookback-5m-days", type=int, default=180)
    parser.add_argument("--lookback-15m-days", type=int, default=252)
    parser.add_argument("--lookback-1d-days", type=int, default=756)
    parser.add_argument("--min-eligible-symbols", type=int, default=150)
    parser.add_argument("--skip-download", action="store_true")
    parser.add_argument("--skip-train", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    result = AlphaRobustTrainingService().run_alpha_robust_training(
        strategy_name=args.strategy,
        symbols=args.symbols,
        symbols_file=args.symbols_file,
        top_n=args.top_n,
        timeframes=args.timeframes,
        lookback_days={
            "1m": args.lookback_1m_days,
            "5m": args.lookback_5m_days,
            "15m": args.lookback_15m_days,
            "1d": args.lookback_1d_days,
        },
        min_eligible_symbols=args.min_eligible_symbols,
        skip_download=args.skip_download,
        skip_train=args.skip_train,
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
