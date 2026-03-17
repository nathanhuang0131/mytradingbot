# One-Shot Master Brief

Build a new institutional-style quant trading platform from scratch in this repository.

This project is based on the product requirements and design discussions from prior planning conversations, but it must not reuse or reference any previous codebase.

## Platform objectives

The platform must:
- use qlib for dataset, training, and predictions
- support scalping, intraday, short_term, and long_term strategies
- support paper trading first
- support live trading with explicit safeguards
- expose a Streamlit dashboard as the main operator interface
- include LLM-assisted advisory workflows
- include diagnostics, maintenance, validation, and reporting

## User experience objective

The user should primarily operate the system through the dashboard:
- choose strategy
- choose trading mode
- trigger training and maintenance
- refresh predictions
- run sessions
- inspect diagnostics
- review post-market outcomes

## Implementation objective

Create a clean modular repo with:
- strong boundaries
- thin scripts
- typed models
- strong testing
- future-proof structure