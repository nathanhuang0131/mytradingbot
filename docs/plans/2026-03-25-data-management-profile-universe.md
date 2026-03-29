# Data Management Profile Universe Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Default the Streamlit `Data Management` page to the selected profile's active universe file and allow operators to override it with another universe JSON/CSV path.

**Architecture:** Extend the data-management UI service with profile-aware universe-source resolution and file-scoped action parameters, then update the Streamlit page to use that service for both display and action routing. Keep the page thin by leaving symbol-file resolution, validation, and preview loading in the service layer.

**Tech Stack:** Streamlit, Pydantic models, repo-local path helpers, existing `SetupWizardService`/`UniverseStorage`, pytest.

---

### Task 1: Add failing tests for profile-aware universe resolution

**Files:**
- Modify: `tests/unit/ui_services/test_data_training.py`
- Test: `tests/unit/ui_services/test_data_training.py`

**Step 1: Write the failing test**

Add tests that verify:
- `DataTrainingService.get_payload()` surfaces saved profile names.
- a new universe-source helper resolves the profile-specific active universe path and loads symbols from it.

**Step 2: Run test to verify it fails**

Run: `python -m pytest -q tests/unit/ui_services/test_data_training.py`

Expected: FAIL because the payload/service does not yet expose profile-aware universe information.

**Step 3: Write minimal implementation**

Add payload fields and the universe-source helper to `src/mytradingbot/ui_services/data_training.py`.

**Step 4: Run test to verify it passes**

Run: `python -m pytest -q tests/unit/ui_services/test_data_training.py`

Expected: PASS

### Task 2: Add failing tests for file-scoped action routing

**Files:**
- Modify: `tests/unit/ui_services/test_data_training.py`
- Test: `tests/unit/ui_services/test_data_training.py`

**Step 1: Write the failing test**

Add tests that verify:
- `download_market_data()` forwards `symbols_file`
- `update_market_data()` forwards `symbols_file`
- `build_dataset()` forwards `symbols_file`
- `check_training_data_quality()` resolves symbols from `symbols_file`
- `run_alpha_robust_training()` forwards `symbols_file`

**Step 2: Run test to verify it fails**

Run: `python -m pytest -q tests/unit/ui_services/test_data_training.py`

Expected: FAIL because the service methods do not yet accept or use `symbols_file`.

**Step 3: Write minimal implementation**

Update `src/mytradingbot/ui_services/data_training.py` to support `symbols_file` and use it as the default path-based source.

**Step 4: Run test to verify it passes**

Run: `python -m pytest -q tests/unit/ui_services/test_data_training.py`

Expected: PASS

### Task 3: Add failing smoke assertions for the page UI

**Files:**
- Modify: `tests/smoke/test_streamlit_structure.py`
- Test: `tests/smoke/test_streamlit_structure.py`

**Step 1: Write the failing test**

Assert that `app/pages/03_Data_Management.py` includes:
- a profile selector
- a universe file path input
- a hint referencing `active_universes`
- service-driven universe resolution

**Step 2: Run test to verify it fails**

Run: `python -m pytest -q tests/smoke/test_streamlit_structure.py`

Expected: FAIL because the current page does not expose those elements.

**Step 3: Write minimal implementation**

Update `app/pages/03_Data_Management.py` to use the new service payload/helper and to route file-scoped actions through the resolved universe path by default.

**Step 4: Run test to verify it passes**

Run: `python -m pytest -q tests/smoke/test_streamlit_structure.py`

Expected: PASS

### Task 4: Run focused and smoke verification

**Files:**
- Modify: none unless failures require fixes
- Test: `tests/unit/ui_services/test_data_training.py`
- Test: `tests/smoke/test_streamlit_structure.py`

**Step 1: Run focused verification**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/ui_services/test_data_training.py tests/smoke/test_streamlit_structure.py
```

**Step 2: Fix any failing behavior**

Make minimal corrections only if the focused tests expose gaps.

**Step 3: Run the broader smoke suite**

Run: `python -m pytest -q tests/smoke`

Expected: PASS

### Task 5: Run a headless Streamlit launch

**Files:**
- Modify: none unless launch fails
- Test: `app/app.py`

**Step 1: Launch Streamlit headlessly**

Run a short headless boot using `python -m streamlit run app/app.py --server.headless true`.

**Step 2: Confirm startup succeeds**

Expected: startup banner appears and the process can be terminated cleanly.
