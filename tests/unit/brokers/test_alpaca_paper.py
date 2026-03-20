from __future__ import annotations

from datetime import datetime, timezone
from types import SimpleNamespace

from mytradingbot.core.enums import RuntimeMode
from mytradingbot.core.models import BracketPlan, ExecutionRequest
from mytradingbot.core.paths import RepoPaths
from mytradingbot.core.settings import AppSettings


class _FakeTradingClient:
    def __init__(self) -> None:
        self.submitted = []
        self.orders = []
        self.positions = []
        self.account = SimpleNamespace(status="ACTIVE", buying_power="25000")

    def get_account(self):
        return self.account

    def submit_order(self, order_data):
        self.submitted.append(order_data)
        return SimpleNamespace(
            id="alpaca-order-1",
            client_order_id=getattr(order_data, "client_order_id", None),
            symbol=getattr(order_data, "symbol", "AAPL"),
            side=getattr(order_data, "side", None),
            qty=getattr(order_data, "qty", None),
            status="accepted",
            submitted_at=datetime.now(timezone.utc),
            filled_at=None,
            filled_qty="0",
            filled_avg_price=None,
            order_class=getattr(order_data, "order_class", None),
            limit_price=None,
            stop_price=None,
            legs=[],
        )

    def get_orders(self, filter=None):
        return list(self.orders)

    def get_all_positions(self):
        return list(self.positions)

    def get(self, path: str, data=None, **kwargs):
        if path == "/account/activities":
            return []
        return []


def _bracket_request() -> ExecutionRequest:
    return ExecutionRequest(
        symbol="AAPL",
        side="buy",
        quantity=5,
        strategy_name="scalping",
        mode=RuntimeMode.PAPER,
        limit_price=100.0,
        client_order_id="SCALPING-AAPL-BUY-202603201030",
        bracket_plan=BracketPlan(
            planned_entry_price=100.0,
            planned_stop_loss_price=99.0,
            planned_take_profit_price=102.0,
            planned_quantity=5.0,
            risk_per_share=1.0,
            gross_reward_per_share=2.0,
            estimated_fees=0.0,
            estimated_slippage=0.0,
            estimated_fee_per_share=0.0,
            estimated_slippage_per_share=0.0,
            estimated_fixed_fees=0.0,
            net_reward_per_share=2.0,
            reward_risk_ratio=2.0,
            expected_net_profit=10.0,
            time_in_force="day",
            exit_reason_metadata={"take_profit": "tp", "stop_loss": "sl"},
        ),
        metadata={"signal_source": "qlib_plus_rules"},
    )


def test_alpaca_paper_broker_preflight_fails_without_credentials(tmp_path) -> None:
    from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker

    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.alpaca_api_key = ""
    settings.broker.alpaca_secret_key = ""

    broker = AlpacaPaperBroker(settings=settings, trading_client_factory=lambda _settings: _FakeTradingClient())

    result = broker.preflight()

    assert not result.ok
    assert "credentials" in result.message.lower()


def test_alpaca_paper_broker_maps_long_bracket_orders_to_alpaca_payload(tmp_path) -> None:
    from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker

    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.alpaca_api_key = "key"
    settings.broker.alpaca_secret_key = "secret"
    fake_client = _FakeTradingClient()

    broker = AlpacaPaperBroker(settings=settings, trading_client_factory=lambda _settings: fake_client)

    broker.submit_order(_bracket_request())

    submitted = fake_client.submitted[0]
    assert submitted.client_order_id == "SCALPING-AAPL-BUY-202603201030"
    assert submitted.order_class.value == "bracket"
    assert submitted.take_profit.limit_price == 102.0
    assert submitted.stop_loss.stop_price == 99.0


def test_alpaca_paper_broker_rounds_bracket_prices_to_valid_penny_increments(tmp_path) -> None:
    from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker

    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.alpaca_api_key = "key"
    settings.broker.alpaca_secret_key = "secret"
    fake_client = _FakeTradingClient()
    broker = AlpacaPaperBroker(settings=settings, trading_client_factory=lambda _settings: fake_client)
    request = _bracket_request().model_copy(deep=True)
    request.limit_price = 208.76
    request.bracket_plan = request.bracket_plan.model_copy(
        update={
            "planned_entry_price": 208.76,
            "planned_stop_loss_price": 207.8902,
            "planned_take_profit_price": 210.3257,
        }
    )

    broker.submit_order(request)

    submitted = fake_client.submitted[0]
    assert submitted.take_profit.limit_price == 210.33
    assert submitted.stop_loss.stop_price == 207.89


def test_alpaca_paper_broker_reconciliation_keeps_bot_owned_and_foreign_state_separate(tmp_path) -> None:
    from mytradingbot.brokers.alpaca_paper import AlpacaPaperBroker
    from mytradingbot.runtime.store import RuntimeStateStore

    settings = AppSettings(paths=RepoPaths.for_root(tmp_path))
    settings.broker.alpaca_api_key = "key"
    settings.broker.alpaca_secret_key = "secret"
    fake_client = _FakeTradingClient()
    fake_client.orders = [
        SimpleNamespace(
            id="bot-parent",
            client_order_id="SCALPING-AAPL-BUY-202603201030",
            symbol="AAPL",
            side=SimpleNamespace(value="buy"),
            qty="5",
            filled_qty="5",
            filled_avg_price="100.0",
            status=SimpleNamespace(value="filled"),
            submitted_at=datetime(2026, 3, 20, 10, 30, tzinfo=timezone.utc),
            filled_at=datetime(2026, 3, 20, 10, 30, tzinfo=timezone.utc),
            order_class=SimpleNamespace(value="bracket"),
            limit_price=None,
            stop_price=None,
            legs=[],
        )
    ]
    fake_client.positions = [
        SimpleNamespace(
            symbol="MSFT",
            qty="10",
            avg_entry_price="250.0",
            current_price="255.0",
            unrealized_pl="50.0",
        )
    ]

    store = RuntimeStateStore(settings=settings)
    broker = AlpacaPaperBroker(
        settings=settings,
        runtime_store=store,
        trading_client_factory=lambda _settings: fake_client,
    )

    snapshot = broker.reconcile_runtime_state(strategy_name="scalping")

    assert snapshot.bot_owned_order_count == 1
    assert snapshot.foreign_position_count == 1
    assert store.list_order_records()[0].client_order_id == "SCALPING-AAPL-BUY-202603201030"
    assert store.list_observed_positions()[0].ownership_class == "foreign"
