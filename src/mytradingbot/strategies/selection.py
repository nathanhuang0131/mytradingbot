"""Candidate ranking and deterministic top-N selection helpers."""

from __future__ import annotations

from pydantic import BaseModel, Field

from mytradingbot.core.models import StrategyDecision


class TopNSelectionResult(BaseModel):
    """Selection results for a single evaluation cycle."""

    selected: list[StrategyDecision] = Field(default_factory=list)
    rejected: list[StrategyDecision] = Field(default_factory=list)
    effective_limit: int


def apply_top_n_selection(
    decisions: list[StrategyDecision],
    *,
    top_n_per_cycle: int,
    available_position_slots: int | None = None,
) -> TopNSelectionResult:
    """Keep the strongest eligible candidates and reject the rest deterministically."""

    ranked = sorted(
        decisions,
        key=lambda decision: (
            -(decision.quality.quality_score if decision.quality is not None else float("-inf")),
            decision.candidate_rank if hasattr(decision, "candidate_rank") else 0,
            decision.symbol,
        ),
    )
    effective_limit = max(0, top_n_per_cycle)
    if available_position_slots is not None:
        effective_limit = min(effective_limit, max(0, available_position_slots))

    selected: list[StrategyDecision] = []
    rejected: list[StrategyDecision] = []
    for index, decision in enumerate(ranked, start=1):
        quality = decision.quality.model_copy(deep=True) if decision.quality is not None else None
        if quality is not None:
            quality.selection_rank = index
            quality.top_n_eligible = True
        if index <= effective_limit:
            if quality is not None:
                quality.selected_in_top_n = True
            selected.append(decision.model_copy(update={"quality": quality}, deep=True))
            continue

        if quality is not None:
            quality.selected_in_top_n = False
        rejected.append(
            decision.model_copy(
                update={
                    "should_trade": False,
                    "reason": "top_n_selection_cutoff",
                    "failed_filters": [*decision.failed_filters, "top_n_selection_cutoff"],
                    "quality": quality,
                },
                deep=True,
            )
        )

    return TopNSelectionResult(
        selected=selected,
        rejected=rejected,
        effective_limit=effective_limit,
    )
