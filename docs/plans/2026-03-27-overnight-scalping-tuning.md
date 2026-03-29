# Overnight Scalping Tuning Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Tune the overnight scalping path to improve controlled accepted submissions while preserving execution quality, restart safety, and fee-aware expectancy discipline.

**Architecture:** Update the existing typed session setup, runtime, strategy, and reporting layers rather than introducing parallel tuning systems. Keep the qlib-to-signal-to-strategy pipeline intact, tighten diagnostics, and make the overnight defaults consistent across core settings, wizard presets, runtime mapping, and session reports.

**Tech Stack:** Python, Pydantic, Streamlit UI services, pytest, repo-local markdown and CSV reporting

---

### Task 1: Capture the new overnight defaults in typed config

**Files:**
- Modify: `src/mytradingbot/core/settings.py`
- Modify: `src/mytradingbot/session_setup/models.py`
- Modify: `src/mytradingbot/session_setup/presets.py`
- Modify: `src/mytradingbot/session_setup/service.py`
- Test: `tests/unit/core/test_settings.py`
- Test: `tests/unit/session_setup/test_service.py`
- Test: `tests/unit/ui_services/test_setup_wizard.py`

**Step 1: Write the failing tests**

- Assert the new default prediction refresh interval is `300` seconds in the typed settings/profile layers.
- Assert the new alpha default predicted return threshold is `0.0008`.
- Assert the overnight preset carries `prediction_refresh_interval_seconds=300` and `predicted_return_threshold=0.0008`.
- Assert the wizard recommended/default copy reflects the new values.

**Step 2: Run the focused tests to verify they fail**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q tests/unit/core/test_settings.py tests/unit/session_setup/test_service.py tests/unit/ui_services/test_setup_wizard.py
```

**Step 3: Implement the minimal config and preset changes**

- Update the core runtime safety default refresh interval to `300`.
- Update session setup profile defaults to `300`.
- Update the overnight preset and recommended defaults.
- Keep loop interval at `300`.

**Step 4: Re-run the focused tests**

Use the same command and verify the config/default assertions pass.

### Task 2: Add tests for scalping throughput tuning behavior

**Files:**
- Test: `tests/unit/strategies/test_scalping_strategy.py`
- Test: `tests/integration/test_paper_session.py`
- Test: `tests/unit/orchestration/test_orchestration_service.py`

**Step 1: Write the failing tests**

- Assert the scalping strategy uses a `6.0` bps spread ceiling.
- Assert a valid signal no longer fails solely because of the synthetic `order_book_imbalance` proxy.
- Assert the predicted return threshold uses the new `0.0008` default path.
- Assert decision audits still reject on VWAP when that rule fails.

**Step 2: Run the focused tests to verify they fail**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q tests/unit/strategies/test_scalping_strategy.py tests/integration/test_paper_session.py tests/unit/orchestration/test_orchestration_service.py
```

**Step 3: Implement the minimal strategy changes**

- Increase the scalping spread threshold to `6.0`.
- Remove the synthetic order-book imbalance proxy as a hard rejection gate, or disable it behind a default-off config flag.
- Preserve the VWAP rule and all expectancy checks.

**Step 4: Re-run the focused tests**

Use the same command and verify the new strategy behavior passes.

### Task 3: Fix invalid payload diagnostics and cooldown enforcement

**Files:**
- Modify: `src/mytradingbot/runtime/models.py`
- Modify: `src/mytradingbot/runtime/service.py`
- Modify: `src/mytradingbot/runtime/store.py`
- Modify: `src/mytradingbot/strategies/scalping.py`
- Test: `tests/unit/runtime/test_runtime_state_service.py`
- Test: `tests/unit/orchestration/test_orchestration_service.py`

**Step 1: Write the failing tests**

- Assert `vwap_relationship` is mapped to a precise rejection code instead of `invalid_signal_payload`.
- Assert `flatten_near_close_logic` is mapped precisely.
- Assert cooldown expiry uses `cooldown_minutes` after a closed bracket rather than the close timestamp itself.
- Assert cooldown survives a new `RuntimeStateService` instance reading the same runtime store.

