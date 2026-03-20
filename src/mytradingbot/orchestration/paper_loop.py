"""Restart-safe overnight paper-trading loop orchestration."""

from __future__ import annotations

import logging
import time
from pathlib import Path
from typing import Callable

from pydantic import BaseModel, Field

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.settings import AppSettings
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService
from mytradingbot.runtime.models import BrokerMode
from mytradingbot.runtime.service import RuntimeStateService

logger = logging.getLogger(__name__)


class PaperTradingLoopCycleResult(BaseModel):
    cycle_number: int
    ok: bool
    message: str
    session_id: str | None = None
    trade_count: int = 0
    rejection_reasons: list[str] = Field(default_factory=list)
    startup_open_positions: int = 0
    startup_open_brackets: int = 0
    ending_open_positions: int = 0
    ending_open_brackets: int = 0
    analytics_paths: list[str] = Field(default_factory=list)
    broker_mode: BrokerMode = "local_paper"


class PaperTradingLoopResult(BaseModel):
    ok: bool
    message: str
    cycle_count: int
    failure_count: int
    log_path: str
    broker_mode: BrokerMode = "local_paper"
    cycles: list[PaperTradingLoopCycleResult] = Field(default_factory=list)


class PaperTradingLoopService:
    """Run supervised paper-trading cycles against persisted SQLite runtime state."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        predictions_path: Path | None = None,
        market_snapshot_path: Path | None = None,
        platform_factory: Callable[[], TradingPlatformService] | None = None,
        runtime_state_service: RuntimeStateService | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.predictions_path = predictions_path
        self.market_snapshot_path = market_snapshot_path
        self.platform_factory = platform_factory
        self.runtime_state_service = runtime_state_service or RuntimeStateService(settings=self.settings)
        self.log_path = self.settings.paths.logs_dir / "paper_trading_loop.log"

    def run(
        self,
        *,
        strategy_name: str,
        mode: RuntimeMode,
        interval_seconds: int,
        max_cycles: int | None = None,
    ) -> PaperTradingLoopResult:
        cycle_results: list[PaperTradingLoopCycleResult] = []
        failure_count = 0
        cycle_number = 0
        broker_mode = self.runtime_state_service.resolve_broker_mode(mode=mode)

        logger.info(
            "paper_loop_startup broker_mode=%s api_base_url=%s runtime_state_db=%s external_broker_submission_enabled=%s ownership_mode=%s",
            broker_mode,
            self.settings.broker.alpaca_base_url,
            self.runtime_state_service.store.database_path,
            self.settings.broker.resolved_external_submission_enabled(),
            self.settings.broker.ownership_policy,
        )

        while max_cycles is None or cycle_number < max_cycles:
            cycle_number += 1
            startup_state = {"open_positions": 0, "open_brackets": 0}

            try:
                service = self._build_platform_service()
                startup_state = self._startup_reconcile(service, strategy_name=strategy_name)
                logger.info(
                    "Paper loop cycle %s startup reconciliation: open_positions=%s open_brackets=%s",
                    cycle_number,
                    startup_state["open_positions"],
                    startup_state["open_brackets"],
                )
                session_result = service.run_session(
                    strategy_name=strategy_name,
                    mode=mode,
                )
                lifecycle_state = self._lifecycle_reconcile(service, strategy_name=strategy_name)
                cycle_ok = session_result.session_summary.status == "completed"
                if not cycle_ok:
                    failure_count += 1
                cycle_result = PaperTradingLoopCycleResult(
                    cycle_number=cycle_number,
                    ok=cycle_ok,
                    message="Session completed." if cycle_ok else "Session finished with failure status.",
                    session_id=session_result.session_summary.session_id,
                    trade_count=session_result.session_summary.trade_count,
                    rejection_reasons=session_result.rejection_reasons,
                    startup_open_positions=startup_state["open_positions"],
                    startup_open_brackets=startup_state["open_brackets"],
                    ending_open_positions=lifecycle_state["open_positions"],
                    ending_open_brackets=lifecycle_state["open_brackets"],
                    analytics_paths=lifecycle_state["analytics_paths"],
                    broker_mode=broker_mode,
                )
                logger.info(
                    "Paper loop cycle %s completed: ok=%s trade_count=%s ending_open_positions=%s ending_open_brackets=%s",
                    cycle_number,
                    cycle_ok,
                    cycle_result.trade_count,
                    cycle_result.ending_open_positions,
                    cycle_result.ending_open_brackets,
                )
            except Exception as exc:  # pragma: no cover - defensive loop safety
                failure_count += 1
                self.runtime_state_service.build_incident(
                    context=None,
                    code="paper_loop_cycle_failure",
                    summary=f"Paper loop cycle {cycle_number} failed.",
                    detail=str(exc),
                    severity="error",
                    metadata={"cycle_number": cycle_number},
                )
                analytics_paths = self.runtime_state_service.materialize_closed_trade_analytics()
                logger.exception("Paper loop cycle %s failed: %s", cycle_number, exc)
                cycle_result = PaperTradingLoopCycleResult(
                    cycle_number=cycle_number,
                    ok=False,
                    message=str(exc),
                    startup_open_positions=startup_state["open_positions"],
                    startup_open_brackets=startup_state["open_brackets"],
                    ending_open_positions=startup_state["open_positions"],
                    ending_open_brackets=startup_state["open_brackets"],
                    analytics_paths=analytics_paths,
                    broker_mode=broker_mode,
                )

            cycle_results.append(cycle_result)
            if max_cycles is not None and cycle_number >= max_cycles:
                break
            logger.info("Paper loop sleeping for %s seconds.", interval_seconds)
            time.sleep(interval_seconds)

        ok = failure_count == 0
        return PaperTradingLoopResult(
            ok=ok,
            message="Paper trading loop completed without cycle failures."
            if ok
            else "Paper trading loop completed with one or more cycle failures.",
            cycle_count=cycle_number,
            failure_count=failure_count,
            log_path=str(self.log_path),
            broker_mode=broker_mode,
            cycles=cycle_results,
        )

    def _build_platform_service(self) -> TradingPlatformService:
        if self.platform_factory is not None:
            return self.platform_factory()
        return TradingPlatformService(
            settings=self.settings,
            qlib_service=QlibWorkflowService(
                settings=self.settings,
                predictions_path=self.predictions_path,
            ),
            market_data_service=MarketDataService(
                settings=self.settings,
                market_snapshot_path=self.market_snapshot_path,
            ),
            runtime_state_service=RuntimeStateService(settings=self.settings),
        )

    @staticmethod
    def _startup_reconcile(service: TradingPlatformService, *, strategy_name: str) -> dict[str, int]:
        service.broker.reconcile_runtime_state(strategy_name=strategy_name)
        return {
            "open_positions": len([position for position in service.broker.list_positions() if abs(position.quantity) > 0]),
            "open_brackets": len([bracket for bracket in service.broker.list_brackets() if bracket.status == "armed"]),
        }

    @staticmethod
    def _lifecycle_reconcile(service: TradingPlatformService, *, strategy_name: str) -> dict[str, int | list[str]]:
        service.broker.reconcile_runtime_state(strategy_name=strategy_name)
        analytics_paths = service.runtime_state_service.materialize_closed_trade_analytics()
        return {
            "open_positions": len([position for position in service.broker.list_positions() if abs(position.quantity) > 0]),
            "open_brackets": len([bracket for bracket in service.broker.list_brackets() if bracket.status == "armed"]),
            "analytics_paths": analytics_paths,
        }
