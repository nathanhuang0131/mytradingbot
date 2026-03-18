# User Manual

## Supported Strategies

- `scalping`
- `intraday`
- `short_term`
- `long_term`

## Page Map

### `app/pages/01_Dashboard.py`

Shows:

- prediction freshness
- platform health
- phase capability snapshot
- recent session summary

### `app/pages/02_Strategy_Control.py`

Lets the operator choose:

- strategy
- `dry_run`
- `paper`
- visible-but-gated `live`

### `app/pages/03_Data_and_Training.py`

Runs:

- repo-local Alpaca historical download
- incremental repo-local update
- qlib dataset build
- qlib model training
- prediction refresh

The page also separates what works without `pyqlib` and what works without Alpaca credentials.

### `app/pages/04_Paper_Trading.py`

Runs:

- `dry_run`
- `paper`

The paper workflow uses:

- `models/predictions/latest.json`
- `data/snapshots/market_snapshot.json`

or explicit CLI artifact paths passed to `scripts/run_paper_trading.py`.

### `app/pages/05_Live_Trading.py`

Shows the guarded phase-4 scaffold only. No real live orders are submitted.

### `app/pages/06_LLM_Copilot.py`

Shows advisory-only summaries and explanations sourced from real session artifacts.

### `app/pages/07_Diagnostics.py`

Shows prediction health, no-trade diagnostics, and post-session review notes, including bracket-plan traceability when present.

### `app/pages/08_Settings.py`

Shows resolved settings and repo-local paths from `src/mytradingbot/core/settings.py` and `src/mytradingbot/core/paths.py`.

## Scalping Operator Notes

`src/mytradingbot/strategies/scalping.py` now requires a typed bracket plan before a buy can be submitted. The paper path records:

- planned entry
- planned stop
- planned target
- estimated fees
- estimated slippage
- net reward/risk
- actual bracket exit reason when synthetic exits fire

## Safety Notes

- qlib remains the authority for direction and ranking
- LLM output from `src/mytradingbot/llm/service.py` is advisory only
- missing or stale predictions fail clearly
- phase 1 remains the default operational path
- phase 4 remains guarded and validation-only
