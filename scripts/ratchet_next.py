#!/usr/bin/env python3
import os, sys, datetime, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent

def next_cycle_id():
    cycles = sorted([p.name for p in (ROOT / "cycles").glob("[0-9][0-9][0-9][0-9]_*/") if p.is_dir()])
    if not cycles:
        return "0000_m0"
    last = cycles[-1]
    m = re.match(r"(\d{4})_(.*)", last)
    if not m:
        return "0000_m0"
    n = int(m.group(1)) + 1
    return f"{n:04d}" + "_step"

def main():
    cid = next_cycle_id()
    today = datetime.date.today().isoformat()
    cdir = ROOT / "cycles" / cid
    (cdir / "artifacts").mkdir(parents=True, exist_ok=True)
    tmpl = (ROOT / "templates" / "cycle_entry.md").read_text()
    content = tmpl.replace("${ID}", cid).replace("${DATE}", today)
    (cdir / "cycle.md").write_text(content)
    (cdir / "selection.md").write_text("# Selection\n\n(Record what survived and why.)\n")
    (cdir / "amplification.md").write_text("# Amplification\n\n(Record what was reinforced and how.)\n")
    (cdir / "iteration.md").write_text("# Iteration\n\n(Leave explicit next steps.)\n")
    print(f"Created {cdir}")

if __name__ == "__main__":
    main()
