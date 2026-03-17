def test_goalcheck_reports_live_mode_gated(script_runner) -> None:
    result = script_runner("scripts/goalcheck.py")

    assert result.returncode == 0
    assert "live trading gated" in result.stdout.lower()
