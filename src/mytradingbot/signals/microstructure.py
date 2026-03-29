"""Lightweight bar-based microstructure proxy for equities scalping."""

from __future__ import annotations

import math
from typing import Literal

import pandas as pd

from mytradingbot.core.models import MicrostructureProxySignal

Direction = Literal["long", "short"]
MicrostructureRelation = Literal[
    "supports",
    "neutral",
    "weak_contradiction",
    "strong_contradiction",
    "unavailable",
]

_REQUIRED_COLUMNS = {"open", "high", "low", "close", "volume", "vwap", "timestamp"}


def build_microstructure_proxy(frame: pd.DataFrame) -> MicrostructureProxySignal:
    """Estimate directional participation from already-loaded bar data."""

    missing = sorted(_REQUIRED_COLUMNS.difference(frame.columns))
    if missing:
        return _unavailable("missing_required_columns")
    if frame.empty or len(frame.index) < 3:
        return _unavailable("insufficient_history")

    ordered = frame.sort_values("timestamp").reset_index(drop=True).copy()
    for column in ("open", "high", "low", "close", "volume", "vwap"):
        ordered[column] = pd.to_numeric(ordered[column], errors="coerce")
    ordered = ordered.dropna(subset=["open", "high", "low", "close", "volume", "vwap"])
    if ordered.empty or len(ordered.index) < 3:
        return _unavailable("invalid_microstructure_payload")

    recent = ordered.tail(5).reset_index(drop=True)
    prior = recent.iloc[:-1] if len(recent.index) > 1 else recent
    latest = recent.iloc[-1]

    body = recent["close"] - recent["open"]
    bar_range = (recent["high"] - recent["low"]).clip(lower=0.0001)
    body_fraction = (body / bar_range).clip(-1.0, 1.0)

    prior_volume_mean = float(prior["volume"].mean()) if not prior.empty else float(latest["volume"])
    relative_volume_ratio = (
        float(latest["volume"]) / prior_volume_mean if prior_volume_mean > 0 else 1.0
    )
    relative_volume = max(0.0, min(2.0, relative_volume_ratio))
    volume_boost = max(0.5, min(relative_volume_ratio, 2.0))

    weights = [0.2, 0.3, 0.5][-len(recent.index) :]
    directional_pressure = _clamp(
        float(
            sum(
                float(component) * weight
                for component, weight in zip(body_fraction.tail(len(weights)), weights, strict=False)
            )
        )
        * volume_boost
    )

    prior_ranges = ((prior["high"] - prior["low"]) / prior["close"]).replace([math.inf, -math.inf], pd.NA).dropna()
    latest_range = float((latest["high"] - latest["low"]) / max(float(latest["close"]), 0.01))
    baseline_range = float(prior_ranges.median()) if not prior_ranges.empty else latest_range
    if baseline_range <= 0 or not math.isfinite(baseline_range):
        range_expansion_ratio = 1.0
    else:
        range_expansion_ratio = latest_range / baseline_range
    range_expansion = max(0.0, min(2.0, range_expansion_ratio))
    latest_body_direction = 1.0 if latest["close"] > latest["open"] else -1.0 if latest["close"] < latest["open"] else 0.0
    range_component = _clamp(max(0.0, min(range_expansion_ratio - 1.0, 1.0)) * latest_body_direction)

    latest_close = float(latest["close"])
    latest_vwap = float(latest["vwap"])
    vwap_bias = _clamp(((latest_close - latest_vwap) / max(latest_close, 0.01)) / 0.0025)

    upper_wick = float(latest["high"] - max(latest["open"], latest["close"]))
    lower_wick = float(min(latest["open"], latest["close"]) - latest["low"])
    wick_bias = _clamp((lower_wick - upper_wick) / max(float(latest["high"] - latest["low"]), 0.0001))

    recent_returns = recent["close"].pct_change().dropna().tail(3)
    if recent_returns.empty:
        persistence = 0.0
    else:
        consistency = float(recent_returns.apply(lambda value: 1 if value > 0 else -1 if value < 0 else 0).mean())
        magnitude = min(1.0, abs(float(recent_returns.mean())) / 0.002)
        persistence = _clamp(consistency * magnitude)

    score = _clamp(
        (directional_pressure * 0.35)
        + (range_component * 0.15)
        + (vwap_bias * 0.20)
        + (wick_bias * 0.10)
        + (persistence * 0.20)
    )
    if score >= 0.2:
        state = "bullish"
    elif score <= -0.2:
        state = "bearish"
    else:
        state = "neutral"

    contributors = {
        "directional_pressure": directional_pressure,
        "range_expansion": range_component,
        "vwap_bias": vwap_bias,
        "wick_bias": wick_bias,
        "persistence": persistence,
    }
    dominant = [
        name
        for name, value in sorted(contributors.items(), key=lambda item: abs(item[1]), reverse=True)
        if abs(value) >= 0.15
    ][:2]
    reason = "_and_".join(dominant) if dominant else "mixed_microstructure"

    return MicrostructureProxySignal(
        state=state,
        score=score,
        directional_pressure=directional_pressure,
        relative_volume=relative_volume,
        range_expansion=range_expansion,
        vwap_bias=vwap_bias,
        wick_bias=wick_bias,
        persistence=persistence,
        reason=reason,
    )


def microstructure_relation_for_direction(
    proxy: MicrostructureProxySignal | None,
    direction: Direction,
) -> tuple[float, MicrostructureRelation]:
    """Translate a directional proxy score into support vs contradiction."""

    if proxy is None or proxy.state == "unavailable":
        return 0.0, "unavailable"
    alignment_score = proxy.score if direction == "long" else -proxy.score
    if alignment_score >= 0.15:
        return alignment_score, "supports"
    if alignment_score <= -0.35:
        return alignment_score, "strong_contradiction"
    if alignment_score <= -0.10:
        return alignment_score, "weak_contradiction"
    return alignment_score, "neutral"


def _unavailable(reason: str) -> MicrostructureProxySignal:
    return MicrostructureProxySignal(
        state="unavailable",
        score=0.0,
        directional_pressure=0.0,
        relative_volume=0.0,
        range_expansion=0.0,
        vwap_bias=0.0,
        wick_bias=0.0,
        persistence=0.0,
        reason=reason,
    )


def _clamp(value: float, *, lower: float = -1.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, float(value)))
