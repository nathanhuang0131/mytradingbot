# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| PRCT | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0020 | 0.9900 | -0.0020 | 25.36 | 0.89 | False | None | vwap_relationship, spread_filter, liquidity_sweep_detection |
| UMAC | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0008 | 0.9900 | -0.0008 | 6.21 | 0.45 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| BLDR | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 2.77 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SLM | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 6.15 | 1.00 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| RCAT | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 10.90 | 0.66 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| ENPH | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 6.30 | 1.00 | True | None | predicted_return_threshold, spread_filter |
| CNH | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 5.80 | 1.00 | True | None | predicted_return_threshold |
| GAP | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 3.04 | 1.00 | True | None | predicted_return_threshold |
| AMAT | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 1.89 | 1.00 | True | None | predicted_return_threshold |
| WVE | 2026-03-27T17:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 15.05 | 0.53 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_sweep_detection |
| ADMA | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9878 | -0.0002 | 9.32 | 0.17 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| UUUU | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 2.81 | 0.79 | True | None | predicted_return_threshold |
| BW | 2026-03-27T17:38:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 5.19 | 1.00 | True | None | predicted_return_threshold |
| BILI | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 4.49 | 1.00 | True | None | predicted_return_threshold |
| LITE | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 5.33 | 1.00 | True | None | predicted_return_threshold |
| RUN | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 2.00 | 0.79 | False | None | predicted_return_threshold, vwap_relationship |
| CPNG | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 2.08 | 0.79 | True | None | predicted_return_threshold |
| JEF | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 1.88 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| SOLS | 2026-03-27T17:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 5.18 | 0.52 | True | None | predicted_return_threshold |
| UAL | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 1.96 | 0.61 | False | None | predicted_return_threshold, vwap_relationship |
| FIGS | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 0.50 | 0.62 | True | None | predicted_return_threshold |
| DOCN | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 8.99 | 0.69 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| WSC | 2026-03-27T17:42:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 4.36 | 0.85 | False | None | predicted_return_threshold, vwap_relationship |
| IREN | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 1.80 | 0.25 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| HUT | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| RNG | 2026-03-27T17:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 2.83 | 1.00 | True | None | predicted_return_threshold |
| SEDG | 2026-03-27T17:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.20 | True | None | predicted_return_threshold, liquidity_filter |
| ALM | 2026-03-27T17:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 1.68 | 0.63 | False | None | predicted_return_threshold, vwap_relationship |
| QBTS | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 1.82 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| ARIS | 2026-03-27T17:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 0.50 | 0.49 | True | None | predicted_return_threshold, liquidity_filter |
| ENTG | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| LULU | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.86 | 0.39 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PONY | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9611 | -0.0001 | 6.78 | 0.08 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| RGTI | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 0.94 | 0.69 | True | None | predicted_return_threshold |
| CORZ | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.84 | 0.74 | True | None | predicted_return_threshold |
| DAR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 0.50 | 0.11 | True | None | predicted_return_threshold, liquidity_filter |
| FIGR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.16 | True | None | predicted_return_threshold, liquidity_filter |
| CDW | 2026-03-27T17:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 1.68 | 0.44 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| LUV | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 1.33 | 0.39 | True | None | predicted_return_threshold, liquidity_filter |
| CGAU | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.75 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GLW | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.20 | 0.80 | False | None | predicted_return_threshold, vwap_relationship |
| PBR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 4.23 | 1.00 | True | None | predicted_return_threshold |
| CG | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 3.26 | 0.96 | False | None | predicted_return_threshold, vwap_relationship |
| LSCC | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| ERAS | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.83 | 0.72 | True | None | predicted_return_threshold |
| SWKS | 2026-03-27T17:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9453 | -0.0001 | 3.26 | 1.00 | True | None | predicted_return_threshold |
| TRU | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 1.13 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| DFTX | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.70 | 0.86 | True | None | predicted_return_threshold |
| PGR | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9416 | -0.0001 | 1.36 | 1.00 | True | None | predicted_return_threshold |
| CNQ | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 2.28 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GLXY | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 2.79 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| SATS | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.88 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| NTNX | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.50 | 0.31 | True | None | predicted_return_threshold, liquidity_filter |
| SJM | 2026-03-27T17:35:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 1.00 | True | None | predicted_return_threshold |
| TGT | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 4.77 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PFE | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 1.83 | 0.57 | True | None | predicted_return_threshold |
| OMC | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 5.40 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| PENN | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 0.50 | 0.30 | True | None | predicted_return_threshold, liquidity_filter |
| TNDM | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.35 | True | None | predicted_return_threshold, liquidity_filter |
| AAL | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 2.42 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.92 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DNLI | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 1.35 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BMNR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 3.40 | 0.53 | False | None | predicted_return_threshold, vwap_relationship |
| ORLA | 2026-03-27T17:40:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 6.06 | 0.22 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| ESTC | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| HMY | 2026-03-27T17:44:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 3.53 | 0.60 | False | None | predicted_return_threshold, vwap_relationship |
| AESI | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| SCO | 2026-03-27T17:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.41 | True | None | predicted_return_threshold, liquidity_filter |
| INSM | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9161 | -0.0001 | 0.69 | 0.36 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CIFR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 0.93 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| QSR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 1.40 | 0.65 | False | None | predicted_return_threshold, vwap_relationship |
| AAOI | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 6.69 | 0.79 | False | None | predicted_return_threshold, vwap_relationship, spread_filter |
| COHR | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.50 | 0.32 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ALKT | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| S | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 1.00 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| GPN | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 1.51 | 0.46 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SN | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 1.98 | 0.54 | True | None | predicted_return_threshold |
| XRAY | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| GLDD | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 0.50 | 0.53 | True | None | predicted_return_threshold |
| NTSK | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| CENX | 2026-03-27T17:22:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| WDC | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9002 | -0.0000 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 10.09 | 0.26 | True | None | predicted_return_threshold, spread_filter, liquidity_filter |
| ZETA | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 0.85 | 0.40 | True | None | predicted_return_threshold, liquidity_filter |
| ALB | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| WFC | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 1.61 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| WULF | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 1.71 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| CDNS | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 0.95 | 0.29 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| BBVA | 2026-03-27T17:31:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| AXTA | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.46 | True | None | predicted_return_threshold, liquidity_filter |
| NU | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 1.82 | 0.38 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KSS | 2026-03-27T17:43:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 1.01 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FLG | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.95 | 0.21 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| OKTA | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 1.98 | 0.89 | True | None | predicted_return_threshold |
| NVAX | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| CAVA | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| BK | 2026-03-27T17:45:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 1.63 | 1.00 | False | None | predicted_return_threshold, vwap_relationship |
| CART | 2026-03-27T17:46:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 2.48 | 0.33 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
