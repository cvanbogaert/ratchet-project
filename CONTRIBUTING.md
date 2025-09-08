# Contributing

## Workflow
1. State the intent in `intents/current_intent.md`.
2. Create a new cycle: `python3 scripts/ratchet_next.py`.
3. Do the work inside the new cycle directory.
4. Update `selection.md`, `amplification.md`, `iteration.md` (explicit next steps).
5. Open a PR. CI must pass.

## Commit hygiene
- Keep commits small and purposeful.
- Reference the cycle ID in commit messages.
- Let pre-commit fix trivial issues: `pre-commit run -a`.
