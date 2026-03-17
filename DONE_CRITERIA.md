# Definition of Done

The agent must not declare the build complete unless all of the following are true.

## 1. Package and install
- `pip install -e .[dev]` succeeds
- `import mytradingbot` succeeds

## 2. Tests
- `pytest -q` passes
- at least:
  - 1 smoke test
  - core unit tests
  - strategy/risk/execution path tests

## 3. Streamlit UI
- `streamlit run app/app.py` launches successfully
- these pages exist:
  - Dashboard
  - Strategy Control
  - Data and Training
  - Paper Trading
  - Live Trading
  - LLM Copilot
  - Diagnostics
  - Settings

## 4. Strategy system
- strategies exist:
  - scalping
  - intraday
  - short_term
  - long_term
- strategy selection maps correctly from UI to backend

## 5. Runtime architecture
- qlib workflow scaffolding exists
- signals are typed objects
- strategies output trade intents
- risk checks occur before execution
- broker code is isolated under brokers/

## 6. Paper trading
- a paper-trading workflow runs without crashing
- live trading remains explicitly gated

## 7. Diagnostics
- no-trade diagnostics exists
- broker diagnostics exists
- stale prediction / artifact diagnostics exists

## 8. LLM advisory
- signal explanation exists
- diagnostics summary exists
- strategy comparison exists
- post-market review exists
- LLM is advisory only

## 9. Docs
- README exists
- docs/ARCHITECTURE.md exists
- docs/FIRST_RUN.md exists
- docs/RUNBOOK.md exists
- docs/USER_MANUAL.md exists

## 10. Final output required from agent
At the end, provide:
1. architecture summary
2. created files summary
3. exact commands to run
4. first-run workflow
5. remaining limitations