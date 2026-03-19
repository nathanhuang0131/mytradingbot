# Architecture

## Overview

The canonical runtime flow is:

`data/raw/alpaca/... parquet -> data/normalized/... parquet -> data/snapshots/market_snapshot.json -> data/qlib/dataset.parquet -> models/qlib/model.pkl -> models/predictions/latest.json -> signal -> strategy -> risk -> execution -> broker -> diagnostics/reporting`

`src/mytradingbot/core/capabilities.py` is the central truth source for phase readiness.

## Phase Capability Model

- Phase 1: paper trading is operational through `src/mytradingbot/orchestration/service.py`, `src/mytradingbot/execution/service.py`, and `src/mytradingbot/brokers/paper.py`.
- Phase 2: repo-local Alpaca download, incremental update, normalization, and snapshot build are provided by `src/mytradingbot/data/pipeline.py`.
- Phase 3: qlib dataset packaging, training, and prediction refresh are provided by `src/mytradingbot/qlib_engine/service.py`, `src/mytradingbot/qlib_engine/dataset.py`, and `src/mytradingbot/qlib_engine/adapter.py`.
- Phase 4: live trading remains guarded through `src/mytradingbot/brokers/alpaca.py`, `src/mytradingbot/risk/service.py`, and `scripts/run_live_trading.py`.

## Core Guarantees

- `src/mytradingbot/qlib_engine/service.py` is the only production authority for direction and ranking.
- `src/mytradingbot/llm/service.py` remains advisory-only.
- `src/mytradingbot/data/providers/alpaca_provider.py` does not leak Alpaca SDK enums outside the provider boundary.
- `src/mytradingbot/data/schema.py` enforces an explicit transformation boundary between repo-local canonical parquet data and qlib-ready data.
- `src/mytradingbot/training/data_quality.py` is the multi-timeframe sufficiency gate for alpha-robust training.
- `src/mytradingbot/runtime/store.py` provides restart-safe runtime state under `data/state/`.
- `src/mytradingbot/runtime/service.py` centralizes freshness checks, decision audit writing, and incident persistence.
- `src/mytradingbot/strategies/scalping.py` emits a typed bracket plan before submission.
- `src/mytradingbot/execution/service.py` enforces whole-share bracket constraints before broker submission.
- `src/mytradingbot/brokers/paper.py` manages synthetic bracket exits for paper mode.

## Layer Map

- `src/mytradingbot/core/`: settings, repo-local paths, enums, shared models, and capability detection.
- `src/mytradingbot/data/`: provider abstraction, Alpaca historical ingestion, parquet storage, normalization, schema validation, and snapshot building.
- `src/mytradingbot/qlib_engine/`: qlib-ready dataset engineering, pyqlib adapter integration, model training, and prediction refresh.
- `src/mytradingbot/signals/`: typed signal exports.
- `src/mytradingbot/strategies/`: canonical strategies and scalping bracket planning.
- `src/mytradingbot/risk/`: live guardrails and intent validation.
- `src/mytradingbot/execution/`: broker execution constraints and routing.
- `src/mytradingbot/brokers/`: paper broker plus guarded Alpaca live scaffold.
- `src/mytradingbot/orchestration/`: end-to-end operator workflows shared by UI and CLI.
- `src/mytradingbot/runtime/`: persistent runtime state, incident storage, and decision/session audit wiring.
- `src/mytradingbot/training/`: training data quality checks, chronological split definitions, and alpha-robust orchestration.
- `src/mytradingbot/diagnostics/`: prediction freshness and no-trade diagnostics.
- `src/mytradingbot/reporting/`: post-session bracket and traceability reporting.
- `src/mytradingbot/llm/`: advisory-only operator tooling.
- `src/mytradingbot/ui_services/`: shared UI service graph for Streamlit pages.

## Data Schema Stages

### Raw Provider Schema

`src/mytradingbot/data/providers/alpaca_provider.py` writes raw parquet with Alpaca-style bar fields under `data/raw/alpaca/bars/<timeframe>/<symbol>.parquet`.

### Normalized Repo Schema

`src/mytradingbot/data/schema.py` normalizes the provider payload into:

- `symbol`
- `timestamp` in UTC
- `timeframe`
- `open`
- `high`
- `low`
- `close`
- `volume`
- `trade_count`
- `vwap`
- `provider`
- `adjustment`
- `feed`

This canonical schema is stored under `data/normalized/bars/<timeframe>/<symbol>.parquet`.

### Qlib-Ready Schema

`src/mytradingbot/data/schema.py` transforms canonical parquet into:

