# Setup Wizard Design

## Goal

Add a dedicated Streamlit setup wizard page that lets an operator create or load a named profile, choose strategy/session/universe behavior, review a resolved session configuration, and launch or save that configuration without replacing the existing dashboard or CLI workflows.

## Locked Product Decisions

- The wizard lives at `app/pages/00_Setup_Wizard.py`.
- The current landing page and dashboard remain unchanged.
- The wizard is additive and discoverable, not mandatory.
- Historical downloaded market data is never deleted when active symbol choices change.
- User and session configuration is auto-saved under repo-local paths.
- Basic mode must be sufficient for a normal operator to complete setup.

## Architecture

The wizard will use a new typed configuration layer under `src/mytradingbot/session_setup/` plus a thin UI service under `src/mytradingbot/ui_services/setup_wizard.py`.

Core parts:

- `session_setup.models`: typed profile, preset, universe, refresh, alpha, risk, execution, and resolved session config models
- `session_setup.storage`: repo-local persistence for profiles, active symbol manifests, and latest resolved session configs
- `session_setup.service`: preset application, profile loading, wizard-state resolution, universe combine/replace logic, and launch preparation
- `ui_services.setup_wizard`: page payloads and start/save actions for Streamlit

The runtime will gain an additive `session_config` integration path so the wizard can launch a real single run or loop-backed session without changing existing CLI defaults.

## Persistence Layout

Wizard persistence will use repo-local paths:

- `configs/user_profiles/<profile>.json`
- `data/runtime/session_profiles/<profile>_latest.json`
- `data/runtime/active_universes/<profile>_active_symbols.json`

The active universe manifest is profile-scoped and separate from the historical raw/normalized data already on disk.

## Universe Behavior

The wizard will support three explicit modes:

- `keep_old`: keep the current active symbol manifest for the profile
- `combine_old_and_new`: generate a new liquidity universe, merge it with the current active manifest, dedupe, and persist the merged active set
- `replace_with_new`: generate a new liquidity universe and replace only the active manifest

None of these modes delete existing downloaded parquet data.

## Runtime Integration

The resolved session config will drive:

- strategy
- broker mode
- session mode (`single_run`, `bounded_smoke`, `loop`)
- symbol scope via a generated active-symbols file
- auto-refresh flags and cadences
- side mode (`long_only`, `short_only`, `both`)

The start action will:

- auto-save the profile
- auto-save the latest resolved session config
- materialize the profile-scoped active universe manifest
- run a one-shot session directly or launch the loop path using the resolved config

Advanced and expert values that are not yet fully enforced by the current runtime will still be typed and persisted so they can feed later dashboard/runtime upgrades without schema churn.

## UI Layout

The wizard page will implement an 8-step flow:

1. User Profile
2. Strategy and Session Mode
3. Symbol Universe
4. Refresh and Data Policy
5. Alpha and Model
6. Risk Controls
7. Execution and Brackets
8. Review and Start

The page will use:

- a progress header
- Previous and Next navigation
- `Basic`, `Advanced`, and `Expert` visibility modes
- consistent recommended-default hints/badges
- summary cards on the review step

## Verification

Tests will cover:

- new profile creation
- existing profile load
- auto-save of resolved session configs
- preset application
- universe keep/combine/replace behavior
- no deletion of historical downloaded data
- resolved config generation
- broker mode and side mode persistence
- wizard UI service metadata for recommended defaults
