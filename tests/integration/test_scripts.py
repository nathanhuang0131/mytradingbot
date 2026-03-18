from __future__ import annotations

import json


def test_run_paper_trading_script_executes_without_crashing(
    script_runner,
    tmp_path,
) -> None:
    predictions_path = tmp_path / "predictions.json"
    market_path = tmp_path / "market.json"
    predictions_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "score": 0.95,
                    "predicted_return": 0.012,
                    "confidence": 0.84,
                    "rank": 1,
                    "direction": "long",
                    "horizon": "intraday",
                }
            ]
        ),
        encoding="utf-8",
    )
    market_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "AAPL",
                    "last_price": 100.0,
                    "vwap": 99.4,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": 0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                }
            ]
        ),
        encoding="utf-8",
    )

    result = script_runner(
        "scripts/run_paper_trading.py",
        "--strategy",
        "scalping",
        "--mode",
        "paper",
        "--predictions-file",
        str(predictions_path),
        "--market-data-file",
        str(market_path),
    )

    assert result.returncode == 0
    assert "session_summary" in result.stdout.lower()


def test_build_train_and_refresh_scripts_report_clear_prerequisite_status(script_runner) -> None:
    build = script_runner("scripts/build_qlib_dataset.py", "--strategy", "scalping")
    train = script_runner("scripts/train_models.py", "--strategy", "scalping")
    refresh = script_runner("scripts/refresh_predictions.py", "--strategy", "scalping")

    assert build.returncode == 0
    assert any(
        message in build.stdout.lower()
        for message in [
            "pyqlib",
            "normalized repo-local parquet data is missing",
            "qlib-ready dataset artifact built",
        ]
    )
    assert train.returncode == 0
    assert any(
        message in train.stdout.lower()
        for message in [
            "pyqlib",
            "qlib dataset artifact is missing",
            "qlib model training completed",
        ]
    )
    assert refresh.returncode == 0
    assert any(
        message in refresh.stdout.lower()
        for message in [
            "pyqlib",
            "qlib dataset artifact is missing",
            "predictions refreshed",
        ]
    )


def test_run_daily_maintenance_reports_missing_alpaca_credentials(script_runner) -> None:
    result = script_runner("scripts/run_daily_maintenance.py", "--action", "update")

    assert result.returncode == 0
    assert "credentials" in result.stdout.lower()
