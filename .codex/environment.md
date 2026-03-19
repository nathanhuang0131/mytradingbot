# Codex Project Environment

Project root: MyTradingBot_Next
Python environment: **mytradingbot**

Activate before running any commands:

Windows:

```
mytradingbot\Scripts\activate
```

Dependencies:

```
pip install -e .[dev]
```
```md
## Repository operating rules

- Always operate from the repo-local root: `C:\Users\User\Documents\MyTradingBot_Next`
- Do not introduce writes outside the repository root
- Prefer the canonical `mytradingbot` environment
- Preserve the working end-to-end pipeline unless a change is clearly required
- All signal decisions must be observable and reportable
- Every buy, bracket buy, short, bracket short, rejection, skip, or no-action must be traceable through logs and audit artifacts
- Favor typed, modular, testable changes
- When changing runtime behavior, update docs and tests in the same patch