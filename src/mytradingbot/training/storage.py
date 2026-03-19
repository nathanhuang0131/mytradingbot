"""Artifact writers for training quality and robust training summaries."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from mytradingbot.core.settings import AppSettings
from mytradingbot.training.models import AlphaTrainingRunResult, TrainingDataQualityReport


class TrainingArtifactStore:
    """Persist training quality and manifest artifacts under repo-local storage."""

    def __init__(self, settings: AppSettings | None = None) -> None:
        self.settings = settings or AppSettings()
        self.settings.ensure_runtime_directories()

    def write_quality_report(self, report: TrainingDataQualityReport) -> list[str]:
        reports_dir = self.settings.paths.reports_training_dir
        reports_dir.mkdir(parents=True, exist_ok=True)
        universe_dir = self.settings.paths.universe_dir
        universe_dir.mkdir(parents=True, exist_ok=True)
        quality_json = reports_dir / "training_data_quality_summary.json"
        quality_md = reports_dir / "training_data_quality_report.md"
        coverage_csv = reports_dir / "timeframe_coverage_summary.csv"
        eligible_json = universe_dir / "latest_training_eligible_universe.json"
        eligible_csv = reports_dir / "training_eligible_universe.csv"

        quality_json.write_text(report.model_dump_json(indent=2), encoding="utf-8")
        quality_md.write_text(self._render_quality_markdown(report), encoding="utf-8")
        self._write_coverage_csv(coverage_csv, report)
        eligible_json.write_text(
            json.dumps([{"symbol": symbol} for symbol in report.eligible_symbols], indent=2),
            encoding="utf-8",
        )
        with eligible_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["symbol"])
            writer.writeheader()
            for symbol in report.eligible_symbols:
                writer.writerow({"symbol": symbol})
        return [str(quality_json), str(quality_md), str(coverage_csv), str(eligible_json), str(eligible_csv)]

    def write_run_summary(self, result: AlphaTrainingRunResult) -> list[str]:
        reports_dir = self.settings.paths.reports_training_dir
        reports_dir.mkdir(parents=True, exist_ok=True)
        registry_dir = self.settings.paths.data_dir / "registry"
        registry_dir.mkdir(parents=True, exist_ok=True)
        summary_md = reports_dir / "robust_training_run_summary.md"
        manifest_json = registry_dir / "latest_training_manifest.json"
        summary_md.write_text(self._render_run_markdown(result), encoding="utf-8")
        manifest_json.write_text(result.model_dump_json(indent=2), encoding="utf-8")
        return [str(summary_md), str(manifest_json)]

    @staticmethod
    def _render_quality_markdown(report: TrainingDataQualityReport) -> str:
        lines = [
            "# Training Data Quality Report",
            "",
            f"- ok: `{report.ok}`",
            f"- requested symbols: `{len(report.requested_symbols)}`",
            f"- eligible symbols: `{len(report.eligible_symbols)}`",
            "",
            "| Timeframe | Passing Symbols | Median Coverage | Lookback Days | Sufficiency |",
            "| --- | ---: | ---: | ---: | --- |",
        ]
        for summary in report.timeframe_summaries:
            lines.append(
                f"| {summary.timeframe} | {summary.symbols_passing_quality} | "
                f"{summary.median_coverage_ratio:.2f} | {summary.lookback_window_days_achieved} | "
                f"{summary.sufficiency_pass} |"
            )
        return "\n".join(lines) + "\n"

    @staticmethod
    def _write_coverage_csv(path: Path, report: TrainingDataQualityReport) -> None:
        with path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "timeframe",
                    "symbol",
                    "row_count",
                    "unique_trading_days",
                    "coverage_ratio",
                    "stale",
                    "schema_ok",
                    "interval_alignment_ok",
                    "passes",
                    "failure_reason",
                ],
            )
            writer.writeheader()
            for summary in report.timeframe_summaries:
                for detail in summary.symbol_details:
                    writer.writerow(
                        {
                            "timeframe": summary.timeframe,
                            "symbol": detail.symbol,
                            "row_count": detail.row_count,
                            "unique_trading_days": detail.unique_trading_days,
                            "coverage_ratio": detail.coverage_ratio,
                            "stale": detail.stale,
                            "schema_ok": detail.schema_ok,
                            "interval_alignment_ok": detail.interval_alignment_ok,
                            "passes": detail.passes,
                            "failure_reason": detail.failure_reason,
                        }
                    )

    @staticmethod
    def _render_run_markdown(result: AlphaTrainingRunResult) -> str:
        return "\n".join(
            [
                "# Robust Training Run Summary",
                "",
                f"- ok: `{result.ok}`",
                f"- build_ok: `{result.build_ok}`",
                f"- train_ok: `{result.train_ok}`",
                f"- refresh_ok: `{result.refresh_ok}`",
                f"- eligible symbols: `{len(result.eligible_symbols)}`",
                "",
                "## Artifacts",
                "",
                *[f"- `{artifact}`" for artifact in result.artifacts],
                "",
                "## Reports",
                "",
                *[f"- `{report}`" for report in result.reports],
            ]
        ) + "\n"
