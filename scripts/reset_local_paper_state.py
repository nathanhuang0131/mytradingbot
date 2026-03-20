from __future__ import annotations

import argparse

from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.reset import LocalPaperStateResetService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Archive repo-local local paper runtime state and analytics artifacts."
    )
    parser.add_argument(
        "--yes",
        action="store_true",
        help="Required confirmation flag. Without this, nothing is reset.",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    settings = AppSettings()
    result = LocalPaperStateResetService(settings=settings).reset(confirm=args.yes)
    print(result.model_dump_json(indent=2))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
