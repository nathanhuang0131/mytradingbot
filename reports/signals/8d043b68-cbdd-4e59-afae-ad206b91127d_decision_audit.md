# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| ACHC | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | bracket_invalid | 0.0025 | 0.9900 | 0.0025 | 3.71 | 1.00 | True | False | fee_adjusted_expectancy |
| MKSI | 2026-03-27T14:50:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0017 | 0.9900 | 0.0017 | 9.91 | 0.42 | True | None | spread_filter, liquidity_filter |
| NTSK | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0013 | 0.9900 | 0.0013 | 14.14 | 0.95 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| SRAD | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 2.89 | 0.56 | True | None | predicted_return_threshold |
| BATL | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9900 | -0.0004 | 12.00 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| CC | 2026-03-27T14:50:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9900 | -0.0004 | 1.17 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BRBR | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9900 | -0.0003 | 13.42 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| LITE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 3.09 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 3.98 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| FDX | 2026-03-27T14:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9891 | 0.0003 | 2.42 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| CE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| CCL | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 3.07 | 1.00 | True | None | predicted_return_threshold |
| TXG | 2026-03-27T14:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9854 | -0.0002 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| GEN | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 2.03 | 1.00 | True | None | predicted_return_threshold |
| ALKT | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SSRM | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 8.09 | 0.91 | True | None | predicted_return_threshold, spread_filter |
| PSTG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 10.30 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| TSEM | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 2.36 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| BRZE | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| GEO | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 2.92 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| APP | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 6.35 | 0.76 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CDE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 13.15 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| INSM | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| CAVA | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 8.04 | 0.64 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| AMKR | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| INTU | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 1.08 | 0.96 | True | None | predicted_return_threshold |
| CUK | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 1.03 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TRI | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 4.03 | 0.88 | False | None | predicted_return_threshold, vwap_relationship |
| LCID | 2026-03-27T14:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.31 | 0.85 | False | None | predicted_return_threshold, vwap_relationship |
| VG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 2.17 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| PGNY | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| RKLB | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 7.88 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| AA | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 8.99 | 0.91 | True | None | predicted_return_threshold, spread_filter |
| PONY | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| FLY | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| DOCU | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 3.29 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| SVM | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| GPN | 2026-03-27T14:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9526 | -0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| NTNX | 2026-03-27T14:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.67 | 0.57 | True | None | predicted_return_threshold |
| HPE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 5.71 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MA | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.51 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| OTEX | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| BTU | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 7.56 | 0.06 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| ADBE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 3.13 | 0.90 | True | None | predicted_return_threshold |
| U | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 4.60 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SOLS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| RDDT | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.50 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VSCO | 2026-03-27T14:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| DOCN | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 2.95 | 0.60 | False | None | predicted_return_threshold, vwap_relationship |
| ZSL | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| CRCL | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 4.87 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CIEN | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| BAM | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.02 | 1.00 | True | None | predicted_return_threshold |
| CELH | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.66 | True | None | predicted_return_threshold |
| VALE | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 3.29 | 1.00 | True | None | predicted_return_threshold |
| CENX | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9307 | -0.0001 | 3.48 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DFTX | 2026-03-27T14:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| DNLI | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9282 | -0.0001 | 1.99 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NOG | 2026-03-27T14:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VRT | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| BX | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 2.06 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LYV | 2026-03-27T14:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 3.40 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MDLN | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 2.41 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| NBIS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9209 | -0.0001 | 4.29 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KRC | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| GIS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9185 | -0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| NVT | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| AEO | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 2.30 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| YPF | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 3.04 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| WT | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| FROG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| NXE | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9112 | -0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| OS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| PBR | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 2.42 | 1.00 | True | None | predicted_return_threshold |
| UMAC | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 3.92 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TNGX | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| ARIS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9051 | -0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| RNA | 2026-03-27T14:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 4.75 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BSY | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| IQV | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9015 | -0.0001 | 2.41 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SEDG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T14:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| ORLA | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| SAP | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 1.06 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| ONB | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8954 | -0.0000 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| WMG | 2026-03-27T14:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| V | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 2.01 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| ROKU | 2026-03-27T14:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| RNG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 5.86 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LW | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8893 | -0.0000 | 1.23 | 0.03 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BCS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.58 | True | None | predicted_return_threshold |
| CGAU | 2026-03-27T14:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| PATH | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 4.67 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ASTS | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 0.50 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TPG | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8832 | -0.0000 | 0.63 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FLUT | 2026-03-27T14:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T14:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| ODD | 2026-03-27T14:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8796 | -0.0000 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
