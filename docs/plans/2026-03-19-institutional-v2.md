# Institutional V2 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build the downloader truth fix, top-liquidity universe, persistent runtime state, training quality gates, and institutional orchestration on top of the current working paper-trading repo.

**Architecture:** Extend the current `core -> data -> qlib_engine -> strategies/risk/execution -> brokers -> orchestration` graph rather than replacing it. Add new `universe`, `runtime`, and `training` packages, and make reporting/state shared across CLI and UI.

**Tech Stack:** Python 3.11, Pydantic, pandas, pyarrow parquet, SQLite, Alpaca SDK, pyqlib, pytest, Streamlit.

---

### Task 1: Downloader Truth Foundation

**Files:**
- Modify: `src/mytradingbot/core/settings.py`
- Modify: `src/mytradingbot/data/models.py`
- Modify: `src/mytradingbot/data/pipeline.py`
- Modify: `src/mytradingbot/data/providers/alpaca_provider.py`
- Modify: `src/mytradingbot/data/storage.py`
- Modify: `scripts/run_daily_maintenance.py`
- Test: `tests/unit/data/test_pipeline.py`
- Test: `tests/unit/data/test_alpaca_provider.py`
- Test: `tests/integration/test_scripts.py`

**Steps:**
1. Write failing tests for full-refresh window resolution, symbol-file parsing, shortfall reporting, and normalization refusal after empty download.
2. Run the failing downloader tests and verify the red state.
3. Add explicit start/end handling, timeframe defaults, coverage summaries, and no-mask acceptance gates.
4. Add Alpaca chunking/pagination-safe request handling and deterministic symbol ordering.
5. Re-run downloader tests and adjust until green.

### Task 2: Universe Generation

**Files:**
- Create: `src/mytradingbot/universe/models.py`
- Create: `src/mytradingbot/universe/ranking.py`
- Create: `src/mytradingbot/universe/storage.py`
- Create: `src/mytradingbot/universe/service.py`
- Create: `scripts/generate_top_liquidity_universe.py`
- Modify: `src/mytradingbot/orchestration/service.py`
- Test: `tests/unit/universe/test_ranking.py`
- Test: `tests/unit/universe/test_service.py`
- Test: `tests/integration/test_universe_script.py`

**Steps:**
1. Write failing tests for asset filtering, liquidity ranking, artifact writing, and empty-output failure handling.
2. Implement the universe package and CLI with deterministic ordering and repo-local outputs.
3. Wire `--symbols-file` support into downstream orchestration.
4. Re-run universe tests until green.

### Task 3: Training Quality and Robust Training

**Files:**
- Create: `src/mytradingbot/training/models.py`
- Create: `src/mytradingbot/training/data_quality.py`
- Create: `src/mytradingbot/training/splits.py`
- Create: `src/mytradingbot/training/storage.py`
- Create: `src/mytradingbot/training/service.py`
- Create: `scripts/check_training_data_quality.py`
- Create: `scripts/run_alpha_robust_training.py`
- Modify: `src/mytradingbot/qlib_engine/dataset.py`
- Modify: `src/mytradingbot/qlib_engine/service.py`
- Test: `tests/unit/training/test_data_quality.py`
- Test: `tests/unit/training/test_splits.py`
- Test: `tests/unit/training/test_service.py`

**Steps:**
1. Write failing tests for timeframe sufficiency checks, training-eligible universe construction, chronological splits, and manifest/report writing.
2. Implement the training package and robust runner.
3. Add dataset/model metadata and training acceptance gates.
4. Re-run training tests until green.

### Task 4: Persistent Runtime State and Observability

**Files:**
- Create: `src/mytradingbot/runtime/models.py`
- Create: `src/mytradingbot/runtime/store.py`
- Create: `src/mytradingbot/runtime/service.py`
- Create: `src/mytradingbot/runtime/reconcile.py`
- Modify: `src/mytradingbot/core/models.py`
- Modify: `src/mytradingbot/brokers/paper.py`
- Modify: `src/mytradingbot/execution/service.py`
- Modify: `src/mytradingbot/risk/service.py`
- Modify: `src/mytradingbot/reporting/models.py`
- Modify: `src/mytradingbot/reporting/service.py`
- Modify: `src/mytradingbot/diagnostics/service.py`
- Modify: `src/mytradingbot/orchestration/service.py`
- Test: `tests/unit/runtime/test_store.py`
- Test: `tests/unit/runtime/test_service.py`
- Test: `tests/unit/reporting/test_audit_service.py`
- Test: `tests/integration/test_restart_safe_runtime.py`

**Steps:**
1. Write failing tests for cooldown persistence, duplicate-order prevention, bracket persistence, incident ledgers, and audit generation on zero-trade sessions.
2. Implement the runtime SQLite store and reconciliation helpers.
3. Persist session/order/fill/position/bracket/cooldown/incidents through the paper broker and orchestration flow.
4. Emit CSV/JSON/Markdown decision audit and session report artifacts.
5. Re-run runtime and reporting tests until green.

### Task 5: Institutional Orchestration and Freshness Gates

**Files:**
- Modify: `src/mytradingbot/data/service.py`
- Modify: `src/mytradingbot/qlib_engine/models.py`
- Modify: `src/mytradingbot/qlib_engine/service.py`
- Modify: `src/mytradingbot/ui_services/dashboard.py`
- Modify: `src/mytradingbot/ui_services/data_training.py`
- Create: `scripts/run_institutional_pipeline.py`
- Modify: `scripts/run_loop_trading.py`
- Test: `tests/unit/orchestration/test_institutional_pipeline.py`
- Test: `tests/integration/test_institutional_pipeline.py`

**Steps:**
1. Write failing tests for stale artifact blocking, supervised loop behavior, and canonical pipeline summary outputs.
2. Implement freshness policies and integrate them into orchestration.
3. Add the institutional pipeline script and replace the naive loop with a supervised stateful runner.
4. Re-run orchestration tests until green.

### Task 6: Docs, Metadata, and Final Verification

**Files:**
- Modify: `README.md`
- Create: `SUCCESS.md`
- Modify: `docs/FIRST_RUN.md`
- Modify: `docs/RUNBOOK.md`
- Modify: `docs/USER_MANUAL.md`
- Modify: `docs/ARCHITECTURE.md`
- Create: `docs/RELEASE_NOTES_V2.md`
- Modify: `pyproject.toml`

**Steps:**
1. Update operator docs for the v2 downloader, universe generation, training quality, runtime state, and institutional pipeline.
2. Add only the minimal package metadata changes required.
3. Run the full repo verification commands in the `mytradingbot` environment.
4. Record exact outputs, artifact paths, counts, and remaining limitations in the final report.
