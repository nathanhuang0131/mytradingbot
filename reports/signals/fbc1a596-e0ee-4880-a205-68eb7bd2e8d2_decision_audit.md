# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| ADMA | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0008 | 0.9900 | 0.0008 | 3.95 | 0.20 | True | None | liquidity_filter |
| CELH | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 0.73 | 0.63 | True | None | predicted_return_threshold |
| ONON | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 1.91 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| INSM | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| FROG | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 1.44 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| DNLI | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 4.05 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WAY | 2026-03-27T17:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 7.32 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| QBTS | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 3.59 | 0.06 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| INDV | 2026-03-27T17:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| BNL | 2026-03-27T17:09:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| SCO | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9878 | 0.0002 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ODFL | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 5.60 | 1.00 | True | None | predicted_return_threshold |
| CRBG | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 2.75 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| DHI | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| PRMB | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| LBRT | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 1.28 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| VSCO | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| GM | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| IBKR | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| TAP | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| RCL | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 1.00 | 0.54 | False | None | predicted_return_threshold, vwap_relationship |
| LULU | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 0.60 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ODD | 2026-03-27T17:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| OKE | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| VIK | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| DAL | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.95 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| QURE | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 0.50 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| SPOT | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| DOCS | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| NU | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.90 | True | None | predicted_return_threshold |
| COF | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| PSTG | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| WELL | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.51 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TRGP | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 1.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| ALKS | 2026-03-27T17:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 2.97 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| Q | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| UCO | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| LNC | 2026-03-27T17:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| F | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| RCAT | 2026-03-27T17:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| NESR | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 1.73 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| HBAN | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.64 | 1.00 | True | None | predicted_return_threshold |
| DOCN | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 3.56 | 0.68 | True | None | predicted_return_threshold |
| MET | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| SMFG | 2026-03-27T17:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| CNH | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| KMI | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| CF | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.66 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| STM | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| NI | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| ALM | 2026-03-27T17:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.83 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 1.39 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| PANW | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.52 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T17:10:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 5.76 | 0.75 | False | None | predicted_return_threshold, vwap_relationship |
| ALK | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 1.01 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| GE | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| AAOI | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| UBS | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ES | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| AAL | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.00 | True | None | predicted_return_threshold, liquidity_filter |
| FOLD | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| VSNT | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.54 | True | None | predicted_return_threshold |
| BJ | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 0.50 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FLEX | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.58 | 0.66 | True | None | predicted_return_threshold |
| ALKT | 2026-03-27T17:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| GPK | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.55 | True | None | predicted_return_threshold |
| PFE | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| PDD | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| UPS | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 0.53 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PENN | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| RYN | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| WDC | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 3.91 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| KKR | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| ADM | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| CCJ | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.50 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BEAM | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| SMCI | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 2.30 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| APO | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RKLB | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 1.62 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| IONQ | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 2.23 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FSLY | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| LAZ | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 2.15 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ZSL | 2026-03-27T17:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8978 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| HD | 2026-03-27T17:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 0.54 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| PL | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 2.80 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BOIL | 2026-03-27T17:13:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 1.44 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RUN | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| HMC | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| DXCM | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8905 | -0.0001 | 0.50 | 0.90 | True | None | predicted_return_threshold |
| GLW | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 1.29 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| NET | 2026-03-27T17:12:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| XPEV | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| FTNT | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| FLY | 2026-03-27T17:16:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| AM | 2026-03-27T17:14:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| ALAB | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| CAT | 2026-03-27T17:15:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
