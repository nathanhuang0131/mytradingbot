# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| CPNG | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0019 | 0.9900 | 0.0019 | 8.20 | 0.59 | False | None | vwap_relationship, spread_filter |
| NBIS | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | -0.0015 | 0.9900 | -0.0015 | 9.15 | 1.00 | True | None | spread_filter |
| SCO | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | bracket_invalid | 0.0013 | 0.9900 | 0.0013 | 4.77 | 0.62 | True | False | fee_adjusted_expectancy |
| ZSL | 2026-03-27T16:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 16.47 | 0.79 | True | None | predicted_return_threshold, spread_filter, liquidity_sweep_detection |
| QURE | 2026-03-27T16:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 8.36 | 0.67 | True | None | predicted_return_threshold, spread_filter |
| C | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 7.88 | 0.50 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| DOCN | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| CVNA | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 2.82 | 1.00 | True | None | predicted_return_threshold |
| SATS | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 5.76 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DUOL | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.93 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MSTR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 4.15 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HBAN | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 3.28 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| KVYO | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 1.34 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ILMN | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 3.50 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FOUR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| ZS | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 4.53 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| OSCR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 4.42 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FNGU | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 5.04 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| SNDK | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 7.83 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| CRBG | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 2.17 | 0.68 | False | None | predicted_return_threshold, vwap_relationship |
| PCAR | 2026-03-27T16:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.55 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| LYFT | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 4.92 | 0.58 | False | None | predicted_return_threshold, vwap_relationship |
| ARR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.79 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GOOGL | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 3.43 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| NTSK | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 1.59 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| FLY | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9696 | -0.0001 | 2.12 | 0.45 | True | None | predicted_return_threshold, liquidity_filter |
| ERAS | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| BRBR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| MT | 2026-03-27T16:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| MRNA | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| TXG | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.27 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LBRT | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9623 | -0.0001 | 1.26 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| M | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 7.66 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| NET | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 1.79 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| ASX | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 2.88 | 1.00 | True | None | predicted_return_threshold |
| CX | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 2.33 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AMPX | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 6.11 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| GTLB | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 3.65 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ROKU | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 6.59 | 0.54 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CAI | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.73 | 0.74 | False | None | predicted_return_threshold, vwap_relationship |
| LRCX | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.82 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| ALAB | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| CPRT | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.90 | 0.93 | False | None | predicted_return_threshold, vwap_relationship |
| AEO | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 1.54 | 0.67 | False | None | predicted_return_threshold, vwap_relationship |
| JCI | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.76 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| CENX | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9440 | -0.0001 | 5.40 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EMBJ | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| TU | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9416 | -0.0001 | 2.95 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ZETA | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 5.88 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PSKY | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 5.72 | 0.80 | True | None | predicted_return_threshold |
| WAL | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| LITE | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| RYAN | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| SMR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.39 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MA | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 5.38 | 1.00 | True | None | predicted_return_threshold |
| CTRE | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 1.00 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WELL | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 2.30 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| RCAT | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 5.78 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| WT | 2026-03-27T16:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SVM | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 7.26 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| SJM | 2026-03-27T16:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| FRPT | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 1.32 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| LEVI | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| PBF | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| VRT | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| ODFL | 2026-03-27T16:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9185 | -0.0000 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| ALM | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 1.63 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EXPE | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9161 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| CNK | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9148 | -0.0000 | 7.26 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| KHC | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 2.81 | 0.74 | True | None | predicted_return_threshold |
| FOX | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 1.65 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| BW | 2026-03-27T16:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| SRPT | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9100 | 0.0000 | 4.40 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| PATH | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 3.50 | 0.78 | False | None | predicted_return_threshold, vwap_relationship |
| SYF | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9075 | 0.0000 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| WHR | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 2.36 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RBRK | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 2.18 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| U | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 7.30 | 0.28 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| HMC | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| BOIL | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| KRC | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| SFM | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| FLNC | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8978 | -0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| KTOS | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| LYV | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 1.80 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ALB | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 1.81 | 0.40 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KO | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8929 | -0.0000 | 0.99 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ZBH | 2026-03-27T16:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| T | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8905 | -0.0000 | 0.86 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NESR | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 0.50 | 0.92 | True | None | predicted_return_threshold |
| BRX | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| BMRN | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| NEM | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 4.99 | 0.75 | True | None | predicted_return_threshold |
| SMFG | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| AZN | 2026-03-27T16:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| WRBY | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8820 | -0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| HIMS | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 5.08 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PSX | 2026-03-27T16:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 3.74 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
