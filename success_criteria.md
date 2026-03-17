# AGENTS.md

## Mission

Build a brand-new quant trading platform in this repository from scratch.

This project must implement the trading platform discussed across prior project planning conversations, but it must NOT reference, import, modify, or depend on any existing legacy qlibtradingbot repository or code.

The target is a clean, production-shaped, qlib-first, dashboard-first trading platform with paper/live workflows, diagnostics, maintenance, and LLM-assisted operator tooling.

## Product Goals

Create a platform that supports:

- qlib dataset building
- qlib model training
- qlib prediction refresh
- strategy execution
- paper trading
- live trading with explicit safeguards
- diagnostics and validation
- Streamlit dashboard-driven operation
- LLM advisory workflows

## Hard Rules

1. Do not reference any legacy repo or code.
2. Do not assume any old file structure exists.
3. Build everything fresh in this repository.
4. Qlib is the only production authority for direction and ranking.
5. LLM is advisory only and may not reverse qlib direction in production.
6. Paper trading is default.
7. Live trading must be explicitly gated.
8. Missing or stale predictions must fail clearly.
9. No fake production predictions.
10. No hidden fallback behavior.
11. No hard-coded absolute paths outside the repo root.

## Canonical User-Facing Strategies

Use exactly these strategy names:
- scalping
- intraday
- short_term
- long_term

## Scalping Requirements

The scalping strategy must be modular and include support for:
- qlib signal gating
- predicted return threshold
- confidence threshold
- VWAP relationship
- spread filter
- liquidity filter
- liquidity stress filter
- order book imbalance
- liquidity sweep detection
- intraday volatility regime
- adaptive target sizing
- take profit
- stop loss
- timeout exit
- cooldown logic
- flatten-near-close logic

## UI Requirements

Build a Streamlit dashboard as the main operator interface.

Required pages:
- Dashboard
- Strategy Control
- Data and Training
- Paper Trading
- Live Trading
- LLM Copilot
- Diagnostics
- Settings

The UI should allow the user to:
- choose strategy
- choose dry-run / paper / live
- inspect prediction freshness
- trigger maintenance
- trigger training
- trigger prediction refresh
- run paper trading
- inspect diagnostics
- inspect orders, positions, and recent trade attempts

## LLM Requirements

Build advisory-only LLM workflows for:
- signal explanation
- diagnostics summaries
- strategy comparison
- post-market review
- external report/export pack generation
- structured feedback import

## Architecture Requirements

Use clear separation for:
- core
- data
- qlib_engine
- signals
- strategies
- risk
- execution
- brokers
- orchestration
- diagnostics
- reporting
- llm
- ui_services

Strategies must not call broker APIs directly.
Scripts must be thin wrappers.
UI pages must be thin wrappers over ui_services.

## Testing and Validation

Add:
- unit tests
- integration tests
- smoke tests
- goalcheck
- validation scripts

After meaningful implementation steps, run:
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q`

Do not declare completion unless:
- tests pass
- dashboard launches
- docs exist
- strategy selection works
- paper workflow is runnable