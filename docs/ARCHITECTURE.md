# Architecture

## Overview

This platform is a qlib-first, dashboard-first quant trading system built around a phase-1 paper-trading vertical slice.

The implemented runtime flow is:

`prediction artifact -> signal bundle -> strategy decision -> trade intent -> risk decision -> execution request -> broker result -> diagnostics/reporting`

## Core Guarantees

- qlib remains the authority for direction and ranking
- LLM output is advisory only
- paper mode is the default operational path
- live trading is visible but validation-only in phase 1
- missing or stale prediction artifacts fail clearly
- strategies never call broker adapters directly
- Streamlit pages call `ui_services/`, not backend internals

## Layers

### `core`

Repository-aware settings, enums, paths, exceptions, and shared typed runtime models.

### `data`

Runtime market snapshot loading and signal-bundle assembly.

### `qlib_engine`

Adapter-based qlib availability checks, dataset and training scaffolding, prediction refresh scaffolding, artifact freshness inspection, and runtime prediction loading.

### `signals`

Typed signal-layer exports for qlib predictions, market context, trade intents, and strategy decisions.

### `strategies`

Canonical strategy registry plus implementations for `scalping`, `intraday`, `short_term`, and `long_term`.

`scalping` includes modular qlib gating, thresholds, microstructure filters, cooldown logic, flatten-near-close logic, adaptive sizing, and exit-plan generation.

### `risk`

Risk approvals and rejections, including the explicit phase-1 live-mode hard block.

### `execution`

Execution request creation, dry-run skipping, and broker routing.

### `brokers`

An in-memory paper broker for the phase-1 operational path and an Alpaca scaffold that exposes live capability status without submitting real live orders.

### `orchestration`

End-to-end paper and dry-run session coordination, plus qlib maintenance entrypoints.

### `diagnostics`

Prediction health, stale-artifact diagnostics, and no-trade explanations.

### `reporting`

Post-session review construction from real session artifacts.

### `llm`

Advisory-only workflows for signal explanation, diagnostics summaries, strategy comparison, post-market review, export packs, and structured feedback import.

### `ui_services`

Thin application services that prepare payloads for the Streamlit dashboard pages.
