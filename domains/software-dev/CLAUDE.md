# Software Development — AI Engineering Organization

Work flows through three capability types coordinated by a workflow engine.
There is no hierarchy, no departments, and no job titles.

## Quick Start

```
/dev add a REST endpoint for user authentication
/dev fix the race condition in the queue processor
/dev refactor the payment module to use the new gateway interface
/dev research whether we should migrate from REST to gRPC
/dev start a new project from scratch
```

Just `/dev` + what you'd tell an engineer.

## Organizational Model

```
HUMAN → WORKFLOW ENGINE → CAPABILITY TYPES → RULE SYSTEM → MEMORY LAYER
```

### Why Not Roles

Human engineering teams have PMs, architects, developers, QA, security
engineers, and tech writers because humans can only do one thing at a time
and need career paths. An AI agent with the right prompt can write a spec,
design an architecture, implement code, and write docs — those are phases
of work, not different capabilities. What DOES need to be organizationally
separate is the drafter and the reviewer, because self-review is worthless.

### Capability Types (3 + tools)

| Type | Model | What It Does |
|---|---|---|
| **Builder** | Sonnet | Produces artifacts. Dispatched with different prompts for different phases: spec writing, system design, implementation, documentation. One type, many uses. |
| **Reviewer** | Opus (always fresh) | Adversarial critique. Dispatched with different checklists for quality, security, functional correctness, or architecture. Never the same instance that built the artifact. |
| **Scout** | Haiku→Sonnet | Gathers context before building begins. Codebase analysis, domain research, prior art, dependency review. Cheap model first, escalates if depth is needed. |
| **Verifier** | Tools (not an agent) | Deterministic checks: lint, type check, test suite, security scanner. Runs BEFORE any agent review. Tool results are authoritative — agent opinions don't override them. |

### Ceremony Tiers

| Tier | Composition | Review | Human Gates |
|---|---|---|---|
| Trivial | Builder alone | Verifier only | None |
| Small | Builder → Verifier → Reviewer (combined checklist) | One pass | None |
| Medium | Scout → Builder → Verifier → Reviewer (parallel checklists) → cross-model | Three-pass + parallel | Architecture + PR |
| Large | Full pipeline, parallel work units, mid-point checkpoint | Everything | All gates |

### What Changes Between Tiers

The capability types stay the same. What changes is the number and depth of
dispatches. A trivial task dispatches Builder once. A large feature dispatches
Builder 5 times (spec, design, implementation × 3 work units), Reviewer 4 times
(architecture, quality, security, functional — some in parallel), and Scout twice
(domain research, codebase analysis). Same 3 types, different composition.

## Communication Protocol

- **Direct context injection** — orchestrator passes output to next dispatch's prompt
- **No file-based handoffs** — artifacts exist for humans and future sessions, not agent-to-agent
- **Parallel where possible** — review checklists dispatched simultaneously
- **No status reporting** — orchestrator has full visibility

## Quality Standards

- TDD mandatory for all implementation (red → green → refactor)
- Verifier (tools) runs before Reviewer (agent) — always
- Fresh instance for every review dispatch (never self-review)
- Cross-model review (Gemini/GPT) for Medium+ architecture and security
- Adversarial prompting: "find at least N problems" in every review
- Known AI limitations flagged in every review prompt

## Conflict Resolution

1. Security blocking issues override all other concerns
2. Verifier (tool) results override Reviewer (agent) opinions
3. Product spec defines "what" — capabilities build, not debate
4. When dispatches disagree on "how": security wins > simpler approach > CLAUDE.md conventions > human tiebreak
5. Cross-model disagreement → automatic human escalation

Full rules: `.claude/skills/orchestrate/gates/conflict-rules.md`

## Memory Layers

| Layer | Stores |
|---|---|
| This file (CLAUDE.md) | How the org works |
| docs/specs/, docs/designs/, docs/adr/ | Persistent artifacts |
| State tracking (BEADS) | Task state, dependencies |
| Cross-session memory | Cross-project knowledge |
| Auto-memory | Project conventions |
| Git history | Code changes |
