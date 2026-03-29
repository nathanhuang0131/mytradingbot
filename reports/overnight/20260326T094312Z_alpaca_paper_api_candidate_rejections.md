# Overnight Candidate Rejections

- Window Sydney: 2026-03-26T20:43:12.988448+11:00 to 2026-03-27T08:43:12.988448+11:00
- Window UTC: 2026-03-26T09:43:12.988448+00:00 to 2026-03-26T21:43:12.988448+00:00
- Broker mode: `alpaca_paper_api`
- Sessions: 72
- Candidate rows: 3530
- Unique symbols: 368

## Rejection Code Meanings

- `target_return_below_threshold`: 3153 rows, most common detail `predicted_return_threshold` (3153)
- `liquidity_too_low`: 166 rows, most common detail `liquidity_filter` (166)
- `invalid_signal_payload`: 103 rows, most common detail `vwap_relationship` (92)
- `spread_too_wide`: 83 rows, most common detail `spread_filter` (83)
- `bracket_invalid`: 18 rows, most common detail `fee_adjusted_expectancy` (18)
- `score_below_threshold`: 7 rows, most common detail `confidence_threshold` (7)

## Active Criteria Used Last Night

- Per-cycle candidate cap: `50` from the latest prediction batch
- Prediction refresh cadence: every `1800` seconds (30 minutes)
- Loop cadence: every `300` seconds (5 minutes)
- Predicted return threshold used by this profile: `0.001` (0.10%)
- Confidence threshold used by this profile: `0.6`
- Max spread: `5.0` bps
- VWAP rule: long must be at/above VWAP; short must be at/below VWAP
- Min liquidity score: `0.5`
- Max liquidity stress: `0.7`
- Order book imbalance rule: long fails if imbalance < 0; short fails if imbalance > 0
- Liquidity sweep rule: reject when `liquidity_sweep_detected = true`
- Volatility regime rule: reject when regime is `high`
- Cooldown: `15` minutes
- Flatten near close: block when `minutes_to_close <= 10`
- Max holding time: `900` seconds
- Reward/risk floor: `1.4`
- Minimum net reward/share: `$0.01`
- Estimated slippage: `2.5` bps
- Stop loss buffer floor: `20.0` bps
- Take profit multiplier: `1.8`
- Risk budget per trade: `$25.00`
- Max position notional: `$5000.00`
- Execution bracket settings in this profile: take profit `0.6%`, stop loss `0.35%`, fixed quantity `1`

## Symbol Summary

