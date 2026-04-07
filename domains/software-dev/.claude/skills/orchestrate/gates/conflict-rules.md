# Conflict Resolution — Software Development

Inherits universal rules from shared `conflict-rules-base.md`.

---

## Domain-Specific Priority

1. **Security blocks everything.** Critical security finding → workflow stops.
2. **Verifier overrides Reviewer.** Tool says wrong = wrong, regardless of agent opinion.
3. **Spec defines "what."** Builder builds it, Reviewer checks it. Neither debates requirements.
4. **"How" disagreements:** security position wins > simpler approach > CLAUDE.md conventions > human.
5. **Cross-model disagreement → human.** Likely a genuine blind spot.

## Defense in Depth

Five layers, in order of reliability:
1. Verifier (tools) — no bias
2. Reviewer (checklist) — structured prompts force coverage
3. Reviewer (adversarial) — "find N problems" counters agreement bias
4. Cross-model review — catches Claude-specific blind spots
5. Human review — final authority at gates
