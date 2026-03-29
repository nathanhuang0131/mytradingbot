# Qlib Trading Universe And Wizard Thresholds Design

## Goal

Extend the standalone Trading Universe page so operators can inspect the full qlib prediction artifact in table form, see which rows belong to the implemented scalping final trading universe, and view the indicated TP and SL percentages derived from the current scalping logic.

Also extend the Setup Wizard so operators can edit and save the scalping `predicted_return_threshold` and `confidence_threshold` per profile for future runs, without changing any other scalping logic.

## Locked Product Decisions

- The Trading Universe page must show all qlib prediction rows from the current prediction artifact.
- The page must support a toggle between:
  - `Raw qlib prediction artifacts`
  - `Final qlib trading universe`
- The qlib table must use the same resolved final trading universe already implemented for scalping as the source of truth for inclusion.
- The qlib table must include these raw prediction fields:
  - `symbol`
  - `score`
  - `predicted_return`
  - `confidence`
  - `rank`
  - `direction`
  - `generated_at`
  - `horizon`
- The qlib table must also include these derived columns:
  - `is_final_symbol`
  - `indicated_tp_pct`
  - `indicated_sl_pct`
- The Setup Wizard, not the Trading Universe page, is the place where operators edit `predicted_return_threshold` and `confidence_threshold`.
- Changing those two thresholds must leave all other scalping logic unchanged.

## Current Runtime Truth

The current scalping strategy hard-codes:

- `predicted_return_threshold = 0.005`
- `confidence_threshold = 0.6`

These are the current qlib gating thresholds for scalping.

The current TP and SL indications are derived from the existing `_target_deltas()` logic in `src/mytradingbot/strategies/scalping.py`. This design does not change that logic. The page will only surface its current outputs.

## Architecture

The implementation will remain additive and thin at the UI layer.

Core parts:

- `app/pages/09_Trading_Universe.py`: add the qlib prediction toggle and enriched table
- `src/mytradingbot/ui_services/trading_universe.py`: load qlib predictions, enrich rows, and expose raw/final views
- `src/mytradingbot/session_setup/models.py`: add wizard-facing scalping threshold fields
- `src/mytradingbot/session_setup/runtime.py`: apply saved threshold values into runtime settings
- `src/mytradingbot/strategies/scalping.py`: read thresholds from settings instead of fixed class constants
- `src/mytradingbot/core/settings.py`: add repo-default scalping threshold settings so the strategy can consume runtime-configured values cleanly

## Trading Universe Data Flow

For the selected profile, the Trading Universe page will:

1. Resolve the implemented final trading universe using the same existing page/service logic already used by scalping.
2. Load the current qlib prediction artifact through the existing runtime prediction loader path.
3. For each prediction row:
   - preserve the raw qlib attributes
   - mark whether the symbol is in the resolved final trading universe
   - compute `indicated_tp_pct` and `indicated_sl_pct` using the current scalping target-delta logic
4. Present:
   - `Raw qlib prediction artifacts`: all prediction rows
   - `Final qlib trading universe`: only rows where `is_final_symbol = true`

This keeps the prediction table aligned with the same final-universe implementation used by the trading workflow.

## Wizard Data Flow

The Setup Wizard will gain two scalar controls in the `Alpha & Model` step:

- `Predicted return threshold`
- `Confidence threshold`

These values will:

1. be editable in the wizard UI
2. persist into the profile-scoped resolved session config
3. apply to runtime settings during session launch
4. be consumed by the scalping strategy at evaluation time

The values are stored in the same numeric shape already used by the strategy:

- predicted return threshold as decimal return, for example `0.005`
- confidence threshold as a `0.0` to `1.0` score

## UI Layout

### Trading Universe page

Add a new qlib section below the current universe preview/save controls with:

- a view toggle:
  - `Raw qlib prediction artifacts`
  - `Final qlib trading universe`
- a dataframe containing:
  - raw qlib fields
  - `is_final_symbol`
  - `indicated_tp_pct`
  - `indicated_sl_pct`

### Setup Wizard page

In the `Alpha & Model` step, add two controls in the standard editable section:

- predicted return threshold
- confidence threshold

These should be visible in normal workflow, not hidden behind unrelated expert-only settings, because they are the intended operator knobs for qlib gating.

## Persistence Rules

- Trading Universe page inspection remains read-only with respect to prediction artifacts.
- Trading Universe page save behavior remains limited to the active-universe manifest and latest session config alignment.
- Wizard threshold edits must persist into the profile-scoped latest session config.
- No raw parquet, normalized parquet, qlib dataset, model artifact, or prediction artifact is modified by this feature.

## Verification

Tests should cover:

- wizard persistence of `predicted_return_threshold` and `confidence_threshold`
- runtime application of those values to scalping
- qlib prediction table payload generation
- raw-view versus final-view filtering
- correctness of `is_final_symbol`
- correctness of indicated TP/SL percentages using existing scalping logic
- Streamlit smoke coverage for the updated pages
