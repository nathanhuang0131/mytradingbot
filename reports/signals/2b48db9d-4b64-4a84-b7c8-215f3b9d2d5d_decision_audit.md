# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| SMCI | 2026-03-26T20:34:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0078 | 0.9900 | -0.0078 | 3.34 | 0.01 | True | None | liquidity_filter |
| IREN | 2026-03-26T20:41:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0021 | 0.9900 | -0.0021 | 0.50 | 0.01 | True | None | liquidity_filter |
| SOFI | 2026-03-27T12:51:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0016 | 0.9900 | 0.0016 | 0.50 | 0.00 | True | None | liquidity_filter |
| ODD | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | bracket_invalid | 0.0015 | 0.9900 | 0.0015 | 5.58 | 1.00 | True | False | fee_adjusted_expectancy |
| CSX | 2026-03-26T20:11:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0013 | 0.9900 | 0.0013 | 0.50 | 0.01 | True | None | liquidity_filter |
| DYN | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | bracket_invalid | 0.0013 | 0.9900 | 0.0013 | 4.72 | 1.00 | True | False | fee_adjusted_expectancy |
| VTR | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0013 | 0.9900 | -0.0013 | 5.29 | 1.00 | False | None | vwap_relationship |
| LOW | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | bracket_invalid | -0.0011 | 0.9900 | -0.0011 | 4.98 | 1.00 | True | False | fee_adjusted_expectancy |
| HD | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0011 | 0.9900 | -0.0011 | 2.74 | 1.00 | False | None | vwap_relationship |
| PK | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0010 | 0.9889 | 0.0010 | 7.00 | 1.00 | True | None | spread_filter |
| AMKR | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0010 | 0.9877 | 0.0010 | 2.77 | 1.00 | False | None | vwap_relationship |
| SOC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0010 | 0.9865 | 0.0010 | 18.13 | 1.00 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| CPNG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | spread_too_wide | 0.0009 | 0.9852 | 0.0009 | 12.89 | 1.00 | True | None | spread_filter, liquidity_sweep_detection |
| KRMN | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0009 | 0.9840 | 0.0009 | 13.23 | 1.00 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| AAL | 2026-03-26T20:11:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0009 | 0.9828 | -0.0009 | 0.50 | 0.00 | True | None | liquidity_filter |
| ERAS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | 0.0008 | 0.9815 | 0.0008 | 4.13 | 0.74 | False | None | vwap_relationship |
| VG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9803 | 0.0007 | 8.18 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9791 | 0.0007 | 4.63 | 1.00 | True | None | predicted_return_threshold |
| PRGO | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0007 | 0.9779 | 0.0007 | 9.33 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| NVST | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9766 | 0.0006 | 2.90 | 1.00 | True | None | predicted_return_threshold |
| ZSL | 2026-03-27T12:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9754 | -0.0006 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| FIG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9742 | 0.0006 | 9.58 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| WAL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9729 | 0.0006 | 4.27 | 1.00 | True | None | predicted_return_threshold |
| ADMA | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9717 | -0.0006 | 13.58 | 0.97 | True | None | predicted_return_threshold, spread_filter |
| CARR | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9705 | 0.0006 | 6.18 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ES | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.9692 | -0.0005 | 2.02 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| REAL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9680 | 0.0005 | 6.94 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| PSKY | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9668 | 0.0005 | 5.64 | 1.00 | True | None | predicted_return_threshold |
| NESR | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.9656 | -0.0005 | 16.90 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| TNGX | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9643 | 0.0005 | 11.32 | 0.65 | True | None | predicted_return_threshold, spread_filter |
| SMTC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9631 | 0.0005 | 5.23 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PRCT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9619 | 0.0005 | 2.50 | 1.00 | True | None | predicted_return_threshold |
| PATH | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9606 | 0.0005 | 9.06 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| RNA | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9594 | 0.0005 | 11.45 | 0.73 | True | None | predicted_return_threshold, spread_filter |
| ANET | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9582 | 0.0005 | 5.30 | 1.00 | True | None | predicted_return_threshold |
| FLY | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.9569 | -0.0005 | 20.02 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| SFM | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9557 | 0.0004 | 9.22 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| DUOL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9545 | 0.0004 | 3.69 | 1.00 | True | None | predicted_return_threshold |
| INFY | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9533 | -0.0004 | 6.64 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ALKT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9520 | 0.0004 | 3.09 | 1.00 | True | None | predicted_return_threshold |
| Q | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9508 | 0.0004 | 7.77 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| QXO | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9496 | 0.0004 | 11.44 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| SATS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9483 | 0.0004 | 4.04 | 1.00 | True | None | predicted_return_threshold |
| AKAM | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9471 | 0.0004 | 4.90 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FPS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9459 | 0.0004 | 8.30 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| FSLY | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9446 | -0.0004 | 18.78 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| FRPT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9434 | 0.0004 | 6.81 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| CHWY | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9422 | 0.0004 | 5.09 | 1.00 | True | None | predicted_return_threshold |
| NTSK | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9410 | 0.0004 | 4.42 | 1.00 | True | None | predicted_return_threshold |
| CORZ | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9397 | 0.0004 | 10.28 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| ARIS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9385 | 0.0004 | 4.54 | 0.61 | False | None | predicted_return_threshold, vwap_relationship |
| BTSG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9373 | -0.0004 | 4.67 | 0.76 | False | None | predicted_return_threshold, vwap_relationship |
| SLDE | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9360 | 0.0004 | 6.93 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| UMAC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9348 | 0.0004 | 5.60 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| TXG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9336 | 0.0004 | 6.11 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| HAL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9323 | 0.0003 | 9.34 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| UEC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9311 | 0.0003 | 4.79 | 1.00 | True | None | predicted_return_threshold |
| CIEN | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9299 | 0.0003 | 2.06 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| OLN | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9287 | 0.0003 | 5.68 | 1.00 | True | None | predicted_return_threshold |
| BRKR | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9274 | 0.0003 | 6.37 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| M | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9262 | 0.0003 | 4.06 | 1.00 | True | None | predicted_return_threshold |
| FND | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9250 | 0.0003 | 6.66 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| AG | 2026-03-27T12:11:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9237 | 0.0003 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| TENB | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9225 | 0.0003 | 10.25 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| FSK | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9213 | 0.0003 | 6.14 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| BAX | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9200 | 0.0003 | 9.01 | 0.87 | True | None | predicted_return_threshold, spread_filter |
| KTOS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9188 | 0.0003 | 2.47 | 1.00 | True | None | predicted_return_threshold |
| GM | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9176 | 0.0003 | 5.62 | 0.88 | True | None | predicted_return_threshold |
| PAAS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9164 | 0.0003 | 4.03 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CRBG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9151 | 0.0003 | 5.12 | 1.00 | True | None | predicted_return_threshold |
| TRI | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9139 | 0.0003 | 2.35 | 1.00 | True | None | predicted_return_threshold |
| CCL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9127 | -0.0003 | 3.95 | 1.00 | True | None | predicted_return_threshold |
| VXX | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9114 | 0.0003 | 6.13 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| DASH | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9102 | 0.0003 | 2.63 | 0.54 | True | None | predicted_return_threshold |
| FIVN | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9090 | 0.0003 | 4.14 | 1.00 | True | None | predicted_return_threshold |
| MAT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9077 | 0.0003 | 5.99 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| HRL | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9065 | 0.0003 | 5.47 | 1.00 | True | None | predicted_return_threshold |
| QURE | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9053 | 0.0003 | 7.20 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| PAGS | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9041 | 0.0003 | 6.34 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ARM | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9028 | 0.0003 | 3.80 | 1.00 | True | None | predicted_return_threshold |
| MKSI | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9016 | 0.0003 | 3.11 | 1.00 | True | None | predicted_return_threshold |
| ELAN | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9004 | 0.0003 | 6.10 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| MMM | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8991 | 0.0003 | 2.34 | 1.00 | True | None | predicted_return_threshold |
| ACHC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8979 | 0.0003 | 2.62 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| NET | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8967 | 0.0003 | 4.64 | 1.00 | True | None | predicted_return_threshold |
| FROG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8954 | 0.0003 | 7.98 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| CAVA | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8942 | 0.0003 | 4.75 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CAT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8930 | 0.0003 | 5.03 | 1.00 | True | None | predicted_return_threshold |
| NOG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8918 | 0.0003 | 3.29 | 1.00 | True | None | predicted_return_threshold |
| HOG | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8905 | 0.0003 | 8.97 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| CVNA | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.8893 | 0.0003 | 4.14 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CPRI | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8881 | 0.0002 | 6.42 | 0.83 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| XP | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8868 | 0.0002 | 4.71 | 1.00 | True | None | predicted_return_threshold |
| AMPX | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8856 | 0.0002 | 6.55 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| YUMC | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8844 | 0.0002 | 6.00 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| BZ | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8831 | 0.0002 | 6.46 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| PRMB | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8819 | 0.0002 | 5.59 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| VRT | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8807 | 0.0002 | 3.17 | 1.00 | True | None | predicted_return_threshold |
| NLY | 2026-03-26T19:59:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8795 | 0.0002 | 5.34 | 1.00 | True | None | predicted_return_threshold |
| GOOGL | 2026-03-27T12:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.8782 | 0.0002 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
