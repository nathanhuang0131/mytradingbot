# First Run

## Works Without `pyqlib`

- `app/app.py`
- `app/pages/01_Dashboard.py`
- `app/pages/02_Strategy_Control.py`
- `app/pages/04_Paper_Trading.py` with explicit artifacts
- `scripts/run_paper_trading.py --predictions-file <path> --market-data-file <path>`

## Works Without Alpaca Credentials

- `app/app.py`
- `app/pages/01_Dashboard.py`
- `app/pages/02_Strategy_Control.py`
- `app/pages/04_Paper_Trading.py` with explicit artifacts
- `scripts/build_qlib_dataset.py`, `scripts/train_models.py`, and `scripts/refresh_predictions.py` if repo-local normalized data and `pyqlib` already exist

## First-Run Order

1. Install the project.

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

2. Verify the repo.

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
python scripts/validate_system.py
python scripts/goalcheck.py
```

3. Choose one of these first operational paths.

Paper-only with explicit artifacts:

```bash
python scripts/run_paper_trading.py --strategy scalping --mode paper --predictions-file <path> --market-data-file <path>
```

Repo-local phased build:

```bash
python scripts/generate_top_liquidity_universe.py --top-n 800 --lookback-days 30 --min-price 5 --min-avg-volume 500000
python scripts/run_daily_maintenance.py --action download --symbols-file data/universe/latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d
python scripts/check_training_data_quality.py --strategy scalping --symbols-file data/universe/latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d
python scripts/run_alpha_robust_training.py --strategy scalping --symbols-file data/universe/latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d
python scripts/run_paper_trading.py --strategy scalping --mode paper
```

4. Launch the dashboard.

```bash
streamlit run app/app.py
```

## Phase Command Mapping

- Phase 1: `scripts/run_paper_trading.py`, `app/pages/04_Paper_Trading.py`
- Phase 2: `scripts/run_daily_maintenance.py --action download`, `scripts/run_daily_maintenance.py --action update`
- Phase 3: `scripts/build_qlib_dataset.py`, `scripts/train_models.py`, `scripts/refresh_predictions.py`, `scripts/check_training_data_quality.py`, `scripts/run_alpha_robust_training.py`
- Phase 4: `scripts/run_live_trading.py`

## Downloader Window Rules

- `scripts/run_daily_maintenance.py --action download` resolves explicit start windows when `--start-date` is omitted.
- `1m` defaults to 90 trading days.
- `5m` defaults to 180 trading days.
- `15m` defaults to 252 trading days.
- `1d` defaults to 756 trading days.
- `reports/data/raw_download_summary.md` is the first artifact to inspect after a large universe download.
