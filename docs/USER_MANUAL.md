# User Manual

## Purpose

This manual explains the guided setup wizard and the main operator choices in plain language, with **scalping** as the primary example.

If you are new to the platform, start here:

1. Launch the app with `python -m streamlit run app/app.py`
2. Open `Setup Wizard` from the sidebar or click `Start New Trading Session (Wizard)`
3. Choose a scalping preset
4. Review the summary page
5. Start the session

The wizard auto-saves your selections. You do not need to remember command sequences for normal setup.

## Where The Wizard Saves Your Setup

The wizard saves three kinds of files automatically:

- User profile: [configs/user_profiles](C:/Users/User/Documents/MyTradingBot_Next/configs/user_profiles)
- Latest resolved session config: [data/runtime/session_profiles](C:/Users/User/Documents/MyTradingBot_Next/data/runtime/session_profiles)
- Active symbol manifest for that profile: [data/runtime/active_universes](C:/Users/User/Documents/MyTradingBot_Next/data/runtime/active_universes)

Important:

- Changing the active symbol set does **not** delete previously downloaded historical data.
- Old raw and normalized parquet stays on disk for future training and analysis.

## Best Starting Point For Scalping

Recommended presets:

- `Scalping - Local Paper Safe`
  - safest first test
  - uses the repo-local paper broker
  - long only
  - single run
- `Scalping - Alpaca Paper Long Only`
  - sends real paper orders to Alpaca paper
  - long only
  - single run
- `Scalping - Alpaca Paper Long + Short`
  - sends real paper orders to Alpaca paper
  - both long and short allowed
  - single run
- `Scalping - Overnight Loop`
  - designed for unattended paper operation
  - Alpaca paper broker mode
  - both long and short allowed
  - loop mode
  - combines old active symbols with newly generated liquid symbols

If you are unsure, start with:

- `Scalping - Local Paper Safe` for a dry operational check
- `Scalping - Alpaca Paper Long Only` for first live paper-account submission

## Wizard Steps

### Step 1: User Profile

This identifies the operator and loads or creates a saved setup.

Choices:

- `Create new profile`
  - creates a new operator profile
  - best when you want a separate setup from other users or experiments
- `Load existing profile`
  - loads a previously saved profile
  - good when you want to continue a known workflow
- `Use last setup as starting point`
  - restores the latest saved session config for a profile
  - best when you want to tweak yesterday’s setup

Fields:

- `User/profile name`
  - plain name for the operator or setup owner
  - example: `Alice Trader`

### Step 2: Strategy And Session Mode

This defines the runtime mode and how long the session should run.

Fields:

- `Strategy`
  - current primary choice is `scalping`
  - the platform also exposes `intraday`, `short_term`, and `long_term`
- `Run type`
  - currently use `paper` for real paper-account or repo-local paper workflows
- `Broker mode`
  - `local_paper`
    - simulated repo-local broker
    - Alpaca paper UI will not show matching orders
  - `alpaca_paper_api`
    - submits real paper orders to Alpaca paper
    - Alpaca paper dashboard and API will show those bot-owned paper orders
- `Session mode`
  - `single_run`
    - one execution pass
  - `bounded_smoke`
    - small test run
  - `loop`
    - supervised repeated cycle for overnight or longer operation

### Step 3: Symbol Universe

This controls the **active symbol set** used by the session.

It does **not** control whether old downloaded data stays on disk. Old data is retained.

Modes:

- `keep using old symbols`
  - keep the existing active symbol manifest
  - no liquidity flow needed
- `run liquidity flow and combine new symbols with old symbols`
  - generate a fresh liquidity-ranked list
  - merge with the current active symbols
  - dedupe automatically
- `use completely new symbols`
  - generate a fresh liquidity-ranked list
  - replace the active symbol manifest
  - historical raw/normalized data is still retained on disk

Fields shown when liquidity flow is used:

