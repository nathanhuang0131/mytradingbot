"""Chronological split helpers for leakage-safe model training."""

from __future__ import annotations

import math

import pandas as pd

from mytradingbot.core.settings import AppSettings
from mytradingbot.training.models import ChronologicalSplit


def chronological_split(frame: pd.DataFrame, *, settings: AppSettings, prediction_horizon_bars: int) -> ChronologicalSplit:
    ordered_datetimes = sorted(pd.to_datetime(frame["datetime"], utc=True).drop_duplicates())
    if len(ordered_datetimes) < 3:
        raise ValueError("Chronological split requires at least three distinct timestamps.")

    train_end_index = max(0, math.floor((len(ordered_datetimes) - 1) * settings.qlib.train_ratio))
    valid_end_index = max(
        train_end_index + 1,
        math.floor((len(ordered_datetimes) - 1) * (settings.qlib.train_ratio + settings.qlib.validation_ratio)),
    )
    valid_end_index = min(valid_end_index, len(ordered_datetimes) - 2)
    return ChronologicalSplit(
        train_start=ordered_datetimes[0].to_pydatetime(),
        train_end=ordered_datetimes[train_end_index].to_pydatetime(),
        valid_start=ordered_datetimes[train_end_index + 1].to_pydatetime(),
        valid_end=ordered_datetimes[valid_end_index].to_pydatetime(),
        test_start=ordered_datetimes[valid_end_index + 1].to_pydatetime(),
        test_end=ordered_datetimes[-1].to_pydatetime(),
        prediction_horizon_bars=prediction_horizon_bars,
        label_definition=f"future_return_{prediction_horizon_bars}_bars",
    )
