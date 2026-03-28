# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| HTGC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9900 | -0.0006 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| FLG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 3.82 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| MRNA | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 5.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| PRCT | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 4.57 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| ALHC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 8.24 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| VG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 2.89 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RHI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9900 | 0.0001 | 1.01 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ADMA | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9900 | 0.0001 | 4.08 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| STNE | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9891 | 0.0001 | 2.77 | 1.00 | True | None | predicted_return_threshold |
| SSNC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 0.96 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DFTX | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| AESI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| CPB | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 3.41 | 0.58 | True | None | predicted_return_threshold |
| DOCN | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 2.16 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| QXO | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 2.63 | 0.93 | False | None | predicted_return_threshold, vwap_relationship |
| SAIL | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 2.12 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HIMS | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 7.13 | 0.78 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| UUUU | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| APLD | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 2.10 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| LRCX | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| VICI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9745 | -0.0001 | 1.41 | 0.61 | True | None | predicted_return_threshold |
| HBM | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 6.70 | 0.51 | True | None | predicted_return_threshold, spread_filter |
| SOC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.68 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CAI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 11.30 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| GLXY | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9672 | -0.0001 | 15.13 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection, intraday_volatility_regime |
| ORLA | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 2.58 | 0.40 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FND | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 2.74 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| MRK | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 1.36 | 0.40 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AJG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 3.50 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| OKLO | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| IOT | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 2.09 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.58 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| WVE | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9574 | -0.0001 | 23.44 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter, liquidity_sweep_detection |
| RGTI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 6.57 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| BRZE | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| DHT | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9538 | -0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| FLNC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| FNB | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.77 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WHR | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| DLTR | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9489 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| PLNT | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9477 | 0.0000 | 2.36 | 0.55 | False | None | predicted_return_threshold, vwap_relationship |
| GME | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9465 | 0.0000 | 1.69 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| WFRD | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9453 | 0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| OKTA | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9440 | -0.0000 | 0.52 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| GPGI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9428 | 0.0000 | 2.33 | 0.77 | False | None | predicted_return_threshold, vwap_relationship |
| CRBG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9416 | 0.0000 | 3.34 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DKNG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9404 | 0.0000 | 10.22 | 0.80 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| SCHW | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9392 | -0.0000 | 0.81 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CCJ | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9380 | 0.0000 | 1.69 | 0.82 | True | None | predicted_return_threshold |
| LTH | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9367 | 0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| BRO | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9355 | 0.0000 | 1.96 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FRO | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9343 | 0.0000 | 4.45 | 1.00 | True | None | predicted_return_threshold |
| MAS | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9331 | 0.0000 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| DELL | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9319 | 0.0000 | 1.31 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| RF | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9307 | 0.0000 | 2.49 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KVUE | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9294 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SUNB | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9282 | 0.0000 | 1.74 | 0.52 | True | None | predicted_return_threshold |
| S | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9270 | -0.0000 | 0.99 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BANC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9258 | 0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| COIN | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9246 | 0.0000 | 3.11 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DX | 2026-03-27T19:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9234 | -0.0000 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| UPST | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9221 | -0.0000 | 0.50 | 0.65 | True | None | predicted_return_threshold |
| RDDT | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 2.68 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ETN | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 0.50 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FBIN | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 3.59 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.73 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SE | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9161 | -0.0000 | 2.07 | 1.00 | True | None | predicted_return_threshold |
| WMG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9148 | -0.0000 | 0.52 | 0.72 | True | None | predicted_return_threshold |
| SCO | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| EBC | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 0.66 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| LUNR | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 5.65 | 0.74 | False | None | predicted_return_threshold, vwap_relationship |
| CENX | 2026-03-27T19:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9100 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 0.50 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| ZS | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9075 | -0.0000 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| SMR | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 1.20 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| BLDR | 2026-03-27T19:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| GLNG | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| CSTM | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 0.50 | 0.56 | True | None | predicted_return_threshold |
| TRP | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| XPO | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| BROS | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| BNL | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.50 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| AMT | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8966 | -0.0000 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8954 | -0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| BEN | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 1.11 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ENPH | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.67 | 0.53 | True | None | predicted_return_threshold |
| ADI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| FRPT | 2026-03-27T19:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| HL | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 2.82 | 0.94 | False | None | predicted_return_threshold, vwap_relationship |
| AXTI | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 5.84 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| SVM | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 2.46 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GNTX | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8856 | -0.0000 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| ENB | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8844 | -0.0000 | 0.50 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| VLY | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| CHWY | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8820 | -0.0000 | 0.96 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| SOLS | 2026-03-27T19:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 5.02 | 1.00 | True | None | predicted_return_threshold |
| ZBH | 2026-03-27T19:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8796 | -0.0000 | 0.99 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
