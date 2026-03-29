# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| ACHC | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0025 | 0.9900 | 0.0025 | 0.50 | 0.06 | True | None | liquidity_filter |
| MKSI | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0017 | 0.9900 | 0.0017 | 0.50 | 0.03 | True | None | liquidity_filter |
| NTSK | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0013 | 0.9900 | 0.0013 | 0.50 | 0.02 | True | None | liquidity_filter |
| SRAD | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 3.60 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9900 | -0.0004 | 16.47 | 0.19 | True | None | predicted_return_threshold, spread_filter, liquidity_filter, liquidity_sweep_detection |
| CC | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9900 | -0.0004 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| BRBR | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9900 | -0.0003 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| LITE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| BE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| FDX | 2026-03-27T15:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9891 | 0.0003 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| CE | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 11.16 | 0.53 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CCL | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 10.86 | 0.54 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| TXG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9854 | -0.0002 | 12.70 | 0.64 | True | None | predicted_return_threshold, spread_filter, liquidity_sweep_detection |
| GEN | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| ALKT | 2026-03-27T15:04:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| SSRM | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 2.80 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PSTG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 2.59 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BRZE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| GEO | 2026-03-27T15:05:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| APP | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 3.48 | 0.60 | False | None | predicted_return_threshold, vwap_relationship |
| CDE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 5.78 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| INSM | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.69 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| CAVA | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| AMKR | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 4.11 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| INTU | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 1.62 | 0.59 | False | None | predicted_return_threshold, vwap_relationship |
| CUK | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| TRI | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 3.99 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LCID | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.31 | 0.64 | True | None | predicted_return_threshold |
| VG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| PGNY | 2026-03-27T15:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| RKLB | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 2.42 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| AA | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 2.66 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FLY | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| DOCU | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SVM | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.57 | True | None | predicted_return_threshold |
| GPN | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9526 | -0.0001 | 2.02 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| NTNX | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| HPE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 7.80 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| MA | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.30 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| OTEX | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| BTU | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 6.95 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| ADBE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 1.00 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| U | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 9.88 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| SOLS | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| RDDT | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 3.37 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VSCO | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| DOCN | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 3.72 | 1.00 | True | None | predicted_return_threshold |
| ZSL | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 14.33 | 0.39 | True | None | predicted_return_threshold, spread_filter, liquidity_filter, liquidity_sweep_detection |
| CRCL | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 3.78 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| CIEN | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 1.93 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| BAM | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 3.44 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CELH | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| VALE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 3.28 | 0.73 | False | None | predicted_return_threshold, vwap_relationship |
| CENX | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9307 | -0.0001 | 3.70 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| DFTX | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| DNLI | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9282 | -0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| NOG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.45 | True | None | predicted_return_threshold, liquidity_filter |
| VRT | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 3.97 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BX | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 3.30 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| LYV | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MDLN | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 4.21 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| NBIS | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9209 | -0.0001 | 1.83 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| KRC | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| GIS | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9185 | -0.0001 | 0.68 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| NVT | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 3.61 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| AEO | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| YPF | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| WT | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| FROG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 1.70 | 0.80 | True | None | predicted_return_threshold |
| NXE | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9112 | -0.0001 | 1.14 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| OS | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| PBR | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 2.42 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| UMAC | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| TNGX | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| ARIS | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9051 | -0.0001 | 2.17 | 0.52 | False | None | predicted_return_threshold, vwap_relationship |
| RNA | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| BSY | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| IQV | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9015 | -0.0001 | 0.75 | 0.78 | True | None | predicted_return_threshold |
| SEDG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 1.41 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ORLA | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SAP | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| ONB | 2026-03-27T15:05:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8954 | -0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| WMG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 2.08 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| V | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 3.53 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ROKU | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| RNG | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| LW | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8893 | -0.0000 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| BCS | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| CGAU | 2026-03-27T15:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 5.15 | 0.50 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PATH | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 3.50 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ASTS | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| TPG | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8832 | -0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| FLUT | 2026-03-27T15:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 2.85 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| ODD | 2026-03-27T15:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8796 | -0.0000 | 0.95 | 0.81 | False | None | predicted_return_threshold, vwap_relationship |
