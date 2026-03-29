"""Adapter boundary for pyqlib-backed training and prediction workflows."""

from __future__ import annotations

import pickle
import json
from pathlib import Path
from typing import Protocol

import pandas as pd


FEATURE_COLUMNS = [
    "feature_return_1",
    "feature_return_5",
    "feature_intrabar_range",
    "feature_volume_ratio",
    "feature_vwap_gap",
    "feature_volatility_5",
]


class QlibWorkflowAdapter(Protocol):
    """Protocol for qlib-backed dataset, training, and prediction workflows."""

    def build_dataset(self, frame: pd.DataFrame, artifact_path: Path) -> Path:
        """Persist a qlib-ready dataset artifact."""

    def train_model(self, frame: pd.DataFrame, artifact_path: Path, strategy_name: str) -> Path:
        """Train a qlib model from the prepared dataset."""

    def generate_predictions(
        self,
        frame: pd.DataFrame,
        model_path: Path,
        output_path: Path,
        strategy_name: str,
    ) -> Path:
        """Generate runtime prediction artifacts from the trained model."""


class PyQlibWorkflowAdapter:
    """Default adapter that uses pyqlib once it is installed."""

    def build_dataset(self, frame: pd.DataFrame, artifact_path: Path) -> Path:
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_parquet(artifact_path, index=False)
        return artifact_path

    def train_model(self, frame: pd.DataFrame, artifact_path: Path, strategy_name: str) -> Path:
        dataset = frame.dropna(subset=["label"]).copy()
        if dataset.empty:
            raise ValueError("Cannot train a qlib model because the dataset contains no labeled rows.")

        model = self._build_model()
        qlib_dataset = self._build_dataset_object(dataset)
        model.fit(qlib_dataset)

        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        artifact_path.write_bytes(pickle.dumps(model))
        return artifact_path

    def generate_predictions(
        self,
        frame: pd.DataFrame,
        model_path: Path,
        output_path: Path,
        strategy_name: str,
    ) -> Path:
        if not model_path.exists():
            raise FileNotFoundError(f"Trained qlib model artifact is missing: {model_path}")

        prediction_frame = frame.dropna(subset=FEATURE_COLUMNS).copy()
        if prediction_frame.empty:
            raise ValueError("Prediction refresh requires feature rows, but none are available.")

        model = pickle.loads(model_path.read_bytes())
        qlib_dataset = self._build_dataset_object(prediction_frame, include_label=False, segment_name="predict")
        prediction_series = model.predict(qlib_dataset, segment="predict")
        prediction_df = prediction_series.reset_index()
        prediction_df.columns = ["datetime", "instrument", "score"]
        latest_scores = prediction_df.sort_values("datetime").groupby("instrument").tail(1)
        latest_features = prediction_frame.sort_values("datetime").groupby("instrument").tail(1)
        merged = latest_scores.merge(latest_features, on=["instrument", "datetime"], how="left")
        merged["absolute_score"] = merged["score"].abs()
        merged["confidence"] = (
            merged["absolute_score"].rank(pct=True, ascending=True).fillna(0.5)
        )
        payload = []
        for rank, row in enumerate(
            merged.sort_values("absolute_score", ascending=False).itertuples(index=False),
            start=1,
        ):
            payload.append(
                {
                    "symbol": row.instrument,
                    "score": float(row.score),
                    "predicted_return": float(row.score),
                    "confidence": float(max(0.01, min(0.99, row.confidence))),
                    "rank": rank,
                    "direction": "long" if float(row.score) >= 0 else "short",
                    "horizon": strategy_name,
                }
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(payload), encoding="utf-8")
        return output_path

    @staticmethod
    def _build_model():
        from qlib.contrib.model.gbdt import LGBModel

        return LGBModel(loss="mse")

    def _build_dataset_object(
        self,
        frame: pd.DataFrame,
        *,
        include_label: bool = True,
        segment_name: str = "train",
    ):
        from qlib.data.dataset import DatasetH
        from qlib.data.dataset.handler import DataHandlerLP

        working = frame.copy()
        indexed = working.set_index(["datetime", "instrument"]).sort_index()
        feature_frame = indexed[FEATURE_COLUMNS].copy()
        feature_frame.columns = pd.MultiIndex.from_product([["feature"], FEATURE_COLUMNS])
        if include_label:
            label_frame = indexed[["label"]].copy()
            label_frame.columns = pd.MultiIndex.from_product([["label"], ["LABEL0"]])
            dataset_frame = pd.concat([feature_frame, label_frame], axis=1)
        else:
            dataset_frame = feature_frame

        handler = DataHandlerLP.from_df(dataset_frame)
        start = dataset_frame.index.get_level_values(0).min()
        end = dataset_frame.index.get_level_values(0).max()
        return DatasetH(handler=handler, segments={segment_name: (start, end)})
