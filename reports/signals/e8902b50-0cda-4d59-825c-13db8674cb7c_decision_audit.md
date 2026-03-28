# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| KMT | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0044 | 0.9900 | 0.0044 | 13.47 | 0.14 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection |
| GEO | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 1.47 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CIFR | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| VIAV | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 1.44 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RRC | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| SM | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| TRU | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.63 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RNG | 2026-03-27T17:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| LI | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| TU | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9891 | 0.0001 | 2.95 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 7.37 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RKLB | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 2.87 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FRPT | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 0.88 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| AMKR | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| RIOT | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 2.92 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| CIEN | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 0.64 | True | None | predicted_return_threshold |
| MP | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 0.96 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WDC | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.99 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| MCHP | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 1.00 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FNGU | 2026-03-27T17:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.73 | 0.28 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OVV | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| HUT | 2026-03-27T17:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 0.50 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| BE | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| AGNC | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| VRT | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| GEN | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 1.35 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| CAI | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| WPM | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| SOC | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 2.74 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BK | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.58 | True | None | predicted_return_threshold |
| TNDM | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| QBTS | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 5.45 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MDB | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.75 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OMC | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9599 | -0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| FRO | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 1.12 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MKSI | 2026-03-27T17:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| BIRK | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| ABT | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 1.67 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TXG | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| AVGO | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 3.45 | 0.59 | True | None | predicted_return_threshold |
| TALO | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| DOCN | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| STM | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| BCS | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| CSTM | 2026-03-27T17:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| ADM | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 1.03 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| SCCO | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| VST | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.72 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KRC | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 1.77 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| TOST | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 2.43 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MU | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 3.83 | 0.55 | True | None | predicted_return_threshold |
| SLDE | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 0.50 | 0.70 | True | None | predicted_return_threshold |
| NWG | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| SOLS | 2026-03-27T17:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.50 | 0.55 | True | None | predicted_return_threshold |
| ARMK | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| LUNR | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| DVN | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| AA | 2026-03-27T17:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| BMY | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 1.27 | 0.60 | True | None | predicted_return_threshold |
| LNG | 2026-03-27T17:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| GAP | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9258 | -0.0001 | 4.04 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| EQH | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9246 | 0.0000 | 6.64 | 0.42 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| MSTR | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9234 | 0.0000 | 0.99 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WSC | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9221 | 0.0000 | 4.34 | 0.90 | False | None | predicted_return_threshold, vwap_relationship |
| ASTS | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 2.02 | 0.50 | True | None | predicted_return_threshold, liquidity_filter |
| ADMA | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 7.93 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| GME | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| XOM | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.73 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| CENX | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9161 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| BTU | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9148 | 0.0000 | 2.57 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9136 | -0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| DLTR | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SARO | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9100 | 0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| BMNR | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 2.71 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| ACHC | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9075 | 0.0000 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| TQQQ | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 2.55 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| CEG | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| ALB | 2026-03-27T17:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9039 | -0.0000 | 0.50 | 0.55 | True | None | predicted_return_threshold |
| CNC | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 3.13 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| MUR | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 1.19 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| S | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 3.94 | 0.54 | True | None | predicted_return_threshold |
| WVE | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 3.75 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| STX | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| GFS | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| RIVN | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 1.69 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FE | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8917 | -0.0000 | 2.23 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AZN | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8905 | -0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| PYPL | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 1.71 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ROKU | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8881 | -0.0000 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| NET | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| CHD | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8856 | -0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| CDE | 2026-03-27T17:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 2.22 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FIGR | 2026-03-27T17:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| DYN | 2026-03-27T17:32:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ONB | 2026-03-27T17:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
