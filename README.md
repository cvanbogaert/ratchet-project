# The Ratchet Project
*A universal agent architecture built on Foundations, guided by the Horizon, and driven by the Cycle.*

## 🌍 Foundations (substrate law)
Noise survives. Survivors evolve. Evolution yields structure, agency, and meaning.

## 🌅 Horizon (north star)
I want to say what I want, and have it happen with the least possible effort.

## 🔄 The Cycle (the ratchet process)
1. **Variation** → Generate drafts, options, noise.
2. **Selection** → Feedback filters what persists.
3. **Amplification** → Survivors are reinforced and recorded.
4. **Iteration** → Survivors seed the next cycle.

Each cycle must lock in some forward progress, no matter how small.

---

## 🎯 Mission
Build a universal agent that continuously ratchets environmental noise into agency, minimizing human effort to turn intent into reality.

## 🏗️ Stack Layers
- **Foundation Layer** → Treat artifacts as variation; selection via tests/constraints/intent.
- **Cycle Layer** → Encode the ratchet loop explicitly.
- **Intent Interface Layer** → Plain language → intents → DAGs → actions.
- **Horizon Layer** → Measure everything by effort reduced to realize intent.

## 🗂️ History Encoding Principle
- History is a **scaffold, not a burden**.
- Capture just enough: foundations, last cycle state, key artifacts.
- Encode as structured logs, DAG snapshots, fact-sheets.
- Ensure any new agent can pick up and ratchet forward.

---

## 📦 Repo Layout
```
/.ratchet/            # canonical statements of Foundations, Horizon, Cycle
/cycles/              # one folder per cycle (0000_m0, 0001_..., ...)
/facts/               # durable facts worth carrying forward
/history/             # compact event log
/intents/             # backlog + current intent
/plans/               # decompositions/DAG snapshots
/schemas/             # JSON Schemas for core objects
/scripts/             # helper scripts (create next cycle, verify)
/templates/           # markdown templates for cycle entries, DAG, decisions
/tests/               # minimal test plan (selection pressures)
```

## 🚀 Quickstart
1. Edit **intents/current_intent.md** to say what you want.
2. Run:
   ```bash
   python3 scripts/ratchet_next.py
   ```
   This creates a new cycle folder, pre-populated from templates.
3. Execute your variation work in the cycle folder. Update **selection.md**, **amplification.md**, and **iteration.md**.
4. Commit and push. The next agent repeats step 1–3, ratcheting forward.

---

**M0 Date:** 2025-09-08

---

## 🧪 CI
This repo uses GitHub Actions to validate formatting and cycle completeness on every push/PR.

**Local dev**
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
pre-commit install
make ci
```

**Open-source license:** MIT
