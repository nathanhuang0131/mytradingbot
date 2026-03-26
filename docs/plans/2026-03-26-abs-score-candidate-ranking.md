# Absolute Score Candidate Ranking Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Rank qlib predictions by absolute score magnitude while preserving signed score, signed predicted return, and explicit long/short direction so `candidate_count` can surface the strongest long and short ideas.

**Architecture:** Keep the model output and downstream strategy semantics intact, and change only the prediction artifact ordering and confidence derivation. Runtime candidate slicing remains the same, but it will now operate on an artifact ordered by `abs(score)` rather than raw descending score.

**Tech Stack:** Python, pandas, qlib adapter layer, Pydantic models, pytest

---

### Task 1: Add failing tests for absolute-score artifact ranking

**Files:**
- Modify: `tests/unit/qlib_engine/test_service.py`
- Modify: `tests/unit/orchestration/test_orchestration_service.py`

**Step 1: Write the failing test**

Add coverage for:

- a stronger negative score outranking a weaker positive score when ordered by `abs(score)`
- negative scores keeping `direction = short`
- negative scores keeping signed `score` and signed `predicted_return`
- confidence following absolute score strength

**Step 2: Run test to verify it fails**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/qlib_engine/test_service.py tests/unit/orchestration/test_orchestration_service.py
```

Expected: FAIL because the current adapter ranks by raw descending score and gives misleading confidence ordering.

### Task 2: Implement absolute-score ordering in the prediction adapter

**Files:**
- Modify: `src/mytradingbot/qlib_engine/adapter.py`

**Step 1: Write minimal implementation**

Update prediction generation so it:

- computes an absolute-score helper column
- computes confidence from absolute-score percentile rank
- sorts payload rows by absolute-score descending
- preserves signed `score`
- preserves signed `predicted_return`
- preserves `direction` from sign

**Step 2: Run the focused tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/qlib_engine/test_service.py tests/unit/orchestration/test_orchestration_service.py
```

Expected: PASS for the new ranking and candidate-order semantics.

### Task 3: Add or refine runtime candidate-selection regression coverage

**Files:**
- Modify: `tests/unit/orchestration/test_orchestration_service.py`

**Step 1: Add a candidate-count regression test**

Cover a mixed long/short artifact where:

- a negative score with larger absolute value should be included before a smaller positive score
- the selected trade attempt reaches the bot with `direction = short`

**Step 2: Run the targeted runtime tests**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/orchestration/test_orchestration_service.py
```

Expected: PASS with the new artifact ordering flowing into runtime candidate selection.

### Task 4: Update operator-facing docs

**Files:**
- Modify: `README.md`
- Modify: `docs/RUNBOOK.md`

**Step 1: Document the new meaning**

Explain that:

- `rank` now represents absolute predicted move strength
- `direction` tells whether the move is long or short
- signed `predicted_return` is preserved for interpretation
- `candidate_count` can now pick the strongest short ideas as well as the strongest long ideas

**Step 2: Run a quick smoke check**

Run:

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/orchestration/test_orchestration_service.py tests/unit/qlib_engine/test_service.py
```

Expected: PASS while docs-only edits do not affect behavior.

### Task 5: Verify end-to-end

**Files:**
- No new files required

**Step 1: Run focused verification**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
python -m pytest -q tests/unit/qlib_engine/test_service.py tests/unit/orchestration/test_orchestration_service.py
```

**Step 2: Run full repo verification**

```powershell
$env:PYTEST_DISABLE_PLUGIN_AUTOLOAD='1'
pytest -q
```

**Step 3: Confirm outcome**

Verify that:

- the prediction artifact keeps signed scores and signed returns
- top-ranked rows are chosen by `abs(score)`
- short ideas with strong negative scores can land inside the user-selected candidate count
- the runtime still passes explicit long/short direction into the bot
