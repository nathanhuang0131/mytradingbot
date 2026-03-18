from __future__ import annotations

import argparse

from mytradingbot.orchestration.service import TradingPlatformService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Train qlib models from repo-local dataset artifacts.")
    parser.add_argument("--strategy", default="scalping")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    result = TradingPlatformService.bootstrap_default().train_models(
        strategy_name=args.strategy
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
