from __future__ import annotations

import argparse
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a dry-run or paper trading session.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--mode", choices=["dry_run", "paper"], default="paper")
    parser.add_argument("--predictions-file", type=Path, default=None)
    parser.add_argument("--market-data-file", type=Path, default=None)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    qlib_service = QlibWorkflowService(
        predictions_path=args.predictions_file,
    )
    market_data_service = MarketDataService(
        market_snapshot_path=args.market_data_file,
    )
    service = TradingPlatformService(
        qlib_service=qlib_service,
        market_data_service=market_data_service,
    )
    result = service.run_session(
        strategy_name=args.strategy,
        mode=RuntimeMode(args.mode),
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
