# Multi-Phase Capabilities Upgrade Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Extend the validated phase-1 repository in place with a repo-owned Alpaca-first data pipeline, explicit phase capability wiring, qlib dataset and training services, and scalping bracket-aware execution while preserving current paper trading behavior.

**Architecture:** Build on the current phase-1 service graph instead of introducing a parallel subsystem. Shared typed services under `core`, `data`, `qlib_engine`, `execution`, `orchestration`, and `ui_services` remain the single source of truth for CLI, Streamlit, diagnostics, and tests.

**Tech Stack:** Python 3.11, pydantic, pydantic-settings, pandas, pyarrow/parquet via pandas, optional alpaca-py, optional pyqlib, streamlit, pytest

---

### Task 1: Central Capability Model And Repo-Root-Aware Pipeline Settings

**Files:**
- Create: `src/mytradingbot/core/capabilities.py`
- Modify: `src/mytradingbot/core/models.py`
- Modify: `src/mytradingbot/core/settings.py`
- Modify: `src/mytradingbot/core/paths.py`
- Modify: `configs/app.yaml`
- Test: `tests/unit/core/test_capabilities.py`
- Test: `tests/unit/core/test_settings.py`

**Steps:**
1. Write failing tests for phase-state detection, repo-local pipeline paths, and missing `pyqlib` or Alpaca credentials behavior.
2. Run `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/core/test_capabilities.py tests/unit/core/test_settings.py` and verify failure.
3. Implement typed phase capability models, pipeline settings, and repo-root-aware defaults under `data/`, `models/`, and `configs/`.
4. Re-run the targeted tests and make them pass.

### Task 2: Provider Abstraction And Alpaca Historical Adapter

**Files:**
- Create: `src/mytradingbot/data/models.py`
- Create: `src/mytradingbot/data/providers/base.py`
- Create: `src/mytradingbot/data/providers/alpaca_provider.py`
- Create: `src/mytradingbot/data/providers/file_ingest_provider.py`
- Create: `src/mytradingbot/data/storage.py`
- Create: `src/mytradingbot/data/pipeline.py`
- Modify: `src/mytradingbot/data/__init__.py`
- Modify: `pyproject.toml`
- Test: `tests/unit/data/test_alpaca_provider.py`
- Test: `tests/unit/data/test_storage.py`

**Steps:**
1. Write failing tests for enum translation, pagination handling, retry behavior, incremental timestamp detection, whole-batch request shape, and parquet persistence.
2. Run the targeted tests and verify they fail for missing provider and storage logic.
3. Implement provider-agnostic request models, Alpaca enum translation, throttled batched historical-bar fetch logic, file-ingest fallback, and parquet storage helpers.
4. Re-run targeted tests until green.

### Task 3: Normalization, Canonical Schema, And Snapshot Build

**Files:**
- Create: `src/mytradingbot/data/schema.py`
- Modify: `src/mytradingbot/data/service.py`
- Modify: `src/mytradingbot/data/pipeline.py`
- Test: `tests/unit/data/test_normalization.py`
- Test: `tests/unit/data/test_service.py`

**Steps:**
1. Write failing tests for raw-to-canonical normalization, UTC timestamp normalization, duplicate merge behavior, snapshot generation, and chunked symbol processing.
2. Run the targeted data tests and verify failure.
3. Implement canonical normalized schema validation, normalization transforms, snapshot building, and incremental parquet merge behavior.
4. Re-run targeted tests until green.

### Task 4: Qlib-Ready Schema Validation And Transformation Boundary

**Files:**
- Create: `src/mytradingbot/qlib_engine/schema_validator.py`
- Create: `src/mytradingbot/qlib_engine/transformer.py`
- Modify: `src/mytradingbot/qlib_engine/models.py`
- Modify: `src/mytradingbot/qlib_engine/service.py`
- Test: `tests/unit/qlib_engine/test_schema_validator.py`
- Test: `tests/unit/qlib_engine/test_transformer.py`

**Steps:**
1. Write failing tests for canonical schema validation, incompatible schema rejection, qlib-ready transformation, duplicate timestamp handling, and dtype enforcement.
2. Run targeted qlib schema tests and verify failure.
3. Implement explicit canonical-to-qlib-ready validation and transformation services with clear result objects.
4. Re-run targeted tests until green.

### Task 5: Dataset Build, Training, And Prediction Refresh Services

**Files:**
- Create: `src/mytradingbot/qlib_engine/dataset_builder.py`
- Create: `src/mytradingbot/qlib_engine/training.py`
- Create: `src/mytradingbot/qlib_engine/prediction_refresh.py`
- Modify: `src/mytradingbot/qlib_engine/service.py`
- Modify: `configs/qlib/daily.yaml`
- Modify: `configs/qlib/intraday_5min.yaml`
- Test: `tests/unit/qlib_engine/test_service.py`
- Test: `tests/unit/qlib_engine/test_dataset_builder.py`

