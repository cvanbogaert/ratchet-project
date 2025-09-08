#!/usr/bin/env python3
import json, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

REQUIRED_TOP = [".ratchet", "cycles", "facts", "history", "intents", "plans", "schemas", "scripts", "templates", "tests"]

def ok(cond, msg):
    print(("✅" if cond else "❌") + " " + msg)
    return cond

def main():
    all_ok = True
    for d in REQUIRED_TOP:
        all_ok &= ok((ROOT / d).exists(), f"exists: {d}")
    print("Done.")
    sys.exit(0 if all_ok else 1)

if __name__ == "__main__":
    main()
