from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.ui_services.strategy_control import StrategyControlService


def test_strategy_control_service_surfaces_modes_and_mapping() -> None:
    payload = StrategyControlService(
        TradingPlatformService.bootstrap_default()
    ).get_control_payload()

    assert payload.available_strategies == [
        "intraday",
        "long_term",
        "scalping",
        "short_term",
    ]
    assert payload.available_modes == ["dry_run", "paper", "live"]
    assert not payload.live_trading_enabled
