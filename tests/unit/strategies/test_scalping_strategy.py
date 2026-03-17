from mytradingbot.strategies.scalping import ScalpingStrategy


def test_scalping_rejects_signal_below_return_threshold(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(predicted_return=0.001))

    assert not decision.should_trade
    assert "predicted_return_threshold" in decision.failed_filters


def test_scalping_rejects_signal_below_confidence_threshold(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(confidence=0.4))

    assert not decision.should_trade
    assert "confidence_threshold" in decision.failed_filters


def test_scalping_rejects_wide_spread(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(spread_bps=9.0))

    assert not decision.should_trade
    assert "spread_filter" in decision.failed_filters


def test_scalping_respects_cooldown_and_near_close_logic(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    cooldown = strategy.evaluate(signal_bundle_factory(cooldown_active=True))
    near_close = strategy.evaluate(signal_bundle_factory(minutes_to_close=5))

    assert "cooldown_logic" in cooldown.failed_filters
    assert "flatten_near_close_logic" in near_close.failed_filters


def test_scalping_generates_exit_plan_for_valid_signal(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory())

    assert decision.should_trade
    assert decision.intent is not None
    assert decision.intent.exit_plan.take_profit is not None
    assert decision.intent.exit_plan.stop_loss is not None
    assert decision.intent.exit_plan.timeout_seconds is not None
