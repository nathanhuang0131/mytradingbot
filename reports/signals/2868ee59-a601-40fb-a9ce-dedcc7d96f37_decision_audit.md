# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| RDY | 2026-03-27T16:40:00+00:00 | qlib_plus_rules | accepted_bracket_buy |  | 0.0313 | 0.9900 | 0.0313 | 2.76 | 1.00 | True | True |  |
| OSCR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 7.81 | 0.61 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| UAL | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 3.47 | 0.81 | False | None | predicted_return_threshold, vwap_relationship |
| MKSI | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 5.58 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| XPEV | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 2.17 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SEDG | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 5.07 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BATL | 2026-03-27T16:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 4.32 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| BLDR | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| CZR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 11.57 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| COLB | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9891 | 0.0003 | 4.62 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| DAL | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9878 | 0.0003 | 9.75 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| BBIO | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9866 | 0.0003 | 6.78 | 0.84 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| TSEM | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9854 | 0.0003 | 4.50 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| NTSK | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9842 | 0.0003 | 0.50 | 0.65 | True | None | predicted_return_threshold |
| SNOW | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9830 | 0.0003 | 0.50 | 0.75 | True | None | predicted_return_threshold |
| ORLA | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 1.71 | 1.00 | True | None | predicted_return_threshold |
| BBWI | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 6.56 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| USAR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 4.90 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CE | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 7.16 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| FSLY | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9769 | 0.0002 | 4.59 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| TEM | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9757 | 0.0002 | 3.50 | 0.88 | False | None | predicted_return_threshold, vwap_relationship |
| BEAM | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9745 | 0.0002 | 3.94 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| KRMN | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9732 | 0.0002 | 5.49 | 0.64 | False | None | predicted_return_threshold, vwap_relationship |
| GFS | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9720 | 0.0002 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| ZSL | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9708 | -0.0002 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| ACN | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9696 | 0.0002 | 2.98 | 0.78 | False | None | predicted_return_threshold, vwap_relationship |
| NVAX | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9684 | 0.0002 | 2.92 | 0.73 | False | None | predicted_return_threshold, vwap_relationship |
| ABNB | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9672 | 0.0002 | 4.45 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SMTC | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9659 | 0.0002 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| YPF | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9647 | 0.0002 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| SRPT | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9635 | 0.0002 | 0.50 | 0.68 | True | None | predicted_return_threshold |
| PK | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 3.56 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| PR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 2.31 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| USB | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 2.45 | 0.87 | False | None | predicted_return_threshold, vwap_relationship |
| FLEX | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 1.35 | 1.00 | True | None | predicted_return_threshold |
| MTCH | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| HOG | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 3.86 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| VLY | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 3.12 | 0.72 | False | None | predicted_return_threshold, vwap_relationship |
| VSCO | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| GDDY | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.69 | True | None | predicted_return_threshold |
| EXPE | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| KMT | 2026-03-27T16:36:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 2.13 | 0.71 | False | None | predicted_return_threshold, vwap_relationship |
| CSGP | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9489 | -0.0001 | 10.83 | 0.61 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| BABA | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 1.22 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| UMAC | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| FANG | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 3.40 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BAM | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 2.31 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CRWD | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 1.90 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| TECH | 2026-03-27T16:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 2.19 | 0.59 | False | None | predicted_return_threshold, vwap_relationship |
| XYZ | 2026-03-27T16:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 4.40 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| DYN | 2026-03-27T16:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9380 | -0.0001 | 6.90 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| HIMS | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 3.85 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| DAR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9355 | -0.0001 | 4.65 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| SWKS | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| AKAM | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.55 | 0.91 | False | None | predicted_return_threshold, vwap_relationship |
| AXTI | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| QSR | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.70 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| MUR | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 2.37 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| C | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 6.44 | 0.08 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| REAL | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.60 | True | None | predicted_return_threshold |
| ONDS | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 4.19 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BAX | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 1.55 | 0.56 | False | None | predicted_return_threshold, vwap_relationship |
| KLAR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 1.01 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GPN | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| FIVN | 2026-03-27T16:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| AXP | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 1.27 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| MSTR | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.80 | 0.87 | False | None | predicted_return_threshold, vwap_relationship |
| CNK | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 6.33 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| INSM | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 0.87 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| HPE | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 2.07 | 0.89 | False | None | predicted_return_threshold, vwap_relationship |
| DDOG | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| BEN | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 2.16 | 0.88 | False | None | predicted_return_threshold, vwap_relationship |
| HPQ | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 3.23 | 0.47 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ADM | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| BSY | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.44 | True | None | predicted_return_threshold, liquidity_filter |
| VIAV | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 1.08 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CHYM | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.79 | True | None | predicted_return_threshold |
| APH | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 3.62 | 0.68 | True | None | predicted_return_threshold |
| IOT | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| DXCM | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 3.62 | 0.42 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WPM | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 1.71 | 0.32 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TXG | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9002 | -0.0001 | 4.53 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| CG | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 1.08 | 0.61 | True | None | predicted_return_threshold |
| SOFI | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8978 | -0.0001 | 4.89 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| BROS | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 3.19 | 0.62 | False | None | predicted_return_threshold, vwap_relationship |
| NBIS | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 2.08 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| SBSW | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 2.16 | 1.00 | True | None | predicted_return_threshold |
| DOCS | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 1.06 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RHI | 2026-03-27T16:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 2.53 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| M | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 3.49 | 0.34 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FROG | 2026-03-27T16:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 1.14 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SMFG | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 1.31 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| W | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 2.47 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| ADP | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 1.49 | 0.79 | False | None | predicted_return_threshold, vwap_relationship |
| SJM | 2026-03-27T16:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SUNB | 2026-03-27T16:41:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 6.32 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| SOLS | 2026-03-27T16:37:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| PYPL | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 3.99 | 0.57 | False | None | predicted_return_threshold, vwap_relationship |
| BHP | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 1.79 | 0.85 | False | None | predicted_return_threshold, vwap_relationship |
