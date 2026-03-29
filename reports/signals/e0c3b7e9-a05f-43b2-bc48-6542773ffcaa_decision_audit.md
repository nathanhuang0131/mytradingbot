# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| NVST | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0569 | 0.9900 | -0.0569 | 0.50 | 0.02 | True | None | liquidity_filter |
| USB | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0364 | 0.9900 | 0.0364 | 1.96 | 0.02 | True | None | liquidity_filter |
| BAX | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0105 | 0.9900 | -0.0105 | 0.76 | 0.02 | True | None | liquidity_filter |
| UCO | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0100 | 0.9900 | -0.0100 | 0.50 | 0.03 | True | None | liquidity_filter, intraday_volatility_regime |
| BEN | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0094 | 0.9900 | -0.0094 | 0.50 | 0.01 | True | None | liquidity_filter |
| WULF | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0057 | 0.9900 | 0.0057 | 13.29 | 0.19 | True | None | spread_filter, liquidity_filter |
| BN | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0056 | 0.9900 | -0.0056 | 1.59 | 0.05 | False | None | vwap_relationship, liquidity_filter |
| PONY | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0040 | 0.9900 | -0.0040 | 6.90 | 0.04 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| PL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | -0.0034 | 0.9900 | -0.0034 | 11.44 | 0.32 | True | None | spread_filter, liquidity_filter, intraday_volatility_regime |
| CPRI | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0028 | 0.9891 | 0.0028 | 4.31 | 0.03 | False | None | vwap_relationship, liquidity_filter |
| KRMN | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0028 | 0.9878 | -0.0028 | 0.50 | 0.04 | True | None | liquidity_filter |
| XP | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0028 | 0.9866 | -0.0028 | 0.50 | 0.02 | True | None | liquidity_filter |
| PRGO | 2026-03-27T13:41:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0027 | 0.9854 | 0.0027 | 0.50 | 0.00 | True | None | liquidity_filter |
| ETSY | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0026 | 0.9842 | 0.0026 | 11.09 | 0.10 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| ENPH | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0025 | 0.9830 | 0.0025 | 0.50 | 0.09 | True | None | liquidity_filter |
| ADMA | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0024 | 0.9818 | 0.0024 | 13.03 | 0.73 | True | None | spread_filter, intraday_volatility_regime |
| PRMB | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0024 | 0.9805 | -0.0024 | 0.50 | 0.04 | True | None | liquidity_filter |
| TENB | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0023 | 0.9793 | 0.0023 | 0.50 | 0.02 | True | None | liquidity_filter, intraday_volatility_regime |
| ORLA | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0022 | 0.9781 | -0.0022 | 1.77 | 0.06 | True | None | liquidity_filter |
| DDOG | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0022 | 0.9769 | 0.0022 | 1.50 | 0.11 | True | None | liquidity_filter, intraday_volatility_regime |
| WT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0021 | 0.9757 | -0.0021 | 3.48 | 0.13 | False | None | vwap_relationship, liquidity_filter |
| TSEM | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0019 | 0.9745 | 0.0019 | 0.94 | 0.09 | True | None | liquidity_filter |
| FROG | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | -0.0018 | 0.9732 | -0.0018 | 34.12 | 0.20 | True | None | spread_filter, liquidity_filter, liquidity_sweep_detection, intraday_volatility_regime |
| EQH | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0018 | 0.9720 | -0.0018 | 0.50 | 0.06 | True | None | liquidity_filter |
| S | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0015 | 0.9708 | 0.0015 | 17.01 | 0.37 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| CRWV | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0014 | 0.9696 | 0.0014 | 9.06 | 0.18 | True | None | spread_filter, liquidity_filter |
| JBS | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0013 | 0.9684 | -0.0013 | 3.00 | 0.09 | False | None | vwap_relationship, liquidity_filter |
| ALLY | 2026-03-27T13:44:00+00:00 | qlib_candidate_only | rejected | bracket_invalid | -0.0013 | 0.9672 | -0.0013 | 0.50 | 0.57 | True | False | fee_adjusted_expectancy |
| W | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0013 | 0.9659 | -0.0013 | 1.91 | 0.05 | False | None | vwap_relationship, liquidity_filter |
| DT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0012 | 0.9647 | 0.0012 | 3.49 | 0.23 | False | None | vwap_relationship, liquidity_filter |
| FLNC | 2026-03-27T13:43:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0012 | 0.9635 | -0.0012 | 0.50 | 0.02 | True | None | liquidity_filter |
| HUN | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0012 | 0.9623 | 0.0012 | 0.50 | 0.01 | True | None | liquidity_filter |
| MEOH | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0012 | 0.9611 | -0.0012 | 1.95 | 0.12 | True | None | liquidity_filter, intraday_volatility_regime |
| DASH | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | -0.0011 | 0.9599 | -0.0011 | 9.23 | 0.04 | True | None | spread_filter, liquidity_filter |
| ONDS | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0011 | 0.9586 | 0.0011 | 12.32 | 0.06 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| SNDK | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0011 | 0.9574 | 0.0011 | 6.21 | 0.22 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| U | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0011 | 0.9562 | 0.0011 | 5.19 | 0.05 | True | None | liquidity_filter, intraday_volatility_regime |
| BCS | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0011 | 0.9550 | -0.0011 | 0.50 | 0.01 | True | None | liquidity_filter |
| ZETA | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0011 | 0.9538 | 0.0011 | 1.59 | 0.07 | True | None | liquidity_filter |
| ELAN | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0010 | 0.9526 | -0.0010 | 2.05 | 0.03 | False | None | vwap_relationship, liquidity_filter |
| SAP | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9513 | 0.0010 | 1.52 | 0.03 | True | None | liquidity_filter |
| NTSK | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9501 | 0.0010 | 0.50 | 0.03 | True | None | liquidity_filter |
| FIVN | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9489 | 0.0010 | 0.50 | 0.03 | True | None | liquidity_filter |
| CNC | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0010 | 0.9477 | 0.0010 | 0.50 | 0.01 | True | None | liquidity_filter |
| ARES | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0009 | 0.9465 | 0.0009 | 0.50 | 0.02 | True | None | liquidity_filter |
| SAIL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9453 | 0.0009 | 4.29 | 0.01 | False | None | vwap_relationship, liquidity_filter |
| ORCL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0009 | 0.9440 | 0.0009 | 7.74 | 0.18 | True | None | spread_filter, liquidity_filter |
| NET | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9428 | 0.0009 | 0.50 | 0.05 | False | None | vwap_relationship, liquidity_filter |
| PANW | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9416 | 0.0009 | 13.94 | 0.33 | False | None | vwap_relationship, spread_filter, liquidity_filter, intraday_volatility_regime |
| BBWI | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0009 | 0.9404 | -0.0009 | 4.28 | 0.41 | True | None | liquidity_filter |
| BATL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0008 | 0.9392 | 0.0008 | 4.07 | 0.04 | True | None | liquidity_filter, intraday_volatility_regime |
| IQV | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0008 | 0.9380 | 0.0008 | 4.51 | 0.08 | False | None | vwap_relationship, liquidity_filter |
| PAYX | 2026-03-27T13:42:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0008 | 0.9367 | -0.0008 | 3.15 | 0.07 | False | None | vwap_relationship, liquidity_filter |
| VRT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0008 | 0.9355 | 0.0008 | 10.03 | 0.08 | True | None | spread_filter, liquidity_filter |
| BOX | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0008 | 0.9343 | 0.0008 | 2.67 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0008 | 0.9331 | 0.0008 | 12.05 | 0.07 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| CCL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0008 | 0.9319 | -0.0008 | 10.97 | 0.03 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| SPOT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0008 | 0.9307 | 0.0008 | 2.02 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SOC | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9294 | -0.0007 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| AXTA | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9282 | -0.0007 | 2.76 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NTNX | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9270 | 0.0007 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| CSX | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9258 | -0.0007 | 0.50 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TEAM | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9246 | 0.0007 | 11.57 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| SPGI | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9234 | 0.0007 | 3.89 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| QXO | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9221 | 0.0007 | 7.11 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RIOT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9209 | 0.0007 | 3.75 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| RDDT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9197 | 0.0007 | 6.00 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HMC | 2026-03-27T13:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9185 | -0.0007 | 3.52 | 0.65 | True | None | predicted_return_threshold |
| OC | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9173 | -0.0007 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9161 | 0.0007 | 12.12 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, intraday_volatility_regime |
| FSLY | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9148 | 0.0007 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| BA | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0007 | 0.9136 | -0.0007 | 1.43 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CRBG | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9124 | -0.0006 | 1.06 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TEVA | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9112 | -0.0006 | 0.50 | 0.00 | True | None | predicted_return_threshold, liquidity_filter |
| FTNT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9100 | 0.0006 | 0.50 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CHWY | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9088 | -0.0006 | 6.20 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RKLB | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9075 | 0.0006 | 8.81 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| ESTC | 2026-03-27T13:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9063 | 0.0006 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| IOT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9051 | 0.0006 | 8.85 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| GLL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9039 | 0.0006 | 2.21 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HOOD | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9027 | 0.0006 | 3.14 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CRCL | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9015 | -0.0006 | 5.91 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| ALM | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9002 | -0.0006 | 3.38 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GTLB | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.8990 | 0.0006 | 7.36 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| NTLA | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.8978 | 0.0006 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| REAL | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8966 | 0.0005 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| ZS | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8954 | 0.0005 | 13.46 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, intraday_volatility_regime |
| FIG | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8942 | 0.0005 | 7.25 | 0.04 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| WVE | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8929 | -0.0005 | 7.59 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| TNGX | 2026-03-27T13:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8917 | 0.0005 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| PRCT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8905 | 0.0005 | 2.50 | 1.00 | True | None | predicted_return_threshold |
| BMNR | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8893 | -0.0005 | 9.83 | 0.80 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| TXG | 2026-03-27T13:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8881 | 0.0005 | 7.54 | 0.15 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| ODD | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8869 | 0.0005 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter, intraday_volatility_regime |
| SNOW | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8856 | 0.0005 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter, intraday_volatility_regime |
| BRZE | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8844 | -0.0005 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| CCJ | 2026-03-27T13:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.8832 | -0.0005 | 0.50 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| INTU | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8820 | 0.0005 | 8.19 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RCAT | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8808 | 0.0005 | 14.49 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| DHR | 2026-03-27T13:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.8796 | 0.0005 | 5.15 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
