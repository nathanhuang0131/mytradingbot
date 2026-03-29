# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| UUUU | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9900 | -0.0007 | 4.96 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| ARM | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 1.64 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FIVN | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| AMKR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T18:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ZSL | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| ONDS | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| MU | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.31 | 0.59 | True | None | predicted_return_threshold |
| BBWI | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9891 | 0.0001 | 1.48 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| FSM | 2026-03-27T18:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 1.33 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SMTC | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 0.50 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| U | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 3.32 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AXIA | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 4.69 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| ADMA | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 23.05 | 0.65 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| SNOW | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 3.21 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| COHR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 1.03 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BRKR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| KTOS | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| BSY | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 2.15 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AJG | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.60 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FNGU | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 3.48 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| LUNR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 4.87 | 0.82 | False | None | predicted_return_threshold, vwap_relationship |
| ACHC | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| IOT | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| QURE | 2026-03-27T18:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 8.38 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| OTIS | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.65 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| TECK | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| NTLA | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| ODD | 2026-03-27T18:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| CSTM | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| WRBY | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 1.23 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| IONQ | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 4.98 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 2.31 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SYY | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9586 | -0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| TPG | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| SNDK | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| DNLI | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HMY | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| BX | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.58 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CIEN | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9501 | -0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| CTSH | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| CCJ | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| QBTS | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 5.44 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ABT | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 2.15 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| SCCO | 2026-03-27T18:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| LAZ | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 4.42 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| PANW | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| VITL | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| SE | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| M | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9380 | 0.0000 | 1.40 | 0.73 | False | None | predicted_return_threshold, vwap_relationship |
| ARIS | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9367 | 0.0000 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| CC | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9355 | 0.0000 | 2.34 | 0.59 | False | None | predicted_return_threshold, vwap_relationship |
| FSLY | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9343 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| PGNY | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9331 | 0.0000 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| MIR | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9319 | 0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9307 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SAIL | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9294 | 0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| PBF | 2026-03-27T18:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9282 | 0.0000 | 3.17 | 0.03 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PINS | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9270 | 0.0000 | 2.82 | 0.83 | False | None | predicted_return_threshold, vwap_relationship |
| BRZE | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9258 | 0.0000 | 2.20 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| RKLB | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9246 | 0.0000 | 1.44 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| BJ | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9234 | -0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SCO | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9221 | 0.0000 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| DDOG | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| CIFR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| NVT | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| MEOH | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9161 | -0.0000 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| EXLS | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9148 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| GLDM | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| VIAV | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 0.72 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CME | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 1.36 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PCAR | 2026-03-27T18:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9100 | -0.0000 | 0.50 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NET | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| TSCO | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9075 | 0.0000 | 2.23 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DOCN | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 3.41 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| TXG | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9051 | -0.0000 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| OKTA | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| YPF | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9027 | -0.0000 | 3.89 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TENB | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 9.11 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| AEM | 2026-03-27T18:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| OTEX | 2026-03-27T18:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8990 | -0.0000 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| CGAU | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| WAY | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| VNET | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 2.99 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CAI | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| LITE | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.50 | 0.50 | True | None | predicted_return_threshold, liquidity_filter |
| EXK | 2026-03-27T18:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 1.41 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NXE | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.59 | True | None | predicted_return_threshold |
| ELV | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 1.62 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| ANET | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 1.24 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| MKSI | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8856 | -0.0000 | 2.61 | 0.74 | False | None | predicted_return_threshold, vwap_relationship |
| W | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 2.29 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SW | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 1.27 | 0.40 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CX | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| AMT | 2026-03-27T19:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8808 | -0.0000 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| BMNR | 2026-03-27T19:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 5.45 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
