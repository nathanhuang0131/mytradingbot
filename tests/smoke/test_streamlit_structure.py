from pathlib import Path


def test_streamlit_page_files_exist() -> None:
    project_root = Path(__file__).resolve().parents[2]
    required = [
        "app/app.py",
        "app/pages/01_Dashboard.py",
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
