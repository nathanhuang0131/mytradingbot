# Multi-Phase Capabilities Upgrade Design

**Date:** 2026-03-17

## Goal

Extend the existing phase-1 repository in place into an explicit phase-1 through phase-4 architecture while preserving the validated paper-trading path and adding a canonical repo-owned Alpaca-first data and qlib pipeline.

## Current Baseline

The repository already has a working phase-1 path:

- typed signal, strategy, risk, execution, and broker flow
- in-memory paper broker
- diagnostics and reporting
- advisory-only LLM services
- thin CLI wrappers
- Streamlit dashboard pages

The current gap is that phase-2 and phase-3 workflows are still scaffolds. There is no repo-owned download, update, normalize, qlib-ready transform, or qlib dataset build pipeline yet.

## Phase Model

The repository will explicitly support these stages:

- Phase 1: paper trading operational
- Phase 2: repo-local market data download, update, normalize, and snapshot operational
- Phase 3: qlib dataset build, training, and prediction refresh operational
- Phase 4: broker persistence and guarded live execution scaffolding

Each phase must report truthful capability state:

- enabled
- partial
- blocked

Each blocked or partial state must include actionable operator guidance.

## Architecture Direction

The implementation extends the current phase-1 service graph instead of creating a parallel subsystem. Shared services remain the single source of truth for both CLI and Streamlit.

### Core additions

- central capability and phase status service
- repo-root-aware data pipeline settings
- provider abstraction for historical market data
- canonical normalized schema and explicit qlib-ready transformation boundary
- qlib operational services for dataset build, training, and prediction refresh
- bracket-aware scalping planning and synthetic paper bracket execution

## Data Pipeline Design

The canonical provider for phase 2 is Alpaca historical market data behind a clean provider abstraction.

### Provider abstraction

- `MarketDataProvider` protocol for provider-agnostic download and update requests
- `AlpacaHistoricalProvider` as the first real implementation
- `FileIngestProvider` as a secondary offline and testing path

Provider specifics remain inside the adapter:

- Alpaca SDK enums
- pagination tokens
- batching and throttling
- retry and backoff
- request objects

### Canonical storage

Repo-local parquet is the operational format.

Suggested storage layout:

- `data/raw/alpaca/bars/<timeframe>/<symbol>.parquet`
- `data/normalized/bars/<timeframe>/<symbol>.parquet`
- `data/qlib_ready/bars/<timeframe>/<symbol>.parquet`
- `data/snapshots/market_snapshot.json`
- `data/qlib/<dataset artifacts>`
- `models/qlib/<trained artifacts>`
- `models/predictions/latest.json`

### Operational path

1. download or update raw Alpaca bar data into raw parquet
2. normalize raw provider data into the repo canonical parquet schema
3. validate canonical schema
4. transform canonical schema into qlib-ready schema
5. build qlib-compatible dataset artifacts
6. train model artifacts
7. refresh predictions artifact
8. run paper trading from refreshed artifacts plus market snapshot

Incremental update is the default mode. Full rebuild remains explicit and exceptional.

## Schema Boundary

The repo canonical normalized schema is not forced to equal qlib's schema.

The pipeline will define:

- raw provider schema
- normalized repo schema
- qlib-ready schema

An explicit validation and transformation stage sits between normalized parquet and qlib packaging. Missing columns, wrong dtypes, duplicate timestamps, timezone issues, and naming inconsistencies fail clearly.

## Capability Behavior

- Phase 1 remains runnable without Alpaca and without `pyqlib` if explicit artifacts are supplied.
- Phase 2 can run without `pyqlib`, but needs Alpaca credentials for the canonical provider.
- Phase 3 requires `pyqlib`; missing `pyqlib` produces actionable messages.
- Phase 4 remains guarded and visible only as a scaffold.

There is no fallback to `qlib.run.get_data`.

## Scalping Bracket Planning

Scalping approval is upgraded so entry and bracket plan are approved together.

The strategy and execution path will support:

- typed bracket plan
- stop-loss and take-profit validation
- fee and slippage-adjusted net expectancy
- stop-distance-driven sizing
- provider-agnostic strategy output
- whole-share execution constraints in Alpaca-compatible execution

For paper trading, bracket exits are managed synthetically:

- persist open bracket state
- trigger TP or SL once price thresholds are crossed
- prevent double exits
- support near-close flattening
- report planned versus realized outcome and exit reason

## Concurrency And Performance

Network concurrency and offline worker concurrency are separate settings.

The design includes:

- bounded batch requests
- retry with backoff and jitter
- configurable request concurrency
- configurable processing worker count
- parquet-based incremental processing
- chunked symbol processing
- no uncontrolled multiprocessing from UI import paths

## UI And CLI

The Streamlit dashboard and scripts will consume the same shared capability and orchestration services.

The `Data and Training` page and related scripts will expose:

- phase status
- credential readiness
- raw data readiness
- normalized data readiness
- qlib-ready data readiness
- model readiness
- prediction readiness

## Testing Strategy

Tests remain offline and deterministic.

Coverage additions include:

- capability detection with and without `pyqlib`
- Alpaca enum translation
- pagination and incremental update behavior
- parquet merge and dedupe logic
- schema validation and qlib-ready transformation
- explicit failure without `qlib.run.get_data`
- bracket planning, whole-share rounding, and synthetic bracket exits

## Risks

Main implementation risks:

- broad but necessary surface area across data, qlib, execution, UI, and docs
- keeping phase-1 behavior unchanged while extending scalping execution
- managing provider abstraction without leaking Alpaca SDK types
- keeping tests fast while covering new parquet and pipeline stages

The mitigation is to extend the current graph in small, typed, test-driven steps and run the full suite after each meaningful milestone.
