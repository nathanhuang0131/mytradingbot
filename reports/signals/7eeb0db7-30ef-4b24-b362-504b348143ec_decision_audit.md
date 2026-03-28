# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| SHOP | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9900 | -0.0007 | 5.85 | 1.00 | True | None | predicted_return_threshold |
| BBVA | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 4.84 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BATL | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 4.18 | 0.55 | True | None | predicted_return_threshold |
| LYV | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 5.13 | 0.81 | False | None | predicted_return_threshold, vwap_relationship |
| FBIN | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 6.16 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| AMPX | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 22.14 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| RNA | 2026-03-27T15:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| U | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 16.63 | 0.31 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| BTSG | 2026-03-27T15:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 1.77 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| S | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 7.98 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| KSS | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9878 | -0.0002 | 3.01 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WHR | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 2.36 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CNK | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 8.18 | 0.88 | True | None | predicted_return_threshold, spread_filter |
| OC | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| SNOW | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.82 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| YPF | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 4.89 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| IQV | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 3.17 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OLN | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 1.76 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| XRAY | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9769 | 0.0002 | 1.09 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| CGNX | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9757 | 0.0002 | 4.43 | 0.88 | True | None | predicted_return_threshold |
| HUT | 2026-03-27T15:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9745 | 0.0002 | 7.11 | 0.53 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| DKNG | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9732 | 0.0002 | 4.20 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FSLY | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 3.22 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AU | 2026-03-27T15:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| NKE | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 4.86 | 0.82 | False | None | predicted_return_threshold, vwap_relationship |
| ALB | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| UDR | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 4.42 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| EQX | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 3.95 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WULF | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9647 | -0.0001 | 5.08 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TALO | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 2.98 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| Z | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 5.16 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| TSEM | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| ALLY | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 1.30 | 0.63 | True | None | predicted_return_threshold |
| KTOS | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 1.13 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WFRD | 2026-03-27T15:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 4.14 | 0.68 | False | None | predicted_return_threshold, vwap_relationship |
| BW | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| CDW | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 1.05 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| FIGS | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| WAL | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.10 | 0.67 | False | None | predicted_return_threshold, vwap_relationship |
| GM | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 3.05 | 1.00 | True | None | predicted_return_threshold |
| VNOM | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 2.08 | 1.00 | True | None | predicted_return_threshold |
| ELV | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.78 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ARCC | 2026-03-27T15:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 3.54 | 1.00 | True | None | predicted_return_threshold |
| CPRI | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 3.61 | 0.76 | True | None | predicted_return_threshold |
| PLNT | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9440 | -0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| GLDM | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 2.79 | 0.74 | True | None | predicted_return_threshold |
| CVNA | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 3.81 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GLL | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 5.22 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| ATI | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.62 | True | None | predicted_return_threshold |
| GFI | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9380 | -0.0001 | 4.74 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VSNT | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 2.45 | 0.68 | False | None | predicted_return_threshold, vwap_relationship |
| FTNT | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 4.29 | 1.00 | True | None | predicted_return_threshold |
| EQH | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.07 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| KMT | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| RELX | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 4.30 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| WM | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 2.74 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PINS | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 4.92 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| RCAT | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.95 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| XENE | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SMFG | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 1.95 | 0.77 | False | None | predicted_return_threshold, vwap_relationship |
| UCO | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 1.20 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PUMP | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| JEF | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 3.72 | 0.44 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ASTS | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 6.14 | 0.35 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| TWO | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 1.12 | 0.84 | True | None | predicted_return_threshold |
| SOFI | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 6.49 | 0.55 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| PBI | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 1.14 | 0.61 | False | None | predicted_return_threshold, vwap_relationship |
| INDV | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 2.56 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MTCH | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 1.65 | 0.70 | False | None | predicted_return_threshold, vwap_relationship |
| NET | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 6.97 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| KRMN | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 9.13 | 0.59 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| NTLA | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 4.94 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HDB | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 6.57 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| NVST | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.99 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ESI | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 1.13 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| MGM | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 6.84 | 0.53 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| PONY | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 5.30 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| A | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 2.24 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| LBRT | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| RBRK | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 0.55 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SAIL | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 4.28 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| XPO | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SPOT | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 3.90 | 0.52 | False | None | predicted_return_threshold, vwap_relationship |
| BWA | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 4.60 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ENTG | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| FLY | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| AL | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| FLEX | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 7.38 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| NG | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 1.52 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| MUFG | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 1.52 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| FNB | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 2.29 | 0.90 | False | None | predicted_return_threshold, vwap_relationship |
| ADMA | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8869 | -0.0001 | 2.60 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| DYN | 2026-03-27T15:17:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 2.09 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BRBR | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.84 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| DT | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 2.11 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| NWG | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 0.50 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 2.71 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DDOG | 2026-03-27T15:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 4.01 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
