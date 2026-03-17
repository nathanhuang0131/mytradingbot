# Paper Trading Platform Design

**Date:** 2026-03-17

**Goal**

Build a brand-new, production-shaped, qlib-first, dashboard-first quant trading platform in this repository with a fully runnable phase-1 paper trading path, visible live-trading gating, diagnostics, reporting, and advisory-only LLM tooling.

## Scope and Success Target

Phase 1 delivers a complete paper trading system that is runnable and testable from both the CLI and the Streamlit dashboard. The paper trading path is the primary operational target and must support:

- strategy selection
- dry-run and paper modes
- typed signal generation
- strategy to risk to execution to broker flow
- positions, orders, and trade-attempt visibility
- stale prediction and no-trade diagnostics
- post-session reporting

Live trading remains visible in the architecture and UI, but only as validation and preflight scaffolding. No real live order submission is implemented in phase 1.

## Design Principles

- Qlib is the only production authority for direction and ranking.
- LLM outputs are advisory only and cannot override qlib direction.
- Paper trading is the default operating mode.
- Missing or stale predictions fail explicitly with operator guidance.
- No hidden fallbacks, fake predictions, or temporary shortcut behavior.
- Strategies generate intents only; broker APIs are isolated under `brokers/`.
- Streamlit pages are thin wrappers over `ui_services/`.
- Diagnostics, reporting, and LLM surfaces use real workflow artifacts.

## Architecture

All application code stays under `src/mytradingbot/` using the repository's required package layout:

- `core/`: settings, paths, enums, exceptions, logging, and shared typed runtime models
- `data/`: market snapshots, universe metadata, validation helpers, and data-source abstractions
- `qlib_engine/`: dataset, training, prediction refresh, artifact loading, and qlib availability checks
- `signals/`: typed qlib prediction objects plus enriched market context needed by strategies
- `strategies/`: strategy registry and strategy implementations returning typed trade intents
- `risk/`: risk checks, sizing controls, live-mode guards, and rejection reasons
- `execution/`: execution planning, routing, order lifecycle objects, and broker handoff
- `brokers/`: paper broker implementation and Alpaca validation scaffold
- `orchestration/`: maintenance, prediction refresh, dry-run sessions, paper sessions, and live preflight
- `diagnostics/`: health checks, no-trade diagnostics, broker diagnostics, stale artifact diagnostics
- `reporting/`: session reports, post-market review data, and export-ready artifacts
- `llm/`: advisory-only explanation and summarization services
- `ui_services/`: application services consumed by Streamlit pages

## Runtime Flow

The core runtime flow is:

`qlib prediction -> Signal -> Strategy evaluation -> TradeIntent -> Risk evaluation -> ExecutionRequest -> Broker adapter -> Fill/Status -> Diagnostics/Reporting`

The platform supports three operator-visible modes:

- `dry_run`: executes the full decision pipeline without mutating broker state
- `paper`: executes the full paper trading lifecycle and records orders, fills, positions, and attempts
- `live`: visible but phase-1 gated to validation and preflight only

Every session produces a trace record that preserves:

- signal inputs and freshness state
- strategy decisions and filter outcomes
- risk approvals or rejections
- execution requests
- broker events and simulated fills

## Qlib Integration Strategy

Phase 1 uses adapter-based qlib integration. The dashboard and paper workflow must still load if `pyqlib` is unavailable, but qlib-dependent actions fail clearly and do not silently degrade.

The qlib boundary provides:

- dependency detection for `pyqlib`
- artifact freshness inspection
- dataset build entrypoints
- training entrypoints
- prediction refresh entrypoints
- prediction loading for runtime use

If qlib is unavailable or required artifacts are missing or stale, services return explicit failure results with concrete guidance such as installing `pyqlib`, running training, or refreshing predictions. No synthetic or fallback production predictions are generated.

## Typed Domain Model

Typed models anchor every layer boundary. Shared objects include:

- application settings and mode selection
- artifact metadata and freshness status
- market snapshot
- qlib prediction record
- enriched signal bundle
- strategy decision
- trade intent
- risk decision
- execution request
- broker order
- fill event
- position snapshot
- trade attempt trace
- session diagnostics summary
- post-session report

These models make the signal-to-broker path auditable and allow diagnostics, UI services, and LLM advisory tools to reuse the same real artifacts.

## Strategy Design

The strategy registry uses the exact canonical names:

- `scalping`
- `intraday`
- `short_term`
- `long_term`

All strategies consume typed signals and return typed intents plus structured reasoning.

