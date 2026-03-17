from mytradingbot.core.settings import AppSettings


def test_repo_paths_resolve_inside_project() -> None:
    settings = AppSettings()
    assert settings.paths.repo_root.exists()
    assert settings.paths.configs_dir.name == "configs"
    assert settings.paths.src_dir.name == "src"


def test_runtime_artifact_dirs_live_under_repo() -> None:
    settings = AppSettings()
    assert settings.paths.data_dir.parent == settings.paths.repo_root
    assert settings.paths.reports_dir.parent == settings.paths.repo_root
