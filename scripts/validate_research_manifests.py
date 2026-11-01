#!/usr/bin/env python3
"""Validate all research-run manifest JSON files against the shared schema."""
import json
import sys
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
except ImportError:
    sys.exit("Missing dependency: install with 'python -m pip install jsonschema'")

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "research/templates/research-run-manifest.schema.json"
schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema, format_checker=FormatChecker())
paths = sorted((ROOT / "research/provisions").rglob("*-manifest.json"))
if not paths:
    sys.exit("No research run manifests found")
failures = 0
for path in paths:
    try:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(manifest), key=lambda e: str(e.path))
        for error in errors:
            print(f"{path.relative_to(ROOT)}: {'.'.join(map(str,error.path)) or '<root>'}: {error.message}")
        failures += len(errors)
        if not errors:
            print(f"OK {path.relative_to(ROOT)}")
    except (ValueError, OSError) as exc:
        print(f"{path.relative_to(ROOT)}: {exc}")
        failures += 1
sys.exit(1 if failures else 0)
