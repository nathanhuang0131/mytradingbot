# Market Data Progress Design

## Goal

Add a live operator progress window to the Streamlit `Data Management` page's `Market Data` tab so the user can see market-data download and update actions progressing by timeframe and stage instead of only receiving a final JSON payload.

## Scope

This change only affects the `Download Market Data` and `Update Market Data` actions in the `Market Data` tab.

The progress view must show:
- whether a run is waiting, running, completed, or failed
- the current stage being executed
- per-timeframe status such as `1m in progress`, `5m completed`, `1d waiting`
- how many symbols were requested
- how many symbols were downloaded or updated for each timeframe
- which folders are receiving output
- which remaining steps are still pending

This change does not require live progress for the other tabs.

## Current Behavior

The page currently calls the market-data action synchronously and stores only the final `MarketDataPipelineResult` payload in Streamlit session state. The pipeline already produces useful post-run data in `raw_download_summary`, `artifacts`, and `report_paths`, but the page does not shape that into a readable operator workflow view and does not surface stage-by-stage progress while the run is active.

## Proposed Approach

Add a lightweight progress tracker around the market-data pipeline that writes repo-local progress state to a JSON file under the runtime directory. The Streamlit page will render a dedicated progress window for the active market-data run and refresh itself while the run is in progress.

### Backend responsibilities

- Introduce typed progress models for a market-data run, including:
  - overall run status
  - operation mode (`download` or `update`)
  - current step label
  - requested symbols count
  - requested timeframes
  - per-timeframe stage state
  - written raw/normalized folders
  - completed and remaining steps
- Add a small tracker service that:
  - initializes a run state file
  - updates per-timeframe and overall status as the pipeline advances
  - marks the run as completed or failed
- Extend the market-data pipeline with an optional progress callback that emits events at these points:
  - run started
  - timeframe started
  - timeframe raw download completed
  - timeframe normalization completed
  - snapshot started
  - snapshot completed
  - run completed / failed
- Expose the latest progress state through the UI service so the page can render a structured view.

### Frontend responsibilities

- Replace the single raw JSON-focused experience in the `Market Data` tab with a structured operator progress section.
- When the user starts `Download Market Data` or `Update Market Data`, initialize a progress record and run the action with progress tracking enabled.
- Show:
  - a run summary card
  - a per-timeframe progress table
  - a remaining/completed steps list
  - folder targets for raw, normalized, and snapshot outputs
  - the final result payload as a secondary expandable detail
- While a run is still marked as `running`, trigger page refresh so the view keeps updating.

## Data Model

Recommended progress model shape:

- `MarketDataProgressPayload`
  - `run_id`
  - `operation`
  - `status`
  - `message`
  - `current_step`
  - `requested_symbol_count`
  - `requested_symbols_preview`
  - `requested_timeframes`
  - `raw_output_root`
  - `normalized_output_root`
  - `snapshot_output_path`
  - `completed_steps`
  - `remaining_steps`
  - `timeframe_progress`
  - `started_at`
  - `updated_at`
  - `finished_at`

- `TimeframeProgress`
  - `timeframe`
  - `status`
  - `stage`
  - `symbols_requested`
  - `symbols_with_data`
  - `symbols_without_data`
  - `rows_downloaded`
  - `raw_folder`
  - `normalized_folder`
  - `resolved_start_at`
  - `resolved_end_at`

## Error Handling

- If the pipeline fails before any timeframe completes, the progress window should still show the run as `failed` and preserve the last known stage.
- If a timeframe is partial or empty, the row should show `partial` or `failed`-style status via the existing `RawDownloadTimeframeSummary.status`.
- If no valid universe file or manual symbols are present, the page behavior should remain unchanged and keep the buttons disabled.

## Testing

Add tests for:
- progress tracker initialization and status updates
- UI service shaping of progress payloads from market-data results
- Streamlit page structure for the new progress window
- pipeline callback integration at the major stage boundaries

## Success Criteria

- Starting a market-data action gives the operator an immediately visible run-status window.
- The window clearly shows timeframe-level states like waiting, in progress, and completed.
- The operator can see symbol counts and output folders without digging through raw JSON.
- Existing market-data behavior and result artifacts remain intact.
