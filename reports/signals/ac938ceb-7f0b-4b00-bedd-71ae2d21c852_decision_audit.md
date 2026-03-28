# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| KMT | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0044 | 0.9900 | 0.0044 | 19.71 | 0.21 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection |
| GEO | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 7.35 | 0.60 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CIFR | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 1.84 | 0.90 | False | None | predicted_return_threshold, vwap_relationship |
| VIAV | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 4.33 | 1.00 | True | None | predicted_return_threshold |
| RRC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 6.02 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| SM | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 8.47 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| TRU | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| RNG | 2026-03-27T17:04:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.64 | True | None | predicted_return_threshold |
| LI | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 2.82 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TU | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9891 | 0.0001 | 0.99 | 0.65 | True | None | predicted_return_threshold |
| AXTI | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| RKLB | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 3.88 | 0.97 | False | None | predicted_return_threshold, vwap_relationship |
| FRPT | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| AMKR | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 0.50 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| RIOT | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 1.95 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| CIEN | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| MP | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 0.50 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| WDC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 2.35 | 1.00 | True | None | predicted_return_threshold |
| MCHP | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 2.78 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| FNGU | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 0.50 | 0.59 | True | None | predicted_return_threshold |
| OVV | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 3.63 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| HUT | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 1.84 | 0.57 | True | None | predicted_return_threshold |
| BE | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.67 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| AGNC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 2.57 | 0.77 | True | None | predicted_return_threshold |
| VRT | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| GEN | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 3.38 | 1.00 | True | None | predicted_return_threshold |
| CAI | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 3.01 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WPM | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.60 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SOC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| BK | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TNDM | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 3.49 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| QBTS | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.90 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MDB | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| OMC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9599 | -0.0001 | 1.51 | 0.68 | True | None | predicted_return_threshold |
| FRO | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.57 | True | None | predicted_return_threshold |
| MKSI | 2026-03-27T17:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| BIRK | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.52 | True | None | predicted_return_threshold |
| ABT | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 5.47 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| TXG | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 2.58 | 1.00 | True | None | predicted_return_threshold |
| AVGO | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 1.83 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| TALO | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 6.05 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| BEAM | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 4.46 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| DOCN | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.55 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| STM | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 1.54 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BCS | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| CSTM | 2026-03-27T17:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ADM | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 2.40 | 0.60 | True | None | predicted_return_threshold |
| SCCO | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 1.54 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| VST | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 8.29 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| KRC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 2.65 | 0.92 | True | None | predicted_return_threshold |
| TOST | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 4.37 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| MU | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 1.25 | 0.59 | False | None | predicted_return_threshold, vwap_relationship |
| SLDE | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 0.71 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| NWG | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| SOLS | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| ARMK | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| LUNR | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| DVN | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 3.62 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AA | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| BMY | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 2.97 | 0.86 | True | None | predicted_return_threshold |
| LNG | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| GAP | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9258 | -0.0001 | 1.01 | 0.44 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EQH | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9246 | 0.0000 | 6.96 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| MSTR | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9234 | 0.0000 | 3.37 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9221 | 0.0000 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| ASTS | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 0.62 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| ADMA | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 6.55 | 0.11 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| GME | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.50 | 0.50 | True | None | predicted_return_threshold |
| XOM | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 3.30 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CENX | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9161 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| BTU | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9148 | 0.0000 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9136 | -0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| DLTR | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SARO | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9100 | 0.0000 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| BMNR | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 4.08 | 0.81 | False | None | predicted_return_threshold, vwap_relationship |
| ACHC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9075 | 0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| TQQQ | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| CEG | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| ALB | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9039 | -0.0000 | 0.50 | 0.71 | False | None | predicted_return_threshold, vwap_relationship |
| CNC | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 1.56 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| MUR | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.89 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| S | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 2.97 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| Q | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| WVE | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 7.44 | 0.83 | True | None | predicted_return_threshold, spread_filter |
| STX | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 2.15 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| GFS | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 1.45 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RIVN | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.84 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| FE | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8917 | -0.0000 | 1.98 | 0.84 | False | None | predicted_return_threshold, vwap_relationship |
| AZN | 2026-03-27T17:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8905 | -0.0000 | 1.97 | 1.00 | True | None | predicted_return_threshold |
| PYPL | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 3.42 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| ROKU | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8881 | -0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| NET | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| CHD | 2026-03-27T17:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8856 | -0.0000 | 1.58 | 0.74 | False | None | predicted_return_threshold, vwap_relationship |
| CDE | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 1.47 | 0.03 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FIGR | 2026-03-27T17:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 1.20 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OC | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.71 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DYN | 2026-03-27T17:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| ONB | 2026-03-27T17:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
