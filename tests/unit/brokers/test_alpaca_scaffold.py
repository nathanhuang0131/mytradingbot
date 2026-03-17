def test_alpaca_scaffold_reports_live_submission_disabled() -> None:
    from mytradingbot.brokers.alpaca import AlpacaBrokerScaffold

    status = AlpacaBrokerScaffold().get_live_capability_status()

    assert not status.is_enabled
    assert "disabled" in status.message.lower()
