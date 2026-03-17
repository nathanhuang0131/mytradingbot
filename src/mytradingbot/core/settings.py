"""Application settings and repo-aware defaults."""

from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from mytradingbot.core.enums import RuntimeMode, StrategyName
from mytradingbot.core.paths import RepoPaths


class RuntimeSettings(BaseModel):
    """Runtime mode and operator behavior defaults."""

    default_mode: RuntimeMode = RuntimeMode.PAPER
    live_trading_enabled: bool = False


class StrategySettings(BaseModel):
    """Canonical strategy availability and defaults."""

    default_strategy: StrategyName = StrategyName.SCALPING
    available: list[str] = Field(
        default_factory=lambda: [strategy.value for strategy in StrategyName]
    )


class BrokerSettings(BaseModel):
    """Broker-related runtime settings."""

    alpaca_api_key: str = ""
    alpaca_secret_key: str = ""
    alpaca_base_url: str = "https://paper-api.alpaca.markets"


class LLMSettings(BaseModel):
    """Optional LLM client configuration."""

    openai_api_key: str = ""
    enabled: bool = False


class LoggingSettings(BaseModel):
    """Logging defaults."""

    level: str = "INFO"


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
    llm: LLMSettings = LLMSettings()
    logging: LoggingSettings = LoggingSettings()
    paths: RepoPaths = Field(default_factory=RepoPaths.discover)
    environment_name: str = "development"

    def prediction_artifact_path(self) -> Path:
        """Return the default runtime predictions artifact location."""

        return self.paths.models_dir / "predictions" / "latest.json"

    def ensure_runtime_directories(self) -> None:
        """Create runtime directories used by the platform."""

        self.paths.ensure_runtime_directories()
