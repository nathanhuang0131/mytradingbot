# Trading Universe Page Design

## Goal

Add a standalone Streamlit sidebar page that lets an operator inspect the final trading universe before running scalping, compare it against the previous active universe, choose how to merge old and new symbols, add manual symbols that persist into future runs, and save the resolved active universe manifest for the selected profile.

Also add a repo-root `standard operation.md` runbook that documents the current command and UI entry points, including standard liquidity, data, qlib, prediction, paper-trading, validation, one-off, and Streamlit workflows.

## Locked Product Decisions

- The feature lives as a standalone Streamlit sidebar page, not only inside the setup wizard.
- The page reuses the existing profile-scoped storage under `configs/user_profiles/`, `data/runtime/session_profiles/`, and `data/runtime/active_universes/`.
- Manual symbol additions are part of the final active universe manifest and persist into future runs.
- The page must show total final symbols, removed symbols versus the prior universe, and added symbols versus the prior universe.
- The operator can choose exactly one universe mode:
  - `keep_old`
  - `combine_old_and_new`
  - `only_new`
- Historical downloaded market data is never deleted by this page.
- The new runbook must describe current code paths only. No invented commands or hidden flows.

## Architecture

The page will remain thin and delegate all logic to service and model layers.

Core parts:

- `app/pages/09_Trading_Universe.py`: standalone Streamlit page
- `src/mytradingbot/ui_services/trading_universe.py`: UI-facing payloads and save/preview actions
- `src/mytradingbot/session_setup/service.py`: reusable final-universe resolution helpers shared with the wizard
- `src/mytradingbot/session_setup/models.py`: typed payloads for universe preview, diffs, manual additions, and save results
- `src/mytradingbot/session_setup/storage.py`: active-manifest and latest-session-config persistence updates

The setup wizard remains intact, but the new page will use the same underlying active-universe rules so there is still one authority for profile-scoped tradable symbols.

## Data Flow

For the selected profile, the page will:

1. Load the previous active universe manifest from `data/runtime/active_universes/<profile>_active_symbols.json`.
2. Load the latest resolved session config if it exists so the page can inherit prior universe filters and keep the latest session metadata aligned.
3. Generate or reuse a new top-liquidity candidate universe using the same repo-local liquidity flow already used by the wizard.
4. Apply the selected mode:
   - `keep_old`: use only the previous manifest, plus manual additions
   - `combine_old_and_new`: merge previous symbols, generated new symbols, and manual additions, then dedupe
   - `only_new`: use generated new symbols plus manual additions
5. Compute:
   - final symbol count
   - removed symbols versus the previous manifest
   - added symbols versus the previous manifest
   - manual additions included in the final set
6. Persist the final manifest back to the profile-scoped active-universe file.
7. Update the latest session config for that profile when present so `active_symbols_path`, active symbol count, and universe-selection metadata stay aligned with the saved manifest.

## UI Layout

The standalone page should present:

- profile selector
- current strategy context, with scalping called out clearly
- universe-mode selector: `keep_old`, `combine_old_and_new`, `only_new`
- editable filters for generating the new liquidity universe when the selected mode needs one
- manual symbol additions textarea with uppercase normalization and dedupe
- preview/save actions
- metric cards for:
  - final symbol count
  - removed count
  - added count
  - manual additions count
- clear list/table sections for:
  - previous universe
  - generated new universe
  - removed symbols
  - added symbols
  - final saved universe

The page should explain that removed/added counts are always computed versus the prior saved active universe for the selected profile.

## Persistence Rules

- Saving never writes outside the repo root.
- Saving updates only the profile-scoped active-universe manifest and, when present, the latest saved session config for that same profile.
- Manual additions are stored inside the final manifest rather than as a separate monitor-only list.
- The page does not modify raw parquet, normalized parquet, qlib datasets, model artifacts, predictions, or broker state.

## Runbook Scope

Create `standard operation.md` in the repo root as an operator-facing command/reference runbook.

It will cover:

- environment and baseline verification commands
- Streamlit launch commands and the current dashboard pages
- top-liquidity update/generation commands
- raw data download and update commands
- quality-check commands
- qlib dataset build commands
- training commands
- prediction refresh commands
- scalping paper loop commands
- one-off maintenance, smoke, reset, validation, and broker-check commands
- the currently existing UI and Streamlit entry points

Each command section should include:

- what the command does
- when to use it
- the canonical syntax
- supported options and what each option means
- notes about important file outputs or operational expectations when that is already represented in current code

## Verification

Tests should cover:

- final-universe diff math for keep/combine/only-new
- manual additions being normalized, deduped, and persisted
- session-config alignment after saving a new final manifest
- UI-service payload generation for the new page
- Streamlit smoke coverage for the new sidebar page
- runbook file creation as part of repo documentation updates
