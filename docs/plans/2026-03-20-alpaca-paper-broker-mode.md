# Alpaca Paper Broker Mode Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a real `alpaca_paper_api` broker mode alongside the existing `local_paper` simulator, with bot-owned-only reconciliation, Alpaca-backed paper execution, fee-aware analytics, and restart-safe reporting.

**Architecture:** Keep strategy, risk, and execution provider-agnostic. Select the broker at orchestration startup, isolate Alpaca Trading API behavior in a dedicated broker adapter, reconcile bot-owned Alpaca state into the existing repo-local SQLite runtime store, and keep foreign/manual paper activity visible but read-only and excluded from bot profitability by default.

**Tech Stack:** Python, pydantic, sqlite3, alpaca-py Trading API, pytest

---

### Task 1: Write broker-mode and ownership tests

**Files:**
- Modify: `tests/unit/runtime/test_runtime_state_service.py`
- Create: `tests/unit/brokers/test_alpaca_paper.py`
- Create: `tests/unit/runtime/test_reconcile.py`

**Step 1: Write the failing tests**

- Add tests for `broker_mode=alpaca_paper_api`
- Add tests for `bot_owned`, `foreign`, and `unknown` ownership classification
- Add tests for same-symbol foreign exposure blocking new entries

**Step 2: Run the targeted tests to verify they fail**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/runtime/test_runtime_state_service.py tests/unit/brokers/test_alpaca_paper.py tests/unit/runtime/test_reconcile.py`

**Step 3: Implement the minimal runtime/broker model additions**

- add broker mode config/model extensions
- add ownership class models

**Step 4: Re-run the targeted tests**

Run the same command and keep iterating until green.

### Task 2: Implement Alpaca paper broker adapter

**Files:**
- Create: `src/mytradingbot/brokers/alpaca_paper.py`
- Modify: `src/mytradingbot/brokers/base.py`
- Modify: `src/mytradingbot/core/settings.py`

**Step 1: Write the failing broker adapter tests**

- preflight failure on missing credentials or account query failure
- bracket payload mapping for long bracket orders
- deterministic `client_order_id` propagation
- reconcile bot-owned orders without adopting foreign orders

**Step 2: Run the targeted broker tests to verify they fail**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/brokers/test_alpaca_paper.py`

**Step 3: Implement the adapter**

- use Alpaca paper endpoint only
- use existing Alpaca settings pattern
- support account query, order submit, order query, cancel, and reconciliation
- classify ownership from `client_order_id` and lineage

**Step 4: Re-run targeted tests**

Keep iterating until green.

### Task 3: Wire broker selection into orchestration

**Files:**
- Modify: `src/mytradingbot/orchestration/service.py`
- Modify: `src/mytradingbot/orchestration/paper_loop.py`
- Modify: `scripts/run_paper_trading.py`

**Step 1: Write failing routing tests**

- local paper still routes to `src/mytradingbot/brokers/paper.py`
- Alpaca paper mode uses the new adapter
- loop startup banner includes broker mode, base URL, submission flag, runtime DB, and ownership mode

**Step 2: Run targeted tests to verify failure**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/orchestration/test_paper_loop_service.py tests/integration/test_scripts.py`

**Step 3: Implement broker selection and preflight**

- add `--broker-mode`
- enforce Alpaca preflight before session execution
- log/persist startup banner and ownership policy

**Step 4: Re-run tests**

### Task 4: Implement ownership-aware reconciliation and risk context

**Files:**
- Create: `src/mytradingbot/runtime/reconcile.py`
- Modify: `src/mytradingbot/runtime/store.py`
- Modify: `src/mytradingbot/runtime/service.py`
- Modify: `src/mytradingbot/risk/service.py`

**Step 1: Write the failing reconciliation tests**

- bot-owned-only reconciliation
- no accidental adoption of foreign positions
- same-symbol foreign exposure blocks new entry
- restart-safe dedupe from Alpaca lineage/client order IDs

**Step 2: Run tests to verify failure**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/runtime/test_reconcile.py tests/unit/risk/test_service.py`

**Step 3: Implement reconciliation and risk hooks**

- persist ownership class
- store foreign exposure snapshots and incidents
- block same-symbol new entries on foreign/unknown open exposure

**Step 4: Re-run tests**

### Task 5: Implement fee and cost analytics

**Files:**
- Create: `src/mytradingbot/analytics/fees.py`
- Create: `src/mytradingbot/analytics/costs.py`
- Modify: `src/mytradingbot/reporting/analytics.py`
- Create: `tests/unit/analytics/test_fees.py`
- Modify: `tests/unit/reporting/test_analytics.py`

**Step 1: Write the failing fee tests**

- direct fee calculation
- platform-cost allocation
- analytics exclusion of foreign activity
- `fee_schedule_version` propagation

**Step 2: Run tests to verify failure**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/analytics/test_fees.py tests/unit/reporting/test_analytics.py`

**Step 3: Implement the fee/cost layer**

- add configurable Alpaca fee schedule defaults
- compute gross and net PnL fields
- exclude foreign/unknown trades from strategy profitability by default

**Step 4: Re-run tests**

### Task 6: Add Alpaca paper broker probe utility

**Files:**
- Create: `scripts/check_alpaca_paper_broker.py`
- Modify: `tests/integration/test_scripts.py`

**Step 1: Write the failing probe tests**

- account probe output includes broker mode, ownership policy, account status, and recent order summaries

**Step 2: Run targeted tests to verify failure**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/integration/test_scripts.py`

**Step 3: Implement the probe script**

- validate credentials
- query paper account
- print account status and buying power
- show broker mode and ownership policy
- optionally summarize bot-owned vs foreign recent orders

**Step 4: Re-run tests**

### Task 7: Update docs

**Files:**
- Modify: `README.md`
- Modify: `docs/RUNBOOK.md`

**Step 1: Update operator docs**

- explain `local_paper` vs `alpaca_paper_api`
- explain `bot_owned_only`
- explain foreign read-only exposure
- explain fee model fields and platform cost allocation
- add smoke-test and overnight commands

**Step 2: Review docs against actual commands and artifact paths**

### Task 8: Full verification

**Files:**
- No new files

**Step 1: Run the full suite**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests`

**Step 2: Run the broker probe**

Run: `python scripts/check_alpaca_paper_broker.py`

**Step 3: Run a bounded local paper session**

Run: `python scripts/run_paper_trading.py --strategy scalping --mode paper --broker-mode local_paper --loop --interval-seconds 0 --max-cycles 1 --verbose`

**Step 4: Run a bounded Alpaca paper session**

Run: `python scripts/run_paper_trading.py --strategy scalping --mode paper --broker-mode alpaca_paper_api --loop --interval-seconds 0 --max-cycles 1 --verbose`

**Step 5: Verify outputs**

- Alpaca paper account receives the bot-owned order
- repo analytics show the reconciled order/fill state
- foreign/manual activity is visible but not adopted

