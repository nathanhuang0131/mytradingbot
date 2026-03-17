# MyTradingBot Next

MyTradingBot Next is a clean, qlib-first quant trading platform built from scratch for modular strategy development, dashboard-driven operation, paper/live workflows, diagnostics, reporting, and advisory-only LLM tooling.

## Goals

- qlib-based dataset, training, and prediction workflows
- canonical strategy support for `scalping`, `intraday`, `short_term`, and `long_term`
- paper trading first
- live trading with explicit safeguards
- Streamlit dashboard-first UX
- diagnostics, validation, and reporting
- advisory-only LLM tools for operator assistance

## Phase 1 Status

Phase 1 delivers a fully runnable paper-trading path with:

- typed signal, strategy, risk, execution, broker, and trace artifacts
- qlib adapter scaffolding with explicit stale or missing prediction failures
- a working in-memory paper broker
- a Streamlit dashboard and all required pages
- diagnostics and reporting services grounded in session artifacts
- advisory-only LLM summaries and explanations

Live trading is visible in the codebase and UI, but it remains validation-only and explicitly gated.

## Runtime Artifacts

Paper and dry-run sessions require:

- a runtime predictions artifact, default path: `models/predictions/latest.json`
- a runtime market snapshot artifact, default path: `data/runtime/market_snapshot.json`

The dashboard still loads if these artifacts are missing or if `pyqlib` is unavailable. Qlib-dependent maintenance actions fail clearly with guidance instead of falling back silently.

## Main Areas

- `app/` Streamlit dashboard
- `configs/` configuration
- `scripts/` thin operational wrappers
- `src/mytradingbot/` package code
- `tests/` validation
- `docs/` architecture and operator docs

## Initial Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
streamlit run app/app.py
```

## Common Commands

```bash
python scripts/validate_system.py
python scripts/goalcheck.py
python scripts/run_live_trading.py
python scripts/run_paper_trading.py --strategy scalping --mode paper --predictions-file <path> --market-data-file <path>
python scripts/build_qlib_dataset.py
python scripts/train_models.py
python scripts/refresh_predictions.py
```
