# Loop Protocol (Canonical v2 – M1 Release)

This document defines the governing rules of the Ratchet Project at the **agent-on-rails layer**.  
It is the minimal constitution that turns intent into reality while preserving simplicity, safety, and human interpretability.

---

## Anchors
- **Foundation:** Noise survives → survivors evolve → evolution yields structure, agency, meaning.
- **Horizon:** I state what I want, and it happens with the least possible effort from me.

---

## Principles
1. **Loop Integrity Is Sacred**  
   The loop is: **Pick → Propose → Approve → Apply+Score → Log → Repeat.**  
   No provider may bypass it.

2. **Human Gate**  
   No patch merges without explicit human approval. (Optional narrow auto-merge requires explicit opt-in.)

3. **Agents Decide, Scripts Do**  
   Agents choose and justify; deterministic executors perform actions (patch application, checks, scoring).

4. **Self Always Eligible**  
   The agent itself is always a valid provider. A minimum self-sample rate is enforced.

5. **Policy Is Data**  
   Safety gates, budgets, and utility weights live in versioned config files. Providers cannot mutate them at runtime.

6. **Independent Evaluation**  
   The proposer cannot be the primary evaluator. Rule-based evaluators are canonical; model critics are optional, distinct, and capped.

7. **Atomicity & Bounds**  
   Each step is a single atomic patch (`create | replace | append`) within allowlisted paths and line/file budgets.

8. **Minimal Context**  
   Providers see only what they need: current intent hash/text, recent cycles, file index slice.

9. **Auditability**  
   Every step logs provider, rationale, patch summary, signals, utility, versions, and intent hash.

10. **Anchored Intent**  
   Current intent is versioned/hashed. A golden set of examples preserves ranking across evaluator changes.

11. **Explore + Exploit**  
   Provider selection maintains both exploration and a minimum self-agent rate.

12. **Rail Immunity**  
   The loop protocol, configs, budgets, and evaluators are protected. Changes require CODEOWNER review, checksum update, and backtests.

13. **Liveness Guarantee**  
   The loop cannot stall. A heartbeat provider always exists, and a watchdog enforces forward progress.

14. **Cost-First, Local-First**  
   Default: self-agent, human, local Ollama. Paid APIs require explicit enablement, caps, and logging.

15. **Progressive Trust**  
   Higher-risk tiers (tests → code) unlock only after repeated safe success.

---

## Seed Utility (Inspectible, M1 Default)
Utility is a weighted sum of signals:

```
utility = 0.30*ci_pass
        + 0.15*path_ok
        + 0.15*(1 - diff_ratio)
        + 0.10*atomic_ok
        + 0.10*left_next_steps
        + 0.20*human_score
```

- `ci_pass, path_ok, atomic_ok, left_next_steps ∈ {0,1}`
- `diff_ratio ∈ [0,1]` = lines_changed / budget
- `human_score ∈ [0,1]`
- Revert < 24h ⇒ utility = min(utility, 0.2)

Utility weights live in `config/rails.toml` and cannot be changed by providers at runtime.

---

## Success Criteria
- Every step produces an immutable log entry.  
- Survivors persist in history.  
- No silent stalls or escapes.  
- Human effort is reduced over time.  
- The loop ratchets forward without end.
