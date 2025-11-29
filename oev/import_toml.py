"""Compatibility module named ``import_toml`` used by `oev/main.py`.

This duplicates the small TOML-loading utilities so code that imports
``import_toml`` (instead of the file named ``import.py``) works from
the CLI and tests.
"""

from __future__ import annotations

import json
import sys
import tomllib
from pathlib import Path
from typing import Optional, Union, Any, Dict


def find_file_in_parent_dirs(
    filename: str, start_path: Union[str, Path, None] = None
) -> Optional[Path]:
    start = Path(start_path).resolve() if start_path is not None else Path.cwd().resolve()
    for candidate_dir in (start, *start.parents):
        candidate = candidate_dir / filename
        if candidate.is_file():
            return candidate
    return None


def load_toml_from_parent(filename: str = "config.toml", start_path: Union[str, Path, None] = None) -> Dict[str, Any]:
    path = find_file_in_parent_dirs(filename, start_path)
    if path is None:
        raise FileNotFoundError(f"Could not find '{filename}' starting at '{start_path or Path.cwd()}'.")
    with path.open("rb") as fh:
        return tomllib.load(fh)


def _main(argv: list[str] | None = None) -> int:
    import argparse

    argv = argv if argv is not None else sys.argv[1:]
    parser = argparse.ArgumentParser(description="Find and print a TOML file from parent directories.")
    parser.add_argument("-f", "--file", default="config.toml", help="Filename to search for")
    parser.add_argument("-s", "--start", default=None, help="Start directory to search from (default: cwd)")
    parser.add_argument("-j", "--json", action="store_true", help="Print as JSON")
    args = parser.parse_args(argv)

    try:
        data = load_toml_from_parent(args.file, args.start)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    print(json.dumps(data, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
