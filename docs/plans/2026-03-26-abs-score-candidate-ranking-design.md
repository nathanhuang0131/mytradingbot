# Absolute Score Candidate Ranking Design

## Goal

Update qlib prediction ranking so scalping candidate selection can surface the strongest predicted moves on either side of the book instead of only the strongest positive scores.

The system must keep the signed raw `score` and signed `predicted_return`, preserve explicit long/short direction, and rank the prediction artifact by `abs(score)` so the operator-selected `candidate_count` can include strong short ideas as well as strong long ideas.

## Locked Product Decisions

- Keep `score` signed.
- Keep `predicted_return` signed.
- Keep `direction = long` when score is positive or zero.
- Keep `direction = short` when score is negative.
- Re-rank the prediction artifact by `abs(score)` descending.
- Recompute `confidence` from `abs(score)` ranking so higher-magnitude predictions have higher confidence regardless of sign.
- Keep the existing runtime flow where candidate selection slices the ordered prediction artifact after session-config filters.
- Do not flatten short predictions into positive returns.

## Current Problem

The current prediction artifact sorts rows by raw `score` descending and assigns rank in that order. That means:

- strong positive predictions appear first
- strong negative predictions appear last
- `candidate_count` effectively prefers longs

At the same time, the current `confidence` calculation is based on a percentile rank that does not align with the artifact ordering for practical scalping use, which makes the top rows look weak while deep negative rows look artificially confident.

## Desired Runtime Meaning

For scalping:

- positive score means the model expects positive forward return, which is favorable for a long trade
- negative score means the model expects negative forward return, which is unfavorable for a long trade but favorable for a short trade
- larger absolute magnitude means stronger directional conviction, independent of side

The artifact should therefore present:

- signed score for reporting and audit
- signed predicted return for thresholding and trade intent
- explicit direction for long/short routing
- rank based on absolute score magnitude
- confidence based on absolute score magnitude

## Architecture

The change is centered in the qlib prediction artifact builder and covered with targeted runtime tests.

Primary touchpoints:

- `src/mytradingbot/qlib_engine/adapter.py`: generate prediction artifact ordered by absolute score magnitude and confidence by absolute score percentile
- `src/mytradingbot/session_setup/runtime.py`: keep `candidate_count` slicing behavior but rely on the newly ordered artifact
- `tests/unit/orchestration/test_orchestration_service.py`: verify session config candidate selection can include short-side predictions when their absolute score is strongest
- `tests/unit/qlib_engine` or nearby ranking-facing tests: verify artifact rank, confidence, and direction semantics

No broker, strategy, or execution code needs semantic changes because the existing runtime already passes `direction` through to the strategy and bot.

## Data Flow

1. The trained qlib model emits a signed regression output.
2. The adapter stores that raw output as signed `score`.
3. The adapter stores the same signed value as signed `predicted_return`.
4. The adapter derives `direction` from the sign:
   - positive or zero -> `long`
   - negative -> `short`
5. The adapter ranks rows by `abs(score)` descending.
6. The adapter derives `confidence` from `abs(score)` percentile rank.
7. Runtime session filtering keeps applying:
   - side mode
   - long threshold
   - short threshold
   - `candidate_count`
8. The bot receives the selected signal with explicit `direction`, so the downstream trade remains long or short.

## Error Handling And Compatibility

- Existing signed `predicted_return` threshold logic remains valid.
- Existing long/short direction logic remains valid.
- Existing audit reporting remains meaningful because signed values are preserved.
- Any UI or report that shows `rank` will now be interpreting rank as absolute conviction, not only positive-score ordering.

## Verification

Tests should cover:

- prediction artifact rows are ordered by `abs(score)` descending
- `rank` follows that absolute-score ordering
- `confidence` increases with absolute-score strength rather than raw signed score ordering
- negative scores remain negative in both `score` and `predicted_return`
- negative scores are still labeled `direction = short`
- session-config `candidate_count` can now select strong short signals ahead of weaker long signals
