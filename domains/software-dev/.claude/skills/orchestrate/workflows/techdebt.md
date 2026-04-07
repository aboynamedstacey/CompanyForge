# Tech Debt / Refactor Workflow

Always incremental. Every step leaves the system working.

**Prerequisite:** Ceremony tier determined.

---

## Phase 1: ANALYZE

Dispatch **Scout** (Sonnet):

> Analyze this tech debt: "{description}"
> 1. **Impact** — what depends on the code being changed? Blast radius?
> 2. **Risk** — what could break? What's hard to test?
> 3. **Dependency map** — graph of affected modules
> 4. **Prior experience** — query cross-session memory for similar refactors

---

## Phase 2: PLAN

Dispatch **Builder** (Opus, design prompt):

> Plan an incremental refactor.
> **Analysis:** {scout_output}
>
> Each increment must be:
> - Independently shippable (system works after each step)
> - Rollback-safe (clear path to undo)
> - Ordered by risk (safe foundational changes first)
> - No big-bang rewrites — strangler fig preferred
>
> Per increment: what changes, tests to add BEFORE changing code,
> how to verify, file scope.

---

## Phase 3: HUMAN GATE [Large only]

> **Refactoring Plan**
> Increments: {count} | Risk: {assessment}
> Approve / Reduce scope / Reject?

---

## Phase 4: IMPLEMENT (per increment)

Same as Feature Phase 6, but: run COMPLETE test suite after EVERY increment.
Refactors have unexpected blast radius.

---

## Phase 5: RELEASE

Builder (release prompt) → PR with increment summary.

---

## Phase 6: HUMAN GATE

Present with increment summary and full regression results.
