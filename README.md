# MyTradingBot Next

MyTradingBot Next is a qlib-first, dashboard-first quant trading platform with a production-ready phase-1 paper workflow and explicit phase-2 through phase-4 rollout support inside this repository.

## Phase Map

- Phase 1: `scripts/run_paper_trading.py` plus `app/app.py` run paper and dry-run sessions from real artifacts.
- Phase 2: `scripts/run_daily_maintenance.py --action download` and `scripts/run_daily_maintenance.py --action update` drive the repo-local Alpaca historical data pipeline.
- Phase 3: `scripts/build_qlib_dataset.py`, `scripts/train_models.py`, and `scripts/refresh_predictions.py` build qlib-ready artifacts from repo-local parquet data.
- Phase 4: `scripts/run_live_trading.py` remains visible and validation-only. No real live order submission is enabled.

## Works Without `pyqlib`

- `app/app.py`
- `app/pages/01_Dashboard.py`
- `app/pages/02_Strategy_Control.py`
- `app/pages/04_Paper_Trading.py` when explicit prediction and market snapshot artifacts are provided
- `scripts/run_paper_trading.py --predictions-file <path> --market-data-file <path>`
- `scripts/run_daily_maintenance.py --action download` and `scripts/run_daily_maintenance.py --action update` only if Alpaca credentials and `alpaca-py` are available

## Works Without Alpaca Credentials

- `app/app.py`
- `app/pages/01_Dashboard.py`
- `app/pages/02_Strategy_Control.py`
- `app/pages/04_Paper_Trading.py` with explicit artifacts
- `scripts/run_paper_trading.py --predictions-file <path> --market-data-file <path>`
- `scripts/build_qlib_dataset.py`, `scripts/train_models.py`, and `scripts/refresh_predictions.py` only if repo-local normalized data and `pyqlib` are already available

## Canonical Data And Qlib Flow

1. `scripts/run_daily_maintenance.py --action download` writes raw parquet to `data/raw/alpaca/bars/<timeframe>/<symbol>.parquet`.
2. `scripts/run_daily_maintenance.py --action update` performs incremental parquet updates and normalization into `data/normalized/bars/<timeframe>/<symbol>.parquet`.
3. `src/mytradingbot/data/schema.py` validates the canonical repo schema and transforms it into the qlib-ready schema.
4. `scripts/build_qlib_dataset.py --strategy scalping` builds `data/qlib/dataset.parquet`.
5. `scripts/train_models.py --strategy scalping` writes `models/qlib/model.pkl`.
6. `scripts/refresh_predictions.py --strategy scalping` writes `models/predictions/latest.json`.
7. `scripts/run_paper_trading.py --strategy scalping --mode paper` runs the strategy -> risk -> execution -> broker path against the refreshed artifacts.

`src/mytradingbot/data/providers/alpaca_provider.py` is the canonical phase-2 provider. `src/mytradingbot/data/providers/file_ingest_provider.py` exists for fixtures, offline imports, and tests only.

## Runtime Artifact Paths

- `models/predictions/latest.json`
- `data/snapshots/market_snapshot.json`
- `data/runtime/market_snapshot.json` as the current paper-session compatibility mirror
- `data/qlib/dataset.parquet`
- `models/qlib/model.pkl`

## Initial Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
streamlit run app/app.py
```

## Canonical Commands

```bash
python scripts/validate_system.py
python scripts/goalcheck.py
python scripts/run_daily_maintenance.py --action download --symbols AAPL MSFT NVDA --timeframes 1m 5m 15m 1d
python scripts/run_daily_maintenance.py --action update --symbols AAPL MSFT NVDA --timeframes 1m 5m 15m 1d
python scripts/build_qlib_dataset.py --strategy scalping
python scripts/train_models.py --strategy scalping
python scripts/refresh_predictions.py --strategy scalping
python scripts/run_paper_trading.py --strategy scalping --mode paper --predictions-file <path> --market-data-file <path>
python scripts/run_live_trading.py
```

The canonical implementation lives under `src/mytradingbot/core/`, `src/mytradingbot/data/`, `src/mytradingbot/qlib_engine/`, `src/mytradingbot/strategies/`, `src/mytradingbot/risk/`, `src/mytradingbot/execution/`, `src/mytradingbot/brokers/`, `src/mytradingbot/orchestration/`, `src/mytradingbot/diagnostics/`, `src/mytradingbot/reporting/`, `src/mytradingbot/llm/`, and `src/mytradingbot/ui_services/`.
