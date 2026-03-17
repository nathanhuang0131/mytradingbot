from __future__ import annotations

import json

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
                }
            ]
        ),
        encoding="utf-8",
    )

    service = TradingPlatformService(
        qlib_service=QlibWorkflowService(
            pyqlib_available=False,
            predictions_path=predictions_path,
        ),
        market_data_service=MarketDataService(market_snapshot_path=market_path),
    )

    result = service.run_session(strategy_name="scalping", mode=RuntimeMode.PAPER)

    assert result.session_summary.mode == RuntimeMode.PAPER
    assert result.trade_attempts
    assert result.traceability[0].signal is not None
    assert result.traceability[0].signal.symbol == "AAPL"
    assert result.orders
