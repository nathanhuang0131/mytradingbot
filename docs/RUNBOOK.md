# Runbook

## Daily Workflow

1. Launch `streamlit run app/app.py`.
2. Check `Dashboard` for prediction readiness and health.
3. Use `Strategy Control` to confirm the active strategy and mode.
4. Use `Data and Training` to inspect qlib action readiness.
5. Run a `dry_run` or `paper` session from `Paper Trading`.
6. Review orders, positions, and trade attempts.
7. Open `Diagnostics` to inspect stale artifacts and no-trade explanations.
8. Open `LLM Copilot` for advisory-only summaries.

## Paper Trading Notes

- `paper` is the default operational mode.
- `dry_run` exercises the full pipeline but does not mutate broker state.
- Both paths require a prediction artifact and a market snapshot artifact.

## If No Trades Happen

Check:

- prediction freshness
- missing prediction artifact
- predicted return threshold
- confidence threshold
- VWAP relationship
- spread and liquidity filters
- cooldown logic
- flatten-near-close logic
- risk rejection reasons

## If Qlib Actions Fail

Expected phase-1 causes:

- `pyqlib` is not installed
- no concrete qlib workflow is configured yet
- prediction artifact is missing or stale

The system should fail with explicit guidance and keep the dashboard available.

## Live Trading Status

Live trading is intentionally gated in phase 1.

- the Live Trading page is visible
- Alpaca live submission is disabled
- risk blocks live order approval
- the scaffold is validation-only
