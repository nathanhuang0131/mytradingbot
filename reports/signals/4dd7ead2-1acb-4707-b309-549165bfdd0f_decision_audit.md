# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| PNC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0011 | 0.9900 | 0.0011 | 16.12 | 1.00 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| C | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 25.02 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| ADMA | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 12.91 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CELH | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 11.18 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| TFC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 15.68 | 0.72 | True | None | predicted_return_threshold, spread_filter, liquidity_sweep_detection |
| FITB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 9.19 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| BXP | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 2.39 | 1.00 | True | None | predicted_return_threshold |
| COLB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 7.39 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| PRGO | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 2.66 | 1.00 | True | None | predicted_return_threshold |
| RCAT | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9891 | 0.0003 | 1.92 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| FMC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9878 | 0.0003 | 9.54 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| UMAC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9866 | 0.0003 | 0.50 | 0.84 | True | None | predicted_return_threshold |
| SYF | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9854 | 0.0003 | 2.66 | 0.87 | False | None | predicted_return_threshold, vwap_relationship |
| USB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 10.03 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| NOMD | 2026-03-27T15:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 1.29 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| WFC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 7.72 | 0.90 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| BTSG | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 1.77 | 0.69 | False | None | predicted_return_threshold, vwap_relationship |
| UBS | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 2.03 | 1.00 | True | None | predicted_return_threshold |
| CFG | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 9.94 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| LUNR | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9769 | 0.0002 | 1.38 | 0.59 | True | None | predicted_return_threshold |
| TREX | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9757 | 0.0002 | 1.39 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BAC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9745 | 0.0002 | 6.31 | 0.79 | True | None | predicted_return_threshold, spread_filter |
| GPK | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9732 | 0.0002 | 2.73 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ICE | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9720 | 0.0002 | 1.62 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| XRAY | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 2.17 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| PAGS | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9696 | -0.0001 | 1.26 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| RF | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 7.89 | 0.42 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| QURE | 2026-03-27T15:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 8.97 | 0.56 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| KMX | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 3.90 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| ALB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 4.44 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| MP | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 2.60 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MSTR | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 11.07 | 0.54 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| JPM | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 5.92 | 1.00 | True | None | predicted_return_threshold |
| SOC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 8.25 | 0.63 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| AAOI | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| ELAN | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.54 | 0.70 | True | None | predicted_return_threshold |
| FSK | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 2.46 | 0.51 | True | None | predicted_return_threshold |
| FNB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 4.58 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FNGU | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 5.04 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| TRU | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| FLY | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| CUK | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 1.03 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| BAX | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.87 | True | None | predicted_return_threshold |
| TD | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 4.49 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| CZR | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.59 | True | None | predicted_return_threshold |
| HBAN | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 7.38 | 0.03 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| DAR | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| ORLA | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.53 | True | None | predicted_return_threshold |
| FIS | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 5.30 | 1.00 | True | None | predicted_return_threshold |
| SIRI | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 1.64 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AXP | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.27 | 0.73 | True | None | predicted_return_threshold |
| CUZ | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 3.47 | 0.97 | True | None | predicted_return_threshold |
| ALKS | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.85 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SGI | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| ZSL | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9331 | -0.0001 | 15.44 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| TMO | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 1.94 | 0.84 | True | None | predicted_return_threshold |
| LKQ | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.85 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GEO | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 2.93 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| UPST | 2026-03-27T15:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| RKT | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 1.79 | 0.64 | True | None | predicted_return_threshold |
| COHR | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| FLEX | 2026-03-27T15:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| AESI | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 1.84 | 0.57 | True | None | predicted_return_threshold |
| OLN | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9221 | -0.0001 | 4.86 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T15:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| ASB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 7.43 | 0.13 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| ONB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 5.78 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OVV | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 1.81 | 1.00 | True | None | predicted_return_threshold |
| BX | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 5.79 | 0.70 | True | None | predicted_return_threshold |
| CC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| KKR | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 7.03 | 0.79 | True | None | predicted_return_threshold, spread_filter |
| BN | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 1.27 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MRSH | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 2.61 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| HPQ | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 2.57 | 0.73 | True | None | predicted_return_threshold |
| LEVI | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| BNS | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 2.57 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BW | 2026-03-27T15:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 1.70 | 0.44 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AG | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 5.52 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AA | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| SDOW | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 3.36 | 1.00 | True | None | predicted_return_threshold |
| TENB | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 5.23 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| RNA | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 1.92 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TNDM | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| PFE | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 1.37 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ARM | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 3.58 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| ERAS | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| IBM | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 0.50 | 0.80 | True | None | predicted_return_threshold |
| COF | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 1.26 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T15:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| ERIC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 2.23 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PPG | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| HWM | 2026-03-27T15:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| RUN | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| AKAM | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 2.63 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| OBDC | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 1.14 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| CUBE | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 1.38 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| BMNR | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 8.63 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| USFD | 2026-03-27T15:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 0.82 | 0.55 | True | None | predicted_return_threshold |
| WVE | 2026-03-27T16:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 1.92 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
