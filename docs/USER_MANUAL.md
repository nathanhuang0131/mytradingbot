# User Manual

## What This Platform Does

This platform provides:

- qlib workflow scaffolding for dataset, training, and prediction refresh
- typed signal-to-broker paper trading workflows
- a Streamlit dashboard as the main operator interface
- diagnostics and reporting grounded in recorded session artifacts
- advisory-only LLM assistance

## Supported Strategies

- `scalping`
- `intraday`
- `short_term`
- `long_term`

## Main Pages

### Dashboard

Shows health, prediction readiness, and recent session status.

### Strategy Control

Lets you choose the active strategy and select `dry_run`, `paper`, or visible-but-gated `live`.

### Data and Training

Lets you trigger qlib dataset, training, and prediction refresh scaffolding. These actions fail clearly until qlib is installed and configured.

### Paper Trading

Runs dry-run or paper sessions and displays:

- session summary
- orders
- positions
- trade attempts

### Live Trading

Shows the phase-1 live trading gate. No real live orders are submitted.

### LLM Copilot

Shows advisory-only:

- signal explanation
- diagnostics summary
- strategy comparison

### Diagnostics

Shows stale prediction health, no-trade explanations, and post-session notes.

### Settings

Shows resolved application settings and paths.

## Main Safety Notes

- paper mode first
- qlib remains the authority
- LLM is advisory only
- stale or missing predictions fail clearly
- live trading is gated in phase 1
