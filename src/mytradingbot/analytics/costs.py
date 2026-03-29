"""Cost allocation helpers used by analytics exports."""

from __future__ import annotations


def allocate_monthly_data_cost(
    *,
    monthly_data_plan_usd: float,
    allocation_mode: str,
    monthly_trade_count: int | None = None,
) -> float:
    if allocation_mode != "fully_loaded_with_allocated_monthly_data_cost":
        return 0.0
    divisor = max(1, int(monthly_trade_count or 1))
    return monthly_data_plan_usd / divisor
