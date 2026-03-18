"""Application settings and repo-aware defaults."""

from __future__ import annotations

import os
from pathlib import Path

from pydantic import AliasChoices, BaseModel, Field, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import dotenv_values

from mytradingbot.core.enums import RuntimeMode, StrategyName
from mytradingbot.core.paths import RepoPaths


class RuntimeSettings(BaseModel):
    """Runtime mode and operator behavior defaults."""

    default_mode: RuntimeMode = Field(
        default=RuntimeMode.PAPER,
        validation_alias=AliasChoices("RUNTIME__DEFAULT_MODE", "DEFAULT_MODE"),
    )
    live_trading_enabled: bool = Field(
        default=False,
        validation_alias=AliasChoices(
            "RUNTIME__LIVE_TRADING_ENABLED",
            "LIVE_TRADING_ENABLED",
        ),
    )


class StrategySettings(BaseModel):
    """Canonical strategy availability and defaults."""

    default_strategy: StrategyName = StrategyName.SCALPING
    available: list[str] = Field(
        default_factory=lambda: [strategy.value for strategy in StrategyName]
    )


class BrokerSettings(BaseModel):
    """Broker-related runtime settings."""

    alpaca_api_key: str = Field(
        default="",
        validation_alias=AliasChoices("BROKER__ALPACA_API_KEY", "ALPACA_API_KEY"),
    )
    alpaca_secret_key: str = Field(
        default="",
        validation_alias=AliasChoices("BROKER__ALPACA_SECRET_KEY", "ALPACA_SECRET_KEY"),
    )
    alpaca_base_url: str = Field(
        default="https://paper-api.alpaca.markets",
        validation_alias=AliasChoices("BROKER__ALPACA_BASE_URL", "ALPACA_BASE_URL"),
    )
    alpaca_data_feed: str = Field(
        default="iex",
        validation_alias=AliasChoices("BROKER__ALPACA_DATA_FEED", "ALPACA_DATA_FEED"),
    )
    alpaca_adjustment: str = Field(
        default="raw",
        validation_alias=AliasChoices("BROKER__ALPACA_ADJUSTMENT", "ALPACA_ADJUSTMENT"),
    )


class DataPipelineSettings(BaseModel):
    """Repo-local market data pipeline settings."""

    default_provider: str = "alpaca"
    default_timeframes: list[str] = Field(
        default_factory=lambda: ["1m", "5m", "15m", "1d"]
    )
    batch_size: int = 100
    request_page_limit: int = 10_000
    request_concurrency: int = 2
    retry_count: int = 3
    retry_backoff_seconds: float = 1.0
    request_throttle_seconds: float = 0.25
    processing_workers: int = 1
    parquet_compression: str = "snappy"
    symbol_chunk_size: int = 50
    qlib_symbol_chunk_size: int = 25
    qlib_prediction_chunk_size: int = 25
    snapshot_timeframe: str = "1m"
    incremental_overlap_minutes: int = 5
    scalping_lookback_bars: int = 30
    default_symbols: list[str] = Field(default_factory=lambda: ["AAPL", "MSFT", "NVDA"])


class QlibSettings(BaseModel):
    """Qlib workflow defaults."""

    label_horizon_bars: int = 5
    train_ratio: float = 0.7
    validation_ratio: float = 0.15
    prediction_top_k: int = 20
    handler_artifact_name: str = "handler.pkl"
    model_artifact_name: str = "model.pkl"
    dataset_artifact_name: str = "dataset.parquet"


class ScalpingBracketSettings(BaseModel):
    """Bracket-planning controls for scalping."""

    minimum_reward_risk_ratio: float = 1.4
    estimated_slippage_bps: float = 2.5
    estimated_fee_per_share: float = 0.0
    estimated_fixed_fees: float = 0.0
    minimum_net_reward_per_share: float = 0.01
    max_holding_seconds: int = 900
    stop_loss_buffer_bps: float = 20.0
    take_profit_multiplier: float = 1.8
    whole_share_required_for_alpaca_brackets: bool = True
    risk_budget_per_trade: float = 25.0
    max_position_notional: float = 5_000.0


