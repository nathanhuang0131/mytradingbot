# Paper Trading Platform Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a fully runnable, testable phase-1 paper trading platform with qlib-first signals, Streamlit operations, diagnostics, reporting, and advisory-only LLM tooling.

**Architecture:** Implement a vertical slice centered on the paper trading workflow so the same typed models, orchestration services, broker boundary, and diagnostics power both CLI scripts and Streamlit pages. Keep qlib behind adapters so the dashboard can boot without `pyqlib`, while qlib-dependent actions fail clearly and produce explicit operator guidance.

**Tech Stack:** Python 3.11, pydantic, pydantic-settings, pandas, numpy, streamlit, plotly, typer, rich, loguru, optional pyqlib, optional openai, pytest

---

### Task 1: Package Foundations And Shared Settings

**Files:**
- Create: `src/mytradingbot/core/enums.py`
- Create: `src/mytradingbot/core/exceptions.py`
- Create: `src/mytradingbot/core/paths.py`
- Create: `src/mytradingbot/core/logging_utils.py`
- Create: `src/mytradingbot/core/settings.py`
- Create: `src/mytradingbot/core/__init__.py`
- Modify: `src/mytradingbot/__init__.py`
- Test: `tests/unit/core/test_settings.py`
- Test: `tests/unit/core/test_paths.py`

**Step 1: Write the failing test**

```python
from mytradingbot.core.settings import AppSettings


def test_default_mode_is_paper() -> None:
    settings = AppSettings()
    assert settings.runtime.default_mode.value == "paper"
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/core/test_settings.py tests/unit/core/test_paths.py`
Expected: FAIL because `AppSettings` and path discovery do not exist yet.

**Step 3: Write minimal implementation**

```python
class AppSettings(BaseSettings):
    runtime: RuntimeSettings = RuntimeSettings()
    paths: RepoPaths = RepoPaths.discover()
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/core/test_settings.py tests/unit/core/test_paths.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/__init__.py src/mytradingbot/core tests/unit/core
git commit -m "feat: add core settings and path discovery"
```

### Task 2: Typed Runtime Models And Session Artifacts

**Files:**
- Create: `src/mytradingbot/core/models.py`
- Create: `src/mytradingbot/signals/models.py`
- Create: `src/mytradingbot/execution/models.py`
- Create: `src/mytradingbot/risk/models.py`
- Create: `src/mytradingbot/reporting/models.py`
- Create: `src/mytradingbot/signals/__init__.py`
- Create: `src/mytradingbot/execution/__init__.py`
- Create: `src/mytradingbot/risk/__init__.py`
- Create: `src/mytradingbot/reporting/__init__.py`
- Test: `tests/unit/core/test_models.py`

**Step 1: Write the failing test**

```python
from mytradingbot.core.models import ArtifactStatus, TradeAttemptTrace


def test_trade_attempt_trace_preserves_pipeline_states() -> None:
    trace = TradeAttemptTrace.for_symbol("AAPL")
    assert trace.symbol == "AAPL"
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/core/test_models.py`
Expected: FAIL because the typed models are not implemented.

**Step 3: Write minimal implementation**

```python
class ArtifactStatus(BaseModel):
    name: str
    is_ready: bool
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/core/test_models.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/core/models.py src/mytradingbot/signals src/mytradingbot/execution src/mytradingbot/risk src/mytradingbot/reporting tests/unit/core/test_models.py
git commit -m "feat: add typed trading runtime models"
```

### Task 3: Qlib Availability, Artifact Freshness, And Prediction Loading

**Files:**
- Create: `src/mytradingbot/qlib_engine/service.py`
- Create: `src/mytradingbot/qlib_engine/models.py`
- Create: `src/mytradingbot/qlib_engine/__init__.py`
- Create: `configs/qlib/daily.yaml`
- Create: `configs/qlib/intraday_5min.yaml`
- Test: `tests/unit/qlib_engine/test_service.py`

**Step 1: Write the failing test**

```python
from mytradingbot.qlib_engine.service import QlibWorkflowService


def test_missing_pyqlib_returns_explicit_guidance() -> None:
    service = QlibWorkflowService(pyqlib_available=False)
    result = service.get_runtime_prediction_status()
    assert not result.is_ready
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/qlib_engine/test_service.py`
Expected: FAIL because qlib service scaffolding does not exist.

**Step 3: Write minimal implementation**

```python
class QlibWorkflowService:
    def get_runtime_prediction_status(self) -> PredictionRuntimeStatus:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/qlib_engine/test_service.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/qlib_engine configs/qlib tests/unit/qlib_engine/test_service.py
git commit -m "feat: add qlib workflow availability and artifact checks"
```

### Task 4: Strategy Registry And Canonical Mapping

