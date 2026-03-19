from __future__ import annotations

from pathlib import Path

from mytradingbot.orchestration.service import TradingPlatformService


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    service = TradingPlatformService.bootstrap_default()
    capabilities = service.get_capabilities()
    payload = {
        "import_ok": True,
        "strategies": service.get_strategy_names(),
        "pages_present": (project_root / "app/pages/01_Dashboard.py").exists(),
        "live_trading_enabled": service.settings.runtime.live_trading_enabled,
        "institutional_pipeline_present": (project_root / "scripts/run_institutional_pipeline.py").exists(),
        "alpha_training_present": (project_root / "scripts/run_alpha_robust_training.py").exists(),
        "universe_generator_present": (project_root / "scripts/generate_top_liquidity_universe.py").exists(),
        "runtime_state_store_path": str(
            service.settings.paths.state_dir / service.settings.runtime_safety.sqlite_filename
        ),
        "phase_1_status": capabilities.phase_1.status,
        "phase_2_status": capabilities.phase_2.status,
        "phase_3_status": capabilities.phase_3.status,
        "phase_4_status": capabilities.phase_4.status,
    }
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
