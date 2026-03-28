# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| DNLI | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0009 | 0.9900 | 0.0009 | 3.42 | 0.27 | True | None | liquidity_filter |
| TXG | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9900 | 0.0007 | 3.89 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| KTOS | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| BOIL | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 5.66 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CZR | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 1.92 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| DFTX | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| HUN | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.99 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VXX | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 1.28 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LYB | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 4.96 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SCO | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ACHC | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 1.09 | 0.69 | True | None | predicted_return_threshold |
| PYPL | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 1.71 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| TEM | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 1.46 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| DYN | 2026-03-27T18:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| ZETA | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 11.94 | 0.39 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| DLTR | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| U | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 8.75 | 0.09 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| DOG | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9793 | -0.0002 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| WYNN | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| TNDM | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9757 | -0.0001 | 0.59 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| NESR | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| M | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| DXC | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| NTR | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| CRGY | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| ARR | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| SRAD | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| BN | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.96 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DDOG | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.88 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| BANC | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| IVZ | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 1.08 | 0.98 | True | None | predicted_return_threshold |
| BATL | 2026-03-27T18:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| SOC | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 1.36 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CTRA | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| MGM | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.69 | 0.78 | False | None | predicted_return_threshold, vwap_relationship |
| ROST | 2026-03-27T18:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| CG | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.82 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 1.42 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| BAX | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.57 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| ZSL | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| BDX | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| FRPT | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| DVN | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| LOW | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.76 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| CUK | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| CART | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| MAT | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.87 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| CTVA | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| MOS | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.50 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| WDAY | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.90 | 0.51 | True | None | predicted_return_threshold |
| ALK | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 1.37 | 0.94 | False | None | predicted_return_threshold, vwap_relationship |
| BRKR | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9355 | -0.0001 | 0.74 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| ORLY | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.55 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EXE | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 1.42 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PRCT | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| QURE | 2026-03-27T18:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9307 | -0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| APLD | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 4.21 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| IREN | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9282 | -0.0001 | 2.49 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| ERAS | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9270 | -0.0001 | 4.12 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| CBRE | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VEEV | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 2.02 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| COP | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 2.79 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| SAN | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| SATS | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.59 | True | None | predicted_return_threshold |
| MMM | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| MUR | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| MS | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| LUNR | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9161 | -0.0001 | 2.77 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| FNGU | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| CSGP | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 3.11 | 0.61 | True | None | predicted_return_threshold |
| FLG | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 0.95 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| TRI | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.98 | 0.61 | True | None | predicted_return_threshold |
| NTSK | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 6.34 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| OXY | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 2.11 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TECH | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SWKS | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| TMO | 2026-03-27T18:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 0.50 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NXE | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.73 | True | None | predicted_return_threshold |
| EXK | 2026-03-27T18:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| CUBE | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| DUK | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| KSS | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| CARR | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 1.15 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SPOT | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8966 | -0.0001 | 0.93 | 0.77 | True | None | predicted_return_threshold |
| AMKR | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| SHOP | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| VZ | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RYAN | 2026-03-27T18:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 1.55 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| MGY | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.77 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| ILMN | 2026-03-27T18:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| SIRI | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| PM | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| AS | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 0.50 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CE | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 2.59 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DINO | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| CC | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| NG | 2026-03-27T18:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| NRG | 2026-03-27T18:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