### Scalping Priority Design

Scalping receives the most complete phase-1 implementation. It is built from modular filters and planners so each decision is explainable and testable. The evaluation order is:

1. qlib direction and ranking gate
2. predicted return threshold
3. confidence threshold
4. VWAP relationship
5. spread filter
6. liquidity filter
7. liquidity stress filter
8. order book imbalance
9. liquidity sweep detection
10. intraday volatility regime
11. adaptive target sizing
12. exit plan generation
13. cooldown logic
14. flatten-near-close logic

The result includes trade direction, target size, take-profit, stop-loss, timeout, and a detailed list of passed and failed filters.

### Other Strategies

`intraday`, `short_term`, and `long_term` reuse the same typed pipeline while varying thresholds, holding period assumptions, turnover expectations, and sizing heuristics. They remain real and runnable in phase 1, but with less microstructure sophistication than `scalping`.

## Risk and Execution

Risk evaluation occurs before any broker interaction and is always explicit. The risk layer handles:

- mode-aware guards
- max position and exposure constraints
- per-symbol throttles
- cooldown enforcement
- duplicate-order prevention
- live-mode hard block in phase 1

The execution layer translates approved trade intents into execution requests. It does not own signal logic and does not embed broker-specific policy. The execution layer delegates to broker adapters only after risk approval.

## Broker Layer

The paper broker is the operational phase-1 broker path. It supports:

- order submission and simulated acceptance
- deterministic or rule-based fill simulation
- position updates
- order history
- trade-attempt storage
- broker diagnostics

The Alpaca path remains a scaffold in phase 1. It validates settings and surfaces readiness or configuration issues, but it does not send live orders.

## UI Design

The Streamlit dashboard is the main operator interface. `app/` contains only thin page wrappers that call `ui_services/`. Required pages are:

- Dashboard
- Strategy Control
- Data and Training
- Paper Trading
- Live Trading
- LLM Copilot
- Diagnostics
- Settings

Each page operates on the same typed state and artifact services used by the CLI scripts. The UI must expose strategy selection, mode selection, health status, prediction freshness, maintenance actions, paper-session execution, diagnostics, and traceability views.

## Diagnostics and Reporting

Diagnostics are first-class outputs, not log-only side effects. Phase-1 diagnostics include:

- system health summary
- qlib dependency and artifact availability
- stale prediction detection
- no-trade diagnostics
- broker diagnostics
- recent orders, positions, and trade attempts
- trace inspection from signal to broker result

Reporting uses session artifacts to produce:

- paper session summary
- post-session review surfaces
- export-ready structured payloads

## LLM Advisory Design

LLM tooling is grounded in real workflow artifacts and never acts as a trading authority. Phase-1 advisory workflows include:

- signal explanation
- diagnostics summary
- strategy comparison
- post-market review
- export pack generation
- structured feedback import

Every LLM prompt is built from typed artifacts generated by the paper trading system. LLM output cannot reverse qlib direction or bypass risk and execution boundaries.

## Testing Strategy

Testing is organized under:

- `tests/unit/`
- `tests/integration/`
- `tests/smoke/`

Coverage focuses on:

- shared models and settings
- qlib availability and artifact freshness handling
- strategy registry and mapping
- scalping filters and exit planning
- risk approvals and rejections
- execution routing
- paper broker state transitions
- orchestration flows for dry-run and paper sessions
- diagnostics and reporting generation
- UI-service behavior
- dashboard startup smoke coverage

`scripts/goalcheck.py` validates the required phase-1 capabilities, including strategy mapping, diagnostics presence, paper workflow, LLM advisory availability, and live-mode gating visibility.

## Documentation Deliverables

Phase 1 maintains and updates:

- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/FIRST_RUN.md`
- `docs/RUNBOOK.md`
- `docs/USER_MANUAL.md`

These docs must reflect the real paper-trading workflow, live gating, qlib failure guidance, and operator usage patterns.

## Delivery Plan

The implementation proceeds as a vertical slice anchored on the paper-trading path:

1. package foundations and settings
2. typed models and runtime state
3. qlib scaffolding with explicit failure handling
4. strategy registry and scalping-first implementation
5. risk and execution flow
6. paper broker and Alpaca validation scaffold
7. orchestration and CLI wrappers
8. Streamlit UI and ui_services
9. diagnostics, reporting, and LLM advisory
10. tests, goalcheck, validation, and doc updates

This order prioritizes a real end-to-end paper workflow over broad placeholder scaffolding.
