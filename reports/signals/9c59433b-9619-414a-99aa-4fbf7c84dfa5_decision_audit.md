# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| FIG | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0013 | 0.9900 | 0.0013 | 6.88 | 0.16 | True | None | spread_filter, liquidity_filter |
| SMR | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0008 | 0.9900 | 0.0008 | 4.89 | 0.29 | True | None | liquidity_filter |
| WHR | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| JEF | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| ARIS | 2026-03-27T18:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| ALKT | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 4.92 | 1.00 | True | None | predicted_return_threshold |
| QURE | 2026-03-27T18:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| SMTC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| U | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 6.13 | 0.62 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| PFGC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| UBS | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 1.37 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| OBDC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| CX | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 2.33 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| CPNG | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 4.14 | 0.53 | True | None | predicted_return_threshold |
| CRCL | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9830 | -0.0001 | 1.35 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TMO | 2026-03-27T18:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| AEO | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 1.56 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| DYN | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| DFTX | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 3.50 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| STNE | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.84 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EXEL | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| GFI | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 0.50 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VITL | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.97 | 1.00 | True | None | predicted_return_threshold |
| FIGS | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.85 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| KRC | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| TQQQ | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 2.24 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| MMM | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| APO | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 4.03 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| ONB | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| MET | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 1.11 | 1.00 | True | None | predicted_return_threshold |
| LUNR | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 4.21 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| FDX | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| EXPE | 2026-03-27T18:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| ETSY | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| UNH | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 4.75 | 0.60 | True | None | predicted_return_threshold |
| HPE | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 5.19 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| CAI | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 1.51 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RNA | 2026-03-27T18:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| HTGC | 2026-03-27T18:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.58 | True | None | predicted_return_threshold |
| REAL | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.41 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| FNB | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| BAC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.06 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FSK | 2026-03-27T18:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 1.25 | 0.93 | True | None | predicted_return_threshold |
| ENTG | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| OKTA | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 1.38 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| TXG | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.65 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| LNC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| SMCI | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 5.81 | 0.82 | True | None | predicted_return_threshold |
| BW | 2026-03-27T18:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 3.45 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| LUV | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 5.68 | 0.68 | True | None | predicted_return_threshold |
| CIFR | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9380 | -0.0001 | 0.92 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| XENE | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| TECH | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| LEVI | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.75 | 0.98 | True | None | predicted_return_threshold |
| CG | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 6.00 | 1.00 | True | None | predicted_return_threshold |
| AGNC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| DOC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| AVGO | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 1.07 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| GFS | 2026-03-27T18:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| UCO | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| WFRD | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| SEDG | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| DT | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| RCAT | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| HMC | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 1.36 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TRI | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| SSNC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| ADMA | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 2.68 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| KRMN | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.72 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NOMD | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 9.01 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| DHI | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| KVYO | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9112 | -0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T18:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| KHC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 2.83 | 0.83 | True | None | predicted_return_threshold |
| MOS | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 1.99 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| VLY | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| BE | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| INDV | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| IONS | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| BRKR | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.73 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| FWONK | 2026-03-27T18:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9002 | -0.0000 | 0.50 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| HON | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| GEN | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| COHR | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 1.66 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| PSTG | 2026-03-27T18:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| AMRZ | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| UEC | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 1.91 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ESI | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 1.87 | 0.85 | False | None | predicted_return_threshold, vwap_relationship |
| WVE | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 1.90 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ARMK | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 1.88 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| APG | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| XP | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.71 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BTU | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 4.47 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| NVDA | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 0.67 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OPCH | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| SRAD | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 8.75 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| IREN | 2026-03-27T18:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8808 | -0.0000 | 2.16 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| FISV | 2026-03-27T18:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8796 | -0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
