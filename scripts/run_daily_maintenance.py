from __future__ import annotations

from mytradingbot.orchestration.service import TradingPlatformService


def main() -> int:
    service = TradingPlatformService.bootstrap_default()
    payload = {
        "prediction_status": service.get_prediction_status().model_dump(mode="json"),
        "refresh_result": service.refresh_predictions().model_dump(mode="json"),
    }
    print(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
