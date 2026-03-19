# Release Notes V2

## Summary

Version `0.2.0` upgrades the repository from a phase-1 runnable paper path into a stricter v2 institutional paper-trading system.

## Added

- `src/mytradingbot/universe/` for top-liquidity universe generation.
- `src/mytradingbot/runtime/` for persistent runtime state, decision audit, incidents, and restart-safe paper execution state.
- `src/mytradingbot/training/` for training data sufficiency checks and alpha-robust orchestration.
- `src/mytradingbot/orchestration/institutional.py` for the canonical v2 institutional pipeline.
- `scripts/generate_top_liquidity_universe.py`
- `scripts/check_training_data_quality.py`
- `scripts/run_alpha_robust_training.py`
- `scripts/run_institutional_pipeline.py`

## Changed

- `src/mytradingbot/data/pipeline.py` now enforces explicit full-refresh windows and refuses to hide downloader failure behind normalization.
- `src/mytradingbot/data/providers/alpaca_provider.py` now uses deterministic chunking and guarded multi-window fetch behavior.
- `src/mytradingbot/strategies/scalping.py`, `src/mytradingbot/risk/service.py`, `src/mytradingbot/execution/service.py`, and `src/mytradingbot/brokers/paper.py` now operate with typed bracket planning and persistent runtime safety context.
- `src/mytradingbot/orchestration/service.py` now records decision audit artifacts and uses restart-safe runtime state.
- `app/pages/03_Data_and_Training.py` and `src/mytradingbot/ui_services/data_training.py` now expose universe generation, training quality, and alpha-robust training actions.

## Canonical V2 Command

`python scripts/run_institutional_pipeline.py --strategy scalping --use-top-liquidity-universe --timeframes 1m 5m 15m 1d --mode paper`
