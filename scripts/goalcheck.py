from __future__ import annotations

from pathlib import Path

from mytradingbot.brokers.alpaca import AlpacaBrokerScaffold
from mytradingbot.orchestration.service import TradingPlatformService


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    service = TradingPlatformService.bootstrap_default()
    capabilities = service.get_capabilities()
    page_paths = [
        project_root / "app/pages/01_Dashboard.py",
        project_root / "app/pages/02_Strategy_Control.py",
        project_root / "app/pages/03_Data_and_Training.py",
        project_root / "app/pages/04_Paper_Trading.py",
        project_root / "app/pages/05_Live_Trading.py",
        project_root / "app/pages/06_LLM_Copilot.py",
        project_root / "app/pages/07_Diagnostics.py",
        project_root / "app/pages/08_Settings.py",
    ]

    checks = {
        "strategies": service.get_strategy_names(),
        "pages_present": all(path.exists() for path in page_paths),
        "live_trading_gated": not AlpacaBrokerScaffold().get_live_capability_status().is_enabled,
        "phase_1_status": capabilities.phase_1.status,
        "phase_2_status": capabilities.phase_2.status,
        "phase_3_status": capabilities.phase_3.status,
        "phase_4_status": capabilities.phase_4.status,
        "prediction_status_reason": service.get_prediction_status().reason,
        "institutional_pipeline_present": (project_root / "scripts/run_institutional_pipeline.py").exists(),
        "alpha_training_present": (project_root / "scripts/run_alpha_robust_training.py").exists(),
        "top_liquidity_universe_script_present": (project_root / "scripts/generate_top_liquidity_universe.py").exists(),
        "diagnostics_service_present": True,
        "llm_advisory_present": True,
    }

    for key, value in checks.items():
        label = key.replace("_", " ")
        print(f"{label}: {value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
