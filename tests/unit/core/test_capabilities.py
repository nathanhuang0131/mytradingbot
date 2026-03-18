from __future__ import annotations

from mytradingbot.core.capabilities import CapabilityService
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings


def test_phase_one_remains_available_without_pyqlib_or_alpaca(tmp_path) -> None:
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))

    snapshot = CapabilityService(
        settings=settings,
        pyqlib_available=False,
        alpaca_sdk_available=False,
    ).detect()

    assert snapshot.phase_1.status == "partial"
    assert snapshot.phase_1.works_without_pyqlib
    assert snapshot.phase_1.works_without_alpaca_credentials
    assert snapshot.phase_2.status == "blocked"
    assert snapshot.phase_3.status == "blocked"


def test_phase_two_reports_missing_alpaca_credentials_clearly(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("ALPACA_API_KEY", raising=False)
    monkeypatch.delenv("ALPACA_SECRET_KEY", raising=False)
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))

    snapshot = CapabilityService(
        settings=settings,
        pyqlib_available=False,
        alpaca_sdk_available=True,
    ).detect()

    assert snapshot.phase_2.status == "blocked"
    assert any("alpaca" in line.lower() for line in snapshot.phase_2.guidance)


def test_phase_three_reports_missing_pyqlib_clearly(tmp_path, monkeypatch) -> None:
    monkeypatch.chdir(tmp_path)
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))

    snapshot = CapabilityService(
        settings=settings,
        pyqlib_available=False,
        alpaca_sdk_available=True,
    ).detect()

    assert snapshot.phase_3.status == "blocked"
    assert any("pyqlib" in line.lower() for line in snapshot.phase_3.guidance)
