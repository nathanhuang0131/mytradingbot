from mytradingbot.core.settings import AppSettings


def test_default_mode_is_paper() -> None:
    settings = AppSettings()
    assert settings.runtime.default_mode.value == "paper"


def test_strategy_names_are_canonical() -> None:
    settings = AppSettings()
    assert settings.strategies.available == [
        "scalping",
        "intraday",
        "short_term",
        "long_term",
    ]


def test_repo_local_pipeline_paths_stay_under_repo_root() -> None:
    settings = AppSettings()

    assert settings.paths.raw_data_dir.is_relative_to(settings.paths.repo_root)
    assert settings.paths.normalized_data_dir.is_relative_to(settings.paths.repo_root)
    assert settings.paths.snapshots_dir.is_relative_to(settings.paths.repo_root)
    assert settings.paths.qlib_dir.is_relative_to(settings.paths.repo_root)
    assert settings.paths.runtime_dir.is_relative_to(settings.paths.repo_root)


def test_data_pipeline_defaults_include_minute_timeframes() -> None:
    settings = AppSettings()

    assert settings.data.default_timeframes == ["1m", "5m", "15m", "1d"]
    assert settings.data.request_page_limit >= 1000
    assert settings.data.request_concurrency >= 1
    assert settings.data.processing_workers >= 1


def test_scalping_runtime_defaults_align_with_overnight_tuning_pass() -> None:
    settings = AppSettings()

    assert settings.runtime_safety.prediction_refresh_interval_seconds == 600
    assert settings.scalping.predicted_return_threshold == 0.0008
    assert settings.scalping.confidence_threshold == 0.6
    assert settings.scalping.cooldown_minutes == 10
    assert settings.scalping.top_n_per_cycle == 3
    assert settings.scalping.edge_after_cost_min_buffer == 0.0005
    assert settings.scalping.higher_timeframe_filter_enabled is True
    assert settings.scalping.higher_timeframe_source_timeframe == "15m"
    assert settings.scalping.higher_timeframe_fast_ma_length == 5
    assert settings.scalping.higher_timeframe_slow_ma_length == 10
    assert settings.scalping.enable_pseudo_order_book_gate is False


def test_flat_env_aliases_load_broker_credentials(monkeypatch) -> None:
    monkeypatch.setenv("ALPACA_API_KEY", "key")
    monkeypatch.setenv("ALPACA_SECRET_KEY", "secret")

    settings = AppSettings()

    assert settings.broker.alpaca_api_key == "key"
    assert settings.broker.alpaca_secret_key == "secret"


def test_dotenv_flat_aliases_load_broker_credentials(tmp_path, monkeypatch) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "ALPACA_API_KEY=key_from_file\nALPACA_SECRET_KEY=secret_from_file\n",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)

    settings = AppSettings()

    assert settings.broker.alpaca_api_key == "key_from_file"
    assert settings.broker.alpaca_secret_key == "secret_from_file"
