# Bug Fix Workflow

Typically Small or Medium. If a bug needs Large ceremony, it's probably
a feature or redesign.

**Prerequisite:** Ceremony tier determined.

---

## Phase 1: INVESTIGATE

Dispatch **Scout** (Sonnet):

> Investigate this bug: "{description}"
> 1. **Reproduce** — exact steps or conditions
> 2. **Root cause** — trace data/control flow to where it breaks
> 3. **Blast radius** — what else shares the same root cause
> 4. **Prior experience** — check cross-session memory for similar bugs
>
> DO NOT propose a fix. Investigate only.
> Output: reproduction steps, root cause with file:line, blast radius.

---

## Phase 2: FIX (TDD)

Dispatch **Builder** (Sonnet) with implementation prompt:

> Fix this bug using TDD.
> **Root cause:** {scout_output}
>
> 1. Write a failing test that reproduces the bug exactly
> 2. Verify it FAILS (if it passes, test doesn't capture the bug)
> 3. Fix the root cause — minimal changes
> 4. Verify test PASSES
> 5. Run FULL regression suite
> 6. Commit
>
> Fix the root cause, not symptoms. If root cause differs from report,
> report back before fixing.

---

## Phase 3: VERIFY

Verifier (tools): type check, lint, full test suite. All must pass.

---

## Phase 4: REVIEW

Small: Reviewer with combined checklist. Focus: root cause addressed? Regressions? Test accurate?
Medium: Reviewer 3× parallel (quality ‖ security ‖ functional).

---

## Phase 5: RELEASE

Builder (release prompt) → create PR.

---

## Phase 6: HUMAN GATE [Medium only]

Small bugs: PR created, human reviews async.
Medium bugs: explicit approval gate.

---

## Phase 7: POST-FIX [Medium only]

Scout (knowledge extraction): Was this bug class preventable? Propose checklist addition.
