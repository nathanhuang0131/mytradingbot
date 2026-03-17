# Codex Agent Rules

This repository already defines the full architecture.

The agent MUST follow these rules.

---

## 1. Do not create new top-level folders

Allowed folders only:

app/
configs/
data/
docs/
logs/
models/
reference/
reports/
scripts/
src/
tests/

Do not create any additional root folders.

---

## 2. Python package structure must stay stable

All Python code must exist under:

src/mytradingbot/

Modules allowed:

core/
data/
qlib_engine/
signals/
strategies/
risk/
execution/
brokers/
orchestration/
diagnostics/
reporting/
llm/
ui_services/

Do not invent new package layers.

---

## 3. UI rules

Streamlit UI must stay inside:

app/

Pages must remain inside:

app/pages/

Do not move UI code into the Python package.

---

## 4. Scripts

Operational scripts must remain inside:

scripts/

Scripts allowed:

build_qlib_dataset.py
train_models.py
refresh_predictions.py
run_paper_trading.py
run_live_trading.py
run_daily_maintenance.py
validate_system.py
smoke_test_broker.py
launch_dashboard.py
goalcheck.py

---

## 5. Testing

Tests must exist only in:

tests/

Test structure:

tests/unit/
tests/integration/
tests/smoke/

---

## 6. Dependencies

Dependencies must be declared in:

pyproject.toml

Do not install global packages.

---

## 7. Implementation order

Agent must implement the system in this order:

1. Package scaffolding
2. Configuration system
3. Data ingestion layer
4. Qlib integration
5. Signal generation
6. Strategy framework
7. Risk engine
8. Execution engine
9. Broker adapters
10. Orchestration layer
11. Diagnostics
12. Reporting
13. Streamlit dashboard
14. LLM copilot
15. Testing

---

## 8. Quality rules

All modules must include:

• docstrings
• typing hints
• logging
• minimal unit tests

---

## 9. Safety rules

Do NOT implement live trading execution before paper trading works.

Paper trading must pass tests first.

---

## 10. Success condition

The build is complete when:

pytest passes

AND

Streamlit dashboard launches:

streamlit run app/app.py

AND

paper trading simulation runs without error.