**Steps:**
1. Write failing tests for phase-2 versus phase-3 capability gating, qlib dataset build orchestration, training failure messaging, prediction refresh contracts, and a guard against `qlib.run.get_data`.
2. Run targeted qlib service tests and verify failure.
3. Implement repo-local dataset build, training, and prediction refresh orchestration using prepared repo-local parquet inputs and explicit `pyqlib` gating.
4. Re-run targeted tests until green.

### Task 6: Orchestration And Thin Scripts For The Canonical Multi-Phase Flow

**Files:**
- Modify: `src/mytradingbot/orchestration/service.py`
- Modify: `scripts/build_qlib_dataset.py`
- Modify: `scripts/train_models.py`
- Modify: `scripts/refresh_predictions.py`
- Modify: `scripts/run_daily_maintenance.py`
- Modify: `scripts/validate_system.py`
- Modify: `scripts/goalcheck.py`
- Create: `scripts/download_market_data.py`
- Create: `scripts/update_market_data.py`
- Create: `scripts/build_market_snapshot.py`
- Test: `tests/integration/test_pipeline_scripts.py`
- Test: `tests/smoke/test_goalcheck.py`

**Steps:**
1. Write failing tests for the canonical CLI flow and phase-aware status reporting.
2. Run the targeted integration and smoke tests and verify failure.
3. Refactor orchestration so scripts are thin wrappers over shared services for download, update, normalize, snapshot, qlib build, training, and refresh.
4. Re-run targeted tests until green.

### Task 7: Scalping Bracket Planning And Synthetic Paper Bracket Execution

**Files:**
- Modify: `src/mytradingbot/core/models.py`
- Modify: `src/mytradingbot/strategies/scalping.py`
- Modify: `src/mytradingbot/risk/service.py`
- Modify: `src/mytradingbot/execution/service.py`
- Modify: `src/mytradingbot/brokers/paper.py`
- Modify: `configs/strategies/scalping.yaml`
- Modify: `configs/risk/default.yaml`
- Test: `tests/unit/strategies/test_scalping_strategy.py`
- Test: `tests/unit/execution/test_service.py`
- Test: `tests/unit/brokers/test_paper_broker.py`
- Test: `tests/integration/test_paper_session.py`

**Steps:**
1. Write failing tests for bracket-plan approval, fee-adjusted expectancy rejection, stop-distance sizing, whole-share rounding down, zero-share skip, synthetic TP or SL exits, and near-close flatten against an open bracket.
2. Run the targeted strategy, execution, broker, and integration tests and verify failure.
3. Implement typed bracket planning, provider-agnostic strategy outputs, execution-layer share constraints, and synthetic bracket state management in the paper broker.
4. Re-run targeted tests until green.

### Task 8: UI Services, Streamlit Pages, And Capability Truth

**Files:**
- Modify: `src/mytradingbot/ui_services/dashboard.py`
- Modify: `src/mytradingbot/ui_services/data_training.py`
- Modify: `src/mytradingbot/ui_services/diagnostics.py`
- Modify: `src/mytradingbot/ui_services/live_trading.py`
- Modify: `src/mytradingbot/ui_services/paper_trading.py`
- Modify: `app/app.py`
- Modify: `app/pages/01_Dashboard.py`
- Modify: `app/pages/03_Data_and_Training.py`
- Modify: `app/pages/04_Paper_Trading.py`
- Modify: `app/pages/05_Live_Trading.py`
- Modify: `app/pages/07_Diagnostics.py`
- Test: `tests/unit/ui_services/test_dashboard.py`
- Test: `tests/unit/ui_services/test_data_training.py`

**Steps:**
1. Write failing tests for capability-aware UI payloads and truthful phase-2 or phase-3 messaging.
2. Run targeted UI tests and verify failure.
3. Implement shared UI payloads for download, update, normalize, snapshot, qlib build, training, refresh, and capability status without causing network calls at import time.
4. Re-run targeted tests until green.

### Task 9: Docs, Runbooks, And Full Verification

**Files:**
- Modify: `README.md`
- Modify: `docs/ARCHITECTURE.md`
- Modify: `docs/FIRST_RUN.md`
- Modify: `docs/RUNBOOK.md`
- Modify: `docs/USER_MANUAL.md`
- Test: `tests/smoke/test_streamlit_structure.py`

**Steps:**
1. Update docs to describe phases 1 through 4, canonical Alpaca-first parquet flow, qlib gating, and the new command order.
2. Run `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q` and verify the full suite passes.
3. Run `python scripts/validate_system.py`, `python scripts/goalcheck.py`, a Streamlit headless launch, and a paper-trading CLI run from refreshed artifacts.
4. Record any remaining guarded or partial limitations explicitly in the docs and final summary.
