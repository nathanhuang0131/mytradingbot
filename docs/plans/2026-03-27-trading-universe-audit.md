# Trading Universe Audit Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a repo-native reporting utility that generates a single overnight trading universe audit file tracing qlib predictions, filter outcomes, and final trade/no-trade decisions across the whole loop.

**Architecture:** Add a focused reporting service under `src/mytradingbot/reporting/` that reads repo-local session profile, paper-session JSON, and decision-audit JSON artifacts and renders one Markdown report under `reports/overnight/`. Expose it through a thin script wrapper in `scripts/` and cover the behavior with a unit test that uses a temporary repo layout.

**Tech Stack:** Python, pathlib, json, markdown rendering, pytest

---

### Task 1: Add the failing report-generation test

**Files:**
- Create: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\reporting\test_trading_universe_audit.py`

**Step 1: Write the failing test**

Add a test that creates a temporary repo layout with:
- one session profile JSON
- one active universe file
- multiple paper-session JSON artifacts
- matching decision-audit JSON artifacts

Then assert the generator creates one Markdown report containing:
- `Trading Universe Audit`
- the profile name
- configured universe size
- per-session summary information
- symbol-level trade/no-trade reasons

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/reporting/test_trading_universe_audit.py`

Expected: FAIL because the trading universe audit service does not exist yet.

### Task 2: Implement the reporting service

**Files:**
- Create: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\reporting\trading_universe_audit.py`

**Step 1: Write minimal implementation**

Implement a service that:
- resolves the latest session profile or an explicit profile slug
- loads the configured overnight universe
- selects loop sessions within a configurable lookback window anchored to the latest completed session
- matches each session to its decision audit JSON
- derives per-session qlib candidate symbols, trade-approved symbols, blocked symbols, failed filters, and decision reasons
- renders one Markdown audit file into `reports/overnight/`

**Step 2: Run the targeted test**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/reporting/test_trading_universe_audit.py`

Expected: PASS

### Task 3: Add the thin script wrapper

**Files:**
- Create: `C:\Users\User\Documents\MyTradingBot_Next\scripts\generate_trading_universe_audit.py`

**Step 1: Add CLI wrapper**

Parse a small set of flags such as:
- `--profile-slug`
- `--lookback-hours`

Call the reporting service and print the generated file path.

**Step 2: Verify manually**

Run: `python scripts/generate_trading_universe_audit.py --profile-slug nathan_1st_test --lookback-hours 12`

Expected: the command prints a new Markdown report path under `reports/overnight/`.

### Task 4: Verify and document the output

**Files:**
- Create at runtime: `C:\Users\User\Documents\MyTradingBot_Next\reports\overnight\*_trading_universe_audit.md`

**Step 1: Run focused verification**

Run:
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/reporting/test_trading_universe_audit.py`
- `python scripts/generate_trading_universe_audit.py --profile-slug nathan_1st_test --lookback-hours 12`

**Step 2: Inspect the generated report**

Confirm the file shows:
- whole-loop session coverage
- per-session qlib candidate universe
- trade-approved symbols
- explicit reasons for each not-traded symbol
