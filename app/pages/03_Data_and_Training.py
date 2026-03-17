from __future__ import annotations

import streamlit as st

from app.components.runtime import get_platform_service
from mytradingbot.ui_services.data_training import DataTrainingService

service = DataTrainingService(get_platform_service())

st.title("Data and Training")
st.caption("Run qlib dataset, training, and prediction refresh actions.")

if st.button("Build Dataset"):
    st.json(service.build_dataset().model_dump(mode="json"))

if st.button("Train Models"):
    st.json(service.train_models().model_dump(mode="json"))

if st.button("Refresh Predictions"):
    st.json(service.refresh_predictions().model_dump(mode="json"))
