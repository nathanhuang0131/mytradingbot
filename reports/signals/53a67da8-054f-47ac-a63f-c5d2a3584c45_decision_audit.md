# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| FND | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0098 | 0.9900 | 0.0098 | 0.50 | 0.02 | True | None | liquidity_filter |
| ALKT | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0029 | 0.9900 | 0.0029 | 0.50 | 0.04 | True | None | liquidity_filter |
| CNM | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0013 | 0.9900 | 0.0013 | 0.51 | 0.01 | True | None | liquidity_filter |
| ZSL | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | -0.0010 | 0.9900 | -0.0010 | 2.72 | 0.06 | True | None | liquidity_filter |
| SCO | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | liquidity_too_low | 0.0008 | 0.9900 | 0.0008 | 0.50 | 0.13 | True | None | liquidity_filter |
| AXTI | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 1.61 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| RNG | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0005 | 0.9900 | -0.0005 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BIRK | 2026-03-27T14:20:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9900 | -0.0004 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| MRNA | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| HUN | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9891 | -0.0004 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| MDLN | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9878 | 0.0004 | 0.91 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| BSY | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9866 | -0.0004 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| FIVN | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0004 | 0.9854 | -0.0004 | 1.70 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| U | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9842 | 0.0004 | 4.06 | 0.06 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ADMA | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9830 | 0.0004 | 5.26 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| SOC | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9818 | 0.0004 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| ARES | 2026-03-27T14:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9805 | -0.0003 | 4.35 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| GPN | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9793 | -0.0003 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| SN | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9781 | -0.0003 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| RHI | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9769 | 0.0003 | 1.01 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CGAU | 2026-03-27T14:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9757 | 0.0003 | 0.76 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| KT | 2026-03-27T14:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9745 | -0.0003 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| GLL | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0003 | 0.9732 | -0.0003 | 0.56 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FNGU | 2026-03-27T14:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9720 | 0.0003 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| VXX | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9708 | 0.0003 | 2.28 | 0.60 | True | None | predicted_return_threshold |
| CHWY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9696 | 0.0002 | 6.66 | 0.19 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| CIFR | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9684 | 0.0002 | 3.66 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TSEM | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9672 | 0.0002 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| PANW | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9659 | 0.0002 | 8.63 | 0.13 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| WAY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9647 | -0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| APP | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9635 | -0.0002 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| ETN | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9623 | 0.0002 | 1.88 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| PRCT | 2026-03-27T14:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9611 | 0.0002 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| WDAY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9599 | 0.0002 | 1.41 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| TENB | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9586 | 0.0002 | 6.88 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RYAN | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9574 | -0.0002 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| PCOR | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9562 | -0.0002 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| PSX | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9550 | 0.0002 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| PGNY | 2026-03-27T14:19:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9538 | -0.0002 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| TNGX | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9526 | 0.0002 | 3.84 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| STX | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9513 | 0.0002 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| FLY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9501 | -0.0002 | 2.65 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| SM | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 1.91 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| YPF | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 5.05 | 0.86 | False | None | predicted_return_threshold, vwap_relationship |
| AG | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 3.13 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CRWV | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9453 | 0.0001 | 3.01 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| WHR | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| DFTX | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9428 | -0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| NESR | 2026-03-27T14:24:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9416 | -0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| UAL | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9404 | -0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| OC | 2026-03-27T14:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| BBIO | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 4.95 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| W | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BW | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| SLB | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 3.07 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| UMAC | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9331 | -0.0001 | 0.98 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| DOC | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 1.50 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ASTS | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 10.04 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| GLXY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 2.04 | 0.15 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ROKU | 2026-03-27T14:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9282 | -0.0001 | 0.50 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BATL | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 12.38 | 0.50 | True | None | predicted_return_threshold, spread_filter, intraday_volatility_regime |
| CE | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 4.93 | 0.07 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ARIS | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9246 | -0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| DOCU | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9234 | -0.0001 | 1.10 | 0.16 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| TTD | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 1.75 | 0.09 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CF | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 1.78 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| NEM | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| LRCX | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| KD | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9173 | -0.0001 | 1.00 | 0.44 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CC | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9161 | -0.0001 | 1.16 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| UUUU | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9148 | -0.0001 | 0.50 | 0.01 | True | None | predicted_return_threshold, liquidity_filter |
| INSM | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 6.93 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| IONQ | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9124 | -0.0001 | 3.98 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| IOT | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.82 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| SQQQ | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 2.33 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| TXG | 2026-03-27T14:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| DOG | 2026-03-27T14:21:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9075 | -0.0001 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| RELY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 1.64 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9051 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ZS | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9039 | 0.0001 | 6.58 | 0.18 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| UEC | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9027 | -0.0001 | 1.95 | 0.12 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SVM | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9015 | 0.0001 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| AJG | 2026-03-27T14:27:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9002 | 0.0001 | 0.50 | 0.27 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| JBS | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8990 | 0.0001 | 2.22 | 0.36 | True | None | predicted_return_threshold, liquidity_filter |
| DASH | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8978 | -0.0001 | 0.77 | 0.06 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HMY | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8966 | 0.0001 | 1.78 | 0.50 | False | None | predicted_return_threshold, vwap_relationship |
| JEF | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8954 | 0.0001 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| HL | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8942 | 0.0001 | 2.86 | 0.18 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BBWI | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8929 | 0.0001 | 6.52 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| NTSK | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8917 | -0.0001 | 1.58 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SPGI | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8905 | 0.0001 | 1.26 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| NET | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8893 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| DBX | 2026-03-27T14:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8881 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| ZBH | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8869 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| NG | 2026-03-27T14:25:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8856 | -0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| SUZ | 2026-03-27T14:26:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8844 | 0.0001 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| PATH | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8832 | 0.0001 | 3.53 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FPS | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8820 | 0.0001 | 5.87 | 0.14 | True | None | predicted_return_threshold, liquidity_filter |
| OKTA | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.8808 | 0.0001 | 3.40 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| EQX | 2026-03-27T14:28:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.8796 | -0.0001 | 6.12 | 0.05 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
