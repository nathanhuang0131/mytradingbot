# Trading Universe Page Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a standalone Streamlit Trading Universe page that previews and persists the final profile-scoped active universe for scalping, including old/new diff counts, manual symbol additions, and shared storage with the existing setup wizard; also add a repo-root `standard operation.md` covering the current CLI/UI command surface.

**Architecture:** Extend the existing `session_setup` domain with reusable final-universe preview and save helpers, expose them through a new `ui_services.trading_universe` layer, and render them from a new `app/pages/09_Trading_Universe.py` sidebar page. Keep the page thin, reuse profile/session-config storage, and generate the runbook from the currently implemented scripts and Streamlit entry points rather than inventing new operations.

**Tech Stack:** Streamlit, Pydantic, repo-local JSON persistence, existing universe/session-setup services, argparse-based scripts, pytest

---

### Task 1: Add failing domain tests for final-universe preview and persistence

**Files:**
- Modify: `tests/unit/session_setup/test_service.py`

**Step 1: Write the failing tests**

Add tests for:

- previewing final symbols for `keep_old`, `combine_old_and_new`, and `only_new`
- counting removed symbols versus the previous manifest
- counting added symbols versus the previous manifest
- normalizing, deduping, and persisting manual additions
- updating the latest session config metadata after saving a final universe

**Step 2: Run the tests to verify failure**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/session_setup/test_service.py
```

Expected: FAIL because the new final-universe preview/save behavior does not exist yet.

**Step 3: Commit**

```powershell
git add tests/unit/session_setup/test_service.py
git commit -m "test: add trading universe service coverage"
```

### Task 2: Add failing UI and Streamlit coverage for the new sidebar page

**Files:**
- Create: `tests/unit/ui_services/test_trading_universe.py`
- Modify: `tests/smoke/test_streamlit_structure.py`

**Step 1: Write the failing tests**

Cover:

- UI service payload generation for saved profiles and final-universe preview data
- save action result metadata
- presence of `app/pages/09_Trading_Universe.py` in Streamlit smoke coverage

**Step 2: Run the tests to verify failure**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/ui_services/test_trading_universe.py tests/smoke/test_streamlit_structure.py
```

Expected: FAIL because the UI service and page do not exist yet.

**Step 3: Commit**

```powershell
git add tests/unit/ui_services/test_trading_universe.py tests/smoke/test_streamlit_structure.py
git commit -m "test: add trading universe UI coverage"
```

### Task 3: Implement reusable final-universe models and service logic

**Files:**
- Modify: `src/mytradingbot/session_setup/models.py`
- Modify: `src/mytradingbot/session_setup/service.py`
- Modify: `src/mytradingbot/session_setup/storage.py`

**Step 1: Add minimal typed models**

Add models for:

- manual symbol input payload
- final-universe preview payload
- diff counts and symbol lists
- save result payload

Keep names and fields focused on what the page needs now.

**Step 2: Implement final-universe preview helpers**

Add service methods that:

- load the previous active manifest for a selected profile
- accept `keep_old`, `combine_old_and_new`, or `only_new`
- merge generated symbols and manual additions
- normalize to uppercase and dedupe
- compute added/removed/final counts and lists

**Step 3: Implement save helpers**

Add service methods that:

- persist the final manifest to `data/runtime/active_universes/<profile>_active_symbols.json`
- update the latest session config for the same profile when present
- keep historical raw/normalized data untouched

**Step 4: Run the targeted tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/session_setup/test_service.py
```

Expected: PASS for the new domain behavior.

**Step 5: Commit**

```powershell
git add src/mytradingbot/session_setup/models.py src/mytradingbot/session_setup/service.py src/mytradingbot/session_setup/storage.py tests/unit/session_setup/test_service.py
git commit -m "feat: add trading universe preview service"
```

### Task 4: Implement the Trading Universe UI service

**Files:**
- Create: `src/mytradingbot/ui_services/trading_universe.py`

**Step 1: Write the minimal UI service**

Expose methods to:

- list profiles and current profile metadata
- preview the final universe for the selected profile
- save the final universe manifest
- reuse existing top-liquidity generation through the session-setup service

Keep all non-UI logic delegated to the service layer.

**Step 2: Run the UI test**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/ui_services/test_trading_universe.py
```

Expected: PASS for the new UI service payloads.

**Step 3: Commit**

```powershell
git add src/mytradingbot/ui_services/trading_universe.py tests/unit/ui_services/test_trading_universe.py
git commit -m "feat: add trading universe UI service"
```

### Task 5: Add the standalone Streamlit sidebar page

**Files:**
- Create: `app/pages/09_Trading_Universe.py`
- Modify: `tests/smoke/test_streamlit_structure.py`

**Step 1: Build the page**

Render:

- profile selector
- universe mode selector
- liquidity filter inputs when generation is required
- manual additions textarea
- preview and save buttons
- metrics for final total, removed count, added count, and manual additions
- symbol lists for previous, new, added, removed, and final universes

**Step 2: Keep the page thin**

Call only the new UI service from the page. Do not place merge/diff/persistence logic in Streamlit callbacks.

**Step 3: Run the smoke and UI tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/ui_services/test_trading_universe.py tests/smoke/test_streamlit_structure.py
```

Expected: PASS with the new page present.

**Step 4: Commit**

```powershell
git add app/pages/09_Trading_Universe.py tests/smoke/test_streamlit_structure.py
git commit -m "feat: add trading universe streamlit page"
```

### Task 6: Add the standard operations runbook and documentation links

**Files:**
- Create: `standard operation.md`
- Modify: `README.md`
- Modify: `docs/RUNBOOK.md`

**Step 1: Document the current operator surfaces**

Cover:

- Streamlit launch and current page inventory
- standard universe, data, quality, qlib, training, prediction, and scalping loop commands
- one-off commands already present under `scripts/`
- validation and smoke commands

**Step 2: Capture real option surfaces**

Use the current script parsers and current Streamlit page files so the runbook reflects what the repo actually supports now.

**Step 3: Run documentation-adjacent tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/smoke/test_streamlit_structure.py
```

Expected: PASS and documentation updated without breaking page expectations.

**Step 4: Commit**

```powershell
git add "standard operation.md" README.md docs/RUNBOOK.md
git commit -m "docs: add standard operations runbook"
```

### Task 7: Verify end-to-end

**Files:**
- No new files required

**Step 1: Run focused tests**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/session_setup/test_service.py tests/unit/ui_services/test_trading_universe.py tests/smoke/test_streamlit_structure.py
```

**Step 2: Run the full suite required by the repo instructions**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q
```

**Step 3: Smoke the dashboard launch**

```powershell
python -m streamlit run app/app.py --server.headless true --server.port 8512
```

**Step 4: Confirm operator outcomes**

Verify that:

- the new `Trading Universe` page appears in the sidebar
- a saved profile can preview its final active universe
- manual additions land in the saved manifest
- the saved manifest updates the latest session config when present
- `standard operation.md` documents the current CLI/UI flows, including one-off commands and Streamlit pages
