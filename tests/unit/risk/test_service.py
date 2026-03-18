from mytradingbot.core.enums import RuntimeMode
from mytradingbot.risk.service import RiskEngine


def test_risk_engine_blocks_live_orders_in_phase_one(approved_trade_intent) -> None:
    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.LIVE)

    assert not decision.approved
    assert decision.reason == "live_mode_disabled"


def test_risk_engine_approves_valid_paper_trade(approved_trade_intent) -> None:
    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)

    assert decision.approved
    assert decision.intent is not None


def test_risk_engine_rejects_trade_above_position_limit(approved_trade_intent) -> None:
    approved_trade_intent.quantity = 50

    decision = RiskEngine(max_position_size=10).evaluate(
        intent=approved_trade_intent,
        mode=RuntimeMode.PAPER,
    )

    assert not decision.approved
    assert decision.reason == "max_position_size_exceeded"


def test_risk_engine_rejects_scalping_buy_without_bracket_plan(approved_trade_intent) -> None:
    approved_trade_intent.bracket_plan = None

    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.PAPER)

    assert not decision.approved
    assert decision.reason == "missing_bracket_plan"
