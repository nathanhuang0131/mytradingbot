from __future__ import annotations

from mytradingbot.core.models import (
    CandidateCostEstimate,
    CandidateQualitySnapshot,
    HigherTimeframeTrend,
    StrategyDecision,
    TradeIntent,
)
from mytradingbot.strategies.selection import apply_top_n_selection


def _approved_decision(symbol: str, quality_score: float) -> StrategyDecision:
    return StrategyDecision.approve(
        strategy_name="scalping",
        symbol=symbol,
        intent=TradeIntent(
            symbol=symbol,
            strategy_name="scalping",
            side="buy",
            quantity=1.0,
            predicted_return=0.01,
            confidence=0.8,
        ),
        passed_filters=["predicted_return_threshold", "confidence_threshold"],
        quality=CandidateQualitySnapshot(
            expected_edge_after_cost=0.006,
            quality_score=quality_score,
            trend=HigherTimeframeTrend(
                source_timeframe="15m",
                fast_ma_length=5,
                slow_ma_length=10,
                state="bullish",
                long_allowed=True,
                short_allowed=False,
                reason="close_above_vwap_and_fast_above_slow",
            ),
            cost_estimate=CandidateCostEstimate(
                gross_predicted_return=0.01,
                estimated_spread_cost=0.0002,
                estimated_slippage_cost=0.0002,
                estimated_fee_cost=0.0,
                estimated_regulatory_fee_cost=0.00005,
                estimated_total_cost=0.00045,
                expected_edge_after_cost=0.00955,
            ),
        ),
    )


def test_top_n_selection_keeps_only_highest_quality_candidates() -> None:
    decisions = [
        _approved_decision("AAPL", 0.91),
        _approved_decision("MSFT", 0.83),
        _approved_decision("NVDA", 0.77),
    ]

    result = apply_top_n_selection(
        decisions,
        top_n_per_cycle=2,
        available_position_slots=5,
    )

    assert [decision.symbol for decision in result.selected] == ["AAPL", "MSFT"]
    assert result.selected[0].quality is not None
    assert result.selected[0].quality.selection_rank == 1
    assert result.selected[1].quality is not None
    assert result.selected[1].quality.selection_rank == 2
    assert result.rejected[0].reason == "top_n_selection_cutoff"
    assert result.rejected[0].quality is not None
    assert result.rejected[0].quality.selected_in_top_n is False


def test_top_n_selection_respects_available_position_slots() -> None:
    decisions = [
        _approved_decision("AAPL", 0.91),
        _approved_decision("MSFT", 0.83),
    ]

    result = apply_top_n_selection(
        decisions,
        top_n_per_cycle=3,
        available_position_slots=1,
    )

    assert result.effective_limit == 1
    assert [decision.symbol for decision in result.selected] == ["AAPL"]
    assert [decision.symbol for decision in result.rejected] == ["MSFT"]