- `Target symbol count`
  - how many symbols you want in the generated liquid universe
  - example: `100`
  - this is a target, not a guarantee; the final count depends on filters and available symbols
- `Min price`
  - minimum average stock price allowed into the universe
  - example: `15`
  - higher values usually reduce low-priced names and noise
- `Min average volume`
  - minimum average daily share volume
  - example: `500000`
  - higher values bias toward more liquid names
- `Include ETFs`
  - include or exclude ETFs from the generated universe
  - off is usually cleaner for equity-only scalping workflows

### Step 4: Refresh And Data Policy

This controls how aggressively the runtime keeps market and prediction inputs fresh.

Basic fields:

- `Auto-refresh market snapshot`
  - refreshes market data inputs on cadence
  - recommended on
- `Auto-refresh predictions`
  - refreshes prediction artifacts on cadence
  - recommended on
- `Loop interval seconds`
  - how often the supervised loop cycles
  - example: `300` means every 5 minutes
- `Stale input behavior`
  - `block trading`
    - safest
    - if required inputs are stale, the session does not trade
  - `warn only`
    - softer warning mode
  - `stop session`
    - halt the session if stale inputs are detected

Advanced fields:

- `Market snapshot refresh cadence`
  - how often to refresh the market snapshot
- `Prediction refresh cadence`
  - how often to refresh predictions
- `Dataset rebuild cadence`
  - how often the dataset can be rebuilt for inference freshness
- `Keep model training separate from session execution`
  - recommended on
  - model training is intentionally separate from the normal trading loop

Practical meaning:

- The loop can auto-refresh market data, dataset, and predictions
- It does **not** retrain the model on every cycle

### Step 5: Alpha And Model

This step controls how predictions are filtered before the scalping strategy evaluates them.

Basic fields:

- `Use latest trained model`
  - means: use the current model artifact already stored in the repo
  - recommended on
  - this does **not** automatically trigger a new model training run
- `Side mode`
  - `long_only`
  - `short_only`
  - `both`
- `Refresh predictions before run`
  - refresh the prediction artifact using the current model before the session runs
  - recommended on

Advanced fields:

- `Candidate count`
  - maximum number of prediction candidates to pass into the runtime after side filtering
  - example: `20`
  - lower number = narrower candidate set
  - higher number = broader candidate set
- `Long threshold`
  - minimum predicted return required for long candidates
  - `0.005` means about `0.5%`
  - `0.000` means no extra wizard-level long threshold
- `Short threshold`
  - minimum absolute predicted return required for short candidates
  - `0.005` means about `0.5%`
  - `0.000` means no extra wizard-level short threshold
- `Model artifact path`
  - optional manual model path override
  - leave blank unless you are intentionally validating a specific model file

Important current behavior:

- `Use latest trained model` is currently a **policy choice and saved preference**
- session start can refresh the dataset and predictions
- session start does **not** automatically call model training
- if you want a new trained model, run a training workflow separately

### Step 6: Risk Controls

This step defines high-level runtime guardrails.

Basic fields:

- `Max positions`
  - maximum total simultaneous bot-managed positions
  - example: `3`
- `Max dollars per trade`
  - maximum notional budget per trade
  - example: `5000`
  - this caps position size
- `Max daily loss %`
  - daily loss guardrail
  - example: `2.0` means 2%
- `Same-symbol protection`
  - prevents repeated or conflicting same-symbol exposure
  - recommended on

Advanced fields:

- `Max long positions`
  - max simultaneous long positions
- `Max short positions`
  - max simultaneous short positions
- `Cooldown after exit (minutes)`
  - minimum wait after a trade exits before re-entering the same symbol
- `Block foreign/manual exposure`
  - block bot entries when manual or foreign Alpaca positions exist on that symbol
  - recommended on
- `Shortability gate policy`
  - `required`
    - safest
    - block short entries if shortability is not confirmed
  - `warn`
    - warn but continue where allowed
  - `off`
    - least strict
- `Reversal policy`
  - whether the bot can flip from long to short or short to long
