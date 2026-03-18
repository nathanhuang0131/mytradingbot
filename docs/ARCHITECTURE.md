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
