"""Check every tracked JSON, YAML and shell file parses, and every plugin manifest names itself.

Run from the repository root: python3 .github/scripts/validate_files.py
"""
import json
import pathlib
import subprocess
import sys

import yaml

files = subprocess.run(["git", "ls-files", "-z"], capture_output=True, check=True).stdout.decode().split("\0")
problems = []
checked = 0

for name in files:
    path = pathlib.Path(name)
    if not name or not path.is_file():
        continue
    try:
        if path.suffix == ".json":
            data = json.loads(path.read_text(encoding="utf-8"))
            if path.parent.name == ".claude-plugin" and path.name == "plugin.json":
                if not isinstance(data, dict) or not data.get("name"):
                    problems.append(f"{name}: plugin manifest has no name")
        elif path.suffix in (".yml", ".yaml"):
            list(yaml.safe_load_all(path.read_text(encoding="utf-8")))
        elif path.suffix == ".sh":
            result = subprocess.run(["bash", "-n", name], capture_output=True, text=True)
            if result.returncode:
                problems.append(f"{name}: {result.stderr.strip()}")
        else:
            continue
        checked += 1
    except Exception as error:  # report every bad file, not just the first
        problems.append(f"{name}: {error}")

for problem in problems:
    print(f"::error::{problem}")
print(f"Checked {checked} files, {len(problems)} problem(s).")
sys.exit(1 if problems else 0)
