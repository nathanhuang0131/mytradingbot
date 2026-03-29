# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| NVST | 2026-03-27T13:31:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0569 | 0.9900 | -0.0569 | 0.50 | 0.02 | True | None | liquidity_filter |
| USB | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0364 | 0.9900 | 0.0364 | 0.50 | 0.01 | True | None | liquidity_filter |
| BAX | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0105 | 0.9900 | -0.0105 | 3.03 | 0.01 | False | None | vwap_relationship, liquidity_filter |
| UCO | 2026-03-27T13:30:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0100 | 0.9900 | -0.0100 | 0.50 | 0.06 | True | None | liquidity_filter, intraday_volatility_regime |
| BEN | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0094 | 0.9900 | -0.0094 | 0.50 | 0.00 | True | None | liquidity_filter |
| WULF | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0057 | 0.9900 | 0.0057 | 10.75 | 0.29 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| BN | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0056 | 0.9900 | -0.0056 | 0.50 | 0.00 | True | None | liquidity_filter |
| PONY | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0040 | 0.9900 | -0.0040 | 4.04 | 0.01 | False | None | vwap_relationship, liquidity_filter |
| PL | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0034 | 0.9900 | -0.0034 | 12.91 | 0.13 | False | None | vwap_relationship, spread_filter, liquidity_filter, intraday_volatility_regime |
| CPRI | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0028 | 0.9891 | 0.0028 | 0.50 | 0.01 | True | None | liquidity_filter |
| KRMN | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0028 | 0.9878 | -0.0028 | 0.50 | 0.03 | True | None | liquidity_filter |
| XP | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0028 | 0.9866 | -0.0028 | 0.50 | 0.01 | True | None | liquidity_filter |
| PRGO | 2026-03-27T13:30:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0027 | 0.9854 | 0.0027 | 0.50 | 0.01 | True | None | liquidity_filter |
| ETSY | 2026-03-27T13:32:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0026 | 0.9842 | 0.0026 | 27.06 | 0.14 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection |
| ENPH | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0025 | 0.9830 | 0.0025 | 6.42 | 0.22 | True | None | spread_filter, liquidity_filter |
| ADMA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0024 | 0.9818 | 0.0024 | 57.13 | 0.18 | False | None | vwap_relationship, spread_filter, liquidity_filter, intraday_volatility_regime |
| PRMB | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0024 | 0.9805 | -0.0024 | 0.50 | 0.01 | True | None | liquidity_filter |
| TENB | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0023 | 0.9793 | 0.0023 | 33.33 | 1.00 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection, intraday_volatility_regime |
| ORLA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0022 | 0.9781 | -0.0022 | 4.43 | 0.16 | True | None | liquidity_filter |
| DDOG | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0022 | 0.9769 | 0.0022 | 0.50 | 0.06 | True | None | liquidity_filter |
| WT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0021 | 0.9757 | -0.0021 | 0.50 | 0.02 | True | None | liquidity_filter, intraday_volatility_regime |
| TSEM | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0019 | 0.9745 | 0.0019 | 34.98 | 1.00 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| FROG | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0018 | 0.9732 | -0.0018 | 0.50 | 0.02 | True | None | liquidity_filter, intraday_volatility_regime |
| EQH | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0018 | 0.9720 | -0.0018 | 3.97 | 0.03 | True | None | liquidity_filter |
| S | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0015 | 0.9708 | 0.0015 | 24.70 | 0.08 | False | None | vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| CRWV | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0014 | 0.9696 | 0.0014 | 21.68 | 0.66 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| JBS | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0013 | 0.9684 | -0.0013 | 0.50 | 0.02 | True | None | liquidity_filter |
| ALLY | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0013 | 0.9672 | -0.0013 | 0.50 | 0.02 | True | None | liquidity_filter |
| W | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0013 | 0.9659 | -0.0013 | 0.50 | 0.04 | True | None | liquidity_filter |
| DT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0012 | 0.9647 | 0.0012 | 2.09 | 0.17 | False | None | vwap_relationship, liquidity_filter |
| FLNC | 2026-03-27T13:32:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0012 | 0.9635 | -0.0012 | 7.58 | 0.05 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| HUN | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0012 | 0.9623 | 0.0012 | 19.00 | 0.03 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection |
| MEOH | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0012 | 0.9611 | -0.0012 | 3.03 | 0.21 | True | None | liquidity_filter, intraday_volatility_regime |
| DASH | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0011 | 0.9599 | -0.0011 | 2.01 | 0.01 | True | None | liquidity_filter |
| ONDS | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0011 | 0.9586 | 0.0011 | 23.29 | 0.06 | False | None | vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| SNDK | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0011 | 0.9574 | 0.0011 | 16.08 | 0.17 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection |
| U | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0011 | 0.9562 | 0.0011 | 27.43 | 0.22 | False | None | vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection, intraday_volatility_regime |
| BCS | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0011 | 0.9550 | -0.0011 | 0.50 | 0.01 | True | None | liquidity_filter |
| ZETA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0011 | 0.9538 | 0.0011 | 10.36 | 0.08 | True | None | spread_filter, liquidity_filter |
| ELAN | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0010 | 0.9526 | -0.0010 | 0.50 | 0.01 | True | None | liquidity_filter |
| SAP | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9513 | 0.0010 | 0.91 | 0.01 | True | None | liquidity_filter |
| NTSK | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9501 | 0.0010 | 0.50 | 0.01 | True | None | liquidity_filter |
| FIVN | 2026-03-27T13:31:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9489 | 0.0010 | 0.50 | 0.04 | True | None | liquidity_filter |
| CNC | 2026-03-27T13:32:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0010 | 0.9477 | 0.0010 | 19.10 | 0.06 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection |
| ARES | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0009 | 0.9465 | 0.0009 | 0.50 | 0.01 | True | None | liquidity_filter |
| SAIL | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9453 | 0.0009 | 5.31 | 0.07 | False | None | vwap_relationship, liquidity_filter |
| ORCL | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9440 | 0.0009 | 3.40 | 0.14 | False | None | vwap_relationship, liquidity_filter |
| NET | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0009 | 0.9428 | 0.0009 | 13.27 | 0.16 | True | None | spread_filter, liquidity_filter |
| PANW | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0009 | 0.9416 | 0.0009 | 10.20 | 0.22 | True | None | spread_filter, liquidity_filter, intraday_volatility_regime |
| BBWI | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0009 | 0.9404 | -0.0009 | 5.71 | 0.10 | False | None | vwap_relationship, liquidity_filter |
| BATL | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0008 | 0.9392 | 0.0008 | 55.64 | 1.00 | True | None | spread_filter, liquidity_sweep_detection, intraday_volatility_regime |
| IQV | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0008 | 0.9380 | 0.0008 | 0.50 | 0.02 | True | None | liquidity_filter |
| PAYX | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0008 | 0.9367 | -0.0008 | 0.50 | 0.03 | True | None | liquidity_filter |
| VRT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0008 | 0.9355 | 0.0008 | 9.40 | 0.12 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| BOX | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0008 | 0.9343 | 0.0008 | 5.38 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| UUUU | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0008 | 0.9331 | 0.0008 | 0.72 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| CCL | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0008 | 0.9319 | -0.0008 | 22.74 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| SPOT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0008 | 0.9307 | 0.0008 | 3.72 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| SOC | 2026-03-27T13:32:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9294 | -0.0007 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| AXTA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9282 | -0.0007 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| NTNX | 2026-03-27T13:32:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9270 | 0.0007 | 35.30 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| CSX | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9258 | -0.0007 | 0.50 | 0.01 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TEAM | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9246 | 0.0007 | 5.74 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SPGI | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9234 | 0.0007 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| QXO | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9221 | 0.0007 | 7.12 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RIOT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9209 | 0.0007 | 4.69 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| RDDT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9197 | 0.0007 | 14.43 | 0.50 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| HMC | 2026-03-27T13:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9185 | -0.0007 | 3.52 | 0.65 | True | None | predicted_return_threshold |
| OC | 2026-03-27T13:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9173 | -0.0007 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9161 | 0.0007 | 20.70 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection, intraday_volatility_regime |
| FSLY | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9148 | 0.0007 | 27.54 | 0.17 | True | None | predicted_return_threshold, spread_filter, liquidity_filter, liquidity_sweep_detection |
| BA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9136 | -0.0007 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| CRBG | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9124 | -0.0006 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| TEVA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9112 | -0.0006 | 5.55 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| FTNT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9100 | 0.0006 | 5.78 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| CHWY | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9088 | -0.0006 | 4.28 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RKLB | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9075 | 0.0006 | 20.02 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| ESTC | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9063 | 0.0006 | 7.09 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| IOT | 2026-03-27T13:32:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9051 | 0.0006 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T13:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9039 | 0.0006 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| HOOD | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9027 | 0.0006 | 8.11 | 0.58 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CRCL | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9015 | -0.0006 | 11.05 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| ALM | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9002 | -0.0006 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| GTLB | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.8990 | 0.0006 | 6.07 | 0.12 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| NTLA | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.8978 | 0.0006 | 0.96 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| REAL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8966 | 0.0005 | 6.94 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| ZS | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8954 | 0.0005 | 7.30 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, intraday_volatility_regime |
| FIG | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8942 | 0.0005 | 4.72 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WVE | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8929 | -0.0005 | 3.91 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TNGX | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8917 | 0.0005 | 11.32 | 0.65 | True | None | predicted_return_threshold, spread_filter |
| PRCT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8905 | 0.0005 | 2.50 | 1.00 | True | None | predicted_return_threshold |
| BMNR | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8893 | -0.0005 | 3.93 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| TXG | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8881 | 0.0005 | 8.19 | 0.28 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| ODD | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8869 | 0.0005 | 27.45 | 0.35 | True | None | predicted_return_threshold, spread_filter, liquidity_filter, liquidity_sweep_detection, intraday_volatility_regime |
| SNOW | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8856 | 0.0005 | 4.78 | 0.29 | True | None | predicted_return_threshold, liquidity_filter, intraday_volatility_regime |
| BRZE | 2026-03-27T13:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8844 | -0.0005 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| CCJ | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8832 | -0.0005 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| INTU | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8820 | 0.0005 | 6.01 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RCAT | 2026-03-27T13:34:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8808 | 0.0005 | 19.97 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| DHR | 2026-03-27T13:33:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8796 | 0.0005 | 3.10 | 0.03 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
