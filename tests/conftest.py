from __future__ import annotations

import sys
import subprocess
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = PROJECT_ROOT / "src"

if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from mytradingbot.core.models import (
    HigherTimeframeTrend,
    MarketSnapshot,
    MicrostructureProxySignal,
    QlibPrediction,
    SignalBundle,
    TradeIntent,
)
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import (
    ArtifactStatus,
    BracketPlan,
    HealthStatus,
    SessionResult,
    SessionSummary,
    TradeAttemptTrace,
)


@pytest.fixture
def signal_bundle_factory():
    def factory(**overrides):
        prediction = QlibPrediction(
            symbol=overrides.get("symbol", "AAPL"),
            score=overrides.get("score", 0.91),
            predicted_return=overrides.get("predicted_return", 0.012),
            confidence=overrides.get("confidence", 0.84),
            rank=overrides.get("rank", 1),
            direction=overrides.get("direction", "long"),
            horizon=overrides.get("horizon", "intraday"),
        )
        market = MarketSnapshot(
            symbol=overrides.get("symbol", "AAPL"),
            last_price=overrides.get("last_price", 100.0),
            vwap=overrides.get("vwap", 99.4),
            spread_bps=overrides.get("spread_bps", 1.2),
            volume=overrides.get("volume", 1_500_000.0),
            liquidity_score=overrides.get("liquidity_score", 0.88),
            liquidity_stress=overrides.get("liquidity_stress", 0.2),
            order_book_imbalance=overrides.get("order_book_imbalance", 0.35),
            liquidity_sweep_detected=overrides.get("liquidity_sweep_detected", False),
            volatility_regime=overrides.get("volatility_regime", "normal"),
            microstructure_proxy=overrides.get(
                "microstructure_proxy",
                MicrostructureProxySignal(
                    state="bullish",
                    score=0.55,
                    directional_pressure=0.6,
                    relative_volume=0.7,
                    range_expansion=0.4,
                    vwap_bias=0.5,
                    wick_bias=0.2,
                    persistence=0.5,
                    reason="price_volume_vwap_alignment",
                ),
            ),
            higher_timeframe_trend=overrides.get(
                "higher_timeframe_trend",
                HigherTimeframeTrend(
                    source_timeframe="15m",
                    fast_ma_length=5,
                    slow_ma_length=10,
                    state="bullish" if overrides.get("direction", "long") == "long" else "bearish",
                    long_allowed=overrides.get("direction", "long") == "long",
                    short_allowed=overrides.get("direction", "long") == "short",
                    reason=(
                        "close_above_vwap_and_fast_above_slow"
                        if overrides.get("direction", "long") == "long"
                        else "close_below_vwap_and_fast_below_slow"
                    ),
                    latest_close=overrides.get("last_price", 100.0),
                    latest_vwap=overrides.get("vwap", 99.4),
                    fast_ma=overrides.get("last_price", 100.0),
                    slow_ma=overrides.get("vwap", 99.4),
                    slow_ma_slope_bps=5.0 if overrides.get("direction", "long") == "long" else -5.0,
                ),
            ),
        )
        metadata = {
            "cooldown_active": overrides.get("cooldown_active", False),
            "minutes_to_close": overrides.get("minutes_to_close", 60),
        }
        metadata.update(overrides.get("metadata", {}))
        return SignalBundle(
            symbol=overrides.get("symbol", "AAPL"),
            prediction=prediction,
            market=market,
            metadata=metadata,
        )

    return factory


@pytest.fixture
def approved_trade_intent() -> TradeIntent:
    bracket_plan = BracketPlan(
        planned_entry_price=100.0,
        planned_stop_loss_price=99.0,
        planned_take_profit_price=102.0,
        planned_quantity=2.0,
        risk_per_share=1.0,
        gross_reward_per_share=2.0,
        estimated_fees=0.0,
        estimated_slippage=0.0,
        estimated_fee_per_share=0.0,
        estimated_slippage_per_share=0.0,
        estimated_fixed_fees=0.0,
        net_reward_per_share=2.0,
        reward_risk_ratio=2.0,
        expected_net_profit=4.0,
        time_in_force="day",
        exit_reason_metadata={"stop_loss": "risk_exit", "take_profit": "target_exit"},
    )
    return TradeIntent(
        symbol="AAPL",
        strategy_name="scalping",
        side="buy",
        quantity=2,
        limit_price=100.0,
        predicted_return=0.012,
        confidence=0.84,
        bracket_plan=bracket_plan,
    )


@pytest.fixture
def session_result_factory():
    def factory(*, no_trades: bool = False, stale_prediction: bool = False) -> SessionResult:
        summary = SessionSummary(strategy_name="scalping", mode=RuntimeMode.PAPER)
        prediction_status = (
            ArtifactStatus.stale(
                "predictions",
                freshness_minutes=120,
                guidance=["Refresh predictions."],
            )
            if stale_prediction
            else ArtifactStatus.ready("predictions", freshness_minutes=5)
        )
        attempts = [] if no_trades else [TradeAttemptTrace.for_symbol("AAPL", "scalping")]
        summary.trade_count = 0 if no_trades else 1
        summary.rejected_trade_count = 1 if no_trades else 0
        return SessionResult(
            session_summary=summary,
            prediction_status=prediction_status,
            health_status=HealthStatus(
                summary="ok" if not stale_prediction else "prediction issues",
                ok=not stale_prediction,
                issues=[] if not stale_prediction else ["Predictions are stale."],
            ),
            trade_attempts=attempts,
            rejection_reasons=["predicted_return_threshold"] if no_trades else [],
        )

    return factory


@pytest.fixture
def script_runner():
    def run(script_relative_path: str, *args: str):
        script_path = PROJECT_ROOT / script_relative_path
        env = dict(**__import__("os").environ)
        existing_pythonpath = env.get("PYTHONPATH", "")
        env["PYTHONPATH"] = (
            f"{SRC_DIR}{';' + existing_pythonpath if existing_pythonpath else ''}"
        )
        return subprocess.run(
            [sys.executable, str(script_path), *args],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            env=env,
            check=False,
        )

    return run
