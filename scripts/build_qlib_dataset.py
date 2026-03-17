from __future__ import annotations

from mytradingbot.orchestration.service import TradingPlatformService


def main() -> int:
    result = TradingPlatformService.bootstrap_default().build_dataset()
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
