from mytradingbot.diagnostics.service import DiagnosticsService


def test_no_trade_diagnostics_explain_rejections(session_result_factory) -> None:
    report = DiagnosticsService().build_no_trade_report(
        session_result_factory(no_trades=True)
    )

    assert report.summary
    assert report.reasons


def test_prediction_diagnostics_report_stale_artifacts(session_result_factory) -> None:
    diagnostics = DiagnosticsService().build_prediction_diagnostics(
        session_result_factory(stale_prediction=True)
    )

    assert not diagnostics.ok
    assert diagnostics.issues
