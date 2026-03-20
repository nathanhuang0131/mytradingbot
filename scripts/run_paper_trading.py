from __future__ import annotations

import argparse
import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.paper_loop import PaperTradingLoopService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run a dry-run or paper trading session.")
    parser.add_argument("--strategy", default="scalping")
    parser.add_argument("--mode", choices=["dry_run", "paper"], default="paper")
    parser.add_argument("--broker-mode", choices=["local_paper", "alpaca_paper_api"], default="local_paper")
    parser.add_argument("--predictions-file", type=Path, default=None)
    parser.add_argument("--market-data-file", type=Path, default=None)
    parser.add_argument("--loop", action="store_true")
    parser.add_argument("--interval-seconds", type=int, default=300)
    parser.add_argument("--max-cycles", type=int, default=None)
    parser.add_argument("--verbose", action="store_true")
    return parser


def _configure_logging(*, settings: AppSettings, loop: bool, verbose: bool) -> None:
    settings.ensure_runtime_directories()
    handlers: list[logging.Handler] = [logging.StreamHandler()]
    if loop:
        file_handler = RotatingFileHandler(
            settings.paths.logs_dir / "paper_trading_loop.log",
            maxBytes=1_000_000,
            backupCount=5,
            encoding="utf-8",
        )
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s")
        )
        handlers.append(file_handler)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        handlers=handlers,
        force=True,
    )


def _log_startup_banner(*, settings: AppSettings) -> None:
    logging.getLogger(__name__).info(
        "paper_session_startup broker_mode=%s api_base_url=%s runtime_state_db=%s external_broker_submission_enabled=%s ownership_mode=%s",
        settings.broker.broker_mode,
        settings.broker.alpaca_base_url,
        settings.paths.state_dir / settings.runtime_safety.sqlite_filename,
        settings.broker.resolved_external_submission_enabled(),
        settings.broker.ownership_policy,
    )


def main() -> int:
    args = build_parser().parse_args()
    settings = AppSettings()
    settings.broker.broker_mode = args.broker_mode
    _configure_logging(settings=settings, loop=args.loop, verbose=args.verbose)
    _log_startup_banner(settings=settings)

    if args.loop:
        result = PaperTradingLoopService(
            settings=settings,
            predictions_path=args.predictions_file,
            market_snapshot_path=args.market_data_file,
        ).run(
            strategy_name=args.strategy,
            mode=RuntimeMode(args.mode),
            interval_seconds=args.interval_seconds,
            max_cycles=args.max_cycles,
        )
        print(result.model_dump_json(indent=2))
        return 0 if result.ok else 1

    qlib_service = QlibWorkflowService(
        settings=settings,
        predictions_path=args.predictions_file,
    )
    market_data_service = MarketDataService(
        settings=settings,
        market_snapshot_path=args.market_data_file,
    )
    service = TradingPlatformService(
        settings=settings,
        qlib_service=qlib_service,
        market_data_service=market_data_service,
        broker_mode=args.broker_mode,
    )
    result = service.run_session(
        strategy_name=args.strategy,
        mode=RuntimeMode(args.mode),
    )
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
