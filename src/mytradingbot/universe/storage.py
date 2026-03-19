"""Repo-local universe artifact persistence and symbol-file loading."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from mytradingbot.core.settings import AppSettings
from mytradingbot.universe.models import UniverseLiquidityRow


class UniverseStorage:
    """Write and read universe artifacts under repo-local storage."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()
        self.settings.ensure_runtime_directories()

    def write(self, *, rows: list[UniverseLiquidityRow], output_prefix: str) -> list[str]:
        top_n = len(rows)
        universe_dir = self.settings.paths.universe_dir
        report_dir = self.settings.paths.reports_universe_dir
        universe_dir.mkdir(parents=True, exist_ok=True)
        report_dir.mkdir(parents=True, exist_ok=True)

        versioned_json = universe_dir / f"{output_prefix}_{top_n}.json"
        versioned_csv = universe_dir / f"{output_prefix}_{top_n}.csv"
        latest_json = universe_dir / f"latest_{output_prefix}.json"
        report_path = report_dir / f"{output_prefix}_report.md"

        payload = [row.model_dump(mode="json") for row in rows]
        versioned_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        latest_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        self._write_csv(rows, versioned_csv)
        report_path.write_text(self._render_markdown(rows), encoding="utf-8")
        return [str(versioned_json), str(versioned_csv), str(latest_json), str(report_path)]

    def load_symbols(self, path: Path) -> list[str]:
        suffix = path.suffix.lower()
        if suffix == ".json":
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
            if isinstance(payload, list):
                return [self._extract_symbol(item) for item in payload if self._extract_symbol(item)]
            raise ValueError(f"Unsupported symbols JSON payload in {path}")
        if suffix == ".csv":
            with path.open("r", encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                return [
                    row["symbol"].strip().upper()
                    for row in reader
                    if row.get("symbol") and row["symbol"].strip()
                ]
        raise ValueError(f"Unsupported symbols file format: {path.suffix}")

    @staticmethod
    def _extract_symbol(item) -> str | None:
        if isinstance(item, str):
            return item.strip().upper()
        if isinstance(item, dict):
            symbol = item.get("symbol")
            if isinstance(symbol, str) and symbol.strip():
                return symbol.strip().upper()
        return None

    @staticmethod
    def _write_csv(rows: list[UniverseLiquidityRow], path: Path) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0].model_dump(mode="json").keys()) if rows else ["symbol"])
            writer.writeheader()
            for row in rows:
                writer.writerow(row.model_dump(mode="json"))

    @staticmethod
    def _render_markdown(rows: list[UniverseLiquidityRow]) -> str:
        lines = [
            "# Top Liquidity Universe Report",
            "",
            f"- selected symbols: `{len(rows)}`",
            "",
            "| Rank | Symbol | Avg Close | Avg Volume | Avg Dollar Volume |",
            "| --- | --- | ---: | ---: | ---: |",
        ]
        for row in rows[:20]:
            lines.append(
                f"| {row.rank} | {row.symbol} | {row.avg_close:.2f} | {row.avg_volume:,.0f} | {row.avg_dollar_volume:,.2f} |"
            )
        return "\n".join(lines) + "\n"
