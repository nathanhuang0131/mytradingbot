# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| PRCT | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0011 | 0.9900 | 0.0011 | 2.36 | 0.21 | True | None | liquidity_filter |
| FIG | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 1.86 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| MRNA | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| RIOT | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.98 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| Q | 2026-03-27T19:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SN | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| JHX | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.06 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| SMTC | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 17.01 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| QURE | 2026-03-27T19:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| ZETA | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 5.93 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| TSEM | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| LSCC | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 4.55 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| ILMN | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ALLY | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 0.99 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| TNGX | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 1.41 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| VLO | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| BANC | 2026-03-27T19:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| CHYM | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.47 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 4.17 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| INFY | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 3.90 | 1.00 | True | None | predicted_return_threshold |
| EQH | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.70 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| RUN | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 4.97 | 0.76 | True | None | predicted_return_threshold |
| ABNB | 2026-03-27T19:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.81 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BOX | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 1.09 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| PBF | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| NVAX | 2026-03-27T19:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| SYF | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 1.53 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| INVH | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 2.05 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SNDK | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| VTRS | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| SMCI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 5.19 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 3.19 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| KRMN | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| XP | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 1.41 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| ZM | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 1.78 | 0.30 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MKSI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 2.25 | 1.00 | True | None | predicted_return_threshold |
| C | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NTSK | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 4.80 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| GFI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| VST | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.64 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.58 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WSC | 2026-03-27T19:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 2.91 | 0.70 | True | None | predicted_return_threshold |
| AMZN | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 1.25 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SRPT | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9453 | -0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| NTLA | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ARCC | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| KSS | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 7.08 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| SWKS | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.86 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| BRO | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| YPF | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| VRT | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 2.68 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| IAG | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.12 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| LBRT | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 2.57 | 0.32 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MEOH | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 3.09 | 0.50 | True | None | predicted_return_threshold, liquidity_filter |
| SBRA | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| FLY | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9294 | -0.0001 | 5.72 | 0.65 | True | None | predicted_return_threshold |
| BW | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 2.55 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| FOLD | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| WDC | 2026-03-27T19:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9258 | -0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| KMI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| AGNC | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| UMAC | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 2.09 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| NVDA | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 0.97 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LCID | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| GTX | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| RNA | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| PAGS | 2026-03-27T19:18:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9161 | -0.0000 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| TENB | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9148 | 0.0000 | 5.32 | 1.00 | True | None | predicted_return_threshold |
| AESI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 0.94 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NG | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 1.52 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| CRBG | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 8.87 | 0.71 | True | None | predicted_return_threshold, spread_filter |
| TNDM | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9100 | -0.0000 | 5.95 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 0.50 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| KVYO | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9075 | -0.0000 | 1.34 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| IONS | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 0.50 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| VITL | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| NCLH | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 1.35 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AFRM | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9027 | -0.0000 | 2.95 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ZSL | 2026-03-27T19:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| ON | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 3.65 | 0.51 | True | None | predicted_return_threshold |
| HMY | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 1.76 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| F | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 1.10 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| AS | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 1.60 | 0.55 | True | None | predicted_return_threshold |
| MPC | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| TXN | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| DXCM | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| EW | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 1.89 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| AMKR | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| SPGI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| CSGP | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.63 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| STNE | 2026-03-27T19:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ROKU | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| CHWY | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 4.77 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| CUK | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 3.16 | 0.69 | False | None | predicted_return_threshold, vwap_relationship |
| BIRK | 2026-03-27T19:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| SCHW | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T19:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 7.67 | 0.92 | True | None | predicted_return_threshold, spread_filter |
