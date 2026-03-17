from mytradingbot.core.settings import AppSettings


def test_default_mode_is_paper() -> None:
    settings = AppSettings()
    assert settings.runtime.default_mode.value == "paper"


def test_strategy_names_are_canonical() -> None:
    settings = AppSettings()
    assert settings.strategies.available == [
        "scalping",
        "intraday",
        "short_term",
        "long_term",
    ]
