from __future__ import annotations

from pathlib import Path

from mytradingbot.orchestration.service import TradingPlatformService


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    service = TradingPlatformService.bootstrap_default()
    payload = {
        "import_ok": True,
        "strategies": service.get_strategy_names(),
        "pages_present": (project_root / "app/pages/01_Dashboard.py").exists(),
        "live_trading_enabled": service.settings.runtime.live_trading_enabled,
    }
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
