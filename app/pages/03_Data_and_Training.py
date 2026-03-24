from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

APP_DIR = Path(__file__).resolve().parents[1]
if str(APP_DIR) not in sys.path:
    sys.path.insert(0, str(APP_DIR))

from components.runtime import get_platform_service, get_selected_strategy
from mytradingbot.ui_services.data_training import DataTrainingService

service = DataTrainingService(get_platform_service())
payload = service.get_payload()
strategy = get_selected_strategy() or payload.default_strategy

st.title("Data and Training")
st.caption("Run repo-local data download/update, qlib dataset build, training, and prediction refresh actions.")

st.subheader("Capabilities")
st.json(payload.capabilities.model_dump(mode="json"))

st.subheader("Works Without pyqlib")
st.write(payload.works_without_pyqlib)

st.subheader("Works Without Alpaca Credentials")
st.write(payload.works_without_alpaca_credentials)

if st.button("Download Market Data"):
    st.json(service.download_market_data().model_dump(mode="json"))

if st.button("Update Market Data"):
    st.json(service.update_market_data().model_dump(mode="json"))

if st.button("Build Dataset"):
    st.json(service.build_dataset(strategy_name=strategy).model_dump(mode="json"))

if st.button("Train Models"):
    st.json(service.train_models(strategy_name=strategy).model_dump(mode="json"))

if st.button("Refresh Predictions"):
    st.json(service.refresh_predictions(strategy_name=strategy).model_dump(mode="json"))

if st.button("Generate Top Liquidity Universe"):
    st.json(service.generate_top_liquidity_universe().model_dump(mode="json"))

if st.button("Check Training Data Quality"):
    st.json(service.check_training_data_quality(strategy_name=strategy).model_dump(mode="json"))

if st.button("Run Alpha Robust Training"):
    st.json(service.run_alpha_robust_training(strategy_name=strategy).model_dump(mode="json"))