- `instrument`
- `datetime`
- `open`
- `high`
- `low`
- `close`
- `volume`
- `vwap`
- `trade_count`
- `timeframe`

`src/mytradingbot/qlib_engine/dataset.py` then engineers training and prediction features into `data/qlib/dataset.parquet`.

## Execution And Brackets

- `src/mytradingbot/strategies/scalping.py` creates `BracketPlan` artifacts with planned entry, stop, target, fee/slippage assumptions, expected net profit, and reward/risk.
- `src/mytradingbot/risk/service.py` rejects scalping buy intents that do not carry a bracket plan.
- `src/mytradingbot/execution/service.py` rounds bracketed quantities down to whole shares when broker constraints require it, then re-validates the trade.
- `src/mytradingbot/brokers/paper.py` arms synthetic brackets after entry fills and closes them on take-profit, stop-loss, or flatten commands without double-exit behavior.
## Signal Audit and Session Reporting Layer

### Purpose

The signal-audit and session-reporting layer provides institutional-grade observability for the trading decision path.

Its purpose is to ensure that every candidate symbol evaluated by the strategy is traceable from model output through strategy filters, risk checks, execution decisions, and final paper-trading outcome.

### Design goals

The audit/reporting layer is designed to provide:

- deterministic repo-local artifact generation
- explainability for every final decision
- standardized rejection reason taxonomy
- separation of strategy logic from reporting logic
- machine-readable and analyst-friendly outputs
- testable artifact contracts

### Architectural responsibilities

The reporting layer should be split into focused responsibilities:

#### 1. signal decision model
A typed model representing a single candidate decision, including:
- symbol
- timestamp
- strategy
- signal side
- bracket consideration
- raw model outputs
- filter outcomes
- risk outputs
- final status
- rejection reason code/detail

#### 2. session summary model
A typed model representing one paper-trading session, including:
- session id
- start/end time
- strategy
- mode
- input artifacts used
- counts of candidates, accepted decisions, rejected decisions, submitted orders
- grouped rejection statistics
- generated artifact paths
- environment/build metadata where safe

#### 3. writers / serializers
Dedicated writers should emit:
- JSON
- CSV
- human-readable summary

Writers must be resilient to partial optional fields and must not crash when specific strategy metrics are unavailable.

#### 4. taxonomy
Rejection reason codes must live in a centralized typed module so the same codes are used by:
- strategies
- execution
- reporting
- tests
- documentation

### Separation of concerns

Strategy modules should focus on decision logic.

Reporting modules should focus on:
- collecting decision-state snapshots
- serializing audit artifacts
- generating session summaries

Execution modules should focus on:
- routing accepted decisions
- broker submission
- capturing submission outcome

This separation avoids bloated strategy code and keeps the system maintainable.

### Artifact flow

A typical institutional run produces artifacts in this sequence:

1. market data refresh artifacts
2. qlib dataset artifact
3. trained model artifact
4. refreshed predictions artifact
5. signal decision audit artifacts
6. paper-trading session summary artifact
7. validation summaries

## Downloader Truth Rules

- `src/mytradingbot/data/pipeline.py` resolves explicit full-refresh windows per timeframe instead of issuing unconstrained multi-symbol intraday requests.
- `src/mytradingbot/data/providers/alpaca_provider.py` uses symbol chunking and guarded time-window splitting so large universes do not silently truncate at the first page.
- `src/mytradingbot/data/reports.py` emits downloader truth artifacts before normalization is allowed to continue.

## Training Sufficiency Rules

- `1m` target lookback: 60 to 90 trading days.
- `5m` target lookback: 120 to 180 trading days.
- `15m` target lookback: 180 to 252 trading days.
- `1d` target lookback: 2 to 3 years.

`src/mytradingbot/training/service.py` writes the resulting evidence to `reports/training/` and `data/universe/latest_training_eligible_universe.json`.

### Failure philosophy

The reporting layer must not silently hide failures.

Rules:
- missing required runtime inputs should fail loudly
- optional metrics may be omitted, but omission should be explicit
- every final decision should still produce a valid audit record
- session summary should be produced even when zero trades are placed

### No-trade sessions

The architecture treats a no-trade session as a valid operational outcome when:
- the runtime path completed successfully
- prediction and decision artifacts were produced
- all candidate symbols were rejected or skipped for explicit reasons

This is distinct from:
- runtime failure
- misconfiguration
- missing data
- broken broker integration

### Operational readiness

This architecture supports institutional-grade paper trading by emphasizing:
- reproducibility
- observability
- artifact discipline
- typed contracts
- test-backed behavior

It does not by itself imply live-trading readiness. Live deployment remains a separate gated phase.
