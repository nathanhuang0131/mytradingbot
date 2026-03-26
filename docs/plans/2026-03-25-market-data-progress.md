# Market Data Progress Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add a live progress window to the Streamlit `Data Management` page's `Market Data` tab for download and update actions.

**Architecture:** Add a small market-data progress tracker that records pipeline stage updates to a repo-local runtime JSON file, expose the latest progress state through the data-training UI service, and render a structured progress window in the Streamlit market-data tab. Keep existing market-data result artifacts and final payloads intact.

**Tech Stack:** Python, Pydantic, Streamlit, pytest

---

### Task 1: Add failing tests for progress models and UI service progress state

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\ui_services\test_data_training.py`
- Test: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\ui_services\test_data_training.py`

**Step 1: Write the failing test**

Add tests that expect:
- a progress payload can be read before and after a tracked market-data action
- the payload includes operation, run status, current step, timeframe rows, and output folder paths

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/ui_services/test_data_training.py`

Expected: FAIL because the UI service does not yet expose market-data progress tracking.

**Step 3: Write minimal implementation**

Add progress-related models and a UI service API for reading the latest market-data progress payload.

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/ui_services/test_data_training.py`

Expected: PASS

### Task 2: Add failing tests for pipeline progress event emission

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\data\test_pipeline.py`
- Test: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\data\test_pipeline.py`

**Step 1: Write the failing test**

Add a test that runs the pipeline with a progress callback and expects events for:
- run started
- timeframe started
- timeframe raw download completed
- timeframe normalization completed
- snapshot completed
- run completed

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/data/test_pipeline.py`

Expected: FAIL because the pipeline does not yet emit progress events.

**Step 3: Write minimal implementation**

Extend the pipeline to accept an optional progress callback and emit typed events at each major stage.

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/data/test_pipeline.py`

Expected: PASS

### Task 3: Add failing tests for Streamlit market-data progress rendering

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\tests\smoke\test_streamlit_structure.py`
- Test: `C:\Users\User\Documents\MyTradingBot_Next\tests\smoke\test_streamlit_structure.py`

**Step 1: Write the failing test**

Add structure assertions for:
- a market-data progress section
- per-timeframe table rendering
- remaining-steps rendering
- progress polling/refresh handling while a market-data run is active

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/smoke/test_streamlit_structure.py`

Expected: FAIL because the current page only renders raw JSON results.

**Step 3: Write minimal implementation**

Update the Streamlit page to render the new progress view and refresh behavior.

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/smoke/test_streamlit_structure.py`

Expected: PASS

### Task 4: Implement the progress tracker and UI service integration

**Files:**
- Create: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\market_data_progress.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\data_training.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\data\models.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\data\pipeline.py`

**Step 1: Write the failing test**

Use the tests from Tasks 1 and 2.

**Step 2: Run test to verify it fails**

Run the focused test commands from Tasks 1 and 2.

**Step 3: Write minimal implementation**

Implement:
- progress models
- runtime JSON storage for latest progress state
- pipeline event emission
- tracked market-data action methods in the UI service

**Step 4: Run test to verify it passes**

Run:
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/ui_services/test_data_training.py`
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/data/test_pipeline.py`

Expected: PASS

### Task 5: Implement the Market Data tab progress window

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\app\pages\03_Data_Management.py`
- Test: `C:\Users\User\Documents\MyTradingBot_Next\tests\smoke\test_streamlit_structure.py`

**Step 1: Write the failing test**

Use the smoke assertions from Task 3.

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/smoke/test_streamlit_structure.py`

Expected: FAIL

**Step 3: Write minimal implementation**

Render:
- current market-data run summary
- per-timeframe progress table
- remaining steps
- output folder summary
- final result in an expander

Refresh the page while the run is active.

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/smoke/test_streamlit_structure.py`

Expected: PASS

### Task 6: Verify the full behavior

**Files:**
- Verify: `C:\Users\User\Documents\MyTradingBot_Next\app\pages\03_Data_Management.py`
- Verify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\data_training.py`
- Verify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\data\pipeline.py`

**Step 1: Run focused verification**

Run:
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q tests/unit/ui_services/test_data_training.py tests/unit/data/test_pipeline.py tests/smoke/test_streamlit_structure.py`

Expected: PASS

**Step 2: Run full verification**

Run:
- `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 python -m pytest -q`

Expected: PASS

**Step 3: Run Streamlit smoke boot**

Run:
- `python -m streamlit run app/app.py --server.headless true --server.port 8515`

Expected: Streamlit boots successfully and the renamed `Data Management` page loads in the app structure.
