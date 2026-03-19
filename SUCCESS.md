# SUCCESS

## V2 Definition

The repository is considered v2-ready when these repo-local conditions hold:

- `scripts/generate_top_liquidity_universe.py` can build `data/universe/latest_top_liquidity_universe.json`.
- `scripts/run_daily_maintenance.py` produces truthful raw coverage reports under `reports/data/`.
- `scripts/check_training_data_quality.py` writes `reports/training/training_data_quality_report.md`.
- `scripts/run_alpha_robust_training.py` writes `data/registry/latest_training_manifest.json`.
- `scripts/run_institutional_pipeline.py` writes `reports/pipeline/institutional_pipeline_summary.json`.
- `scripts/run_paper_trading.py` still runs the existing end-to-end paper path.
- `src/mytradingbot/runtime/store.py` persists restart-safe runtime state under `data/state/`.
- `reports/signals/`, `reports/paper_trading/`, `reports/analytics/`, and `data/ledger/` contain decision/session artifacts after a paper run.
- `scripts/run_live_trading.py` remains visible but guarded.
