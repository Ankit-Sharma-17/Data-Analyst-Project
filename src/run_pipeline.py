from __future__ import annotations

from pathlib import Path
import subprocess
import sys


SCRIPTS = [
    "src/generate_data.py",
    "src/etl.py",
    "src/analysis.py",
    "src/visualize.py",
]


def run(script: str, root: Path) -> None:
    cmd = [sys.executable, str(root / script)]
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    for script in SCRIPTS:
        run(script, root)
    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
