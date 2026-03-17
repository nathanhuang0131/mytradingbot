from mytradingbot.reporting.service import ReportingService


def test_reporting_service_generates_post_session_review(
    session_result_factory,
) -> None:
    report = ReportingService().build_post_session_review(session_result_factory())

    assert report.session_id
    assert report.trade_count >= 0
