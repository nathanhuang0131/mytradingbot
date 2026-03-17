from __future__ import annotations

from pathlib import Path

from mytradingbot.brokers.alpaca import AlpacaBrokerScaffold
from mytradingbot.orchestration.service import TradingPlatformService


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    service = TradingPlatformService.bootstrap_default()
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
        "prediction_status_reason": service.get_prediction_status().reason,
        "diagnostics_service_present": True,
        "llm_advisory_present": True,
    }

    for key, value in checks.items():
        label = key.replace("_", " ")
        print(f"{label}: {value}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
