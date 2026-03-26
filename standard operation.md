# Standard Operation

## Canonical Environment

Use the repo-local root and the project environment before running any command:

```powershell
conda activate mytradingbot
Set-Location 'C:\Users\User\Documents\MyTradingBot_Next'
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
```

Key runtime artifacts:

- Top-liquidity universe: `data/universe/latest_top_liquidity_universe.json`
- Raw market data: `data/raw/alpaca/bars/<timeframe>/<symbol>.parquet`
- Normalized market data: `data/normalized/bars/<timeframe>/<symbol>.parquet`
- Qlib dataset: `data/qlib/dataset.parquet`
- Trained qlib model: `models/qlib/model.pkl`
- Latest predictions: `models/predictions/latest.json`
- Profile-scoped active universe: `data/runtime/active_universes/<profile>_active_symbols.json`
- Latest profile session config: `data/runtime/session_profiles/<profile>_latest.json`
- Loop log: `logs/paper_trading_loop.log`

## Standard Scalping Operating Sequence

Use this order for the normal scalping paper workflow:

1. Generate or refresh the top-liquidity universe.
2. Download or update raw market data.
3. Check training data quality.
4. Build the qlib dataset.
5. Train the model.
6. Refresh predictions.
7. Review the final active universe in Streamlit.
8. Run the scalping paper loop.

### 1. Update top liquidity universe

Canonical command:

```powershell
python scripts\generate_top_liquidity_universe.py --top-n 800 --lookback-days 30 --min-price 5 --min-avg-volume 500000 --asset-class us_equity --include-etfs false --output-prefix top_liquidity_universe --verbose
```

What it does:

- ranks tradable assets by liquidity
- writes repo-local JSON, CSV, and markdown report artifacts
- updates `data/universe/latest_top_liquidity_universe.json`

Options:

- `--top-n`: how many symbols to keep in the final ranked universe
- `--lookback-days`: trailing daily-bar window used for the liquidity ranking
- `--min-price`: minimum average price threshold
- `--min-avg-volume`: minimum average volume threshold
- `--asset-class`: asset class filter, normally `us_equity`
- `--include-etfs`: `true` or `false`; include ETFs when true
- `--output-prefix`: artifact filename prefix
- `--verbose`: enables more logging

### 2. Download or update raw market data

Full raw download:

```powershell
python scripts\run_daily_maintenance.py --action download --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --verbose
```

Incremental update:

```powershell
python scripts\run_daily_maintenance.py --action update --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --verbose
```

All-in-one maintenance plus qlib build, training, and prediction refresh:

```powershell
python scripts\run_daily_maintenance.py --action all --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --verbose
```

What it does:

- `download`: full raw refresh
- `update`: incremental parquet update and normalization
- `all`: update plus dataset build, training, and prediction refresh

Options:

- `--action`: `download`, `update`, or `all`
- `--strategy`: strategy name for the qlib steps when `--action all` is used
- `--symbols`: explicit symbol list instead of a file
- `--symbols-file`: JSON or CSV file containing symbols
- `--timeframes`: one or more timeframes such as `1m 5m 15m 1d`
- `--start-date`: optional ISO date/datetime lower bound
- `--end-date`: optional ISO date/datetime upper bound
- `--normalize-only`: skip download and normalize existing raw parquet only
- `--verbose`: enables debug logging

### 3. Check training data quality

Canonical command:

```powershell
python scripts\check_training_data_quality.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --min-eligible-symbols 150 --verbose
```

What it does:

- verifies data sufficiency before alpha-robust training
- confirms enough eligible symbols exist across the requested timeframes

Options:

- `--strategy`: strategy name, normally `scalping`
- `--symbols`: explicit symbol list
- `--symbols-file`: symbol file to validate
- `--timeframes`: timeframe set to check
- `--min-eligible-symbols`: minimum acceptable number of eligible symbols
- `--verbose`: enables debug logging

### 4. Build qlib dataset

Canonical command:

```powershell
python scripts\build_qlib_dataset.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json
```

What it does:

- builds the repo-local qlib dataset artifact used for training and inference

Options:

- `--strategy`: strategy name
- `--symbols`: explicit symbol list
- `--symbols-file`: symbol file for dataset scope

### 5. Train model

Canonical command:

```powershell
python scripts\train_models.py --strategy scalping
```

What it does:

- trains qlib models from the current repo-local dataset artifact

Options:

- `--strategy`: strategy name

### 6. Refresh predictions

Canonical command:

```powershell
python scripts\refresh_predictions.py --strategy scalping
```

What it does:

- refreshes `models/predictions/latest.json` from the current qlib artifacts

Options:

- `--strategy`: strategy name

### 7. Review final trading universe in Streamlit

Canonical dashboard launch:

```powershell
python -m streamlit run app/app.py
```

Use the `Trading Universe` sidebar page to:

