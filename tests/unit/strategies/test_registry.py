from mytradingbot.strategies.registry import StrategyRegistry


def test_registry_exposes_only_canonical_strategy_names() -> None:
    registry = StrategyRegistry.build_default()
    assert registry.names() == ["intraday", "long_term", "scalping", "short_term"]


def test_registry_returns_strategy_by_name() -> None:
    registry = StrategyRegistry.build_default()
    assert registry.get("intraday").name == "intraday"