**Files:**
- Create: `src/mytradingbot/strategies/base.py`
- Create: `src/mytradingbot/strategies/registry.py`
- Create: `src/mytradingbot/strategies/intraday.py`
- Create: `src/mytradingbot/strategies/short_term.py`
- Create: `src/mytradingbot/strategies/long_term.py`
- Create: `src/mytradingbot/strategies/__init__.py`
- Create: `configs/strategies/intraday.yaml`
- Create: `configs/strategies/short_term.yaml`
- Create: `configs/strategies/long_term.yaml`
- Test: `tests/unit/strategies/test_registry.py`

**Step 1: Write the failing test**

```python
from mytradingbot.strategies.registry import StrategyRegistry


def test_registry_exposes_only_canonical_strategy_names() -> None:
    registry = StrategyRegistry.build_default()
    assert registry.names() == ["intraday", "long_term", "scalping", "short_term"]
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/strategies/test_registry.py`
Expected: FAIL because the registry does not exist.

**Step 3: Write minimal implementation**

```python
class StrategyRegistry:
    def __init__(self, strategies: dict[str, BaseStrategy]) -> None:
        self._strategies = strategies
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/strategies/test_registry.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/strategies configs/strategies tests/unit/strategies/test_registry.py
git commit -m "feat: add canonical strategy registry"
```

### Task 5: Scalping Strategy With Modular Filters

**Files:**
- Create: `src/mytradingbot/strategies/scalping.py`
- Create: `configs/strategies/scalping.yaml`
- Test: `tests/unit/strategies/test_scalping_strategy.py`

**Step 1: Write the failing test**

```python
from mytradingbot.strategies.scalping import ScalpingStrategy


def test_scalping_rejects_signal_below_return_threshold(signal_bundle_factory) -> None:
    strategy = ScalpingStrategy()
    decision = strategy.evaluate(signal_bundle_factory(predicted_return=0.001))
    assert not decision.should_trade
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/strategies/test_scalping_strategy.py`
Expected: FAIL because the scalping strategy is not implemented.

**Step 3: Write minimal implementation**

```python
class ScalpingStrategy(BaseStrategy):
    name = "scalping"
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/strategies/test_scalping_strategy.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/strategies/scalping.py configs/strategies/scalping.yaml tests/unit/strategies/test_scalping_strategy.py
git commit -m "feat: implement modular scalping strategy"
```

### Task 6: Risk Engine And Live-Mode Guard

**Files:**
- Create: `src/mytradingbot/risk/service.py`
- Create: `configs/risk/default.yaml`
- Test: `tests/unit/risk/test_service.py`

**Step 1: Write the failing test**

```python
from mytradingbot.core.enums import RuntimeMode
from mytradingbot.risk.service import RiskEngine


def test_risk_engine_blocks_live_orders_in_phase_one(approved_trade_intent) -> None:
    decision = RiskEngine().evaluate(intent=approved_trade_intent, mode=RuntimeMode.LIVE)
    assert not decision.approved
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/risk/test_service.py`
Expected: FAIL because the risk engine is not implemented.

**Step 3: Write minimal implementation**

```python
class RiskEngine:
    def evaluate(self, intent: TradeIntent, mode: RuntimeMode) -> RiskDecision:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/risk/test_service.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/risk/service.py configs/risk/default.yaml tests/unit/risk/test_service.py
git commit -m "feat: add risk engine with phase one live guard"
```

### Task 7: Execution Engine And Broker Boundary

**Files:**
- Create: `src/mytradingbot/execution/service.py`
- Create: `src/mytradingbot/brokers/base.py`
- Create: `src/mytradingbot/brokers/__init__.py`
- Test: `tests/unit/execution/test_service.py`

**Step 1: Write the failing test**

```python
from mytradingbot.execution.service import ExecutionEngine


def test_execution_engine_skips_broker_mutation_in_dry_run(approved_risk_decision, paper_broker) -> None:
    result = ExecutionEngine(broker=paper_broker).execute(approved_risk_decision, dry_run=True)
    assert result.execution_skipped
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/execution/test_service.py`
Expected: FAIL because the execution layer is missing.

**Step 3: Write minimal implementation**

```python
class ExecutionEngine:
    def execute(self, decision: RiskDecision, dry_run: bool) -> ExecutionResult:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/execution/test_service.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/execution/service.py src/mytradingbot/brokers/base.py tests/unit/execution/test_service.py
git commit -m "feat: add execution engine broker boundary"
```

### Task 8: Paper Broker And Alpaca Scaffold

**Files:**
- Create: `src/mytradingbot/brokers/paper.py`
- Create: `src/mytradingbot/brokers/alpaca.py`
- Create: `configs/broker/alpaca.paper.yaml`
- Create: `configs/broker/alpaca.live.yaml`
- Test: `tests/unit/brokers/test_paper_broker.py`
- Test: `tests/unit/brokers/test_alpaca_scaffold.py`