- select a saved profile
- compare the last active universe with the newly generated universe
- choose `Keep old trading universe`, `Combine old and new trading universe`, or `Only new trading universe`
- add extra symbols for monitoring and trading
- inspect qlib prediction rows in `Raw qlib prediction artifacts` or `Final qlib trading universe` view
- review `symbol`, `score`, `predicted_return`, `confidence`, `rank`, `direction`, `generated_at`, `horizon`, `is_final_symbol`, `indicated_tp_pct`, and `indicated_sl_pct`
- save the final active universe manifest for future runs

Use the `Setup Wizard` -> `Alpha & Model` step to change the live scalping gates:

- `Predicted return threshold (%)`: default `0.50%`, stored internally as `0.005`
- `Confidence threshold`: default `0.60`

Lower either threshold to let more symbols through the qlib gate. Raise either threshold to make symbol selection stricter.

### 8. Run the scalping loop

Canonical local-paper loop:

```powershell
python scripts\run_paper_trading.py --strategy scalping --mode paper --broker-mode local_paper --symbols-file data\universe\latest_top_liquidity_universe.json --loop --interval-seconds 300 --verbose
```

Canonical Alpaca paper loop:

```powershell
python scripts\run_paper_trading.py --strategy scalping --mode paper --broker-mode alpaca_paper_api --symbols-file data\universe\latest_top_liquidity_universe.json --loop --interval-seconds 300 --verbose
```

Launch from a saved profile config:

```powershell
python scripts\run_paper_trading.py --session-config data\runtime\session_profiles\<profile>_latest.json --verbose
```

What it does:

- runs one dry-run or paper session, or a supervised overnight paper loop
- can use a saved wizard/profile config
- can auto-refresh market snapshot, dataset, and predictions unless disabled

Options:

- `--strategy`: strategy name
- `--mode`: `dry_run` or `paper`
- `--session-config`: path to a saved profile session config
- `--broker-mode`: `local_paper` or `alpaca_paper_api`
- `--symbols`: explicit symbol list
- `--symbols-file`: symbol file path
- `--predictions-file`: override predictions artifact path
- `--market-data-file`: override market snapshot path
- `--loop`: run repeated supervised cycles instead of one session
- `--interval-seconds`: cycle spacing when `--loop` is used
- `--max-cycles`: cap the number of loop cycles; omit for open-ended loops
- `--disable-auto-refresh`: block when runtime inputs go stale instead of refreshing them
- `--verbose`: enables more logging

## UI And Streamlit Surface

Canonical Streamlit entry:

```powershell
python -m streamlit run app/app.py
```

Current pages:

- `app/app.py`: Dashboard landing page
- `app/pages/00_Setup_Wizard.py`: guided session setup and launch
- `app/pages/02_Strategy_Control.py`: strategy and mode selection
- `app/pages/03_Data_Management.py`: maintenance, qlib, training, predictions, and liquidity generation
- `app/pages/04_Paper_Trading.py`: one-shot dry-run or paper execution
- `app/pages/05_Live_Trading.py`: live-trading status, validation, and managed session visibility
- `app/pages/06_LLM_Copilot.py`: advisory-only LLM workflows
- `app/pages/07_Diagnostics.py`: diagnostics and status inspection
- `app/pages/08_Settings.py`: operator settings view
- `app/pages/09_Trading_Universe.py`: final active-universe review and save flow

Current launch helper status:

- `python scripts\launch_dashboard.py` exists, but it currently fails with a `SyntaxError` because a `from __future__ import annotations` line appears after executable code. Use `python -m streamlit run app/app.py` instead.

## Institutional And One-Command Flows

### `run_institutional_pipeline.py`

Canonical command:

```powershell
python scripts\run_institutional_pipeline.py --strategy scalping --use-top-liquidity-universe --timeframes 1m 5m 15m 1d --mode paper --verbose
```

What it does:

- runs the canonical one-command institutional pipeline
- can include maintenance, validation, training, prediction refresh, and trading

Options:

- `--strategy`: strategy name
- `--symbols`: explicit symbol list
- `--symbols-file`: symbol file path
- `--timeframes`: maintenance/training timeframe set
- `--skip-train`: skip the training step
- `--skip-maintenance`: skip maintenance/download work
- `--skip-validation`: skip validation checks
- `--mode`: `dry_run` or `paper`
- `--use-top-liquidity-universe`: automatically use/generated the top-liquidity universe path
- `--top-n`: universe size when top-liquidity mode is enabled
- `--min-eligible-symbols`: minimum eligible symbol floor for validation
- `--verbose`: enables debug logging

### `run_loop_trading.py`

Canonical command:

```powershell
python scripts\run_loop_trading.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --interval-seconds 60 --cycles 1
```

What it does:

- runs supervised institutional paper-trading cycles
- repeatedly calls the institutional pipeline in paper mode

Options:

- `--strategy`: strategy name
- `--symbols`: explicit symbol list
- `--symbols-file`: symbol file path
- `--timeframes`: timeframe set
- `--interval-seconds`: sleep time between cycles
- `--cycles`: number of cycles; `0` means continuous execution
- `--use-top-liquidity-universe`: use the top-liquidity universe flow automatically

