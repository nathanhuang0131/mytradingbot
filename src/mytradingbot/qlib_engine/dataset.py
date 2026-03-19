"""Qlib-ready dataset preparation from repo-local normalized parquet data."""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from mytradingbot.core.settings import AppSettings
from mytradingbot.data.schema import transform_canonical_to_qlib_ready
from mytradingbot.data.storage import ParquetBarStore


@dataclass(frozen=True)
class StrategyDatasetProfile:
    strategy_name: str
    timeframe: str
    label_horizon_bars: int


def strategy_dataset_profile(strategy_name: str, settings: AppSettings) -> StrategyDatasetProfile:
    mapping = {
        "scalping": StrategyDatasetProfile("scalping", "1m", settings.qlib.label_horizon_bars),
        "intraday": StrategyDatasetProfile("intraday", "5m", 6),
        "short_term": StrategyDatasetProfile("short_term", "15m", 8),
        "long_term": StrategyDatasetProfile("long_term", "1d", 5),
    }
    return mapping[strategy_name]


def build_feature_dataset(
    *,
    settings: AppSettings,
    strategy_name: str,
    store: ParquetBarStore | None = None,
    symbols: list[str] | None = None,
) -> pd.DataFrame:
    """Build a qlib-ready feature dataset from normalized parquet bars."""

    store = store or ParquetBarStore(settings=settings)
    profile = strategy_dataset_profile(strategy_name, settings)
    frames: list[pd.DataFrame] = []
    allowed_symbols = {symbol.strip().upper() for symbol in (symbols or []) if symbol}

    for file_path in store.iter_normalized_files(timeframe=profile.timeframe):
        if allowed_symbols and file_path.stem.upper() not in allowed_symbols:
            continue
        canonical = pd.read_parquet(file_path)
        qlib_ready = transform_canonical_to_qlib_ready(canonical)
        features = _engineer_features(qlib_ready, profile.label_horizon_bars)
        if not features.empty:
            frames.append(features)

    if not frames:
        return pd.DataFrame()

    dataset = pd.concat(frames, ignore_index=True)
    dataset["datetime"] = pd.to_datetime(dataset["datetime"], utc=True)
    return dataset.sort_values(["instrument", "datetime"]).reset_index(drop=True)


def _engineer_features(frame: pd.DataFrame, label_horizon_bars: int) -> pd.DataFrame:
    ordered = frame.sort_values(["instrument", "datetime"]).copy()
    grouped = ordered.groupby("instrument", sort=False)
    ordered["feature_return_1"] = grouped["close"].pct_change(1)
    ordered["feature_return_5"] = grouped["close"].pct_change(5)
    ordered["feature_intrabar_range"] = (ordered["high"] - ordered["low"]) / ordered["close"]
    ordered["feature_volume_ratio"] = ordered["volume"] / grouped["volume"].transform(
        lambda series: series.rolling(20, min_periods=1).mean()
    )
    ordered["feature_vwap_gap"] = (ordered["close"] - ordered["vwap"]) / ordered["close"]
    ordered["feature_volatility_5"] = grouped["close"].transform(
        lambda series: series.pct_change().rolling(5, min_periods=2).std()
    )
    ordered["label"] = grouped["close"].shift(-label_horizon_bars) / ordered["close"] - 1
    required_features = [
        "feature_return_1",
        "feature_return_5",
        "feature_intrabar_range",
        "feature_volume_ratio",
        "feature_vwap_gap",
        "feature_volatility_5",
    ]
    ordered = ordered.dropna(subset=required_features)
    return ordered[
        [
            "instrument",
            "datetime",
            *required_features,
            "label",
            "timeframe",
            "close",
            "volume",
        ]
    ].reset_index(drop=True)
