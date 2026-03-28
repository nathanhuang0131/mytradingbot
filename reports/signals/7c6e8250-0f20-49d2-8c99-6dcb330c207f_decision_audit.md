# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| ADMA | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0008 | 0.9900 | 0.0008 | 19.79 | 1.00 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| CELH | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 10.18 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ONON | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 6.11 | 0.20 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| INSM | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.60 | True | None | predicted_return_threshold |
| FROG | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 3.44 | 0.52 | True | None | predicted_return_threshold |
| DNLI | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 7.46 | 0.90 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| WAY | 2026-03-27T16:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 5.21 | 0.89 | True | None | predicted_return_threshold |
| QBTS | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 1.79 | 0.86 | True | None | predicted_return_threshold |
| INDV | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| BNL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 1.34 | 1.00 | True | None | predicted_return_threshold |
| SCO | 2026-03-27T16:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| ODFL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 4.41 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| CRBG | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 3.30 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DHI | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 2.57 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PRMB | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 2.74 | 0.83 | False | None | predicted_return_threshold, vwap_relationship |
| LBRT | 2026-03-27T17:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 1.69 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| VSCO | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| GM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 2.71 | 0.58 | False | None | predicted_return_threshold, vwap_relationship |
| IBKR | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 5.60 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| TAP | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 7.23 | 0.50 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RCL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 3.60 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| LULU | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 3.78 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ODD | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.65 | True | None | predicted_return_threshold |
| TSEM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 3.21 | 0.78 | False | None | predicted_return_threshold, vwap_relationship |
| OKE | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 2.65 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| VIK | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 0.50 | 0.77 | True | None | predicted_return_threshold |
| DAL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 6.67 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| QURE | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| SPOT | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 3.07 | 0.94 | False | None | predicted_return_threshold, vwap_relationship |
| DOCS | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 3.70 | 0.88 | False | None | predicted_return_threshold, vwap_relationship |
| NU | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.81 | 0.80 | False | None | predicted_return_threshold, vwap_relationship |
| COF | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 3.17 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PSTG | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.62 | True | None | predicted_return_threshold |
| WELL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.83 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TRGP | 2026-03-27T17:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 1.84 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| ALKS | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 3.83 | 1.00 | True | None | predicted_return_threshold |
| Q | 2026-03-27T17:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 2.47 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| UCO | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.83 | True | None | predicted_return_threshold |
| LNC | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 2.90 | 0.80 | False | None | predicted_return_threshold, vwap_relationship |
| F | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 2.19 | 0.63 | False | None | predicted_return_threshold, vwap_relationship |
| RCAT | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.97 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NESR | 2026-03-27T17:00:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 5.18 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| HBAN | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 2.46 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DOCN | 2026-03-27T17:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 5.58 | 0.80 | False | None | predicted_return_threshold, vwap_relationship |
| MET | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 3.50 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SMFG | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.65 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CNH | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 5.76 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| KMI | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 2.18 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| CF | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 1.77 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| STM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 1.53 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| NI | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.08 | 1.00 | True | None | predicted_return_threshold |
| ALM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 4.99 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| PANW | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.60 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 1.44 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| ALK | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 4.03 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GE | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 2.20 | 0.89 | True | None | predicted_return_threshold |
| AAOI | 2026-03-27T17:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| UBS | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 2.04 | 0.63 | False | None | predicted_return_threshold, vwap_relationship |
| ES | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 2.04 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| AAL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 3.59 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FOLD | 2026-03-27T16:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.87 | 1.00 | True | None | predicted_return_threshold |
| VSNT | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 2.82 | 0.81 | False | None | predicted_return_threshold, vwap_relationship |
| BJ | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 3.01 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FLEX | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| ALKT | 2026-03-27T16:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| GPK | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 2.72 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PFE | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 2.29 | 0.85 | False | None | predicted_return_threshold, vwap_relationship |
| PDD | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.99 | 0.52 | True | None | predicted_return_threshold |
| UPS | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 2.37 | 0.76 | False | None | predicted_return_threshold, vwap_relationship |
| PENN | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 3.62 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RYN | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 1.23 | 0.87 | False | None | predicted_return_threshold, vwap_relationship |
| WDC | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 1.35 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KKR | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 3.10 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
| BATL | 2026-03-27T17:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| ADM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| CCJ | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| SMCI | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 4.59 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| APO | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 4.57 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RKLB | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 1.01 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| IONQ | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 2.22 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.91 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| LAZ | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ZSL | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| HD | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 1.69 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PL | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| BOIL | 2026-03-27T17:02:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| RUN | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 2.98 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HMC | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.51 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| DXCM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8905 | -0.0001 | 2.99 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GLW | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 2.21 | 0.62 | True | None | predicted_return_threshold |
| SEI | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| NET | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| XPEV | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 6.57 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| FTNT | 2026-03-27T17:01:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 3.85 | 0.52 | True | None | predicted_return_threshold |
| FLY | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 1.05 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| AM | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 2.67 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| ALAB | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| CAT | 2026-03-27T17:03:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 1.25 | 0.51 | False | None | predicted_return_threshold, vwap_relationship |
