from pathlib import Path


def test_streamlit_page_files_exist() -> None:
    project_root = Path(__file__).resolve().parents[2]
    required = [
        "app/app.py",
        "app/pages/00_Setup_Wizard.py",
        "app/pages/02_Strategy_Control.py",
        "app/pages/03_Data_Management.py",
        "app/pages/05_Live_Trading.py",
        "app/pages/06_LLM_Copilot.py",
        "app/pages/07_Diagnostics.py",
        "app/pages/08_Status_Reference.py",
        "app/pages/09_Trading_Universe.py",
    ]

    for relative_path in required:
        assert (project_root / relative_path).exists(), relative_path

    assert not (project_root / "app/pages/01_Dashboard.py").exists()


def test_streamlit_entrypoints_do_not_use_package_shadowed_runtime_imports() -> None:
    project_root = Path(__file__).resolve().parents[2]
    entrypoints = [
        "app/app.py",
        "app/pages/00_Setup_Wizard.py",
        "app/pages/02_Strategy_Control.py",
        "app/pages/03_Data_Management.py",
        "app/pages/05_Live_Trading.py",
        "app/pages/06_LLM_Copilot.py",
        "app/pages/07_Diagnostics.py",
        "app/pages/08_Status_Reference.py",
        "app/pages/09_Trading_Universe.py",
    ]

    for relative_path in entrypoints:
        source = (project_root / relative_path).read_text(encoding="utf-8")
        assert "from app.components.runtime import" not in source, relative_path


def test_streamlit_app_landing_page_is_dashboard() -> None:
    project_root = Path(__file__).resolve().parents[2]
    source = (project_root / "app/app.py").read_text(encoding="utf-8")

    assert 'st.set_page_config(page_title="Dashboard Summary"' in source
    assert 'st.title("Dashboard Summary")' in source


def test_data_management_page_uses_real_operation_tabs() -> None:
    project_root = Path(__file__).resolve().parents[2]
    source = (project_root / "app/pages/03_Data_Management.py").read_text(encoding="utf-8")

    assert 'st.title("Data Management")' in source
    assert "st.tabs(" in source
    assert '"Universe file path"' in source
    assert "service.resolve_universe_source(" in source
    assert "active_universes" in source
    assert "service.generate_top_liquidity_universe()" in source
    assert "service.download_market_data(" in source
    assert "service.update_market_data(" in source
    assert "service.build_dataset(" in source
    assert "service.train_models(" in source
    assert "service.refresh_predictions(" in source
    assert "service.check_training_data_quality(" in source
    assert "service.run_alpha_robust_training(" in source
    assert "Market Data Progress" in source
    assert "Per-Timeframe Progress" in source
    assert "Remaining Steps" in source
    assert "service.create_market_data_progress_tracker(" in source
    assert "service.get_market_data_progress()" in source
