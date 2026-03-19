from __future__ import annotations

import argparse
from pathlib import Path

from mytradingbot.orchestration.service import TradingPlatformService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build the repo-local qlib dataset artifact.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--symbols", nargs="*", default=None)
    parser.add_argument("--symbols-file", type=Path, default=None)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = TradingPlatformService.bootstrap_default().build_dataset(
        strategy_name=args.strategy,
        symbols=args.symbols,
        symbols_file=args.symbols_file,
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