**Step 1: Write the failing test**

```python
from mytradingbot.brokers.paper import PaperBroker


def test_paper_broker_records_order_and_position(order_request_factory) -> None:
    result = PaperBroker().submit_order(order_request_factory())
    assert result.order is not None
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/brokers/test_paper_broker.py tests/unit/brokers/test_alpaca_scaffold.py`
Expected: FAIL because broker implementations are missing.

**Step 3: Write minimal implementation**

```python
class PaperBroker(BaseBroker):
    def submit_order(self, request: ExecutionRequest) -> BrokerExecutionResult:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/brokers/test_paper_broker.py tests/unit/brokers/test_alpaca_scaffold.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/brokers configs/broker tests/unit/brokers
git commit -m "feat: add paper broker and alpaca scaffold"
```

### Task 9: Orchestration For Dry-Run, Paper Sessions, And Maintenance

**Files:**
- Create: `src/mytradingbot/orchestration/service.py`
- Create: `src/mytradingbot/orchestration/__init__.py`
- Create: `src/mytradingbot/data/service.py`
- Create: `src/mytradingbot/data/__init__.py`
- Test: `tests/integration/test_paper_session.py`
- Test: `tests/integration/test_dry_run_session.py`

**Step 1: Write the failing test**

```python
from mytradingbot.orchestration.service import TradingPlatformService


def test_paper_session_runs_end_to_end_with_traceability(platform_service_factory) -> None:
    result = platform_service_factory().run_session(strategy_name="scalping", mode="paper")
    assert result.trade_attempts
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/integration/test_paper_session.py tests/integration/test_dry_run_session.py`
Expected: FAIL because orchestration is not implemented.

**Step 3: Write minimal implementation**

```python
class TradingPlatformService:
    def run_session(self, strategy_name: str, mode: str) -> SessionResult:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/integration/test_paper_session.py tests/integration/test_dry_run_session.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/orchestration src/mytradingbot/data tests/integration/test_paper_session.py tests/integration/test_dry_run_session.py
git commit -m "feat: add paper session orchestration"
```

### Task 10: Diagnostics And Reporting Surfaces

**Files:**
- Create: `src/mytradingbot/diagnostics/service.py`
- Create: `src/mytradingbot/diagnostics/__init__.py`
- Create: `src/mytradingbot/reporting/service.py`
- Test: `tests/unit/diagnostics/test_service.py`
- Test: `tests/unit/reporting/test_service.py`

**Step 1: Write the failing test**

```python
from mytradingbot.diagnostics.service import DiagnosticsService


def test_no_trade_diagnostics_explain_rejections(session_result_factory) -> None:
    report = DiagnosticsService().build_no_trade_report(session_result_factory(no_trades=True))
    assert report.reasons
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/diagnostics/test_service.py tests/unit/reporting/test_service.py`
Expected: FAIL because diagnostics and reporting services are missing.

**Step 3: Write minimal implementation**

```python
class DiagnosticsService:
    def build_no_trade_report(self, result: SessionResult) -> NoTradeDiagnostics:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/diagnostics/test_service.py tests/unit/reporting/test_service.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/diagnostics src/mytradingbot/reporting tests/unit/diagnostics tests/unit/reporting
git commit -m "feat: add diagnostics and reporting services"
```

### Task 11: Advisory-Only LLM Services

**Files:**
- Create: `src/mytradingbot/llm/service.py`
- Create: `src/mytradingbot/llm/__init__.py`
- Test: `tests/unit/llm/test_service.py`

**Step 1: Write the failing test**

```python
from mytradingbot.llm.service import AdvisoryLLMService


def test_signal_explanation_uses_artifacts_without_overriding_direction(session_result_factory) -> None:
    response = AdvisoryLLMService(client=None).explain_signal(session_result_factory().trade_attempts[0])
    assert response.mode == "advisory"
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/llm/test_service.py`
Expected: FAIL because the LLM service does not exist.

**Step 3: Write minimal implementation**

```python
class AdvisoryLLMService:
    def explain_signal(self, attempt: TradeAttemptTrace) -> AdvisoryResponse:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/llm/test_service.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/llm tests/unit/llm/test_service.py
git commit -m "feat: add advisory llm services"
```

### Task 12: UI Services And Streamlit Pages