| Symbol | Appearances | Reject reasons |
|---|---:|---|
| AAL | 11 | liquidity_too_low (7), target_return_below_threshold (4) |
| AAOI | 12 | target_return_below_threshold (12) |
| ACHC | 15 | target_return_below_threshold (15) |
| ACI | 7 | target_return_below_threshold (7) |
| ADM | 4 | target_return_below_threshold (4) |
| ADMA | 60 | target_return_below_threshold (52), invalid_signal_payload (6), spread_too_wide (2) |
| AEM | 11 | target_return_below_threshold (11) |
| AFRM | 29 | target_return_below_threshold (29) |
| AG | 10 | target_return_below_threshold (6), liquidity_too_low (3), spread_too_wide (1) |
| AGI | 8 | target_return_below_threshold (8) |
| AGNC | 4 | target_return_below_threshold (4) |
| AHR | 12 | target_return_below_threshold (12) |
| AJG | 4 | target_return_below_threshold (4) |
| AKAM | 14 | target_return_below_threshold (14) |
| AL | 14 | invalid_signal_payload (13), liquidity_too_low (1) |
| ALAB | 4 | target_return_below_threshold (4) |
| ALB | 12 | target_return_below_threshold (12) |
| ALHC | 4 | target_return_below_threshold (4) |
| ALKT | 11 | target_return_below_threshold (11) |
| ALM | 8 | target_return_below_threshold (8) |
| AM | 4 | target_return_below_threshold (4) |
| AMD | 4 | target_return_below_threshold (4) |
| AMKR | 12 | target_return_below_threshold (12) |
| AMPX | 4 | target_return_below_threshold (4) |
| AMRZ | 4 | target_return_below_threshold (4) |
| AMZN | 4 | liquidity_too_low (3), invalid_signal_payload (1) |
| ANET | 19 | target_return_below_threshold (19) |
| APH | 8 | target_return_below_threshold (8) |
| APO | 8 | target_return_below_threshold (8) |
| APP | 12 | target_return_below_threshold (12) |
| ARES | 8 | target_return_below_threshold (8) |
| ARIS | 19 | target_return_below_threshold (19) |
| ARM | 8 | target_return_below_threshold (8) |
| ARMK | 4 | target_return_below_threshold (4) |
| AS | 4 | target_return_below_threshold (4) |
| ASTS | 4 | target_return_below_threshold (4) |
| ATI | 29 | target_return_below_threshold (29) |
| AU | 4 | target_return_below_threshold (4) |
| AXIA | 4 | target_return_below_threshold (4) |
| AXP | 4 | target_return_below_threshold (4) |
| AXTI | 26 | target_return_below_threshold (26) |
| BANC | 7 | target_return_below_threshold (7) |
| BATL | 32 | target_return_below_threshold (16), liquidity_too_low (10), invalid_signal_payload (3), spread_too_wide (2), bracket_invalid (1) |
| BAX | 32 | target_return_below_threshold (32) |
| BBWI | 4 | target_return_below_threshold (4) |
| BBY | 7 | target_return_below_threshold (7) |
| BIRK | 11 | target_return_below_threshold (11) |
| BKD | 10 | target_return_below_threshold (10) |
| BN | 4 | target_return_below_threshold (4) |
| BNL | 4 | target_return_below_threshold (4) |
| BNTX | 8 | target_return_below_threshold (8) |
| BOIL | 4 | target_return_below_threshold (4) |
| BOX | 4 | target_return_below_threshold (4) |
| BRBR | 8 | target_return_below_threshold (8) |
| BRKR | 11 | target_return_below_threshold (11) |
| BROS | 4 | target_return_below_threshold (4) |
| BRX | 4 | target_return_below_threshold (4) |
| BRZE | 21 | target_return_below_threshold (14), score_below_threshold (7) |
| BSY | 4 | target_return_below_threshold (4) |
| BTSG | 19 | target_return_below_threshold (19) |
| BTU | 8 | target_return_below_threshold (8) |
| BW | 8 | target_return_below_threshold (8) |
| BX | 8 | target_return_below_threshold (8) |
| CAG | 4 | target_return_below_threshold (4) |
| CAI | 8 | target_return_below_threshold (8) |
| CARR | 15 | target_return_below_threshold (15) |
| CC | 11 | target_return_below_threshold (11) |
| CCJ | 4 | target_return_below_threshold (4) |
| CCL | 11 | target_return_below_threshold (11) |
| CDE | 4 | target_return_below_threshold (4) |
| CDW | 4 | target_return_below_threshold (4) |
| CE | 4 | target_return_below_threshold (4) |
| CELH | 4 | target_return_below_threshold (4) |
| CENX | 8 | target_return_below_threshold (8) |
| CF | 4 | target_return_below_threshold (4) |
| CHWY | 14 | target_return_below_threshold (14) |
| CHYM | 4 | target_return_below_threshold (4) |
| CIFR | 17 | target_return_below_threshold (17) |
| CMCSA | 4 | target_return_below_threshold (4) |
| CNC | 4 | target_return_below_threshold (4) |
| CNH | 10 | target_return_below_threshold (10) |
| CNM | 12 | target_return_below_threshold (12) |
| COIN | 19 | target_return_below_threshold (19) |
| CORZ | 4 | target_return_below_threshold (4) |
| CPNG | 15 | spread_too_wide (11), target_return_below_threshold (4) |
| CPRI | 4 | target_return_below_threshold (4) |
| CRCL | 8 | target_return_below_threshold (8) |
| CRGY | 25 | target_return_below_threshold (21), liquidity_too_low (2), invalid_signal_payload (2) |
| CSGP | 4 | target_return_below_threshold (4) |
| CSTM | 8 | target_return_below_threshold (4), liquidity_too_low (3), spread_too_wide (1) |
| CSX | 7 | liquidity_too_low (7) |
| CUZ | 4 | target_return_below_threshold (4) |
| CVE | 18 | invalid_signal_payload (13), target_return_below_threshold (4), spread_too_wide (1) |
| CVNA | 8 | target_return_below_threshold (4), spread_too_wide (1), bracket_invalid (1), invalid_signal_payload (1), liquidity_too_low (1) |
| CZR | 10 | target_return_below_threshold (10) |
| DASH | 4 | target_return_below_threshold (4) |
| DAWN | 4 | liquidity_too_low (3), invalid_signal_payload (1) |
| DBX | 4 | target_return_below_threshold (4) |
| DDOG | 4 | target_return_below_threshold (4) |
| DELL | 4 | liquidity_too_low (4) |
| DFTX | 4 | target_return_below_threshold (4) |
| DHT | 4 | target_return_below_threshold (4) |
| DOCN | 29 | target_return_below_threshold (29) |
| DOW | 4 | target_return_below_threshold (4) |
| DUOL | 15 | target_return_below_threshold (11), liquidity_too_low (2), spread_too_wide (1), invalid_signal_payload (1) |
| DVN | 4 | target_return_below_threshold (4) |
| DX | 8 | target_return_below_threshold (8) |
| DXC | 4 | target_return_below_threshold (4) |
| DYN | 23 | target_return_below_threshold (19), liquidity_too_low (2), spread_too_wide (1), invalid_signal_payload (1) |
| EIX | 4 | target_return_below_threshold (4) |
| EMR | 8 | target_return_below_threshold (8) |
| ENPH | 4 | target_return_below_threshold (4) |
| ENTG | 4 | target_return_below_threshold (4) |
| EQH | 12 | liquidity_too_low (7), target_return_below_threshold (4), invalid_signal_payload (1) |
| ERAS | 27 | target_return_below_threshold (16), invalid_signal_payload (11) |
| ESI | 25 | target_return_below_threshold (25) |
| ESTC | 4 | target_return_below_threshold (4) |
| ETN | 8 | target_return_below_threshold (8) |
| ETSY | 4 | target_return_below_threshold (4) |
| EXK | 4 | target_return_below_threshold (4) |
| EXLS | 8 | target_return_below_threshold (8) |
| F | 4 | target_return_below_threshold (4) |
| FBIN | 8 | target_return_below_threshold (8) |
| FE | 4 | target_return_below_threshold (4) |
| FIG | 15 | spread_too_wide (11), target_return_below_threshold (4) |
| FIGR | 25 | target_return_below_threshold (21), liquidity_too_low (2), invalid_signal_payload (1), spread_too_wide (1) |
| FIGS | 22 | target_return_below_threshold (22) |
| FIVN | 20 | target_return_below_threshold (16), liquidity_too_low (2), spread_too_wide (1), invalid_signal_payload (1) |
| FLEX | 12 | target_return_below_threshold (12) |
| FLG | 7 | target_return_below_threshold (7) |
| FLR | 4 | target_return_below_threshold (4) |
| FLUT | 7 | target_return_below_threshold (7) |
| FLY | 49 | target_return_below_threshold (45), liquidity_too_low (3), spread_too_wide (1) |
| FND | 4 | target_return_below_threshold (4) |
| FNGU | 24 | target_return_below_threshold (16), liquidity_too_low (8) |
| FOUR | 4 | target_return_below_threshold (4) |
| FPS | 27 | target_return_below_threshold (27) |
| FROG | 21 | spread_too_wide (11), target_return_below_threshold (10) |
| FRPT | 12 | target_return_below_threshold (12) |
| FSK | 8 | target_return_below_threshold (8) |
| FSLY | 23 | target_return_below_threshold (23) |
| FSM | 8 | target_return_below_threshold (8) |
| FTAI | 4 | target_return_below_threshold (4) |
| FWONK | 13 | target_return_below_threshold (13) |
| G | 8 | target_return_below_threshold (8) |
| GE | 4 | target_return_below_threshold (4) |
| GEHC | 4 | target_return_below_threshold (4) |
| GFS | 21 | spread_too_wide (14), target_return_below_threshold (7) |
| GLL | 12 | target_return_below_threshold (8), liquidity_too_low (4) |
| GLW | 8 | target_return_below_threshold (8) |
| GLXY | 12 | target_return_below_threshold (12) |
| GME | 19 | target_return_below_threshold (19) |
| GOOG | 4 | target_return_below_threshold (4) |
| GOOGL | 4 | target_return_below_threshold (4) |
| GTES | 8 | target_return_below_threshold (8) |
| GTLB | 8 | target_return_below_threshold (8) |
| GTX | 8 | target_return_below_threshold (8) |
| HBM | 4 | target_return_below_threshold (4) |
| HIMS | 18 | target_return_below_threshold (18) |
| HL | 8 | target_return_below_threshold (8) |
| HMY | 8 | target_return_below_threshold (8) |
| HOG | 11 | target_return_below_threshold (11) |
| HPE | 12 | target_return_below_threshold (12) |
| HST | 4 | target_return_below_threshold (4) |
| HTGC | 4 | target_return_below_threshold (4) |
| HUT | 4 | target_return_below_threshold (4) |
| IAG | 15 | invalid_signal_payload (11), target_return_below_threshold (4) |
| IBKR | 4 | target_return_below_threshold (4) |
| IBN | 4 | target_return_below_threshold (4) |
| INDV | 4 | target_return_below_threshold (4) |
| INFY | 11 | target_return_below_threshold (11) |
| INTC | 11 | target_return_below_threshold (11) |
| IONQ | 13 | target_return_below_threshold (13) |
| IP | 8 | target_return_below_threshold (8) |
| IQV | 4 | target_return_below_threshold (4) |
| IREN | 11 | target_return_below_threshold (8), liquidity_too_low (3) |
| JBS | 8 | target_return_below_threshold (8) |
| JCI | 4 | target_return_below_threshold (4) |
| JEF | 10 | target_return_below_threshold (10) |
| JHX | 8 | target_return_below_threshold (8) |
| KLAR | 8 | target_return_below_threshold (8) |
| KMT | 16 | target_return_below_threshold (16) |
| KNX | 4 | liquidity_too_low (3), invalid_signal_payload (1) |
| KRMN | 37 | target_return_below_threshold (26), invalid_signal_payload (11) |
| KSS | 4 | target_return_below_threshold (4) |
| KT | 4 | liquidity_too_low (4) |
| KTOS | 23 | target_return_below_threshold (23) |
| KVUE | 14 | spread_too_wide (13), liquidity_too_low (1) |
| KVYO | 25 | target_return_below_threshold (25) |
| LBRT | 4 | target_return_below_threshold (4) |
| LCID | 8 | target_return_below_threshold (8) |
| LITE | 8 | target_return_below_threshold (8) |
| LNC | 4 | target_return_below_threshold (4) |
| LOW | 11 | invalid_signal_payload (11) |
| LRCX | 4 | target_return_below_threshold (4) |
| LSCC | 8 | liquidity_too_low (4), target_return_below_threshold (4) |
| LUNR | 19 | target_return_below_threshold (19) |
| LUV | 4 | target_return_below_threshold (4) |
| MDB | 4 | target_return_below_threshold (4) |
| MET | 4 | target_return_below_threshold (4) |
| META | 4 | liquidity_too_low (3), spread_too_wide (1) |
| MGM | 4 | target_return_below_threshold (4) |
| MIR | 4 | target_return_below_threshold (4) |
| MKSI | 8 | target_return_below_threshold (8) |
| MOS | 4 | target_return_below_threshold (4) |
| MP | 4 | target_return_below_threshold (4) |
| MRVL | 4 | target_return_below_threshold (4) |
| MSTR | 12 | target_return_below_threshold (12) |
| MU | 12 | target_return_below_threshold (12) |
| MUR | 4 | target_return_below_threshold (4) |
| NBIS | 8 | target_return_below_threshold (8) |
| NCLH | 4 | target_return_below_threshold (4) |
| NESR | 12 | liquidity_too_low (5), target_return_below_threshold (4), invalid_signal_payload (1), spread_too_wide (1), bracket_invalid (1) |
| NFLX | 4 | target_return_below_threshold (4) |
| NG | 7 | target_return_below_threshold (7) |
| NLY | 4 | target_return_below_threshold (4) |
| NOG | 4 | target_return_below_threshold (4) |
| NOMD | 4 | target_return_below_threshold (4) |
| NRG | 12 | target_return_below_threshold (12) |
| NTLA | 8 | target_return_below_threshold (8) |
| NTR | 8 | target_return_below_threshold (8) |
| NTSK | 19 | target_return_below_threshold (19) |
| NU | 8 | target_return_below_threshold (8) |
| NVDA | 4 | liquidity_too_low (3), invalid_signal_payload (1) |
| NVT | 4 | target_return_below_threshold (4) |
| ODD | 8 | target_return_below_threshold (4), liquidity_too_low (2), bracket_invalid (1), spread_too_wide (1) |
| OI | 4 | target_return_below_threshold (4) |
| OKLO | 4 | target_return_below_threshold (4) |
| OKTA | 4 | target_return_below_threshold (4) |
| OLN | 17 | target_return_below_threshold (17) |
| ON | 4 | target_return_below_threshold (4) |
| ONB | 4 | target_return_below_threshold (4) |
| ONDS | 12 | target_return_below_threshold (8), invalid_signal_payload (2), liquidity_too_low (1), spread_too_wide (1) |
| ONON | 8 | target_return_below_threshold (4), invalid_signal_payload (3), liquidity_too_low (1) |
| ORCL | 12 | liquidity_too_low (8), target_return_below_threshold (4) |
| ORLA | 8 | target_return_below_threshold (8) |
| OTEX | 4 | target_return_below_threshold (4) |
| OWL | 2 | target_return_below_threshold (2) |
| OXY | 8 | target_return_below_threshold (4), liquidity_too_low (3), spread_too_wide (1) |
| PAGS | 4 | target_return_below_threshold (4) |
| PATH | 15 | target_return_below_threshold (15) |
| PAYX | 4 | target_return_below_threshold (4) |
| PBI | 4 | target_return_below_threshold (4) |
| PCAR | 4 | target_return_below_threshold (4) |
| PCOR | 4 | target_return_below_threshold (4) |
| PDD | 4 | target_return_below_threshold (4) |
| PENN | 29 | target_return_below_threshold (15), bracket_invalid (14) |
| PEP | 4 | target_return_below_threshold (4) |
| PFGC | 12 | target_return_below_threshold (12) |
| PGR | 8 | target_return_below_threshold (8) |
| PINS | 4 | target_return_below_threshold (4) |
| PK | 8 | target_return_below_threshold (8) |
| PL | 4 | target_return_below_threshold (4) |
| PONY | 33 | target_return_below_threshold (29), liquidity_too_low (3), spread_too_wide (1) |
| PR | 4 | target_return_below_threshold (4) |
| PRCT | 19 | target_return_below_threshold (19) |
| PRGO | 19 | target_return_below_threshold (19) |
| PSKY | 21 | target_return_below_threshold (21) |
| PSTG | 4 | target_return_below_threshold (4) |
| PUMP | 25 | target_return_below_threshold (25) |
| Q | 15 | target_return_below_threshold (15) |
| QURE | 35 | target_return_below_threshold (35) |
| QXO | 11 | target_return_below_threshold (11) |
| RBRK | 8 | target_return_below_threshold (8) |
| RCAT | 10 | target_return_below_threshold (10) |
| REAL | 29 | target_return_below_threshold (29) |
| RELY | 4 | target_return_below_threshold (4) |
| RGTI | 21 | target_return_below_threshold (21) |
| RIOT | 8 | target_return_below_threshold (8) |
| RKLB | 4 | liquidity_too_low (4) |
| RKT | 15 | target_return_below_threshold (15) |
| RNG | 14 | target_return_below_threshold (14) |
| ROKU | 4 | target_return_below_threshold (4) |
| RWM | 4 | target_return_below_threshold (4) |
| SAIL | 12 | target_return_below_threshold (12) |
| SAN | 4 | target_return_below_threshold (4) |
| SBRA | 4 | target_return_below_threshold (4) |
| SCCO | 4 | target_return_below_threshold (4) |
| SCO | 4 | target_return_below_threshold (4) |
| SDOW | 12 | target_return_below_threshold (12) |
| SE | 4 | target_return_below_threshold (4) |
| SEI | 20 | target_return_below_threshold (20) |
| SEM | 7 | target_return_below_threshold (7) |
| SFM | 8 | target_return_below_threshold (8) |
| SGI | 8 | target_return_below_threshold (8) |
| SHOP | 4 | target_return_below_threshold (4) |
| SIRI | 17 | target_return_below_threshold (17) |
| SJM | 4 | target_return_below_threshold (4) |
| SLDE | 8 | target_return_below_threshold (8) |
| SLM | 4 | target_return_below_threshold (4) |
| SMCI | 19 | target_return_below_threshold (12), liquidity_too_low (7) |
| SMFG | 4 | target_return_below_threshold (4) |
| SMR | 29 | target_return_below_threshold (29) |
| SMTC | 19 | target_return_below_threshold (19) |
| SN | 8 | target_return_below_threshold (8) |
| SNDK | 8 | target_return_below_threshold (8) |
| SOC | 25 | target_return_below_threshold (25) |
| SOFI | 15 | target_return_below_threshold (15) |
| SOLS | 4 | target_return_below_threshold (4) |
| SPXU | 4 | target_return_below_threshold (4) |
| SRAD | 16 | target_return_below_threshold (16) |
| SRPT | 15 | target_return_below_threshold (15) |
| SSL | 8 | target_return_below_threshold (8) |
| SSNC | 4 | target_return_below_threshold (4) |
| SSRM | 8 | target_return_below_threshold (8) |
| STX | 12 | target_return_below_threshold (12) |
| SU | 4 | target_return_below_threshold (4) |
| SUZ | 4 | target_return_below_threshold (4) |
| SWKS | 11 | target_return_below_threshold (11) |
| T | 4 | target_return_below_threshold (4) |
| TECH | 4 | target_return_below_threshold (4) |
| TECK | 12 | target_return_below_threshold (12) |
| TEL | 4 | target_return_below_threshold (4) |
| TENB | 32 | target_return_below_threshold (32) |
| TER | 4 | target_return_below_threshold (4) |
| TERN | 4 | target_return_below_threshold (4) |
| TGT | 4 | liquidity_too_low (4) |
| TME | 4 | target_return_below_threshold (4) |
| TMUS | 4 | target_return_below_threshold (4) |
| TNDM | 10 | target_return_below_threshold (10) |
| TNGX | 24 | target_return_below_threshold (24) |
| TOST | 4 | target_return_below_threshold (4) |
| TQQQ | 3 | target_return_below_threshold (3) |
| TRI | 8 | target_return_below_threshold (8) |
| TRU | 4 | target_return_below_threshold (4) |
| TSEM | 29 | target_return_below_threshold (29) |
| TSLA | 4 | liquidity_too_low (3), spread_too_wide (1) |
| TSM | 4 | target_return_below_threshold (4) |
| TSN | 4 | target_return_below_threshold (4) |
| TXN | 4 | target_return_below_threshold (4) |
| U | 21 | target_return_below_threshold (21) |
| UAL | 4 | target_return_below_threshold (4) |
| UBER | 4 | target_return_below_threshold (4) |
| UCO | 4 | target_return_below_threshold (4) |
| UEC | 8 | liquidity_too_low (7), spread_too_wide (1) |
| UMAC | 4 | target_return_below_threshold (4) |
| UUUU | 4 | target_return_below_threshold (4) |
| VET | 4 | target_return_below_threshold (4) |
| VFC | 25 | target_return_below_threshold (25) |
| VG | 37 | target_return_below_threshold (37) |
| VIAV | 7 | target_return_below_threshold (7) |
| VISN | 4 | target_return_below_threshold (4) |
| VLO | 4 | target_return_below_threshold (4) |
| VLY | 4 | target_return_below_threshold (4) |
| VNET | 4 | target_return_below_threshold (4) |
| VSNT | 4 | target_return_below_threshold (4) |
| VST | 4 | target_return_below_threshold (4) |
| VTR | 15 | target_return_below_threshold (15) |
| VXX | 4 | target_return_below_threshold (4) |
| W | 4 | target_return_below_threshold (4) |
| WAY | 12 | target_return_below_threshold (8), liquidity_too_low (4) |
| WBS | 4 | target_return_below_threshold (4) |
| WDC | 12 | target_return_below_threshold (12) |
| WIX | 4 | target_return_below_threshold (4) |
| WPM | 4 | liquidity_too_low (4) |
| WRBY | 25 | target_return_below_threshold (25) |
| WSC | 4 | target_return_below_threshold (4) |
| WULF | 16 | liquidity_too_low (7), target_return_below_threshold (4), invalid_signal_payload (3), spread_too_wide (2) |
| XENE | 4 | target_return_below_threshold (4) |
| XPEV | 8 | liquidity_too_low (4), target_return_below_threshold (4) |
| XPO | 4 | target_return_below_threshold (4) |
| XYZ | 4 | target_return_below_threshold (4) |
| YPF | 4 | target_return_below_threshold (4) |
| Z | 4 | target_return_below_threshold (4) |
| ZETA | 4 | target_return_below_threshold (4) |
| ZM | 4 | invalid_signal_payload (3), liquidity_too_low (1) |
| ZSL | 19 | target_return_below_threshold (16), liquidity_too_low (3) |
| ZTO | 4 | target_return_below_threshold (4) |
