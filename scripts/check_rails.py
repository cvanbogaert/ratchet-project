#!/usr/bin/env python3
import hashlib, json, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
cfg_path = ROOT / "config" / "rails_checksums.json"
if not cfg_path.exists():
    print("No rails_checksums.json found; skipping (treat as pass for first run).")
    sys.exit(0)

cfg = json.loads(cfg_path.read_text())
bad=[]
for rel, want in cfg.items():
    p = ROOT / rel
    if not p.exists():
        bad.append(rel + " (missing)")
        continue
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    if h != want:
        bad.append(rel)
if bad:
    print("Rails checksum mismatch for:", ", ".join(bad))
    sys.exit(1)
print("Rails checksums OK.")