**Step 2: Run the focused tests to verify they fail**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q tests/unit/runtime/test_runtime_state_service.py tests/unit/orchestration/test_orchestration_service.py
```

**Step 3: Implement the minimal runtime fixes**

- Extend the rejection reason code mapping with precise strategy-rule codes instead of using the generic invalid payload bucket for known rule failures.
- Preserve strict rejection for truly malformed/unavailable data.
- Add a helper that computes cooldown expiry as `closed_at + cooldown_minutes`.
- Persist and read the cooldown through the existing runtime SQLite store.

**Step 4: Re-run the focused tests**

Use the same command and verify the diagnostics and cooldown behavior pass.

### Task 4: Improve decision observability and tuning analytics

**Files:**
- Modify: `src/mytradingbot/runtime/service.py`
- Modify: `src/mytradingbot/reporting/service.py`
- Modify: `src/mytradingbot/reporting/analytics.py`
- Possibly modify: `src/mytradingbot/reporting/trading_universe_audit.py`
- Test: `tests/unit/reporting/test_service.py`
- Test: `tests/unit/reporting/test_analytics.py`
- Test: `tests/unit/orchestration/test_orchestration_service.py`

**Step 1: Write the failing tests**

- Assert the decision audit CSV/markdown contains the richer per-candidate fields required for tuning.
- Assert the session analytics markdown/CSV summarize candidate count, approved count, reject counts by reason, and top blocked symbols.
- Assert approved symbols by frequency and top blocked symbol sections render deterministically.

**Step 2: Run the focused tests to verify they fail**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q tests/unit/reporting/test_service.py tests/unit/reporting/test_analytics.py tests/unit/orchestration/test_orchestration_service.py
```

**Step 3: Implement the reporting enhancements**

- Enrich decision audit rows with spread proxy, liquidity score, VWAP result, confidence, expectancy/bracket detail, and failed reasons list.
- Improve analytics summary generation rather than adding a duplicate exporter.
- Keep all paths repo-local and artifact names consistent with the current layout.

**Step 4: Re-run the focused tests**

Use the same command and verify the reporting assertions pass.

### Task 5: Update UI/help text and operator docs

**Files:**
- Modify: `app/pages/00_Setup_Wizard.py`
- Modify: `src/mytradingbot/ui_services/descriptive_sections.py`
- Modify: `src/mytradingbot/ui_services/setup_wizard.py`
- Modify: `README.md`
- Possibly modify: `docs/RUNBOOK.md`

**Step 1: Write the failing tests**

- Assert the setup wizard help text reflects `0.08%` predicted return and `300` second prediction refresh as the recommended overnight defaults.
- Assert the UI service review payload still presents the updated values.

**Step 2: Run the focused tests to verify they fail**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q tests/unit/ui_services/test_setup_wizard.py tests/smoke/test_streamlit_structure.py
```

**Step 3: Implement the doc and help text updates**

- Update the wizard captions and descriptive sections.
- Update README/runbook operator guidance.
- Include a short operator note that the new tuning profile improves throughput alignment but does not guarantee profitability.

**Step 4: Re-run the focused tests**

Use the same command and verify the UI/help assertions pass.

### Task 6: Run canonical verification

**Files:**
- No new files expected unless validation reveals a missing test/doc adjustment

**Step 1: Run the targeted suites**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q tests/unit/core/test_settings.py tests/unit/session_setup/test_service.py tests/unit/ui_services/test_setup_wizard.py tests/unit/strategies/test_scalping_strategy.py tests/unit/runtime/test_runtime_state_service.py tests/unit/orchestration/test_orchestration_service.py tests/unit/reporting/test_service.py tests/unit/reporting/test_analytics.py tests/integration/test_paper_session.py tests/integration/test_scripts.py
```

**Step 2: Run the canonical repo validation**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q
python scripts/validate_system.py
python scripts/goalcheck.py
```

**Step 3: Verify results and summarize**

- Report the exact final defaults for predicted return threshold, confidence threshold, prediction refresh interval, spread filter, cooldown, and order-book-imbalance status.
- Call out what changed, what was fixed, and what intentionally stayed strict.
