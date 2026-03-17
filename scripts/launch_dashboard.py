import subprocess
import sys


def main() -> int:
    return subprocess.call([sys.executable, "-m", "streamlit", "run", "app/app.py"])


if __name__ == "__main__":
    raise SystemExit(main())
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    project_root = Path(__file__).resolve().parents[1]
    return subprocess.call(
        [sys.executable, "-m", "streamlit", "run", str(project_root / "app" / "app.py")],
        cwd=project_root,
    )


if __name__ == "__main__":
    raise SystemExit(main())
