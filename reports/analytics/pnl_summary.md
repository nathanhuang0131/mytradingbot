# Realized PnL Summary

- closed trades: `2`
- total realized pnl: `0.2600`
- total wins: `1`
- broker_modes_present: `alpaca_paper_api`
- fee_schedule_version: `alpaca_public_schedule_2026-03-20`

- alpaca_paper_api: `Alpaca paper API broker`
- foreign exposure: `2` observed non-bot position snapshots are excluded from bot profitability attribution.
- foreign open orders: `64` read-only broker-account orders are excluded from bot trade attribution.
- profitability scope: by default, only bot-owned closed trades are included in strategy, signal-source, and broker-mode profitability tables.

## By Symbol

| Broker Mode | Value | Trades | Total PnL | Win Rate | Avg Return % |
| --- | --- | ---: | ---: | ---: | ---: |
| alpaca_paper_api | AMZN | 1 | 0.3700 | 100.00% | 0.0225 |
| alpaca_paper_api | RDY | 1 | -0.1100 | 0.00% | -0.8094 |

## By Strategy

| Broker Mode | Value | Trades | Total PnL | Win Rate | Avg Return % |
| --- | --- | ---: | ---: | ---: | ---: |
| alpaca_paper_api | scalping | 2 | 0.2600 | 50.00% | -0.3935 |

## By Signal Source

| Broker Mode | Value | Trades | Total PnL | Win Rate | Avg Return % |
| --- | --- | ---: | ---: | ---: | ---: |
| alpaca_paper_api | qlib_plus_rules | 2 | 0.2600 | 50.00% | -0.3935 |

## By Broker Mode

| Broker Mode | Value | Trades | Total PnL | Win Rate | Avg Return % |
| --- | --- | ---: | ---: | ---: | ---: |
| alpaca_paper_api | alpaca_paper_api | 2 | 0.2600 | 50.00% | -0.3935 |

