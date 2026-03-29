# Streamlit Status Reference Cleanup Design

## Goal

Replace raw JSON-style UI dumps with readable, descriptive status sections, remove the dedicated Paper Trading page, rename Settings to Status Reference, and add a Trading Track view that surfaces recent session and trade activity.

## Scope

- Change the landing page title from `Dashboard` to `Dashboard Summary`.
- Replace raw dictionary and JSON blocks in the setup wizard review flow with readable status sections.
- Rename the `Settings` page to `Status Reference`.
- Build a profile-aware `Status Reference` page that defaults to the current wizard-selected profile when available and otherwise falls back to the most recently used saved profile.
- Add a `Trading Track` section that shows current in-memory session activity when available and latest persisted paper-session activity otherwise.
- Remove the Streamlit `Paper Trading` page from the sidebar navigation.

## Recommended Approach

Use a shared descriptive-section model in `ui_services` so the same field metadata can drive:

- setup wizard review output
- status reference output
- dashboard summary status sections

This keeps the UI consistent and avoids maintaining duplicated hand-written descriptions across page files.

## Architecture

### Shared descriptive status model

Add a small shared presentation model for:

- section title
- section description
- item label
- item value
- item explanation
- item effect
- optional state badge such as `Recommended default`, `Customized`, or `Status`

The shared model will be produced by `ui_services` and rendered by thin Streamlit pages.

### Setup Wizard cleanup

The setup wizard review step currently mixes readable summaries with raw dictionaries and JSON output. Replace these with descriptive sections for:

- profile and strategy summary
- universe and refresh policy
- risk controls
- execution settings
- recommended defaults retained
- customized values

The defaults/customized view should stop showing raw dotted-key lists and instead show friendly labels with plain-language explanations.

### Status Reference page

Replace the raw settings dump page with a profile-aware status page that shows:

- selected profile and saved artifact paths
- strategy/session settings
- universe settings
- refresh policy
- alpha/model gates
- risk controls
- execution settings
- artifact readiness and freshness

Each field should explain what it controls and what part of the workflow it affects.

### Trading Track

Add a `Trading Track` section to the new status page with two layers:

- current app session summary from `platform_service.last_session_result` when present
- latest saved paper-session report plus recent signal/trade ledger activity from repo-local artifacts

This gives the operator a quick answer to whether anything traded recently without needing the removed paper page.

## Data Sources

- Current wizard-selected profile from Streamlit session state
- Saved profiles and latest configs from `SetupWizardStorage`
- Current in-memory session from `TradingPlatformService.last_session_result`
- Latest paper session report from `reports/paper_trading/*_paper_session.json`
- Recent decision/trade rows from `data/ledger/signal_outcomes.csv`

## Error Handling

- If no saved profiles exist, Status Reference should explain that the wizard must be run first.
- If no latest paper-session report exists, Trading Track should show a clear empty-state message.
- If ledger files are missing, Trading Track should still render the session summary without failing the page.

## Testing Strategy

- Add UI service tests for the new Status Reference payload and Trading Track behavior.
- Extend dashboard/setup wizard UI service tests to verify descriptive sections replace raw status blobs.
- Run targeted UI service tests first, then the full suite.

## Notes

- The Paper Trading backend service can remain in the repo for now; only the Streamlit page is removed.
- A git commit is intentionally not part of this change set because the worktree already contains unrelated modifications.
