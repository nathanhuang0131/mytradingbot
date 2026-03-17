from __future__ import annotations

from mytradingbot.brokers.alpaca import AlpacaBrokerScaffold


def main() -> int:
    result = AlpacaBrokerScaffold().get_live_capability_status()
    print(result.model_dump_json(indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
