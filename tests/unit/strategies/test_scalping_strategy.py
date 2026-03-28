from mytradingbot.core.models import HigherTimeframeTrend
from mytradingbot.core.settings import AppSettings, ScalpingBracketSettings
from mytradingbot.strategies.scalping import ScalpingStrategy


def test_scalping_rejects_signal_below_return_threshold(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(predicted_return=0.0005))

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


def test_scalping_allows_spread_up_to_six_bps_and_rejects_beyond(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()

    at_limit = strategy.evaluate(signal_bundle_factory(spread_bps=6.0))
    above_limit = strategy.evaluate(signal_bundle_factory(spread_bps=6.01))

    assert at_limit.should_trade
    assert not above_limit.should_trade
    assert "spread_filter" in above_limit.failed_filters


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
    assert decision.intent.bracket_plan is not None
    assert decision.intent.bracket_plan.reward_risk_ratio > 0


def test_scalping_rejects_trade_when_fee_adjusted_expectancy_is_poor(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy(
        settings=AppSettings(
            scalping=ScalpingBracketSettings(
                estimated_slippage_bps=40.0,
                estimated_fee_per_share=0.5,
                minimum_reward_risk_ratio=1.5,
                minimum_net_reward_per_share=0.5,
                edge_after_cost_min_buffer=0.0,
            )
        )
    )

    decision = strategy.evaluate(
        signal_bundle_factory(
            predicted_return=0.055,
            confidence=0.8,
            last_price=10.0,
            vwap=9.9,
            spread_bps=0.5,
            liquidity_score=0.9,
        )
    )

    assert not decision.should_trade
    assert "fee_adjusted_expectancy" in decision.failed_filters


def test_scalping_uses_runtime_configured_predicted_return_threshold(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy(
        settings=AppSettings(
            scalping=ScalpingBracketSettings(predicted_return_threshold=0.02)
        )
    )

    decision = strategy.evaluate(signal_bundle_factory(predicted_return=0.012))

    assert not decision.should_trade
    assert "predicted_return_threshold" in decision.failed_filters


def test_scalping_uses_runtime_configured_confidence_threshold(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy(
        settings=AppSettings(
            scalping=ScalpingBracketSettings(confidence_threshold=0.95)
        )
    )

    decision = strategy.evaluate(signal_bundle_factory(confidence=0.84))

    assert not decision.should_trade
    assert "confidence_threshold" in decision.failed_filters


def test_scalping_does_not_hard_reject_on_order_book_imbalance_proxy_by_default(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(order_book_imbalance=-0.95))

    assert decision.should_trade
    assert "order_book_imbalance" not in decision.failed_filters


def test_scalping_rejects_invalid_vwap_payload_before_market_structure_checks(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(vwap=0.0))

    assert not decision.should_trade
    assert decision.reason == "invalid_signal_payload:vwap_unavailable"
    assert "invalid_signal_payload:vwap_unavailable" in decision.failed_filters


def test_scalping_rejects_invalid_minutes_to_close_payload_with_precise_reason(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(signal_bundle_factory(metadata={"minutes_to_close": "soon"}))

    assert not decision.should_trade
    assert decision.reason == "invalid_signal_payload:minutes_to_close_invalid"
    assert "invalid_signal_payload:minutes_to_close_invalid" in decision.failed_filters


def test_scalping_rejects_when_higher_timeframe_trend_is_not_aligned(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(
        signal_bundle_factory(
            metadata={
                "higher_timeframe_trend": HigherTimeframeTrend(
                    source_timeframe="15m",
                    fast_ma_length=5,
                    slow_ma_length=10,
                    state="bearish",
                    long_allowed=False,
                    short_allowed=True,
                    reason="close_below_vwap_and_fast_below_slow",
                    latest_close=99.0,
                    latest_vwap=100.0,
                    fast_ma=99.1,
                    slow_ma=100.4,
                    slow_ma_slope_bps=-12.0,
                )
            },
        )
    )

    assert not decision.should_trade
    assert "higher_timeframe_trend_alignment" in decision.failed_filters


def test_scalping_rejects_when_edge_after_cost_buffer_is_not_met(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy(
        settings=AppSettings(
            scalping=ScalpingBracketSettings(
                predicted_return_threshold=0.0,
                confidence_threshold=0.0,
                edge_after_cost_min_buffer=0.0015,
                estimated_slippage_bps=4.0,
            )
        )
    )

    decision = strategy.evaluate(
        signal_bundle_factory(
            predicted_return=0.0016,
            spread_bps=5.0,
            liquidity_score=1.0,
            metadata={
                "higher_timeframe_trend": HigherTimeframeTrend(
                    source_timeframe="15m",
                    fast_ma_length=5,
                    slow_ma_length=10,
                    state="bullish",
                    long_allowed=True,
                    short_allowed=False,
                    reason="close_above_vwap_and_fast_above_slow",
                    latest_close=101.0,
                    latest_vwap=100.2,
                    fast_ma=100.8,
                    slow_ma=100.1,
                    slow_ma_slope_bps=8.0,
                )
            },
        )
    )

    assert not decision.should_trade
    assert "edge_after_cost_buffer" in decision.failed_filters


def test_scalping_attaches_quality_snapshot_for_selection(
    signal_bundle_factory,
) -> None:
    strategy = ScalpingStrategy()

    decision = strategy.evaluate(
        signal_bundle_factory(
            metadata={
                "higher_timeframe_trend": HigherTimeframeTrend(
                    source_timeframe="15m",
                    fast_ma_length=5,
                    slow_ma_length=10,
                    state="bullish",
                    long_allowed=True,
                    short_allowed=False,
                    reason="close_above_vwap_and_fast_above_slow",
                    latest_close=101.0,
                    latest_vwap=100.2,
                    fast_ma=100.8,
                    slow_ma=100.1,
                    slow_ma_slope_bps=8.0,
                )
            },
        )
    )

    assert decision.should_trade
    assert decision.quality is not None
    assert decision.quality.expected_edge_after_cost > 0
    assert decision.quality.quality_score > 0
    assert decision.quality.trend.state == "bullish"