- `Regime gating enabled`
  - use regime-aware gating where applicable

### Step 7: Execution And Brackets

This step controls the execution style and bracket behavior.

Basic fields:

- `Order type`
  - `market`
  - `limit`
- `Bracket enabled`
  - recommended on
  - bracket protection is especially important for scalping
- `Take-profit %`
  - target distance used by the wizard execution profile
  - example: `0.6` means about `0.6%`
- `Stop-loss %`
  - stop distance used by the wizard execution profile
  - example: `0.35` means about `0.35%`
- `Sizing mode`
  - `fixed_quantity`
  - `risk_budget`
- `Quantity`
  - order quantity when fixed sizing is used

Advanced fields:

- `Enable penny normalization`
  - keep prices aligned to valid market increments
- `Market-open-only policy`
  - intended meaning: only allow new submissions during regular market hours
  - current state: saved as a preference, not yet a fully enforced runtime gate
- `Allow after-hours submission`
  - intended meaning: permit submissions outside the regular session
  - current state: saved as a preference, not yet a fully enforced runtime gate
- `Smoke submission behavior`
  - `auto_cancel`
  - `leave_open`
  - used for bounded smoke-style submissions

## Scalping: Train New Model Or Use Existing Model?

### If You Want To Use The Existing Trained Model

This is the fastest path and is usually fine for a normal trading session.

Wizard choices:

- `Use latest trained model = on`
- `Refresh predictions before run = on`

What happens:

- the existing model artifact is reused
- predictions can be refreshed from new data
- the system does not retrain the model automatically

Good choice when:

- you already trained recently
- you only want fresh predictions and execution
- you are doing normal overnight or intraday paper operation

### If You Want To Train A New Model

Use the Data Management page or the CLI before launching the session.

Typical order:

1. update or download market data
2. build the qlib dataset
3. train the model
4. refresh predictions
5. run paper trading

Typical commands:

```powershell
python scripts\run_daily_maintenance.py --action update --symbols-file data\universe\latest_top_liquidity_universe.json --timeframes 1m 5m 15m 1d
python scripts\build_qlib_dataset.py --strategy scalping --symbols-file data\universe\latest_top_liquidity_universe.json
python scripts\train_models.py --strategy scalping
python scripts\refresh_predictions.py --strategy scalping
python scripts\run_paper_trading.py --strategy scalping --mode paper --broker-mode alpaca_paper_api --symbols-file data\universe\latest_top_liquidity_universe.json --loop --interval-seconds 300 --verbose
```

Use `run_alpha_robust_training.py` if you specifically want the stricter data-sufficiency and training-gate flow.

### Practical Rule

- normal session: use the latest trained model
- major new universe change, long history refresh, or explicit retrain day: run a full training workflow first

## What The Review Page Means

The `Defaults vs customized` box is only a review summary.

- `defaults_applied`
  - settings still matching the wizard’s recommended defaults
- `customized`
  - settings you changed from those recommended defaults

It is not an error. It is just a final sanity check before you start.

## Where To Find Trading Activities, Logs, And Reports

### Main runtime logs

- Loop log: [logs/paper_trading_loop.log](C:/Users/User/Documents/MyTradingBot_Next/logs/paper_trading_loop.log)
- Wizard-launched background logs: [logs](C:/Users/User/Documents/MyTradingBot_Next/logs)

Use these when you want to know:

- whether the loop is running
- whether inputs were fresh
- whether orders were submitted
- whether the session was blocked by stale inputs or risk checks

### Session reports

- Paper session summaries: [reports/paper_trading](C:/Users/User/Documents/MyTradingBot_Next/reports/paper_trading)

Useful files:

- `<session_id>_paper_session.json`
- `<session_id>_paper_session.md`

These tell you:

- broker mode
- decision-pipeline readiness
- order count
- fill count
- no-trade success vs runtime failure

### Candidate and rejection audit

- Decision audits: [reports/signals](C:/Users/User/Documents/MyTradingBot_Next/reports/signals)

