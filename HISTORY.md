# Ratchet Project — M1 Release

## Date
2025-09-08

## Overview
- First stable constitution of the agent-on-rails layer.
- Simplified, interpretable loop: Pick → Propose → Approve → Apply+Score → Log → Repeat.
- Unified config (`config/rails.toml`) for policy, evaluator, budgets, liveness.
- Seed utility formula documented and versioned.
- Golden set anchors established.
- Rail protection policies defined (codeowners, checksums, backtests).
- Heartbeat provider + watchdog guarantee no-flicker-out.
- Explicit human gate ensures no escape.

## Intent Alignment
- **Foundation respected:** every patch is survival pressure.  
- **Horizon respected:** your role is intent + approve/reject only.  
- **Simplicity & interpretability:** config-driven, one file; logs are plain JSON; evaluator is a weighted sum.  
- **Cheap & safe:** local-first, free-first, guardrails always on.
