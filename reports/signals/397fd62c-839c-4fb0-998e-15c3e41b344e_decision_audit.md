# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| PNC | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0011 | 0.9900 | 0.0011 | 0.50 | 0.05 | True | None | liquidity_filter |
| C | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 6.57 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| ADMA | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 5.19 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CELH | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| TFC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 4.17 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| FITB | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 2.23 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| BXP | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| COLB | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| PRGO | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 1.33 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| RCAT | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9891 | 0.0003 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| FMC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9878 | 0.0003 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| UMAC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9866 | 0.0003 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SYF | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9854 | 0.0003 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| USB | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 2.44 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| NOMD | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| WFC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 2.09 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BTSG | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 2.65 | 1.00 | True | None | predicted_return_threshold |
| UBS | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| CFG | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| LUNR | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9769 | 0.0002 | 2.79 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TREX | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9757 | 0.0002 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| BAC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9745 | 0.0002 | 2.90 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GPK | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9732 | 0.0002 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| ICE | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9720 | 0.0002 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| XRAY | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 1.08 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PAGS | 2026-03-27T16:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9696 | -0.0001 | 3.79 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| RF | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| QURE | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| KMX | 2026-03-27T16:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| ALB | 2026-03-27T16:04:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| MP | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 2.82 | 0.78 | True | None | predicted_return_threshold |
| MSTR | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 5.55 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| JPM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 1.93 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SOC | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| AAOI | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| ELAN | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.54 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FSK | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| FNB | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.76 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| FNGU | 2026-03-27T15:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 5.04 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| TRU | 2026-03-27T16:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 1.12 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| FLY | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.07 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| CUK | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| BAX | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| TD | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CZR | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 2.87 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HBAN | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| DAR | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| ORLA | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 2.55 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| FIS | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.50 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SIRI | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| AXP | 2026-03-27T16:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.51 | 0.61 | True | None | predicted_return_threshold |
| CUZ | 2026-03-27T16:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.58 | 0.82 | False | None | predicted_return_threshold, vwap_relationship |
| ALKS | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| SGI | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 8.47 | 0.52 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ZSL | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9331 | -0.0001 | 1.93 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TMO | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| LKQ | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| GEO | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| UPST | 2026-03-27T16:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 1.00 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RKT | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| COHR | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| FLEX | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| AESI | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 2.77 | 0.70 | True | None | predicted_return_threshold |
| OLN | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9221 | -0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T16:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| ASB | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 1.98 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ONB | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| OVV | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.80 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BX | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| CC | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| KKR | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 3.66 | 0.55 | True | None | predicted_return_threshold |
| BN | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 0.64 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| MRSH | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.80 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HPQ | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 5.15 | 0.57 | True | None | predicted_return_threshold |
| LEVI | 2026-03-27T16:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| BNS | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.55 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BW | 2026-03-27T16:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| AG | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 5.47 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| AA | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| SDOW | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 2.68 | 0.87 | False | None | predicted_return_threshold, vwap_relationship |
| TENB | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| RNA | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| TNDM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.65 | True | None | predicted_return_threshold |
| PFE | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 0.50 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ARM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 0.50 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ERAS | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| IBM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| COF | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T16:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| ERIC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| PPG | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| HWM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| RUN | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| AKAM | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| OBDC | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 2.27 | 0.73 | True | None | predicted_return_threshold |
| CUBE | 2026-03-27T16:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 0.69 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| BMNR | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 4.02 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| USFD | 2026-03-27T16:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| WVE | 2026-03-27T16:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
