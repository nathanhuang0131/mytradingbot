from __future__ import annotations

import argparse

from mytradingbot.orchestration.service import TradingPlatformService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run canonical repo-local maintenance steps.")
    parser.add_argument(
        "--action",
        choices=["download", "update", "all"],
        default="update",
        help="download=full raw refresh, update=incremental parquet update, all=update plus qlib build/train/refresh",
    )
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--symbols", nargs="*", default=None)
    parser.add_argument("--timeframes", nargs="*", default=None)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    service = TradingPlatformService.bootstrap_default()
    full_refresh = args.action == "download"
    data_result = service.download_market_data(
        symbols=args.symbols,
        timeframes=args.timeframes,
        full_refresh=full_refresh,
    )
    payload = {
        "capabilities": service.get_capabilities().model_dump(mode="json"),
        "data_pipeline": data_result.model_dump(mode="json"),
    }
    if args.action == "all":
        payload["build_dataset"] = service.build_dataset(
            strategy_name=args.strategy
        ).model_dump(mode="json")
        payload["train_models"] = service.train_models(
            strategy_name=args.strategy
        ).model_dump(mode="json")
        payload["refresh_predictions"] = service.refresh_predictions(
            strategy_name=args.strategy
        ).model_dump(mode="json")
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
