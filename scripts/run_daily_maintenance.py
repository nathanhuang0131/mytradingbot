from __future__ import annotations

import argparse
import logging
from datetime import datetime
from pathlib import Path

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
    parser.add_argument("--symbols-file", type=Path, default=None)
    parser.add_argument("--timeframes", nargs="*", default=None)
    parser.add_argument("--start-date", type=str, default=None)
    parser.add_argument("--end-date", type=str, default=None)
    parser.add_argument("--normalize-only", action="store_true")
    parser.add_argument("--verbose", action="store_true")
    return parser


def _parse_datetime(value: str | None) -> datetime | None:
    if value is None:
        return None
    parsed = datetime.fromisoformat(value)
    return parsed


def main() -> int:
    args = build_parser().parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)
    service = TradingPlatformService.bootstrap_default()
    full_refresh = args.action == "download"
    start_at = _parse_datetime(args.start_date)
    end_at = _parse_datetime(args.end_date)
    data_result = service.download_market_data(
        symbols=args.symbols,
        symbols_file=args.symbols_file,
        timeframes=args.timeframes,
        start_at=start_at,
        end_at=end_at,
        full_refresh=full_refresh,
        normalize_only=args.normalize_only,
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
