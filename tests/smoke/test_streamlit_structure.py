from pathlib import Path


def test_streamlit_page_files_exist() -> None:
    project_root = Path(__file__).resolve().parents[2]
    required = [
        "app/app.py",
        "app/pages/00_Setup_Wizard.py",
        "app/pages/02_Strategy_Control.py",
        "app/pages/03_Data_and_Training.py",
        "app/pages/04_Paper_Trading.py",
        "app/pages/05_Live_Trading.py",
        "app/pages/06_LLM_Copilot.py",
        "app/pages/07_Diagnostics.py",
        "app/pages/08_Settings.py",
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
        "app/pages/03_Data_and_Training.py",
        "app/pages/04_Paper_Trading.py",
        "app/pages/05_Live_Trading.py",
        "app/pages/06_LLM_Copilot.py",
        "app/pages/07_Diagnostics.py",
        "app/pages/08_Settings.py",
    ]

    for relative_path in entrypoints:
        source = (project_root / relative_path).read_text(encoding="utf-8")
        assert "from app.components.runtime import" not in source, relative_path


def test_streamlit_app_landing_page_is_dashboard() -> None:
    project_root = Path(__file__).resolve().parents[2]
    source = (project_root / "app/app.py").read_text(encoding="utf-8")

    assert 'st.set_page_config(page_title="Dashboard"' in source
    assert 'st.title("Dashboard")' in source
