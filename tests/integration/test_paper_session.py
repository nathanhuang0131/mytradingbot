from __future__ import annotations

import json

from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.data.service import MarketDataService
from mytradingbot.orchestration.service import TradingPlatformService
from mytradingbot.qlib_engine.service import QlibWorkflowService


def test_paper_session_runs_end_to_end_with_traceability(tmp_path) -> None:
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
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bullish",
                        "long_allowed": True,
                        "short_allowed": False,
                        "reason": "close_above_vwap_and_fast_above_slow"
                    },
                }
            ]
        ),
        encoding="utf-8",
    )
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(
            settings=settings,
            pyqlib_available=False,
            predictions_path=predictions_path,
        ),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.mode == RuntimeMode.PAPER
    assert result.trade_attempts
    assert result.traceability[0].signal is not None
    assert result.traceability[0].signal.symbol == "AAPL"
    assert result.orders


def test_paper_session_runs_end_to_end_for_short_scalping(tmp_path) -> None:
    predictions_path = tmp_path / "predictions.json"
    market_path = tmp_path / "market.json"
    predictions_path.write_text(
        json.dumps(
            [
                {
                    "symbol": "TSLA",
                    "score": 0.95,
                    "predicted_return": -0.012,
                    "confidence": 0.84,
                    "rank": 1,
                    "direction": "short",
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
                    "symbol": "TSLA",
                    "last_price": 100.0,
                    "vwap": 100.8,
                    "spread_bps": 1.0,
                    "volume": 1500000,
                    "liquidity_score": 0.88,
                    "liquidity_stress": 0.2,
                    "order_book_imbalance": -0.35,
                    "liquidity_sweep_detected": False,
                    "volatility_regime": "normal",
                    "higher_timeframe_trend": {
                        "source_timeframe": "15m",
                        "fast_ma_length": 5,
                        "slow_ma_length": 10,
                        "state": "bearish",
                        "long_allowed": False,
                        "short_allowed": True,
                        "reason": "close_below_vwap_and_fast_below_slow"
                    },
                }
            ]
        ),
        encoding="utf-8",
    )
    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))

    service = TradingPlatformService(
        settings=settings,
        qlib_service=QlibWorkflowService(
            settings=settings,
            pyqlib_available=False,
            predictions_path=predictions_path,
        ),
        market_data_service=MarketDataService(settings=settings, market_snapshot_path=market_path),
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.mode == RuntimeMode.PAPER
    assert result.session_summary.trade_count == 1
    assert result.orders
    assert result.orders[0].side == "sell"
    assert result.positions
    assert result.positions[0].quantity < 0
