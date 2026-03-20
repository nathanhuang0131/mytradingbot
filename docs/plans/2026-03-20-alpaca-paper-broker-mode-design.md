# Alpaca Paper Broker Mode Design

## Goal

Add a real `alpaca_paper_api` execution mode alongside the existing `local_paper` simulator without changing live-trading gates, robust-training gates, or the repo-local runtime/reporting architecture.

## Scope

The platform will support two explicit paper broker modes:

- `local_paper`
- `alpaca_paper_api`

`local_paper` remains the default and must continue working exactly as it does today.

`alpaca_paper_api` will:

- submit real Alpaca paper Trading API orders
- reconcile bot-owned Alpaca paper orders, fills, and positions into the repo-local SQLite runtime state
- keep all reports, diagnostics, ledgers, and analytics repo-local

## Ownership Policy

Ownership is locked to `bot_owned_only`.

Classification rules:

- `bot_owned`: deterministic `client_order_id` matches this repo’s pattern or persisted runtime lineage confirms ownership
- `foreign`: visible in Alpaca paper account state but not owned by this repo
- `unknown`: cannot be matched; treat as `foreign` by default

Behavior:

- only `bot_owned` orders and positions are actively managed
- `foreign` and `unknown` activity is read-only
- `foreign` and `unknown` positions count toward risk/exposure checks
- a same-symbol `foreign` or `unknown` position blocks a new bot entry by default
- profitability attribution excludes `foreign` and `unknown` trades by default

## Architecture

The broker boundary remains the execution seam.

- `src/mytradingbot/brokers/paper.py` continues to implement local simulation
- `src/mytradingbot/brokers/alpaca_paper.py` will implement the real Alpaca paper Trading API adapter
- orchestration selects the broker based on explicit `broker_mode`
- runtime SQLite remains the repo-local operational ledger and analytics source

In `alpaca_paper_api` mode, Alpaca is the source of truth for bot-owned execution state. SQLite stores reconciled state, lineage, incidents, reports, and analytics artifacts.

## Data Flow

### local_paper

1. strategy -> risk -> execution
2. local paper broker simulates fills and bracket lifecycle
3. runtime state persists repo-local order/fill/position truth
4. analytics derive realized PnL from repo-local stored fills

### alpaca_paper_api

1. startup preflight validates credentials, endpoint, and account query
2. startup reconciliation reads Alpaca paper account state
3. ownership classification separates `bot_owned` from `foreign`/`unknown`
4. `foreign` exposure is persisted and surfaced in reports/incidents
5. strategy -> risk -> execution remains unchanged at the intent level
6. execution submits real Alpaca paper bracket orders for valid long scalping entries
7. broker responses, later fills, and position state are reconciled back into SQLite
8. analytics derive realized PnL only from bot-owned reconciled fills by default

## Bracket Order Policy

In `alpaca_paper_api` mode:

- actionable long scalping entries submit real Alpaca bracket orders
- bracket ordering is validated locally before submission
- deterministic `client_order_id` is always attached
- request payload, broker response, and rejection details are persisted

Short bracket support remains opt-in by actual safe support. If the current path is not safe, unsupported short bracket routes must fail clearly before any API call.

## Fee And Cost Model

Add a broker-aware, versioned fee layer.

Required cost fields:

- `commission_fee`
- `sec_fee`
- `taf_fee`
- `cat_fee`
- `borrow_fee`
- `margin_interest`
- `allocated_data_cost`
- `gross_pnl`
- `net_pnl_after_fees`
- `net_pnl_after_fees_and_platform_cost`
- `fee_schedule_version`

Cost modes:

- `trading_fees_only`
- `fully_loaded_with_allocated_monthly_data_cost`

`local_paper` may use explicit zero/simulated fees.

`alpaca_paper_api` uses configured Alpaca paper-equity fee defaults and stamps the fee schedule version into analytics.

## Observability

Every relevant artifact must surface `broker_mode`.

This includes:

- startup banner
- decision audit
- signal outcome ledger
- incidents
- paper session reports
- analytics exports

For `alpaca_paper_api`, reports must also expose read-only foreign/unknown account exposure and ownership classification incidents.

## Safety

- no `alpaca_paper_api` session without successful preflight
- no auto-adoption of foreign/manual paper positions or orders
- no duplicate bot entry submission across restart when a bot-owned lineage or `client_order_id` already exists
- Alpaca wins over local SQLite when bot-owned state disagrees in `alpaca_paper_api` mode
- repo-local reset utilities never touch Alpaca account state

## Acceptance

- `local_paper` behavior unchanged
- `alpaca_paper_api` submits real Alpaca paper bracket orders
- only bot-owned orders and positions are actively managed
- foreign positions appear in reports and risk context
- same-symbol foreign exposure blocks new entry
- analytics exclude foreign trades from strategy profitability by default
- restart reconciliation restores bot-owned Alpaca state without duplicates
