"""Typed qlib workflow result models."""

from __future__ import annotations

import logging

from pydantic import BaseModel, Field

from mytradingbot.core.models import ArtifactStatus, QlibPrediction

logger = logging.getLogger(__name__)


class QlibOperationResult(BaseModel):
    """Status for qlib-dependent maintenance operations."""

    ok: bool
    message: str
    guidance: list[str] = Field(default_factory=list)


class PredictionLoadResult(BaseModel):
    """Status and payload for runtime prediction loading."""

    ok: bool
    message: str
    status: ArtifactStatus
    predictions: list[QlibPrediction] = Field(default_factory=list)
