# Institutional V2 Design

## Goal

Upgrade the current working repo into a restart-safe, observable, alpha-disciplined paper-trading system without breaking the already-working repo-local runtime path.

## Design Summary

The v2 upgrade keeps the existing service graph and extends it in-place around five new institutional concerns:

1. Truthful downloader behavior with explicit full-refresh windows, deterministic chunking, and raw coverage reports.
2. Repo-local universe generation based on Alpaca asset metadata and trailing average dollar volume.
3. Persistent runtime state and decision audit ledgers so sessions survive restarts and zero-trade runs still produce complete records.
4. Alpha-robust training quality gates so qlib training and prediction refresh only run on sufficiently deep, fresh, and complete data.
5. A supervised institutional orchestrator that ties maintenance, training, trading, reconciliation, validation, and reporting into one canonical command.

## Key Decisions

### Downloader

- `download` and `update` stay thin wrappers around the shared market-data pipeline.
- Full refreshes must always resolve concrete `start_at` and `end_at` windows before any provider call.
- Alpaca requests are chunked by symbols and, when necessary, by time window so no single request can silently truncate the universe.
- Download actions must produce raw coverage artifacts under `reports/data/` and fail loudly when no new usable raw data is acquired.
- Normalization is allowed only after a truthful raw acquisition step or via an explicit normalize-only path.

### Universe

- Add a repo-owned `universe` package for discovery, ranking, storage, and report generation.
- Use Alpaca assets plus trailing daily bars to rank liquid common equities by average dollar volume.
- Exclude ETFs by default and document the exact filter policy in code and docs.
- Downstream scripts accept `--symbols-file` so universe artifacts flow directly into maintenance, training, and paper trading.

### Runtime State and Observability

- Add a repo-local SQLite-backed runtime store under `data/runtime/`.
- Persist sessions, orders, fills, positions, brackets, cooldowns, incidents, and artifact references.
- Generate typed decision-audit, session, execution, incident, and ledger records under `reports/` and `data/ledger/`.
- Zero-trade sessions are considered successful only when the audit trail is complete and rejection reasons are explicit.

### Training

- Keep qlib as the only predictive authority.
- Add a dedicated training quality layer with per-timeframe coverage, freshness, and sufficiency checks.
- Build a training-eligible universe by intersecting the liquid universe with the symbols that pass data sufficiency gates.
- Keep the staged modeling architecture simple and explicit: scalping uses a 5-minute primary training frame with higher/lower timeframe context reported and validated, while the existing runtime signal contract remains intact.

### Safety

- Add freshness gates for predictions, market snapshots, dataset metadata, and model metadata.
- Persist circuit-breaker state and cooldowns.
- Replace the naive subprocess loop with a supervised, state-aware institutional pipeline.

## Expected Outputs

- `reports/data/` for raw download summaries and coverage reports
- `data/universe/` and `reports/universe/` for top-liquidity universe artifacts
- `reports/training/` and `reports/pipeline/` for training quality and institutional run summaries
- `data/runtime/` and `data/ledger/` for persistent state and analytics-ready ledgers

## Non-Goals

- No live order submission in this patch.
- No LLM involvement in signal generation.
- No hidden fallback to stale data, stale predictions, or prior normalized artifacts when downloader truth checks fail.
