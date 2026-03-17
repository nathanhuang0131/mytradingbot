from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

from mytradingbot.qlib_engine.service import QlibWorkflowService


def test_missing_pyqlib_blocks_refresh_with_explicit_guidance(tmp_path) -> None:
    service = QlibWorkflowService(
        pyqlib_available=False,
        predictions_path=tmp_path / "latest.json",
    )

    result = service.refresh_predictions()

    assert not result.ok
    assert any("pyqlib" in line.lower() for line in result.guidance)


def test_missing_prediction_artifact_fails_clearly(tmp_path) -> None:
    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=tmp_path / "latest.json",
    )

    result = service.load_predictions()

    assert not result.ok
    assert "refresh" in result.message.lower()


def test_stale_prediction_artifact_is_reported(tmp_path) -> None:
    artifact_path = tmp_path / "latest.json"
    artifact_path.write_text("[]", encoding="utf-8")
    old_time = datetime.now(timezone.utc) - timedelta(minutes=90)
    timestamp = old_time.timestamp()

    import os

    os.utime(artifact_path, (timestamp, timestamp))

    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=artifact_path,
        freshness_threshold_minutes=30,
    )

    result = service.get_runtime_prediction_status()

    assert not result.is_ready
    assert result.reason == "stale"


def test_prediction_artifact_loads_typed_predictions(tmp_path) -> None:
    artifact_path = tmp_path / "latest.json"
    artifact_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.87,
                    "predicted_return": 0.014,
                    "confidence": 0.82,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                }
            ]
        ),
        encoding="utf-8",
    )

    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=artifact_path,
    )

    result = service.load_predictions()

    assert result.ok
    assert result.predictions[0].symbol == "AAPL"


def test_prediction_artifact_with_utf8_bom_loads_cleanly(tmp_path) -> None:
    artifact_path = tmp_path / "latest.json"
    artifact_path.write_text(
        "\ufeff"
        + json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.87,
                    "predicted_return": 0.014,
                    "confidence": 0.82,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                }
            ]
        ),
        encoding="utf-8",
    )

    service = QlibWorkflowService(
        pyqlib_available=True,
        predictions_path=artifact_path,
    )

    result = service.load_predictions()

    assert result.ok
    assert result.predictions[0].symbol == "AAPL"
