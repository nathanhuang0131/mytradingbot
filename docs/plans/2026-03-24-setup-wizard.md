# Setup Wizard Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a dedicated Streamlit setup wizard page with auto-saved user profiles, profile-scoped active universes, resolved session configs, and real session launch wiring while preserving the current dashboard and CLI flows.

**Architecture:** Add a new `session_setup` domain for typed wizard configuration and persistence, then expose it through a thin `ui_services.setup_wizard` layer and a new `app/pages/00_Setup_Wizard.py` page. Extend the runtime with an additive resolved-session-config launch path so the wizard can feed the existing execution stack without replacing current entry points.

**Tech Stack:** Streamlit, Pydantic models, repo-local JSON persistence, existing orchestration/runtime services, pytest

---

### Task 1: Add failing wizard domain tests

**Files:**
- Create: `tests/unit/session_setup/test_service.py`
- Create: `tests/unit/ui_services/test_setup_wizard.py`

**Step 1: Write failing tests**

Cover:

- creating a new profile
- loading an existing profile
- preset application
- keep old symbols behavior
- combine old and new symbols behavior
- replace active symbols behavior without deleting history
- resolved session config generation
- recommended-default metadata exposure

**Step 2: Run tests to verify failure**

Run:

```powershell
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/session_setup/test_service.py tests/unit/ui_services/test_setup_wizard.py
```

Expected: import/module failures for new setup-wizard code

### Task 2: Add typed session setup models and storage

**Files:**
- Create: `src/mytradingbot/session_setup/__init__.py`
- Create: `src/mytradingbot/session_setup/models.py`
- Create: `src/mytradingbot/session_setup/storage.py`
- Modify: `src/mytradingbot/core/paths.py`

**Step 1: Implement minimal models**

Create typed models for:

- user profile
- wizard state
- universe selection profile
- refresh profile
- alpha profile
- risk profile
- execution profile
- resolved session config

**Step 2: Implement repo-local storage**

Add JSON read/write helpers for:

- profile files
- latest resolved session config files
- active universe manifests

**Step 3: Run tests**

Run the same targeted tests and confirm storage/path expectations pass or advance to the next failure.

### Task 3: Add presets and resolution service

**Files:**
- Create: `src/mytradingbot/session_setup/presets.py`
- Create: `src/mytradingbot/session_setup/service.py`

**Step 1: Implement preset catalog**

Add presets:

- `Scalping - Local Paper Safe`
- `Scalping - Alpaca Paper Long Only`
- `Scalping - Alpaca Paper Long + Short`
- `Scalping - Smoke Test`
- `Scalping - Overnight Loop`

**Step 2: Implement resolution logic**

Support:

- load/create profile
- apply preset
- derive active universe manifest from keep/combine/replace rules
- auto-save profile/session config
- resolve expected backend actions summary

**Step 3: Re-run targeted tests**

Confirm wizard domain tests go green.

### Task 4: Wire resolved session configs into runtime launch

**Files:**
- Modify: `src/mytradingbot/orchestration/service.py`
- Modify: `src/mytradingbot/orchestration/paper_loop.py`
- Modify: `scripts/run_paper_trading.py`
- Modify: `src/mytradingbot/qlib_engine/service.py`

**Step 1: Add resolved session config loading/apply path**

Support:

- broker mode
- symbol scope from active symbols manifest
- side mode filtering for predictions
- loop cadence settings

**Step 2: Keep existing CLI defaults intact**

Make all new inputs optional and additive.

**Step 3: Add or extend tests**

Update or add tests if needed for side-mode persistence or runtime symbol filtering.

### Task 5: Build the UI service and Streamlit wizard page

**Files:**
- Create: `src/mytradingbot/ui_services/setup_wizard.py`
- Create: `app/pages/00_Setup_Wizard.py`
- Modify: `app/app.py`
- Modify: `app/pages/01_Dashboard.py`
- Modify: `app/components/runtime.py`

**Step 1: Add UI service**

Expose:

- profile list
- preset list
- recommended-default metadata
- review summary payload
- save/start actions

**Step 2: Add the dedicated page**

Implement the 8-step wizard with:

- progress header
- Previous and Next buttons
- basic/advanced/expert visibility
- recommended-default indicators
- review and start controls

**Step 3: Add discoverability link**

Add a clear wizard entry point from the landing/dashboard without changing default behavior.

**Step 4: Run UI-service tests**

Verify page/service wiring at the unit level.

### Task 6: Document the wizard

**Files:**
- Modify: `README.md`
- Modify: `docs/RUNBOOK.md`

**Step 1: Document**

Add:

- how to launch the wizard
- profile and session-config file locations
- preset names
- symbol keep/combine/new behavior
- historical data retention rule
- wizard as the recommended new setup flow

### Task 7: Verify end-to-end

**Files:**
- No new files required

**Step 1: Run targeted tests**

```powershell
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/session_setup/test_service.py tests/unit/ui_services/test_setup_wizard.py
```

**Step 2: Run the full test suite**

```powershell
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests
```

**Step 3: Smoke the app**

```powershell
python -m streamlit run app/app.py --server.headless true --server.port 8512
```

**Step 4: Confirm wizard-backed config flow**

Verify that:

- the wizard page renders
- a profile file is created
- a resolved session config is written
- the dashboard still renders unchanged
- current scripts still work without using the wizard
