# Qlib Trading Universe And Wizard Thresholds Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add full qlib prediction inspection to the Trading Universe page, including raw/final views and derived TP/SL columns, and add editable scalping predicted-return/confidence thresholds to the Setup Wizard so they persist per profile and apply at runtime without changing other scalping logic.

**Architecture:** Extend the Trading Universe UI service to load and enrich qlib prediction rows using the existing final-universe resolution and current scalping target-delta logic, then render those rows through a new toggle in the standalone Streamlit page. Extend session-setup models/runtime wiring so wizard-saved thresholds flow into runtime settings, and update the scalping strategy to consume those settings instead of hard-coded thresholds.

**Tech Stack:** Streamlit, Pydantic, existing qlib/runtime services, repo-local session config persistence, pytest

---

### Task 1: Add failing tests for wizard threshold persistence and runtime application

**Files:**
- Modify: `tests/unit/session_setup/test_service.py`
- Modify: `tests/unit/orchestration/test_orchestration_service.py`
- Modify: `tests/unit/strategies/test_scalping_strategy.py`

**Step 1: Write the failing tests**

Cover:

- wizard state persists `predicted_return_threshold` and `confidence_threshold`
- resolved session configs carry those values
- runtime application moves them into scalping settings
- scalping evaluates signals using the runtime-configured thresholds instead of fixed class constants

**Step 2: Run the tests to verify failure**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/session_setup/test_service.py tests/unit/orchestration/test_orchestration_service.py tests/unit/strategies/test_scalping_strategy.py
```

Expected: FAIL because the wizard and runtime do not yet carry configurable scalping thresholds.

### Task 2: Add failing tests for qlib prediction table enrichment

**Files:**
- Modify: `tests/unit/ui_services/test_trading_universe.py`

**Step 1: Write the failing tests**

Cover:

- loading all qlib prediction rows into the Trading Universe payload
- `Raw qlib prediction artifacts` view returns all rows
- `Final qlib trading universe` view returns only rows in the resolved final symbol set
- each row includes:
  - raw qlib attributes
  - `is_final_symbol`
  - `indicated_tp_pct`
  - `indicated_sl_pct`

**Step 2: Run the tests to verify failure**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/ui_services/test_trading_universe.py
```

Expected: FAIL because the UI service does not yet expose enriched qlib prediction rows.

### Task 3: Add threshold fields to settings and session-setup models

**Files:**
- Modify: `src/mytradingbot/core/settings.py`
- Modify: `src/mytradingbot/session_setup/models.py`
- Modify: `src/mytradingbot/session_setup/service.py`

**Step 1: Implement minimal settings support**

Add repo-default scalping settings fields for:

- `predicted_return_threshold`
- `confidence_threshold`

Use the current defaults:

- `0.005`
- `0.6`

**Step 2: Extend wizard/session models**

Add the same two fields to the alpha-oriented wizard profile model so they persist with resolved session configs.

**Step 3: Run targeted tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/session_setup/test_service.py
```

Expected: threshold persistence tests pass or move to the next missing runtime hook.

### Task 4: Wire wizard thresholds into runtime execution

**Files:**
- Modify: `src/mytradingbot/session_setup/runtime.py`
- Modify: `src/mytradingbot/strategies/scalping.py`

**Step 1: Apply resolved config to runtime settings**

Map saved wizard values into `settings.scalping`.

**Step 2: Update scalping to consume runtime settings**

Set threshold behavior from `self.settings.scalping` during strategy construction/evaluation while leaving all other scalping logic untouched.

**Step 3: Run focused tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/orchestration/test_orchestration_service.py tests/unit/strategies/test_scalping_strategy.py
```

Expected: PASS for configurable threshold behavior with unchanged TP/SL logic.

### Task 5: Implement qlib prediction enrichment in the Trading Universe UI service

**Files:**
- Modify: `src/mytradingbot/ui_services/trading_universe.py`

**Step 1: Load runtime predictions**

Use the existing prediction loading path so parsing matches the runtime artifact format.

**Step 2: Enrich rows**

For each qlib prediction row, add:

- `is_final_symbol`
- `indicated_tp_pct`
- `indicated_sl_pct`

Use the same resolved final-universe implementation already used by scalping page flow, and derive TP/SL percentages from current scalping target-delta logic only.

**Step 3: Add raw/final view support**

Expose both:

- all rows
- only rows included in the final trading universe

**Step 4: Run the UI tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/ui_services/test_trading_universe.py
```

Expected: PASS for raw/final qlib table payloads.

### Task 6: Update the Streamlit pages

**Files:**
- Modify: `app/pages/09_Trading_Universe.py`
- Modify: `app/pages/00_Setup_Wizard.py`

**Step 1: Update the Trading Universe page**

Add:

- qlib view toggle
- qlib dataframe section
- raw/final filtering
- `is_final_symbol`, `indicated_tp_pct`, and `indicated_sl_pct` columns

Keep the page thin by delegating calculations to the UI service.

**Step 2: Update the Setup Wizard page**

Add editable controls for:

- predicted return threshold
- confidence threshold

Place them in the `Alpha & Model` step and keep them persisted with the rest of the profile config.

**Step 3: Run page-structure tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/smoke/test_streamlit_structure.py tests/unit/ui_services/test_trading_universe.py
```

Expected: PASS with updated page behavior.

### Task 7: Update docs

**Files:**
- Modify: `README.md`
- Modify: `docs/RUNBOOK.md`
- Modify: `standard operation.md`

**Step 1: Document the new operator behavior**

Add notes covering:

- Trading Universe page qlib raw/final views
- meaning of `is_final_symbol`
- wizard control over predicted-return and confidence thresholds
- current default values and how lowering/raising them affects symbol eligibility

**Step 2: Run smoke coverage**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/smoke/test_streamlit_structure.py
```

Expected: PASS with docs updated.

### Task 8: Verify end-to-end

**Files:**
- No new files required

**Step 1: Run focused tests**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/session_setup/test_service.py tests/unit/orchestration/test_orchestration_service.py tests/unit/strategies/test_scalping_strategy.py tests/unit/ui_services/test_trading_universe.py
```

**Step 2: Run full repo verification**

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

- the Trading Universe page shows all qlib prediction rows in raw mode
- final mode shows only symbols included in the implemented final trading universe
- the table includes `is_final_symbol`, `indicated_tp_pct`, and `indicated_sl_pct`
- the wizard saves threshold changes
- future runs use the saved predicted-return and confidence thresholds
