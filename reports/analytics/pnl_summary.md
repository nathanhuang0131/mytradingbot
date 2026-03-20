# Realized PnL Summary

- closed trades: `0`
- total realized pnl: `0.0000`
- total wins: `0`
- broker_modes_present: `local_paper`
- fee_schedule_version: `alpaca_public_schedule_2026-03-20`

- local_paper: `local simulated paper broker`
- local_paper note: local paper broker analytics come from repo-local SQLite/runtime state, not the Alpaca paper account UI.
- foreign exposure: `3` observed non-bot position snapshots are excluded from bot profitability attribution.
- foreign open orders: `64` read-only broker-account orders are excluded from bot trade attribution.
- profitability scope: by default, only bot-owned closed trades are included in strategy, signal-source, and broker-mode profitability tables.

- No closed trades have been materialized from persisted fills yet.
