# Data Management Profile Universe Design

## Goal

Make the Streamlit `Data Management` page default to the selected profile's active-universe manifest instead of the fallback 3-symbol development set, while still allowing the operator to override the universe file path.

## Recommended Approach

Use the profile-scoped active universe file under `data/runtime/active_universes/<profile>_active_symbols.json` as the default source for file-scoped maintenance actions. Expose that path directly in the page as an editable text input, and show a hint for the alternate repo-standard file `data/universe/latest_top_liquidity_universe.json`.

## Scope

- Add profile awareness to the `DataTrainingService` payload.
- Add a service helper that resolves the selected profile's default active-universe file, validates the chosen path, and loads a symbol preview.
- Update file-scoped maintenance actions to accept `symbols_file` and prefer it when no manual symbol override is supplied.
- Update the `Data Management` page to:
  - select a profile
  - prefill the universe file path from that profile
  - show path hints and loaded symbol preview
  - route market-data, dataset, quality-check, and alpha-robust training actions through the selected file by default

## Non-Goals

- No change to the underlying training or scalping logic.
- No change to `Train Models` and `Refresh Predictions`, which operate on existing artifacts rather than a direct symbol file input.
- No persistence of custom universe file overrides beyond normal Streamlit widget state.

## Testing

- Unit-test the service-level profile universe resolution and file-scoped action routing.
- Extend Streamlit smoke coverage to assert the page exposes the universe file input and profile hinting.
