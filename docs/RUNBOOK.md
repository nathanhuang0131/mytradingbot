# Runbook

## Daily Maintenance Order

1. `python scripts/generate_top_liquidity_universe.py --top-n 800 --lookback-days 30 --min-price 5 --min-avg-volume 500000`
2. `python scripts/run_daily_maintenance.py --action update --symbols-file data/universe/latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d`
3. `python scripts/check_training_data_quality.py --strategy scalping --symbols-file data/universe/latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d`
4. `python scripts/build_qlib_dataset.py --strategy scalping --symbols-file data/universe/latest_top_liquidity_universe.json`
5. `python scripts/train_models.py --strategy scalping`
6. `python scripts/refresh_predictions.py --strategy scalping`
7. `python scripts/run_paper_trading.py --strategy scalping --mode dry_run`
8. `python scripts/run_paper_trading.py --strategy scalping --mode paper`
9. `streamlit run app/app.py`

## Guided Setup Wizard

The recommended operator setup flow is the dedicated Streamlit wizard page:

- `app/pages/00_Setup_Wizard.py`
- `app/pages/09_Trading_Universe.py`

Launch the app:

`streamlit run app/app.py`

Then open `Setup Wizard` from the sidebar or use `Start New Trading Session (Wizard)` from the landing page or dashboard.

The wizard coexists with the current dashboard and CLI workflows. It does not replace them.

For the command-by-command reference covering standard scalping operations, one-off scripts, and current Streamlit entry points, see:

- `standard operation.md`

### Auto-saved profile and session files

The wizard automatically writes:

- `configs/user_profiles/<profile>.json`
- `data/runtime/session_profiles/<profile>_latest.json`
- `data/runtime/active_universes/<profile>_active_symbols.json`

You do not need a separate manual save action to persist these files.

### Symbol behavior modes

The wizard supports:

- `keep using old symbols`
- `run liquidity flow and combine new symbols with old symbols`
- `use completely new symbols`

These modes update the profile-scoped active universe manifest only. They do **not** delete any historical market data already downloaded under `data/raw/` or `data/normalized/`.

The standalone `Trading Universe` page lets you preview the final manifest, see added and removed symbols versus the last saved universe, add extra symbols that persist for future runs, and save the final active set before starting scalping.

The same page also exposes the qlib prediction artifact with a toggle between raw rows and the final qlib trading universe, plus `is_final_symbol`, `indicated_tp_pct`, and `indicated_sl_pct` columns derived from the current scalping logic.

Interpret qlib prediction rows as follows:

- `score` is signed model output
- `predicted_return` keeps the same sign as the score
- negative score plus `direction=short` means the model expects downside and the idea is favorable for a short, not a long
- `rank` is ordered by `abs(score)` so the strongest short can outrank a weaker long
- `confidence` follows `abs(score)` strength, not raw positive-score ordering

### Recommended defaults

Fields marked `Recommended default` are the safe operator defaults. Basic mode is sufficient for a standard paper setup. Advanced and expert sections expose additional tuning without forcing every operator to understand the full backend dependency chain.

Use the `Alpha & Model` step to adjust the qlib entry gates for scalping:

- `Predicted return threshold (%)` default: `0.08%`
- `Confidence threshold` default: `0.60`
- `Top-N approvals per cycle` default: `3`
- `Minimum edge after cost (%)` default: `0.05%`
- `Prediction refresh cadence` default: `600 seconds`
- `Cooldown after exit` default: `10 minutes`

The overnight scalping profile keeps the spread proxy at `6.0` bps, applies a `15m` higher-timeframe trend filter using `EMA(5)` and `EMA(10)`, and keeps the pseudo order-book gate disabled by default.

Smarter selection is preferred over simply chasing more trades. The runtime now ranks only hard-filter-eligible names and keeps the best few per cycle by combining predicted return, confidence, edge after cost, spread quality, liquidity quality, higher-timeframe alignment, a lightweight microstructure proxy, and bracket reward/risk. In the equities path, this is based on bars and quote-level spread proxies, not a fabricated stock L2 book.

`edge after cost` is the directional predicted return minus estimated spread, slippage, configured per-share fees, and the lightweight equities regulatory fee hook. It is a throughput and selection discipline control, not a profitability guarantee.

The microstructure proxy is an optional confirmation tool for equities, not a true order book. It uses already-loaded bar context such as candle pressure, relative volume, range expansion, VWAP bias, wick structure, and short persistence. The recommended overnight setting is `soft_rank`, which lets the proxy improve ranking without adding a disruptive hard gate to the existing loop.

## Canonical Institutional Order

`python scripts/run_institutional_pipeline.py --strategy scalping --use-top-liquidity-universe --timeframes 1m 5m 15m 1d --mode paper`

## Overnight Paper Trading

Use the canonical overnight runner with an explicit symbol scope so the loop can keep market snapshot and prediction inputs fresh by itself:

`python scripts/run_paper_trading.py --strategy scalping --mode paper --broker-mode local_paper --symbols-file data/universe/latest_top_liquidity_universe.json --loop --interval-seconds 300 --verbose`

