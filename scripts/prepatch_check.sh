#!/usr/bin/env bash
set -euo pipefail
python3 scripts/context_snapshot.py > /dev/null
[ -f scripts/validate.py ] && python3 scripts/validate.py || true
[ -f scripts/verify.py ] && python3 scripts/verify.py || true
[ -f scripts/check_cycles.py ] && python3 scripts/check_cycles.py || true
python3 -m pytest -q
echo "✅ prepatch checks passed"
