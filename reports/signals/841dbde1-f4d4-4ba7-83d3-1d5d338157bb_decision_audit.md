# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| PRCT | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0011 | 0.9900 | 0.0011 | 5.63 | 0.51 | False | None | vwap_relationship |
| FIG | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 5.00 | 1.00 | True | None | predicted_return_threshold |
| MRNA | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 4.96 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| RIOT | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 4.90 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| Q | 2026-03-27T19:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 3.96 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BATL | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SN | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.70 | 1.00 | True | None | predicted_return_threshold |
| JHX | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 3.44 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SMTC | 2026-03-27T19:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| QURE | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| ZETA | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 9.40 | 0.72 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| TSEM | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| LSCC | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ILMN | 2026-03-27T19:05:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| ALLY | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 1.98 | 1.00 | True | None | predicted_return_threshold |
| TNGX | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 3.86 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| UUUU | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 3.54 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| VLO | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 1.87 | 0.76 | True | None | predicted_return_threshold |
| BANC | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 1.47 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| CHYM | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.47 | 1.00 | True | None | predicted_return_threshold |
| AXTI | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.50 | 0.72 | True | None | predicted_return_threshold |
| INFY | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 2.93 | 0.66 | True | None | predicted_return_threshold |
| EQH | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 2.82 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RUN | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 2.00 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| ABNB | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 2.24 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BOX | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 3.26 | 0.70 | False | None | predicted_return_threshold, vwap_relationship |
| PBF | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 3.19 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NVAX | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.68 | True | None | predicted_return_threshold |
| SYF | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.73 | True | None | predicted_return_threshold |
| INVH | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 3.59 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SNDK | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 7.04 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| VTRS | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.95 | 0.71 | False | None | predicted_return_threshold, vwap_relationship |
| SMCI | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 3.49 | 1.00 | True | None | predicted_return_threshold |
| FSLY | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.92 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| KRMN | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 1.16 | 1.00 | True | None | predicted_return_threshold |
| XP | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 2.12 | 0.76 | False | None | predicted_return_threshold, vwap_relationship |
| ZM | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.64 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| MKSI | 2026-03-27T19:04:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| C | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 1.39 | 0.95 | False | None | predicted_return_threshold, vwap_relationship |
| NTSK | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| GFI | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 2.39 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| VST | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 1.37 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T19:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| AMZN | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 4.89 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| SRPT | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9453 | -0.0001 | 1.24 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NTLA | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 1.03 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| BEAM | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| ARCC | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.72 | 0.60 | True | None | predicted_return_threshold |
| KSS | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SWKS | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.40 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| BRO | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 1.56 | 1.00 | True | None | predicted_return_threshold |
| YPF | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 1.67 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VRT | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| IAG | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 2.13 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LBRT | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 5.14 | 0.57 | True | None | predicted_return_threshold |
| MEOH | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 1.94 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SBRA | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.59 | True | None | predicted_return_threshold |
| FLY | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9294 | -0.0001 | 3.65 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| BW | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| FOLD | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.70 | True | None | predicted_return_threshold |
| WDC | 2026-03-27T18:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9258 | -0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| KMI | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 1.46 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AGNC | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.00 | True | None | predicted_return_threshold, liquidity_filter |
| UMAC | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| NVDA | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 2.54 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LCID | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 3.94 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GTX | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.70 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| RNA | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| PAGS | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9161 | -0.0000 | 3.86 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TENB | 2026-03-27T19:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9148 | 0.0000 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| AESI | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 1.88 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| NG | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| CRBG | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 2.23 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| TNDM | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9100 | -0.0000 | 2.96 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| KVYO | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9075 | -0.0000 | 2.01 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| IONS | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| VITL | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| NCLH | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 4.76 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AFRM | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9027 | -0.0000 | 10.34 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| ZSL | 2026-03-27T19:06:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ON | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| HMY | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| F | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 2.21 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AS | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 4.02 | 0.73 | False | None | predicted_return_threshold, vwap_relationship |
| MPC | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 0.50 | 0.63 | True | None | predicted_return_threshold |
| TXN | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 0.50 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DXCM | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.60 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| EW | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 4.26 | 0.55 | True | None | predicted_return_threshold |
| AMKR | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 5.06 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SPGI | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 0.50 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| CSGP | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 1.25 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| STNE | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ROKU | 2026-03-27T19:08:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 0.50 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CHWY | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 5.30 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| CUK | 2026-03-27T19:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 3.17 | 0.87 | True | None | predicted_return_threshold |
| BIRK | 2026-03-27T19:05:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 1.48 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| SCHW | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 1.77 | 0.91 | True | None | predicted_return_threshold |
| SEI | 2026-03-27T19:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