Canonical Alpaca paper overnight run:

`python scripts/run_paper_trading.py --strategy scalping --mode paper --broker-mode alpaca_paper_api --symbols-file data/universe/latest_top_liquidity_universe.json --loop --interval-seconds 300 --verbose`

Optional bounded overnight run:

`python scripts/run_paper_trading.py --strategy scalping --mode paper --broker-mode alpaca_paper_api --symbols-file data/universe/latest_top_liquidity_universe.json --loop --interval-seconds 300 --max-cycles 12 --verbose`

Operational notes:

- the loop writes a rolling log to `logs/paper_trading_loop.log`
- each cycle rehydrates state from `data/state/institutional_runtime.sqlite3`
- open positions and active brackets are reconciled at cycle startup
- each cycle refreshes the market snapshot when due, refreshes predictions when due, and only rebuilds the dataset incrementally when needed for inference freshness
- per-cycle failures are logged and persisted, then the loop continues to the next cycle
- closed-trade analytics are refreshed after every cycle
- pass `--disable-auto-refresh` only for debugging, because the loop will then block explicitly instead of trading on stale inputs

Deterministic bounded smoke commands:

`python -m pytest -q tests/integration/test_paper_session.py -k traceability`

`python -m pytest -q tests/integration/test_paper_session.py -k short`

Real Alpaca paper submission smoke commands:

`python scripts/run_alpaca_paper_submission_smoke.py --symbol AMZN --side long --verbose`

`python scripts/run_alpaca_paper_submission_smoke.py --symbol TSLA --side short --verbose`

Each smoke is one-shot and bounded: one synthetic candidate, at most one Alpaca paper bracket order, one session report, one decision audit, and immediate cancel-after-submit unless `--leave-open` is passed.

## Morning Analysis Workflow

Inspect these in order:

1. `logs/paper_trading_loop.log`
2. `reports/paper_trading/`
3. `reports/signals/`
4. `reports/analytics/closed_trades.csv`
5. `reports/analytics/pnl_attribution.csv`
6. `reports/analytics/pnl_summary.md`

The analytics exports are realized-only. They are built from persisted entry and exit fills already stored in SQLite, not from hypothetical marks.

## Local Paper Broker Vs Alpaca Paper Account

The overnight paper loop supports both `local_paper` and `alpaca_paper_api`. `local_paper` remains the default.

In `local_paper` mode:

- fills, positions, brackets, cooldowns, incidents, and closed-trade analytics come from `data/state/institutional_runtime.sqlite3`
- `reports/paper_trading/`, `reports/signals/`, `reports/analytics/`, and `data/ledger/` reflect repo-local simulated paper broker activity
- the Alpaca paper account UI will not show matching orders because `external_broker_submission_enabled=false`

Use the startup banner in `logs/paper_trading_loop.log` to confirm:

- `broker_mode=local_paper`
- `runtime_state_db=<repo-local sqlite path>`
- `external_broker_submission_enabled=false`

To probe the real Alpaca paper Trading API path without running a full session:

`python scripts/check_alpaca_paper_broker.py --list-orders`

To route a real bounded paper submission smoke to Alpaca's paper account:

`python scripts/run_alpaca_paper_submission_smoke.py --symbol AMZN --side long --verbose`

`python scripts/run_alpaca_paper_submission_smoke.py --symbol TSLA --side short --verbose`

In `alpaca_paper_api` mode:

- bot-owned Alpaca paper orders and positions are actively managed
- foreign or unknown Alpaca paper orders and positions are read-only by default
- foreign or unknown same-symbol exposure blocks new bot entries
- repo-local analytics continue to live under `reports/analytics/`, but strategy profitability excludes foreign activity by default
- the Alpaca paper dashboard will show the submitted orders because `external_broker_submission_enabled=true`
- the same supervised loop keeps runtime inputs fresh on cadence, so healthy broker connectivity no longer masks stale decision artifacts

If you need a clean repo-local paper slate before the next overnight run:

`python scripts/reset_local_paper_state.py --yes`

That command archives only repo-local local paper state and local paper analytics artifacts. It does not modify market data, qlib artifacts, universe files, or any Alpaca account state.

## Raw Download Coverage Reports

Inspect:

- `reports/data/raw_download_summary.json`
- `reports/data/raw_download_summary.md`
- `reports/data/raw_symbol_coverage.csv`

## Daily UI Order

1. Launch `app/app.py` with Streamlit and start from the Dashboard landing page.
2. Check the phase capability snapshot and prediction freshness.
3. Use `app/pages/03_Data_Management.py` for phase-2 and phase-3 actions.
4. Use `app/pages/09_Trading_Universe.py` to review and save the final active universe for the selected profile.
5. Use `app/pages/00_Setup_Wizard.py` to save the selected profile and launch sessions.
6. Use `app/pages/08_Status_Reference.py` to review the saved profile state, artifact readiness, and recent Trading Track activity.
7. Use `app/pages/07_Diagnostics.py` and `app/pages/06_LLM_Copilot.py` for review.

