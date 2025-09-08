#!/usr/bin/env python3
import hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
targets = [
    "scripts/loop.py",
    "config/rails.toml",
    "scripts/evaluator_backtest.py",
    "docs/LOOP_PROTOCOL.md",
]
out = {}
for rel in targets:
    p = ROOT / rel
    if not p.exists():
        continue
    out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()

cfg_path = ROOT / "config" / "rails_checksums.json"
cfg_path.parent.mkdir(parents=True, exist_ok=True)
cfg_path.write_text(json.dumps(out, indent=2))
print("Wrote", cfg_path)
