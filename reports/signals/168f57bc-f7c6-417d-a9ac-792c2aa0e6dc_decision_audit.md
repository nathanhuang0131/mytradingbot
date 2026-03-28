# Decision Audit

- candidates audited: `100`
- broker_mode: `alpaca_paper_api`
- broker_description: `Alpaca paper API broker`

| Symbol | Timestamp | Source | Status | Rejection | Score | Confidence | Predicted Return | Spread (bps) | Liquidity | VWAP OK | Expectancy OK | Rejection Reasons |
| --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| PRCT | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | vwap_relationship_blocked | -0.0020 | 0.9900 | -0.0020 | 9.05 | 0.49 | False | None | vwap_relationship, spread_filter, liquidity_filter |
| UMAC | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0008 | 0.9900 | -0.0008 | 6.26 | 0.20 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| BLDR | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0006 | 0.9900 | 0.0006 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| SLM | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| RCAT | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 0.50 | 0.04 | True | None | predicted_return_threshold, liquidity_filter |
| ENPH | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0004 | 0.9900 | 0.0004 | 6.73 | 0.26 | False | None | predicted_return_threshold, vwap_relationship, spread_filter, liquidity_filter |
| CNH | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| GAP | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 2.03 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| AMAT | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0003 | 0.9900 | 0.0003 | 1.04 | 0.50 | True | None | predicted_return_threshold, liquidity_filter |
| WVE | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9891 | 0.0002 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| ADMA | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0002 | 0.9878 | -0.0002 | 5.32 | 0.19 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| UUUU | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9866 | 0.0002 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| BW | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9854 | 0.0002 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| BILI | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9842 | 0.0002 | 1.12 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| LITE | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0002 | 0.9830 | 0.0002 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| RUN | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9818 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| CPNG | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9805 | 0.0001 | 0.50 | 0.88 | True | None | predicted_return_threshold |
| JEF | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9793 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| SOLS | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9781 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| UAL | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9769 | 0.0001 | 2.82 | 0.60 | False | None | predicted_return_threshold, vwap_relationship |
| FIGS | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9757 | 0.0001 | 1.70 | 0.87 | True | None | predicted_return_threshold |
| DOCN | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9745 | 0.0001 | 0.50 | 0.17 | True | None | predicted_return_threshold, liquidity_filter |
| WSC | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9732 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| IREN | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9720 | 0.0001 | 0.72 | 0.60 | True | None | predicted_return_threshold |
| HUT | 2026-03-27T17:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9708 | 0.0001 | 0.50 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| RNG | 2026-03-27T17:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9696 | 0.0001 | 1.42 | 0.75 | True | None | predicted_return_threshold |
| SEDG | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9684 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| ALM | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9672 | 0.0001 | 1.69 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| QBTS | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9659 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| ARIS | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9647 | 0.0001 | 4.44 | 0.41 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| ENTG | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9635 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| LULU | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9623 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| PONY | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9611 | -0.0001 | 0.50 | 0.24 | True | None | predicted_return_threshold, liquidity_filter |
| RGTI | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9599 | 0.0001 | 1.88 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| CORZ | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9586 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| DAR | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9574 | 0.0001 | 2.32 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| FIGR | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9562 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| CDW | 2026-03-27T17:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9550 | 0.0001 | 1.68 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| LUV | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9538 | 0.0001 | 0.67 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| CGAU | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9526 | 0.0001 | 0.50 | 0.47 | True | None | predicted_return_threshold, liquidity_filter |
| GLW | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9513 | 0.0001 | 1.30 | 0.28 | True | None | predicted_return_threshold, liquidity_filter |
| PBR | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9501 | 0.0001 | 1.21 | 0.02 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| CG | 2026-03-27T17:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9489 | 0.0001 | 0.50 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| LSCC | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9477 | 0.0001 | 0.50 | 0.22 | True | None | predicted_return_threshold, liquidity_filter |
| ERAS | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9465 | 0.0001 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| SWKS | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9453 | -0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| TRU | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9440 | 0.0001 | 0.50 | 0.23 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| DFTX | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9428 | 0.0001 | 0.50 | 0.37 | True | None | predicted_return_threshold, liquidity_filter |
| PGR | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9416 | -0.0001 | 0.50 | 0.72 | True | None | predicted_return_threshold |
| CNQ | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9404 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| GLXY | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9392 | 0.0001 | 1.40 | 0.04 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SATS | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9380 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| NTNX | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9367 | 0.0001 | 0.67 | 0.28 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SJM | 2026-03-27T17:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9355 | 0.0001 | 0.50 | 0.58 | True | None | predicted_return_threshold |
| TGT | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9343 | 0.0001 | 4.18 | 0.37 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| PFE | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9331 | 0.0001 | 0.50 | 0.42 | True | None | predicted_return_threshold, liquidity_filter |
| OMC | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9319 | 0.0001 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| PENN | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9307 | 0.0001 | 5.47 | 0.94 | True | None | predicted_return_threshold |
| TNDM | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9294 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| AAL | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9282 | 0.0001 | 1.21 | 0.10 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| KLAR | 2026-03-27T17:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9270 | 0.0001 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| FSLY | 2026-03-27T17:52:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9258 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| DNLI | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9246 | 0.0001 | 0.50 | 0.27 | True | None | predicted_return_threshold, liquidity_filter |
| BMNR | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9234 | 0.0001 | 4.10 | 0.29 | True | None | predicted_return_threshold, liquidity_filter |
| ORLA | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9221 | 0.0001 | 0.50 | 0.06 | True | None | predicted_return_threshold, liquidity_filter |
| ESTC | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9209 | 0.0001 | 0.50 | 0.19 | True | None | predicted_return_threshold, liquidity_filter |
| HMY | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9197 | 0.0001 | 0.50 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| AESI | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9185 | 0.0001 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| SCO | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9173 | 0.0001 | 0.50 | 0.10 | True | None | predicted_return_threshold, liquidity_filter |
| INSM | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0001 | 0.9161 | -0.0001 | 3.45 | 0.15 | True | None | predicted_return_threshold, liquidity_filter |
| CIFR | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9148 | 0.0001 | 2.78 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| QSR | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9136 | 0.0001 | 0.50 | 0.07 | True | None | predicted_return_threshold, liquidity_filter |
| AAOI | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9124 | 0.0001 | 4.90 | 0.26 | True | None | predicted_return_threshold, liquidity_filter |
| COHR | 2026-03-27T17:54:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9112 | 0.0001 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| ALKT | 2026-03-27T17:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9100 | 0.0001 | 0.50 | 0.48 | True | None | predicted_return_threshold, liquidity_filter |
| S | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9088 | 0.0001 | 1.00 | 0.05 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| GPN | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9075 | 0.0001 | 0.50 | 0.24 | False | None | predicted_return_threshold, vwap_relationship, liquidity_filter |
| SN | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0001 | 0.9063 | 0.0001 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| XRAY | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9051 | 0.0000 | 1.09 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| GLDD | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9039 | 0.0000 | 0.50 | 0.02 | True | None | predicted_return_threshold, liquidity_filter |
| NTSK | 2026-03-27T17:56:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9027 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| CENX | 2026-03-27T17:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.9015 | 0.0000 | 0.50 | 0.03 | True | None | predicted_return_threshold, liquidity_filter |
| WDC | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | -0.0000 | 0.9002 | -0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BEAM | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8990 | 0.0000 | 0.50 | 0.05 | True | None | predicted_return_threshold, liquidity_filter |
| ZETA | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8978 | 0.0000 | 1.70 | 0.38 | True | None | predicted_return_threshold, liquidity_filter |
| ALB | 2026-03-27T17:50:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8966 | 0.0000 | 0.50 | 0.53 | True | None | predicted_return_threshold |
| WFC | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8954 | 0.0000 | 1.13 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| WULF | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8942 | 0.0000 | 1.71 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| CDNS | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8929 | 0.0000 | 1.46 | 0.21 | True | None | predicted_return_threshold, liquidity_filter |
| BBVA | 2026-03-27T17:47:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8917 | 0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| AXTA | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8905 | 0.0000 | 0.50 | 0.09 | True | None | predicted_return_threshold, liquidity_filter |
| NU | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8893 | 0.0000 | 2.74 | 0.33 | True | None | predicted_return_threshold, liquidity_filter |
| KSS | 2026-03-27T17:58:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8881 | 0.0000 | 0.50 | 0.23 | True | None | predicted_return_threshold, liquidity_filter |
| FLG | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8869 | 0.0000 | 0.50 | 0.18 | True | None | predicted_return_threshold, liquidity_filter |
| OKTA | 2026-03-27T17:49:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8856 | 0.0000 | 2.40 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| AU | 2026-03-27T17:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8844 | 0.0000 | 0.50 | 0.08 | True | None | predicted_return_threshold, liquidity_filter |
| NVAX | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8832 | 0.0000 | 0.50 | 0.12 | True | None | predicted_return_threshold, liquidity_filter |
| CAVA | 2026-03-27T17:57:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8820 | 0.0000 | 0.50 | 0.13 | True | None | predicted_return_threshold, liquidity_filter |
| BK | 2026-03-27T17:51:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8808 | 0.0000 | 0.50 | 0.25 | True | None | predicted_return_threshold, liquidity_filter |
| CART | 2026-03-27T17:55:00+00:00 | qlib_candidate_only | rejected | target_return_below_threshold | 0.0000 | 0.8796 | 0.0000 | 0.50 | 0.57 | True | None | predicted_return_threshold |
