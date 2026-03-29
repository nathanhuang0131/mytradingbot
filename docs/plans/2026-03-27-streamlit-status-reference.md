# Streamlit Status Reference Cleanup Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Replace raw JSON-like UI dumps with readable status sections, remove the Paper Trading page, and introduce a profile-aware Status Reference page with Trading Track.

**Architecture:** Add shared descriptive-section models in `ui_services`, update the setup wizard and dashboard to consume them, and replace the raw settings page with a richer Status Reference service that reads saved profile/session artifacts and recent trading history.

**Tech Stack:** Python, Streamlit, Pydantic, pytest

---

### Task 1: Add failing tests for descriptive status payloads

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\ui_services\test_setup_wizard.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\ui_services\test_dashboard.py`
- Create: `C:\Users\User\Documents\MyTradingBot_Next\tests\unit\ui_services\test_status_reference.py`

**Step 1: Write the failing tests**

- Add a setup wizard UI service test that expects friendly review sections instead of raw defaults/customized key dumps.
- Add a dashboard UI service test that expects descriptive capability sections for the landing page.
- Add a status reference UI service test that expects:
  - profile-aware default selection
  - readable sections for the saved config
  - Trading Track data from current session or saved paper-session artifacts

**Step 2: Run tests to verify they fail**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'; pytest -q tests\unit\ui_services\test_setup_wizard.py tests\unit\ui_services\test_dashboard.py tests\unit\ui_services\test_status_reference.py
```

Expected: failing assertions because the current services do not expose the new descriptive payloads.

### Task 2: Implement shared descriptive status models and service helpers

**Files:**
- Create: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\descriptive_sections.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\setup_wizard.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\dashboard.py`
- Create: `C:\Users\User\Documents\MyTradingBot_Next\src\mytradingbot\ui_services\status_reference.py`

**Step 1: Write minimal implementation**

- Add shared Pydantic models for descriptive sections and rows.
- Centralize field labels and “what it is / what it affects” descriptions for strategy, universe, refresh, alpha, risk, and execution fields.
- Extend `SetupWizardUIService` with review-section payload builders.
- Extend `DashboardService` with summary sections instead of only raw capability payloads.
- Implement `StatusReferenceService` to:
  - resolve the active profile
  - load the latest saved config
  - build readable sections
  - assemble Trading Track data from current memory and persisted artifacts

**Step 2: Run targeted tests**

Run the same UI service tests again and iterate until they pass.

### Task 3: Update Streamlit pages to use the new payloads

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\app\app.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\app\components\runtime.py`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\app\pages\00_Setup_Wizard.py`
- Delete: `C:\Users\User\Documents\MyTradingBot_Next\app\pages\04_Paper_Trading.py`
- Move: `C:\Users\User\Documents\MyTradingBot_Next\app\pages\08_Settings.py` -> `C:\Users\User\Documents\MyTradingBot_Next\app\pages\08_Status_Reference.py`

**Step 1: Update the landing page**

- Change the page title and visible title to `Dashboard Summary`.
- Replace the raw capability JSON block with descriptive sections.

**Step 2: Update session-state profile tracking**

- Add helper functions for selected profile name in `app/components/runtime.py`.
- Set the selected profile when the wizard initializes or loads a profile.

**Step 3: Update the setup wizard review rendering**

- Replace raw dict output for risk, execution, and defaults/customized with descriptive sections.
- Replace raw action result JSON with readable saved/launch summaries where practical.

**Step 4: Replace Settings with Status Reference**

- Render the profile selector, readable config sections, artifact status, and Trading Track from `StatusReferenceService`.

### Task 4: Refresh docs and verify end-to-end behavior

**Files:**
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\README.md`
- Modify: `C:\Users\User\Documents\MyTradingBot_Next\docs\RUNBOOK.md`

**Step 1: Update docs**

- Replace references to the `Settings` page with `Status Reference`.
- Remove references to the dedicated `Paper Trading` page where appropriate.
- Note that paper-session review now lives in wizard launch flows and `Status Reference`.

**Step 2: Run verification**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'; pytest -q tests\unit\ui_services\test_setup_wizard.py tests\unit\ui_services\test_dashboard.py tests\unit\ui_services\test_status_reference.py
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'; pytest -q
```

Run a Streamlit smoke check:

```powershell
@'
import subprocess
import sys
import time
from pathlib import Path

root = Path(r"C:\Users\User\Documents\MyTradingBot_Next")
proc = subprocess.Popen(
    [sys.executable, "-m", "streamlit", "run", "app/app.py", "--server.headless", "true", "--server.port", "8513"],
    cwd=root,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
)
try:
    time.sleep(12)
    print(f"RUNNING={proc.poll() is None}")
finally:
    if proc.poll() is None:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except Exception:
            proc.kill()
'@ | python -
```

Expected: targeted tests pass, full suite passes, and Streamlit starts successfully.
