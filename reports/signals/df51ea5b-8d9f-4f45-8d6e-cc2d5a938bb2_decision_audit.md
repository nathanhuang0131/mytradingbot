# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| UUUU | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9900 | -0.0007 | 4.95 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ARM | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 4.07 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FIVN | 2026-03-27T18:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 2.60 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BATL | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| AMKR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 1.68 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GLL | 2026-03-27T18:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 1.15 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| ZSL | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ONDS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| MU | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.38 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BBWI | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9891 | 0.0001 | 5.20 | 1.00 | True | None | predicted_return_threshold |
| FSM | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 1.32 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| SMTC | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 17.74 | 0.58 | True | None | predicted_return_threshold, spread_filter, liquidity_sweep_detection |
| U | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 5.34 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| AXIA | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 2.34 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| ADMA | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 10.76 | 0.66 | True | None | predicted_return_threshold, spread_filter |
| SNOW | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| COHR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| BRKR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| KTOS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 1.04 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| BSY | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.79 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| AJG | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 2.76 | 1.00 | True | None | predicted_return_threshold |
| FNGU | 2026-03-27T18:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 5.17 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LUNR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 6.23 | 0.79 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ACHC | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 5.48 | 1.00 | True | None | predicted_return_threshold |
| IOT | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 5.88 | 0.70 | False | None | predicted_return_threshold, vwap_relationship |
| QURE | 2026-03-27T18:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| OTIS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 2.62 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| TECK | 2026-03-27T18:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.51 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NTLA | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 4.08 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ODD | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| CSTM | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 3.21 | 0.28 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WRBY | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 2.45 | 0.56 | True | None | predicted_return_threshold |
| IONQ | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 4.50 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 2.31 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SYY | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9586 | -0.0001 | 0.50 | 0.79 | True | None | predicted_return_threshold |
| TPG | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 1.27 | 0.67 | False | None | predicted_return_threshold, vwap_relationship |
| SNDK | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| DNLI | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T18:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| HMY | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 1.76 | 0.84 | False | None | predicted_return_threshold, vwap_relationship |
| BX | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 3.91 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| CIEN | 2026-03-27T18:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9501 | -0.0001 | 4.19 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CTSH | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.84 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| CCJ | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 5.06 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| QBTS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 5.40 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ABT | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 1.91 | 0.75 | False | None | predicted_return_threshold, vwap_relationship |
| SCCO | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| LAZ | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.95 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| PANW | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 3.07 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VITL | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 1.90 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| SE | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.28 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| M | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9380 | 0.0000 | 0.70 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| ARIS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9367 | 0.0000 | 0.73 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| CC | 2026-03-27T18:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9355 | 0.0000 | 4.10 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FSLY | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9343 | 0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| PGNY | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9331 | 0.0000 | 1.45 | 0.82 | False | None | predicted_return_threshold, vwap_relationship |
| MIR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9319 | 0.0000 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9307 | 0.0000 | 1.80 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| SAIL | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9294 | 0.0000 | 2.10 | 0.77 | False | None | predicted_return_threshold, vwap_relationship |
| PBF | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9282 | 0.0000 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| PINS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9270 | 0.0000 | 1.41 | 0.73 | False | None | predicted_return_threshold, vwap_relationship |
| BRZE | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9258 | 0.0000 | 1.64 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| RKLB | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9246 | 0.0000 | 1.23 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| BJ | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9234 | -0.0000 | 0.50 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| SCO | 2026-03-27T18:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9221 | 0.0000 | 3.19 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DDOG | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| CIFR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 2.74 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| AXTI | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| NVT | 2026-03-27T18:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.50 | 0.52 | True | None | predicted_return_threshold |
| MEOH | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9161 | -0.0000 | 0.77 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EXLS | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9148 | 0.0000 | 1.67 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GLDM | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 0.84 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| VIAV | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 0.50 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CME | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 1.44 | 0.97 | False | None | predicted_return_threshold, vwap_relationship |
| PCAR | 2026-03-27T18:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9100 | -0.0000 | 0.99 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| NET | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 0.50 | 0.68 | True | None | predicted_return_threshold |
| TSCO | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9075 | 0.0000 | 2.51 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DOCN | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 1.24 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TXG | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9051 | -0.0000 | 0.65 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OKTA | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| YPF | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9027 | -0.0000 | 4.16 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| TENB | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| AEM | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 3.06 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| OTEX | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8990 | -0.0000 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| CGAU | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| WAY | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| VNET | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| CAI | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 4.55 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LITE | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| EXK | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 2.81 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| NXE | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 2.26 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ELV | 2026-03-27T18:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 0.50 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ANET | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| MKSI | 2026-03-27T18:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T18:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8856 | -0.0000 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| W | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| SW | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 2.54 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| CX | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| AMT | 2026-03-27T18:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8808 | -0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| BMNR | 2026-03-27T18:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 3.38 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
