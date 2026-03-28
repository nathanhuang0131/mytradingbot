# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| RDY | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0313 | 0.9900 | 0.0313 | 0.50 | 0.14 | True | None | liquidity_filter, duplicate_position |
| OSCR | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 2.24 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| UAL | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0005 | 0.9900 | 0.0005 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| MKSI | 2026-03-27T16:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 5.58 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| XPEV | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 2.17 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SEDG | 2026-03-27T16:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| BATL | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| BLDR | 2026-03-27T16:50:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| CZR | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| COLB | 2026-03-27T16:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9891 | 0.0003 | 0.50 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DAL | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9878 | 0.0003 | 1.33 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BBIO | 2026-03-27T16:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9866 | 0.0003 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| TSEM | 2026-03-27T16:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9854 | 0.0003 | 0.50 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NTSK | 2026-03-27T16:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9842 | 0.0003 | 1.61 | 0.11 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SNOW | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9830 | 0.0003 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| ORLA | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9818 | 0.0002 | 2.57 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| BBWI | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9805 | 0.0002 | 2.92 | 0.49 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| USAR | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9793 | 0.0002 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| CE | 2026-03-27T16:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9781 | 0.0002 | 1.59 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9769 | 0.0002 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| TEM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9757 | 0.0002 | 4.07 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9745 | 0.0002 | 0.50 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| KRMN | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9732 | 0.0002 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| GFS | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9720 | 0.0002 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| ZSL | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9708 | -0.0002 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ACN | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9696 | 0.0002 | 0.65 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| NVAX | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9684 | 0.0002 | 2.91 | 0.34 | True | None | predicted_return_threshold, liquidity_filter |
| ABNB | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9672 | 0.0002 | 0.61 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SMTC | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9659 | 0.0002 | 4.80 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| YPF | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9647 | 0.0002 | 2.45 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| SRPT | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9635 | 0.0002 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| PK | 2026-03-27T16:50:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| PR | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9611 | 0.0001 | 1.15 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| USB | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.50 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FLEX | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| MTCH | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| HOG | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| VLY | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| VSCO | 2026-03-27T16:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| GDDY | 2026-03-27T16:48:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 3.15 | 0.73 | True | None | predicted_return_threshold |
| EXPE | 2026-03-27T16:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| KMT | 2026-03-27T16:50:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| CSGP | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9489 | -0.0001 | 1.86 | 0.14 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BABA | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| UMAC | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| FANG | 2026-03-27T16:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 0.50 | 0.81 | True | None | predicted_return_threshold |
| BAM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| CRWD | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 1.16 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| TECH | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9416 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| XYZ | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| DYN | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| SEI | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9380 | -0.0001 | 3.00 | 0.48 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HIMS | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9367 | -0.0001 | 3.20 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DAR | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9355 | -0.0001 | 4.36 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| SWKS | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| AKAM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| AXTI | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| QSR | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| MUR | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| C | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| REAL | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 2.90 | 0.83 | True | None | predicted_return_threshold |
| ONDS | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 1.39 | 0.06 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BAX | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 1.55 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 3.05 | 0.69 | True | None | predicted_return_threshold |
| GPN | 2026-03-27T16:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| FIVN | 2026-03-27T16:50:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 1.73 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| AXP | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| MSTR | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 1.39 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| CNK | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 2.26 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| INSM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9161 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| HPE | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| DDOG | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| BEN | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| HPQ | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| ADM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 5.60 | 0.74 | True | None | predicted_return_threshold |
| BSY | 2026-03-27T16:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| VIAV | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 3.94 | 0.32 | True | None | predicted_return_threshold, liquidity_filter |
| CHYM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| APH | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| IOT | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 1.25 | 0.22 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DXCM | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9027 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| WPM | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 1.00 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| TXG | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9002 | -0.0001 | 1.94 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| CG | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| SOFI | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8978 | -0.0001 | 2.44 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BROS | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 6.39 | 0.28 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| NBIS | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 1.10 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| SBSW | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 3.23 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DOCS | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| RHI | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8917 | 0.0001 | 1.01 | 0.57 | True | None | predicted_return_threshold |
| M | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 2.79 | 0.40 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FROG | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| SMFG | 2026-03-27T16:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| W | 2026-03-27T16:53:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| ADP | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8856 | 0.0001 | 0.50 | 0.51 | True | None | predicted_return_threshold |
| SJM | 2026-03-27T16:07:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| SUNB | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 5.47 | 0.61 | False | None | predicted_return_threshold, vwap_relationship |
| SOLS | 2026-03-27T16:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| PYPL | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 2.28 | 0.13 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BHP | 2026-03-27T16:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8796 | 0.0001 | 0.71 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
