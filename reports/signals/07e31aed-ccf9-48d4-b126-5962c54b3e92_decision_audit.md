# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| SHOP | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9900 | -0.0007 | 4.68 | 0.93 | False | None | predicted_return_threshold, vwap_relationship |
| BBVA | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| LYV | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 1.71 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| FBIN | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| AMPX | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 2.27 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RNA | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| U | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 9.20 | 0.20 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| BTSG | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.59 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| S | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 3.97 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| KSS | 2026-03-27T15:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9878 | -0.0002 | 1.00 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| WHR | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 0.50 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| CNK | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 0.50 | 0.60 | True | None | predicted_return_threshold |
| SNOW | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.98 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| YPF | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 3.26 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AXTI | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 6.87 | 0.24 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| IQV | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 2.71 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| OLN | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 2.63 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| XRAY | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9769 | 0.0002 | 4.32 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| CGNX | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9757 | 0.0002 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| HUT | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9745 | 0.0002 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| DKNG | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9732 | 0.0002 | 5.40 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 2.27 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| NKE | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 2.42 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| ALB | 2026-03-27T15:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| UDR | 2026-03-27T15:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| EQX | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 8.84 | 0.17 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| WULF | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9647 | -0.0001 | 6.67 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| TALO | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.49 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| Z | 2026-03-27T15:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T15:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| ALLY | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| KTOS | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T15:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 5.16 | 1.00 | True | None | predicted_return_threshold |
| WFRD | 2026-03-27T15:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BW | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 6.82 | 0.48 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| CDW | 2026-03-27T15:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.52 | 0.51 | True | None | predicted_return_threshold |
| FIGS | 2026-03-27T15:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| WAL | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.55 | True | None | predicted_return_threshold |
| GM | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 4.39 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| VNOM | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| ELV | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ARCC | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| CPRI | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 1.43 | 0.51 | True | None | predicted_return_threshold |
| PLNT | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9440 | -0.0001 | 2.16 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| GLDM | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 2.78 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CVNA | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 2.59 | 0.83 | True | None | predicted_return_threshold |
| GLL | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| ATI | 2026-03-27T15:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| GFI | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9380 | -0.0001 | 2.65 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VSNT | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 1.39 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FTNT | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 1.58 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| EQH | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 3.44 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| KMT | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| RELX | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| WM | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.66 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| PINS | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 1.40 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| RCAT | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 5.66 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| XENE | 2026-03-27T15:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SMFG | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| UCO | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| PUMP | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| JEF | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| ASTS | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| TWO | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.94 | True | None | predicted_return_threshold |
| SOFI | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 3.22 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| PBI | 2026-03-27T15:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| INDV | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 3.40 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| MTCH | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| NET | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| KRMN | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 1.27 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| NTLA | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| HDB | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 1.51 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| NVST | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ESI | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| MGM | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 2.64 | 0.52 | True | None | predicted_return_threshold |
| A | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| LBRT | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| RBRK | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| SAIL | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| XPO | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| SPOT | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 2.67 | 0.75 | True | None | predicted_return_threshold |
| BWA | 2026-03-27T15:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ENTG | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| FLY | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 16.84 | 0.50 | True | None | predicted_return_threshold, spread_filter, liquidity_sweep_detection |
| AL | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| FLEX | 2026-03-27T15:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.77 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| NG | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 1.52 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MUFG | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 1.51 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| FNB | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ADMA | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8869 | -0.0001 | 3.88 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DYN | 2026-03-27T15:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| BRBR | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| DT | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 2.44 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| NWG | 2026-03-27T15:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 1.80 | 0.85 | False | None | predicted_return_threshold, vwap_relationship |
| DDOG | 2026-03-27T15:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 2.26 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