**Files:**
- Create: `src/mytradingbot/ui_services/dashboard.py`
- Create: `src/mytradingbot/ui_services/strategy_control.py`
- Create: `src/mytradingbot/ui_services/data_training.py`
- Create: `src/mytradingbot/ui_services/paper_trading.py`
- Create: `src/mytradingbot/ui_services/live_trading.py`
- Create: `src/mytradingbot/ui_services/llm_copilot.py`
- Create: `src/mytradingbot/ui_services/diagnostics.py`
- Create: `src/mytradingbot/ui_services/settings.py`
- Create: `src/mytradingbot/ui_services/__init__.py`
- Modify: `app/app.py`
- Modify: `app/pages/01_Dashboard.py`
- Modify: `app/pages/02_Strategy_Control.py`
- Modify: `app/pages/03_Data_and_Training.py`
- Modify: `app/pages/04_Paper_Trading.py`
- Modify: `app/pages/05_Live_Trading.py`
- Modify: `app/pages/06_LLM_Copilot.py`
- Modify: `app/pages/07_Diagnostics.py`
- Modify: `app/pages/08_Settings.py`
- Test: `tests/unit/ui_services/test_dashboard.py`
- Test: `tests/unit/ui_services/test_strategy_control.py`
- Test: `tests/smoke/test_streamlit_structure.py`

**Step 1: Write the failing test**

```python
from mytradingbot.ui_services.dashboard import DashboardService


def test_dashboard_service_surfaces_prediction_health(platform_service_factory) -> None:
    payload = DashboardService(platform_service_factory()).get_dashboard_payload()
    assert payload.prediction_status is not None
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/ui_services/test_dashboard.py tests/unit/ui_services/test_strategy_control.py tests/smoke/test_streamlit_structure.py`
Expected: FAIL because the UI service layer is missing.

**Step 3: Write minimal implementation**

```python
class DashboardService:
    def get_dashboard_payload(self) -> DashboardPayload:
        ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/unit/ui_services/test_dashboard.py tests/unit/ui_services/test_strategy_control.py tests/smoke/test_streamlit_structure.py`
Expected: PASS

**Step 5: Commit**

```bash
git add src/mytradingbot/ui_services app/app.py app/pages tests/unit/ui_services tests/smoke/test_streamlit_structure.py
git commit -m "feat: add streamlit ui services and pages"
```

### Task 13: Thin CLI Scripts, Validation, And Goalcheck

**Files:**
- Create: `scripts/build_qlib_dataset.py`
- Create: `scripts/train_models.py`
- Create: `scripts/refresh_predictions.py`
- Create: `scripts/run_paper_trading.py`
- Create: `scripts/run_live_trading.py`
- Create: `scripts/run_daily_maintenance.py`
- Create: `scripts/validate_system.py`
- Create: `scripts/smoke_test_broker.py`
- Create: `scripts/launch_dashboard.py`
- Create: `scripts/goalcheck.py`
- Test: `tests/integration/test_scripts.py`
- Test: `tests/smoke/test_goalcheck.py`

**Step 1: Write the failing test**

```python
def test_run_paper_trading_script_executes_without_crashing(script_runner) -> None:
    result = script_runner("scripts/run_paper_trading.py", "--strategy", "scalping")
    assert result.returncode == 0
```

**Step 2: Run test to verify it fails**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/integration/test_scripts.py tests/smoke/test_goalcheck.py`
Expected: FAIL because the scripts do not exist.

**Step 3: Write minimal implementation**

```python
def main() -> int:
    ...
```

**Step 4: Run test to verify it passes**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q tests/integration/test_scripts.py tests/smoke/test_goalcheck.py`
Expected: PASS

**Step 5: Commit**

```bash
git add scripts tests/integration/test_scripts.py tests/smoke/test_goalcheck.py
git commit -m "feat: add operational scripts and goalcheck"
```

### Task 14: Documentation Alignment And Full Verification

**Files:**
- Modify: `README.md`
- Modify: `docs/ARCHITECTURE.md`
- Modify: `docs/FIRST_RUN.md`
- Modify: `docs/RUNBOOK.md`
- Modify: `docs/USER_MANUAL.md`

**Step 1: Write the verification checklist**

```text
- README reflects actual commands
- Architecture doc reflects the implemented vertical slice
- First run doc includes qlib-missing guidance
- Runbook includes paper and live-preflight flows
- User manual documents all required pages and strategies
```

**Step 2: Run system verification**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q`
Expected: PASS only when all implemented layers and tests are complete.

**Step 3: Update documentation to match the real system**

```markdown
## Phase 1

Paper trading is the complete operational path in phase 1. Live trading is visible in the UI but remains validation-only.
```

**Step 4: Run final verification commands**

Run: `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q`
Expected: PASS

Run: `python -m streamlit run app/app.py --server.headless true`
Expected: Streamlit starts without import or runtime errors.

Run: `python scripts/run_paper_trading.py --strategy scalping --mode paper`
Expected: Paper session executes and prints a session summary.

**Step 5: Commit**

```bash
git add README.md docs
git commit -m "docs: align operator documentation with phase one platform"
```
