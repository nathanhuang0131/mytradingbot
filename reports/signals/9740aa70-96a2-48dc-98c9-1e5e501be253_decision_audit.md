# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| HTGC | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0006 | 0.9900 | -0.0006 | 3.63 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| FLG | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 7.62 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| MRNA | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 2.00 | 0.52 | True | None | predicted_return_threshold |
| PRCT | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 7.10 | 0.58 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| FSLY | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 3.67 | 0.57 | True | None | predicted_return_threshold |
| ALHC | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9900 | 0.0002 | 3.01 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| VG | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9900 | -0.0002 | 18.85 | 1.00 | True | None | predicted_return_threshold, spread_filter, liquidity_sweep_detection |
| RHI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9900 | 0.0001 | 3.03 | 0.86 | False | None | predicted_return_threshold, vwap_relationship |
| ADMA | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9900 | 0.0001 | 1.35 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| STNE | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9891 | 0.0001 | 3.68 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| SSNC | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9878 | 0.0001 | 4.38 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DFTX | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9866 | 0.0001 | 6.97 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| AESI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9854 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| CPB | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9842 | 0.0001 | 4.57 | 0.66 | False | None | predicted_return_threshold, vwap_relationship |
| DOCN | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9830 | 0.0001 | 7.10 | 0.71 | True | None | predicted_return_threshold, spread_filter |
| QXO | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 3.95 | 0.97 | False | None | predicted_return_threshold, vwap_relationship |
| SAIL | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 4.21 | 0.97 | False | None | predicted_return_threshold, vwap_relationship |
| HIMS | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 7.77 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| UUUU | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 5.68 | 0.32 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| APLD | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 3.69 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| LRCX | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 5.71 | 0.83 | False | None | predicted_return_threshold, vwap_relationship |
| VICI | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9745 | -0.0001 | 2.81 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| HBM | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 1.93 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| PONY | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 8.07 | 0.31 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| SOC | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 3.43 | 0.52 | False | None | predicted_return_threshold, vwap_relationship |
| CAI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 2.98 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GLXY | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 6.89 | 0.58 | True | None | predicted_return_threshold, spread_filter |
| BATL | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9672 | -0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| ORLA | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 3.46 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| FND | 2026-03-27T19:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 1.00 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| MRK | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 2.18 | 0.91 | True | None | predicted_return_threshold |
| AJG | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 4.44 | 0.88 | True | None | predicted_return_threshold |
| OKLO | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 1.47 | 0.52 | False | None | predicted_return_threshold, vwap_relationship |
| IOT | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 2.08 | 0.87 | True | None | predicted_return_threshold |
| CC | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.59 | True | None | predicted_return_threshold |
| WVE | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9574 | -0.0001 | 11.61 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RGTI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 1.88 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BRZE | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 9.86 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| DHT | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9538 | -0.0001 | 0.50 | 0.85 | True | None | predicted_return_threshold |
| FLNC | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 2.64 | 0.77 | False | None | predicted_return_threshold, vwap_relationship |
| FNB | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.63 | True | None | predicted_return_threshold |
| WHR | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 1.44 | 1.00 | True | None | predicted_return_threshold |
| DLTR | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9489 | 0.0000 | 4.58 | 0.68 | True | None | predicted_return_threshold |
| PLNT | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9477 | 0.0000 | 1.86 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GME | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9465 | 0.0000 | 1.13 | 0.79 | False | None | predicted_return_threshold, vwap_relationship |
| WFRD | 2026-03-27T19:23:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9453 | 0.0000 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| OKTA | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9440 | -0.0000 | 3.08 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GPGI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9428 | 0.0000 | 1.55 | 0.74 | False | None | predicted_return_threshold, vwap_relationship |
| CRBG | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9416 | 0.0000 | 7.74 | 0.87 | True | None | predicted_return_threshold, spread_filter |
| DKNG | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9404 | 0.0000 | 4.21 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SCHW | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9392 | -0.0000 | 1.08 | 0.99 | False | None | predicted_return_threshold, vwap_relationship |
| CCJ | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9380 | 0.0000 | 2.29 | 0.44 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LTH | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9367 | 0.0000 | 1.92 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BRO | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9355 | 0.0000 | 3.12 | 1.00 | True | None | predicted_return_threshold |
| FRO | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9343 | 0.0000 | 1.86 | 1.00 | True | None | predicted_return_threshold |
| MAS | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9331 | 0.0000 | 2.93 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DELL | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9319 | 0.0000 | 5.68 | 0.80 | True | None | predicted_return_threshold |
| RF | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9307 | 0.0000 | 0.99 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| KVUE | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9294 | 0.0000 | 1.42 | 0.95 | True | None | predicted_return_threshold |
| SUNB | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9282 | 0.0000 | 3.09 | 0.86 | False | None | predicted_return_threshold, vwap_relationship |
| S | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9270 | -0.0000 | 1.98 | 0.54 | True | None | predicted_return_threshold |
| BANC | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9258 | 0.0000 | 0.50 | 0.55 | True | None | predicted_return_threshold |
| COIN | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9246 | 0.0000 | 1.70 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DX | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9234 | -0.0000 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| UPST | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9221 | -0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| RDDT | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9209 | 0.0000 | 3.26 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ETN | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9197 | 0.0000 | 2.13 | 1.00 | True | None | predicted_return_threshold |
| FBIN | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9185 | 0.0000 | 0.98 | 0.59 | False | None | predicted_return_threshold, vwap_relationship |
| TSEM | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9173 | 0.0000 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| SE | 2026-03-27T19:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9161 | -0.0000 | 0.96 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WMG | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9148 | -0.0000 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| SCO | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9136 | 0.0000 | 6.41 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| EBC | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9124 | 0.0000 | 1.97 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LUNR | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9112 | 0.0000 | 2.79 | 0.63 | True | None | predicted_return_threshold |
| CENX | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9100 | 0.0000 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T19:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9088 | 0.0000 | 0.56 | 0.95 | True | None | predicted_return_threshold |
| ZS | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9075 | -0.0000 | 3.83 | 0.70 | False | None | predicted_return_threshold, vwap_relationship |
| SMR | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9063 | 0.0000 | 4.82 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| BLDR | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 1.55 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| GLNG | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 2.51 | 0.92 | False | None | predicted_return_threshold, vwap_relationship |
| CSTM | 2026-03-27T19:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 0.50 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| TRP | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.75 | False | None | predicted_return_threshold, vwap_relationship |
| XPO | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9002 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| BROS | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 2.14 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BNL | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.68 | 0.82 | True | None | predicted_return_threshold |
| AMT | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8966 | -0.0000 | 0.50 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| BEAM | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8954 | -0.0000 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| BEN | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 1.66 | 0.76 | False | None | predicted_return_threshold, vwap_relationship |
| ENPH | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 4.97 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ADI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 1.30 | 0.40 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FRPT | 2026-03-27T19:29:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| HL | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 2.10 | 0.43 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 2.92 | 0.35 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SVM | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 1.22 | 0.91 | False | None | predicted_return_threshold, vwap_relationship |
| GNTX | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8856 | -0.0000 | 0.57 | 0.52 | False | None | predicted_return_threshold, vwap_relationship |
| ENB | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8844 | -0.0000 | 0.92 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VLY | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 1.04 | 0.43 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CHWY | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8820 | -0.0000 | 3.82 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SOLS | 2026-03-27T19:30:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 2.01 | 0.78 | False | None | predicted_return_threshold, vwap_relationship |
| ZBH | 2026-03-27T19:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.8796 | -0.0000 | 0.50 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
