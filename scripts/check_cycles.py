#!/usr/bin/env python3
import sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED = ["cycle.md", "selection.md", "amplification.md", "iteration.md"]

def read(p: pathlib.Path): 
    try: return p.read_text(encoding="utf-8").strip()
    except: return ""

def main():
    failures = 0
    for cdir in sorted((ROOT/"cycles").glob("*_*")):
        if not cdir.is_dir(): 
            continue
        missing = [f for f in REQUIRED if not (cdir/f).exists()]
        if missing:
            print(f"❌ {cdir.name}: missing {missing}")
            failures += 1
            continue
        # iteration must contain an explicit next action
        iteration = read(cdir/"iteration.md")
        if not iteration or "next" not in iteration.lower():
            print(f"❌ {cdir.name}: iteration.md should contain explicit next steps")
            failures += 1
        else:
            print(f"✅ {cdir.name}: cycle files present and iteration has next steps")
    if failures:
        sys.exit(1)
    print("✅ All cycles pass completeness checks.")

if __name__ == "__main__":
    main()
