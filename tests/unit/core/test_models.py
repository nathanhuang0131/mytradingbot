from mytradingbot.core.models import ArtifactStatus, TradeAttemptTrace


def test_artifact_status_missing_marks_artifact_not_ready() -> None:
    status = ArtifactStatus.missing("predictions", guidance=["Run prediction refresh."])
    assert status.name == "predictions"
    assert not status.is_ready
    assert status.reason == "missing"
    assert status.guidance == ["Run prediction refresh."]


def test_trade_attempt_trace_preserves_pipeline_state() -> None:
    trace = TradeAttemptTrace.for_symbol("AAPL", strategy_name="scalping")
    assert trace.symbol == "AAPL"
    assert trace.strategy_name == "scalping"
    assert trace.strategy_outcome is None
    assert trace.risk_outcome is None
    assert trace.execution_outcome is None
