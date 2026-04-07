# Iteration Protocol

How review feedback loops work.

---

## Loop

Review returns FAIL → route ALL issues to Builder → Builder fixes + Verifier
runs → re-dispatch Reviewer (fresh instance) → repeat until PASS or cap.

## Caps

- **3 iterations** per checklist. Then escalate to human.
- **30% of budget** consumed by any single review loop. Then escalate regardless.

## Scope Control

Reviewer finds problems in submitted code. It does NOT request features or
suggest redesigns. If review feedback amounts to "redesign this," escalate
to human — don't loop.

Reviewer capped at 5 issues per dispatch to prevent review inflation.

## Fresh Instance

Every iteration: fresh Reviewer. Never sees its own prior review.
Prevents anchoring on previously identified issues.