## Training Utilities

### `run_alpha_robust_training.py`

Canonical command:

```powershell
python scripts\run_alpha_robust_training.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --top-n 800 --min-eligible-symbols 150 --verbose
```

What it does:

- runs the institutional alpha-robust training workflow
- can optionally manage universe selection and lookback windows

Options:

- `--strategy`: strategy name
- `--top-n`: target universe size when the training service resolves its own universe
- `--symbols`: explicit symbol list
- `--symbols-file`: symbol file path
- `--timeframes`: timeframe set
- `--lookback-1m-days`: 1-minute data lookback window
- `--lookback-5m-days`: 5-minute data lookback window
- `--lookback-15m-days`: 15-minute data lookback window
- `--lookback-1d-days`: daily data lookback window
- `--min-eligible-symbols`: minimum eligible symbol floor
- `--skip-download`: skip download/update work
- `--skip-train`: skip the training step
- `--verbose`: enables debug logging

## Validation And Status Utilities

### `validate_system.py`

Command:

```powershell
python scripts\validate_system.py
```

What it does:

- prints a repo-local capability and file-presence summary
- shows strategy names, phase states, and runtime-state-store path

Current note:

- this script currently checks for `app/pages/01_Dashboard.py`, so `pages_present` can show `False` even though the current dashboard entry point is `app/app.py`

### `goalcheck.py`

Command:

```powershell
python scripts\goalcheck.py
```

What it does:

- prints a human-readable status summary for strategies, pages, live gating, pipeline presence, diagnostics, and LLM availability

Current note:

- like `validate_system.py`, it still checks for `app/pages/01_Dashboard.py`, so `pages present` can report `False` against the current page layout

### `run_live_trading.py`

Command:

```powershell
python scripts\run_live_trading.py
```

What it does:

- prints the current live-trading capability status
- current behavior is validation-only; live Alpaca submission remains disabled

## Broker, Smoke, And Reset Utilities

### `check_alpaca_paper_broker.py`

Command:

```powershell
python scripts\check_alpaca_paper_broker.py --list-orders --strategy scalping
```

What it does:

- checks Alpaca paper API connectivity and bot-owned exposure visibility

Options:

- `--list-orders`: include order listing in the connectivity check
- `--strategy`: strategy context for the probe

### `run_alpaca_paper_submission_smoke.py`

Long smoke example:

```powershell
python scripts\run_alpaca_paper_submission_smoke.py --symbol AMZN --side long --strategy scalping --verbose
```

Short smoke example:

```powershell
python scripts\run_alpaca_paper_submission_smoke.py --symbol TSLA --side short --strategy scalping --verbose
```

What it does:

- submits one bounded Alpaca paper bracket-order smoke through the repo

Options:

- `--symbol`: required target symbol
- `--side`: required side, `long` or `short`
- `--strategy`: strategy name
- `--leave-open`: keep the order open instead of immediately cleaning it up
- `--verbose`: enables more logging

### `reset_local_paper_state.py`

Command:

```powershell
python scripts\reset_local_paper_state.py --yes
```

What it does:

- archives repo-local local-paper runtime state and analytics artifacts
- does not touch market data, qlib artifacts, universe files, or Alpaca account state

Options:

- `--yes`: required confirmation flag; nothing happens without it

### `smoke_test_broker.py`

Command:

```powershell
python scripts\smoke_test_broker.py
```

What it does:

- submits a tiny local-paper broker order using `AAPL`, `buy`, quantity `1`, and limit price `100.0`
- useful as a local paper broker sanity check

## Additional Maintenance Commands

### `train_models.py`

Command:

```powershell
python scripts\train_models.py --strategy scalping
```

What it does:

- trains qlib models from the current dataset

Options:

- `--strategy`: strategy name

### `refresh_predictions.py`

Command:

```powershell
python scripts\refresh_predictions.py --strategy scalping
```

What it does:

- refreshes runtime predictions from repo-local qlib artifacts

Options:

- `--strategy`: strategy name

## Verification Commands

Standard test suite:

```powershell
pytest -q
```

Plugin-safe pytest:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q
```

Goal and system checks:

```powershell
python scripts\validate_system.py
python scripts\goalcheck.py
```

## Recommended Daily Set

If you only want the standard daily scalping set, use:

```powershell
python scripts\generate_top_liquidity_universe.py --top-n 800 --lookback-days 30 --min-price 5 --min-avg-volume 500000 --asset-class us_equity --include-etfs false --output-prefix top_liquidity_universe --verbose
python scripts\run_daily_maintenance.py --action update --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --verbose
python scripts\check_training_data_quality.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d --min-eligible-symbols 150 --verbose
python scripts\build_qlib_dataset.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json
python scripts\train_models.py --strategy scalping
python scripts\refresh_predictions.py --strategy scalping
python -m streamlit run app/app.py
python scripts\run_paper_trading.py --strategy scalping --mode paper --broker-mode local_paper --symbols-file data\universe\latest_top_liquidity_universe.json --loop --interval-seconds 300 --verbose
```