class LLMSettings(BaseModel):
    """Optional LLM client configuration."""

    openai_api_key: str = Field(
        default="",
        validation_alias=AliasChoices("LLM__OPENAI_API_KEY", "OPENAI_API_KEY"),
    )
    enabled: bool = Field(
        default=False,
        validation_alias=AliasChoices("LLM__ENABLED", "LLM_ENABLED"),
    )


class LoggingSettings(BaseModel):
    """Logging defaults."""

    level: str = Field(
        default="INFO",
        validation_alias=AliasChoices("LOGGING__LEVEL", "LOG_LEVEL"),
    )


class AppSettings(BaseSettings):
    """Root application settings loaded from environment variables and defaults."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    runtime: RuntimeSettings = RuntimeSettings()
    strategies: StrategySettings = StrategySettings()
    broker: BrokerSettings = BrokerSettings()
    data: DataPipelineSettings = DataPipelineSettings()
    qlib: QlibSettings = QlibSettings()
    scalping: ScalpingBracketSettings = ScalpingBracketSettings()
    llm: LLMSettings = LLMSettings()
    logging: LoggingSettings = LoggingSettings()
    paths: RepoPaths = Field(default_factory=RepoPaths.discover)
    environment_name: str = "development"

    @model_validator(mode="before")
    @classmethod
    def apply_flat_env_aliases(cls, data):
        payload = dict(data or {})
        file_values = _load_dotenv_values(payload.get("_env_file"))
        runtime = dict(payload.get("runtime", {}))
        broker = dict(payload.get("broker", {}))
        llm = dict(payload.get("llm", {}))
        logging_settings = dict(payload.get("logging", {}))

        runtime.setdefault(
            "default_mode",
            _first_available("DEFAULT_MODE", file_values=file_values, fallback=runtime.get("default_mode")),
        )
        runtime.setdefault(
            "live_trading_enabled",
            _first_available(
                "LIVE_TRADING_ENABLED",
                file_values=file_values,
                fallback=runtime.get("live_trading_enabled"),
            ),
        )
        broker.setdefault(
            "alpaca_api_key",
            _first_available("ALPACA_API_KEY", file_values=file_values, fallback=broker.get("alpaca_api_key")),
        )
        broker.setdefault(
            "alpaca_secret_key",
            _first_available(
                "ALPACA_SECRET_KEY",
                file_values=file_values,
                fallback=broker.get("alpaca_secret_key"),
            ),
        )
        broker.setdefault(
            "alpaca_base_url",
            _first_available(
                "ALPACA_BASE_URL",
                file_values=file_values,
                fallback=broker.get("alpaca_base_url"),
            ),
        )
        broker.setdefault(
            "alpaca_data_feed",
            _first_available(
                "ALPACA_DATA_FEED",
                file_values=file_values,
                fallback=broker.get("alpaca_data_feed"),
            ),
        )
        broker.setdefault(
            "alpaca_adjustment",
            _first_available(
                "ALPACA_ADJUSTMENT",
                file_values=file_values,
                fallback=broker.get("alpaca_adjustment"),
            ),
        )
        llm.setdefault(
            "openai_api_key",
            _first_available("OPENAI_API_KEY", file_values=file_values, fallback=llm.get("openai_api_key")),
        )
        llm.setdefault(
            "enabled",
            _first_available("LLM_ENABLED", file_values=file_values, fallback=llm.get("enabled")),
        )
        logging_settings.setdefault(
            "level",
            _first_available("LOG_LEVEL", file_values=file_values, fallback=logging_settings.get("level")),
        )

        payload["runtime"] = runtime
        payload["broker"] = broker
        payload["llm"] = llm
        payload["logging"] = logging_settings
        return payload

    def prediction_artifact_path(self) -> Path:
        """Return the default runtime predictions artifact location."""

        return self.paths.models_dir / "predictions" / "latest.json"

    def market_snapshot_artifact_path(self) -> Path:
        """Return the default market snapshot artifact location."""

        return self.paths.snapshots_dir / "market_snapshot.json"

    def qlib_dataset_artifact_path(self) -> Path:
        """Return the default qlib-ready dataset artifact location."""

        return self.paths.qlib_dir / self.qlib.dataset_artifact_name

    def qlib_model_artifact_path(self) -> Path:
        """Return the default trained qlib model artifact location."""

        return self.paths.models_dir / "qlib" / self.qlib.model_artifact_name

    def ensure_runtime_directories(self) -> None:
        """Create runtime directories used by the platform."""

        self.paths.ensure_runtime_directories()

    def model_post_init(self, __context) -> None:
        file_values = _load_dotenv_values(None)
        default_mode = _first_available("DEFAULT_MODE", file_values=file_values, fallback=None)
        if default_mode:
            self.runtime.default_mode = RuntimeMode(default_mode)
        self.runtime.live_trading_enabled = _coalesce_bool(
            self.runtime.live_trading_enabled,
            _first_available("LIVE_TRADING_ENABLED", file_values=file_values, fallback=None),
        )
        self.broker.alpaca_api_key = self.broker.alpaca_api_key or (
            _first_available("ALPACA_API_KEY", file_values=file_values, fallback="") or ""
        )
        self.broker.alpaca_secret_key = self.broker.alpaca_secret_key or (
            _first_available("ALPACA_SECRET_KEY", file_values=file_values, fallback="") or ""
        )
        self.broker.alpaca_base_url = self.broker.alpaca_base_url or (
            _first_available(
                "ALPACA_BASE_URL",
                file_values=file_values,
                fallback=self.broker.alpaca_base_url,
            )
            or self.broker.alpaca_base_url
        )
        self.broker.alpaca_data_feed = self.broker.alpaca_data_feed or (
            _first_available(
                "ALPACA_DATA_FEED",
                file_values=file_values,
                fallback=self.broker.alpaca_data_feed,
            )
            or self.broker.alpaca_data_feed
        )
        self.broker.alpaca_adjustment = self.broker.alpaca_adjustment or (
            _first_available(
                "ALPACA_ADJUSTMENT",
                file_values=file_values,
                fallback=self.broker.alpaca_adjustment,
            )
            or self.broker.alpaca_adjustment
        )
        self.llm.openai_api_key = self.llm.openai_api_key or (
            _first_available("OPENAI_API_KEY", file_values=file_values, fallback="") or ""
        )
        self.llm.enabled = _coalesce_bool(
            self.llm.enabled,
            _first_available("LLM_ENABLED", file_values=file_values, fallback=None),
        )
        self.logging.level = self.logging.level or (
            _first_available("LOG_LEVEL", file_values=file_values, fallback="INFO") or "INFO"
        )


def _coalesce_bool(current: bool, raw_value: str | bool | None) -> bool:
    if raw_value is None or isinstance(raw_value, bool):
        return current if raw_value is None else raw_value
    return raw_value.lower() in {"1", "true", "yes", "on"}


def _load_dotenv_values(env_file: str | os.PathLike[str] | None) -> dict[str, str]:
    if env_file is None:
        env_path = Path(".env")
    else:
        env_path = Path(env_file)
    if not env_path.exists():
        return {}
    return {
        key.strip(): value.strip() if isinstance(value, str) else value
        for key, value in dotenv_values(env_path).items()
        if key
    }


def _first_available(
    key: str,
    *,
    file_values: dict[str, str],
    fallback: str | bool | None,
) -> str | bool | None:
    env_value = os.getenv(key)
    if env_value not in (None, ""):
        return env_value
    file_value = file_values.get(key)
    if file_value not in (None, ""):
        return file_value
    return fallback