## If Phase 2 Fails

Check:

- `alpaca-py` is installed through `pip install -e .[dev,broker]` or `pip install alpaca-py`
- `ALPACA_API_KEY` or `BROKER__ALPACA_API_KEY` is set
- `ALPACA_SECRET_KEY` or `BROKER__ALPACA_SECRET_KEY` is set
- `data/raw/alpaca/bars/` and `data/normalized/bars/` are writable under the repo root

## If Phase 3 Fails

Check:

- `pyqlib` is installed through `pip install -e .[dev,qlib]` or `pip install pyqlib`
- `data/normalized/bars/` contains parquet for the requested strategy timeframe
- `data/qlib/dataset.parquet` exists before training
- `models/qlib/model.pkl` exists before prediction refresh
- `reports/training/training_data_quality_report.md` passes the timeframe sufficiency rules
- `data/universe/latest_training_eligible_universe.json` contains enough symbols for the configured floor

## If No Trades Happen

Check:

- `models/predictions/latest.json` freshness
- `data/snapshots/market_snapshot.json` freshness
- qlib return and confidence thresholds
- microstructure proxy mode and alignment diagnostics in `reports/signals/` and `reports/analytics/`
- scalping fee-adjusted bracket expectancy
- whole-share execution rounding effects
- cooldown and flatten-near-close logic
- risk rejection reasons

## Live Trading Status

- `scripts/run_live_trading.py` is validation-only
- `src/mytradingbot/risk/service.py` still blocks live approval
- `src/mytradingbot/brokers/alpaca.py` still reports live submission disabled

---

## docs/RUNBOOK.md

```md
## Decision Audit / Rejection Reason Investigation

This runbook section explains how to investigate why a paper-trading session placed trades, rejected trades, or produced no trades.

### Where to look

Primary audit/report locations:

- `reports/signals/`
- `reports/paper_trading/`
- `reports/analytics/`
- `data/ledger/`

Expected outputs per run:

- timestamped JSON decision-audit artifact
- timestamped CSV decision-audit artifact
- session summary artifact
- optional human-readable summary text/markdown

### What the decision audit contains

For each symbol considered by the strategy, inspect:

- timestamp
- strategy
- symbol
- side considered
- whether bracket logic was evaluated
- raw qlib score
- confidence
- predicted return / target return
- spread proxy
- liquidity score
- VWAP relationship result
- bracket expectancy result
- rejection reasons list
- filter outcomes
- risk sizing result
- bracket calculation result
- final decision status
- rejection reason code
- rejection detail

### Standard decision outcomes

Expected final decision statuses include:

- `accepted_buy`
- `accepted_bracket_buy`
- `accepted_short`
- `accepted_bracket_short`
- `rejected`
- `skipped`
- `no_action`

### Standard rejection taxonomy

Common rejection reason codes include:

- `signal_direction_conflict`
- `score_below_threshold`
- `target_return_below_threshold`
- `vwap_relationship_blocked`
- `spread_too_wide`
- `liquidity_too_low`
- `liquidity_stress_too_high`
- `volatility_regime_blocked`
- `imbalance_not_confirmed`
- `liquidity_sweep_not_confirmed`
- `risk_budget_exceeded`
- `position_exists`
- `cooldown_active`
- `near_close_window_blocked`
- `bracket_invalid`
- `broker_rejected`
- `missing_market_data`
- `invalid_signal_payload`
- `execution_guard_blocked`
- `stale_predictions`
- `stale_market_snapshot`
- `strategy_exception`
- `broker_state_unreconciled`

### How to investigate a no-trade paper session

When a run places zero trades:

1. confirm the pipeline itself completed successfully
2. confirm the model and prediction artifacts were refreshed
3. open the latest paper-trading session summary
4. inspect rejection counts by reason
5. inspect the detailed signal audit for each candidate
6. inspect the per-session analytics markdown/CSV for trend blockers, top-ranked symbols, and edge-after-cost distribution
6. determine whether the issue is:
   - normal selectivity
   - insufficient candidate quality
   - overly restrictive filters
   - stale or incomplete market data
   - risk gating
   - a runtime/config defect

A no-trade session is acceptable if all candidates were explicitly rejected for strategy or risk reasons and the run completed cleanly.

### Quick triage checklist

Use this sequence:

1. check `models/predictions/latest.json`
2. check latest `reports/paper_trading/` summary
3. check latest `reports/signals/` audit JSON/CSV
4. review rejection counts by reason
5. confirm whether any candidates passed score thresholds
6. confirm whether edge after cost stayed positive after spread/slippage/fee drag
7. confirm whether higher-timeframe trend alignment blocked otherwise attractive lower-timeframe entries
8. confirm whether spread/liquidity filters are too restrictive
9. confirm whether risk sizing, top-N selection, or bracket validation blocked otherwise valid entries

### Operational expectation

Every buy, bracket buy, short, bracket short, rejection, skip, or no-action outcome must be explainable from the audit outputs.

If any final decision cannot be reconstructed from reports and logs, treat that as an observability defect and fix it before trusting the strategy.
