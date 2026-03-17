from mytradingbot.llm.service import AdvisoryLLMService


def test_signal_explanation_uses_artifacts_without_overriding_direction(
    session_result_factory,
) -> None:
    attempt = session_result_factory().trade_attempts[0]

    response = AdvisoryLLMService(client=None).explain_signal(attempt)

    assert response.mode == "advisory"
    assert "qlib" in response.summary.lower()


def test_strategy_comparison_returns_structured_summary(
    session_result_factory,
) -> None:
    service = AdvisoryLLMService(client=None)
    comparison = service.compare_strategies(
        [session_result_factory(), session_result_factory(no_trades=True)]
    )

    assert comparison.mode == "advisory"
    assert comparison.details
