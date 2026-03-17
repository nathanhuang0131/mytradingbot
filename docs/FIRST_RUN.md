# First Run

## 1. Install The Project

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .[dev]
```

## 2. Verify The Test Suite

```bash
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 pytest -q
```

## 3. Prepare Runtime Artifacts

Paper and dry-run sessions need both of these artifacts:

- `models/predictions/latest.json`
- `data/runtime/market_snapshot.json`

You can also pass explicit file paths to the paper trading CLI:

```bash
python scripts/run_paper_trading.py --strategy scalping --mode paper --predictions-file <path> --market-data-file <path>
```

## 4. Understand Qlib Availability

- The dashboard launches even if `pyqlib` is not installed.
- Dataset build, training, and prediction refresh actions fail clearly until qlib is installed and configured.
- Existing runtime prediction artifacts can still be loaded for paper trading without `pyqlib`.

## 5. Launch The Dashboard

```bash
streamlit run app/app.py
```

## 6. First Operator Workflow

1. Open the dashboard.
2. Go to `Strategy Control` and confirm the selected strategy and mode.
3. Go to `Paper Trading` and run a `dry_run` or `paper` session.
4. Review `Diagnostics` and `LLM Copilot`.
