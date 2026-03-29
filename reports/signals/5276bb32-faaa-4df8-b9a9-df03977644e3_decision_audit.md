# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| DNLI | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9900 | 0.0009 | 11.62 | 1.00 | False | None | vwap_relationship, spread_filter |
| TXG | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9900 | 0.0007 | 1.30 | 1.00 | True | None | predicted_return_threshold |
| KTOS | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 3.82 | 1.00 | True | None | predicted_return_threshold |
| BOIL | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 9.92 | 0.75 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CZR | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 7.71 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| DFTX | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.79 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HUN | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 3.00 | 0.54 | True | None | predicted_return_threshold |
| VXX | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 8.32 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| LYB | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.32 | 1.00 | True | None | predicted_return_threshold |
| SCO | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 3.21 | 0.71 | False | None | predicted_return_threshold, vwap_relationship |
| ACHC | 2026-03-27T18:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 1.64 | 0.88 | False | None | predicted_return_threshold, vwap_relationship |
| PYPL | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 2.00 | 1.00 | True | None | predicted_return_threshold |
| TEM | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 0.50 | 0.83 | True | None | predicted_return_threshold |
| DYN | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 0.72 | 0.83 | False | None | predicted_return_threshold, vwap_relationship |
| ZETA | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 6.95 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| DLTR | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 1.42 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| U | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 4.69 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| DOG | 2026-03-27T18:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9793 | -0.0002 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| AXTI | 2026-03-27T18:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 3.79 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WYNN | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.55 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| TNDM | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9757 | -0.0001 | 12.39 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| NESR | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 2.33 | 0.76 | False | None | predicted_return_threshold, vwap_relationship |
| M | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 4.19 | 1.00 | True | None | predicted_return_threshold |
| DXC | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| NTR | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 4.17 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CRGY | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 3.62 | 1.00 | True | None | predicted_return_threshold |
| ARR | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 1.59 | 1.00 | True | None | predicted_return_threshold |
| SRAD | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.73 | 0.69 | True | None | predicted_return_threshold |
| BN | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 4.80 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DDOG | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 1.65 | 1.00 | True | None | predicted_return_threshold |
| BANC | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.74 | 0.86 | True | None | predicted_return_threshold |
| IVZ | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 4.15 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 1.50 | 0.88 | False | None | predicted_return_threshold, vwap_relationship |
| SOC | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 4.76 | 0.67 | True | None | predicted_return_threshold |
| CTRA | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 1.73 | 0.85 | True | None | predicted_return_threshold |
| MGM | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 2.76 | 0.75 | False | None | predicted_return_threshold, vwap_relationship |
| ROST | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.63 | False | None | predicted_return_threshold, vwap_relationship |
| CG | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| UUUU | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| BAX | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.57 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| ZSL | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 4.74 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| BDX | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.29 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FRPT | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| DVN | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 2.17 | 0.82 | True | None | predicted_return_threshold |
| LOW | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 1.36 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| CUK | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 2.63 | 0.67 | False | None | predicted_return_threshold, vwap_relationship |
| CART | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 1.40 | 0.71 | True | None | predicted_return_threshold |
| MAT | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.88 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CTVA | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 3.67 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| MOS | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 3.00 | 0.80 | False | None | predicted_return_threshold, vwap_relationship |
| WDAY | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 2.82 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ALK | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 5.50 | 1.00 | True | None | predicted_return_threshold |
| BRKR | 2026-03-27T18:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9355 | -0.0001 | 1.46 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| ORLY | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.69 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| EXE | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 1.20 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| PRCT | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| QURE | 2026-03-27T18:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9307 | -0.0001 | 1.65 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| APLD | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 4.78 | 1.00 | True | None | predicted_return_threshold |
| IREN | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9282 | -0.0001 | 8.61 | 0.55 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ERAS | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9270 | -0.0001 | 4.97 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| CBRE | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| VEEV | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 4.20 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| COP | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 3.82 | 1.00 | True | None | predicted_return_threshold |
| SAN | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 1.17 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SATS | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.77 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| MMM | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 1.39 | 0.77 | False | None | predicted_return_threshold, vwap_relationship |
| MUR | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.59 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MS | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| LUNR | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9161 | -0.0001 | 0.70 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| FNGU | 2026-03-27T18:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| CSGP | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 1.57 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| FLG | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 2.86 | 0.80 | True | None | predicted_return_threshold |
| TRI | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 5.90 | 0.61 | False | None | predicted_return_threshold, vwap_relationship |
| NTSK | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| OXY | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 1.91 | 0.57 | True | None | predicted_return_threshold |
| TECH | 2026-03-27T18:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 2.45 | 0.69 | True | None | predicted_return_threshold |
| SWKS | 2026-03-27T18:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| TMO | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 0.95 | 0.75 | True | None | predicted_return_threshold |
| NXE | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| EXK | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| CUBE | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 2.09 | 1.00 | True | None | predicted_return_threshold |
| DUK | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 1.53 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| KSS | 2026-03-27T18:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 3.04 | 0.84 | True | None | predicted_return_threshold |
| CARR | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 0.92 | 0.73 | True | None | predicted_return_threshold |
| SPOT | 2026-03-27T18:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8966 | -0.0001 | 0.50 | 0.84 | False | None | predicted_return_threshold, vwap_relationship |
| AMKR | 2026-03-27T18:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 3.63 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SHOP | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 4.96 | 0.68 | False | None | predicted_return_threshold, vwap_relationship |
| VZ | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 2.48 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| RYAN | 2026-03-27T18:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| MGY | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 2.33 | 1.00 | True | None | predicted_return_threshold |
| ILMN | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SIRI | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 1.65 | 0.67 | False | None | predicted_return_threshold, vwap_relationship |
| PM | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| AS | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 2.82 | 0.68 | False | None | predicted_return_threshold, vwap_relationship |
| CE | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 13.55 | 0.57 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| DINO | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CC | 2026-03-27T18:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 2.95 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| NG | 2026-03-27T18:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| NRG | 2026-03-27T18:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
