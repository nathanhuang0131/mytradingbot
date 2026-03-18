# Runbook

## Daily Maintenance Order

1. `python scripts/run_daily_maintenance.py --action update --symbols AAPL MSFT NVDA --timeframes 1m 5m 15m 1d`
2. `python scripts/build_qlib_dataset.py --strategy scalping`
3. `python scripts/train_models.py --strategy scalping`
4. `python scripts/refresh_predictions.py --strategy scalping`
5. `python scripts/run_paper_trading.py --strategy scalping --mode dry_run`
6. `python scripts/run_paper_trading.py --strategy scalping --mode paper`
7. `streamlit run app/app.py`

## Daily UI Order

1. Open `app/pages/01_Dashboard.py` from the Streamlit sidebar.
2. Check the phase capability snapshot and prediction freshness.
3. Use `app/pages/03_Data_and_Training.py` for phase-2 and phase-3 actions.
4. Use `app/pages/04_Paper_Trading.py` for `dry_run` and `paper` execution.
5. Use `app/pages/07_Diagnostics.py` and `app/pages/06_LLM_Copilot.py` for review.

## If Phase 2 Fails

Check:

- `alpaca-py` is installed through `pip install -e .[dev,broker]` or `pip install alpaca-py`
- `ALPACA_API_KEY` or `BROKER__ALPACA_API_KEY` is set
- `ALPACA_SECRET_KEY` or `BROKER__ALPACA_SECRET_KEY` is set
- `data/raw/alpaca/bars/` and `data/normalized/bars/` are writable under the repo root

## If Phase 3 Fails

Check:

- `pyqlib` is installed through `pip install -e .[dev,qlib]` or `pip install pyqlib`
- `data/normalized/bars/` contains parquet for the requested strategy timeframe
- `data/qlib/dataset.parquet` exists before training
- `models/qlib/model.pkl` exists before prediction refresh

## If No Trades Happen

Check:

- `models/predictions/latest.json` freshness
- `data/snapshots/market_snapshot.json` freshness
- qlib return and confidence thresholds
- scalping fee-adjusted bracket expectancy
- whole-share execution rounding effects
- cooldown and flatten-near-close logic
- risk rejection reasons

## Live Trading Status

- `scripts/run_live_trading.py` is validation-only
- `src/mytradingbot/risk/service.py` still blocks live approval
- `src/mytradingbot/brokers/alpaca.py` still reports live submission disabled
