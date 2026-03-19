# Release Notes - V2

## Summary

V2 upgrades the repository from a working paper-trading prototype to a more institutional-grade paper-trading platform with stronger runtime discipline, signal observability, reporting, and operational documentation.

## Highlights

- repo-local runtime path preserved and reinforced
- real qlib dataset / train / prediction refresh flow retained
- institutional pipeline runner introduced
- signal decision audit added
- session-level paper-trading reporting added
- standardized rejection reason taxonomy added
- stronger artifact-contract testing added
- improved logging and operational traceability
- documentation updated for operator use

## Key operational improvements

### 1. Full decision observability
Every candidate symbol can now be traced through:
- qlib score
- strategy side consideration
- filter outcomes
- risk sizing
- bracket logic
- final accept/reject/skip/no-action decision

### 2. Session-level explainability
Each paper-trading session now produces a summary showing:
- candidates evaluated
- accepted vs rejected decisions
- rejection counts by reason
- order submission totals
- artifact paths used and produced

### 3. Institutional runner
The runtime can now be executed through a single canonical orchestration path rather than relying on manual command sequencing.

### 4. Test coverage improvement
Artifact contracts and observability behaviors are now explicitly tested so refactors do not silently break reporting or runtime outputs.

## Verification expectation

V2 is considered healthy when the following pass in the `mytradingbot` environment:

```powershell
python -m pytest -q tests
python scripts\run_institutional_pipeline.py --strategy scalping --mode paper
python scripts\validate_system.py
python scripts\goalcheck.py