# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| BMNR | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 6.00 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PSKY | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 11.30 | 0.71 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| U | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 17.05 | 0.67 | True | None | predicted_return_threshold, spread_filter |
| FSLY | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 7.24 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| PSTG | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| FIG | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 5.54 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| VITL | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 17.24 | 0.56 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| TXG | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| LYB | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 4.12 | 0.84 | True | None | predicted_return_threshold |
| AR | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 4.46 | 1.00 | True | None | predicted_return_threshold |
| APLD | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 0.51 | 0.81 | False | None | predicted_return_threshold, vwap_relationship |
| UPST | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9866 | -0.0001 | 3.99 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| QURE | 2026-03-27T15:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 8.97 | 0.56 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| BIRK | 2026-03-27T15:32:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| IBKR | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 1.52 | 0.86 | True | None | predicted_return_threshold |
| AXTI | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| SRPT | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 1.24 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WULF | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 4.14 | 0.97 | False | None | predicted_return_threshold, vwap_relationship |
| MIR | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 4.18 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| ALLY | 2026-03-27T15:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.95 | 0.85 | True | None | predicted_return_threshold |
| NTSK | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 12.61 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| KMT | 2026-03-27T15:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9745 | -0.0001 | 9.52 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| SEDG | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| XENE | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 1.36 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SOLS | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 1.16 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KSS | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 2.00 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| DUOL | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 5.79 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| MKSI | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| MEOH | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 2.74 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| ALAB | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| GEO | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.47 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PONY | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 1.32 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| LNG | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 1.60 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CORZ | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 6.50 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| USAR | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 14.46 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| IONQ | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 4.78 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BEAM | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| LITE | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| VRT | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 2.36 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LEVI | 2026-03-27T15:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.68 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9513 | -0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BLDR | 2026-03-27T15:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9501 | -0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| HBM | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.91 | 0.94 | True | None | predicted_return_threshold |
| NTLA | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 8.79 | 0.91 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CE | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| RKLB | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 6.81 | 0.61 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| LRCX | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.70 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SNPS | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 3.58 | 0.71 | False | None | predicted_return_threshold, vwap_relationship |
| ERAS | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 1.64 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KNX | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| WT | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| OKLO | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| GLXY | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| MKC | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 5.16 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WBD | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.30 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| FBIN | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.64 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DDOG | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| AMPX | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 1.51 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RCAT | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 5.69 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KRMN | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| SONY | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.62 | 0.80 | True | None | predicted_return_threshold |
| UMAC | 2026-03-27T15:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| VSCO | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 3.10 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CELH | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 2.15 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MRNA | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9221 | -0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| CAVA | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| WPM | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 4.93 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BRBR | 2026-03-27T15:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 1.67 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SE | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| PBI | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 2.26 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SNDK | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 4.02 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WDC | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 4.42 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WRBY | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 5.97 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DFTX | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SUNB | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| TPG | 2026-03-27T15:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 3.45 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| KMB | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 4.28 | 0.32 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TU | 2026-03-27T15:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9051 | -0.0001 | 0.50 | 0.91 | True | None | predicted_return_threshold |
| VOD | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.85 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| ALB | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| CUZ | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 1.16 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| CPRI | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| RRC | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 1.31 | 0.76 | False | None | predicted_return_threshold, vwap_relationship |
| FULT | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 0.63 | 0.60 | False | None | predicted_return_threshold, vwap_relationship |
| AAL | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 4.75 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PRCT | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| SCCO | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 2.05 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VIAV | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| ASTS | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.61 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| ACHC | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| FNGU | 2026-03-27T15:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| DHT | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 3.46 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ODFL | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| INDV | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| NVAX | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| UPWK | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| FLR | 2026-03-27T15:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| S | 2026-03-27T15:39:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8796 | -0.0000 | 0.99 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