Useful files:

- `<session_id>_decision_audit.json`
- `<session_id>_decision_audit.csv`
- `<session_id>_decision_audit.md`

These tell you:

- which symbols were evaluated
- which ones were accepted or rejected
- why a symbol failed
- whether the source was `qlib_candidate_only` or `qlib_plus_rules`

### Analytics and P&L

- Analytics summary: [reports/analytics/pnl_summary.md](C:/Users/User/Documents/MyTradingBot_Next/reports/analytics/pnl_summary.md)
- Closed trades: [reports/analytics/closed_trades.csv](C:/Users/User/Documents/MyTradingBot_Next/reports/analytics/closed_trades.csv)
- P&L attribution: [reports/analytics/pnl_attribution.csv](C:/Users/User/Documents/MyTradingBot_Next/reports/analytics/pnl_attribution.csv)

These are where you check:

- realized P&L
- win/loss by symbol
- profitability by strategy
- profitability by signal source

### Append-only ledgers

- Signal outcomes: [data/ledger/signal_outcomes.csv](C:/Users/User/Documents/MyTradingBot_Next/data/ledger/signal_outcomes.csv)
- Incidents: [data/ledger/incidents.csv](C:/Users/User/Documents/MyTradingBot_Next/data/ledger/incidents.csv)

Use these when you want a longer-running machine-readable record across sessions.

### Runtime state

- SQLite runtime store: [data/state/institutional_runtime.sqlite3](C:/Users/User/Documents/MyTradingBot_Next/data/state/institutional_runtime.sqlite3)

This is the persistent state backing:

- open orders
- positions
- bracket state
- cooldown state
- reconciliation state

### Model, predictions, and dataset artifacts

- Current model: [models/qlib/model.pkl](C:/Users/User/Documents/MyTradingBot_Next/models/qlib/model.pkl)
- Current predictions: [models/predictions/latest.json](C:/Users/User/Documents/MyTradingBot_Next/models/predictions/latest.json)
- Current dataset: [data/qlib/dataset.parquet](C:/Users/User/Documents/MyTradingBot_Next/data/qlib/dataset.parquet)
- Current market snapshot: [data/snapshots/market_snapshot.json](C:/Users/User/Documents/MyTradingBot_Next/data/snapshots/market_snapshot.json)

These are the main files to inspect when you want to answer:

- was the model trained?
- were predictions refreshed?
- is the market snapshot fresh?

## Common Scalping Questions

### Why did the loop run but no trades happen?

Possible truthful reasons:

- no candidates passed the scalping filters
- predictions were stale
- market snapshot was stale
- risk checks blocked the candidate
- foreign/manual exposure blocked the symbol
- shortability blocked a short candidate

Use:

- [reports/paper_trading](C:/Users/User/Documents/MyTradingBot_Next/reports/paper_trading)
- [reports/signals](C:/Users/User/Documents/MyTradingBot_Next/reports/signals)
- [data/ledger/incidents.csv](C:/Users/User/Documents/MyTradingBot_Next/data/ledger/incidents.csv)

### How do I know if the model was actually used?

Trading uses the prediction artifact, not `model.pkl` directly during the session.

Check:

- [models/predictions/latest.json](C:/Users/User/Documents/MyTradingBot_Next/models/predictions/latest.json)
- latest paper session report
- latest decision audit

If `decision_pipeline_ready = true` and the decision audit is populated, the prediction path was active.

### Can scalping use both long and short?

Yes, if `Side mode = both`.

But:

- same-symbol protection still applies
- shortability still applies
- broker/risk checks can still reject shorts

## Final Notes

- Fields marked `Recommended default` are generally safe to leave alone.
- Basic mode is enough for most normal paper sessions.
- Advanced and expert fields are best treated as tuning controls, not mandatory setup.
- When unsure, keep the defaults, use `local_paper` or a bounded Alpaca paper smoke, and inspect the session and decision-audit reports after the run.
