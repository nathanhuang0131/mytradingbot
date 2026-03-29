# Smarter Selection Upgrade Implementation Plan

## Goal

Upgrade the overnight scalping paper-trading path so trade approval is driven by smarter quality selection instead of threshold-only acceptance. The upgraded path must preserve restart safety, paper-trading correctness, cooldown discipline, bracket expectancy checks, and deterministic auditability.

## Locked Decisions

- Keep predicted return threshold, stop loss, and take profit user-configurable rather than hard-wiring new trading values in this pass.
- Preserve the existing hard execution guards: spread, liquidity, liquidity stress, cooldown, duplicate-position protection, flatten-near-close, bracket expectancy, and fee/slippage-aware validation.
- Add a directional higher-timeframe confirmation filter using existing normalized bars rather than fabricated L2 equity order-book logic.
- Treat the current pseudo order-book signal honestly as a legacy microstructure proxy and keep it disabled as a hard gate by default.
- Add a deterministic top-N selection stage after strategy hard-filter evaluation so the session only routes the best eligible candidates.
- Extend runtime audits and analytics instead of creating a second parallel reporting stack.

## Design

### 1. Typed signal-quality artifacts

Add explicit typed models for:

- higher-timeframe trend state
- per-candidate cost estimate
- per-candidate quality breakdown

These models should be attached to strategy decisions so runtime audit code can log them without parsing free-form notes.

### 2. Higher-timeframe trend computation

Compute a reusable higher-timeframe trend snapshot from existing normalized bars:

- source timeframe default: `15m`
- fast EMA default: `5`
- slow EMA default: `10`
- bullish alignment requires:
  - close at or above higher-timeframe VWAP
  - fast EMA at or above slow EMA
  - slow EMA slope non-negative
- bearish alignment mirrors the bullish conditions

The result should be stored on the market snapshot so the strategy, ranking layer, and reports all share one deterministic view.

### 3. Cost-aware edge gate

For each candidate, compute:

- directional predicted return magnitude
- spread proxy cost
- configured slippage cost
- configured fee-per-share contribution
- lightweight regulatory fee hook from broker fee settings
- expected edge after cost

Candidates must clear a configurable minimum edge-after-cost buffer before they remain eligible.

### 4. Composite ranking and top-N selector

Keep hard filter evaluation inside the strategy, then rank only eligible candidates per cycle using an explicit composite quality score that combines:

- predicted return strength
- confidence surrogate
- edge after cost
- spread quality
- liquidity quality
- higher-timeframe alignment
- bracket reward/risk quality

The selector must:

- rank deterministically with stable tie-breakers
- apply `top_n_per_cycle`
- respect open-position slot limits when a session config is available
- mark rejected-but-otherwise-eligible candidates with a precise top-N rejection reason

### 5. Reporting and analytics

Extend decision audits, session analytics CSV/markdown, and overnight trading-universe reports so operators can see:

- cost inputs and edge-after-cost
- higher-timeframe state
- quality score and selection rank
- top-N selection outcomes
- repeated trend-alignment blockers
- positive-return but negative-edge names

## Planned File Areas

- `src/mytradingbot/core/`
- `src/mytradingbot/data/`
- `src/mytradingbot/strategies/`
- `src/mytradingbot/orchestration/`
- `src/mytradingbot/runtime/`
- `src/mytradingbot/session_setup/`
- `src/mytradingbot/ui_services/`
- `app/pages/`
- `docs/`
- `tests/`

## Verification

- Focused unit tests for trend alignment, edge-after-cost, top-N selection, config wiring, and reporting
- Focused integration test for candidate ranking -> selection -> approval/rejection
- Canonical validation:
  - `PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q`
  - `python scripts/validate_system.py`
  - `python scripts/goalcheck.py`
