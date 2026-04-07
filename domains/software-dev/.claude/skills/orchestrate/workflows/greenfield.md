# Greenfield Workflow

Bootstrap a new project. Always Medium minimum.

---

## Phase 1: RESEARCH

Scout (Sonnet):
> Evaluate technology options for: "{description}"
> - How have others built this? What worked?
> - Framework/language options with trade-offs for THIS project
> - Environment constraints (existing tooling, runtimes)
> - Prior experience from cross-session memory

Present options, not decisions. Human picks the stack.

---

## Phase 2: HUMAN GATE — Technology

> **Technology Options**
> {Options with trade-offs}
> Recommended: {stack} because {rationale}
> Approve / Modify?

---

## Phase 3: SPEC

Builder (Sonnet, spec prompt):
> Define the foundation for: "{description}" on {stack}
> Core entities, core operations (3-5 for day one), API surface,
> non-goals for v1, acceptance criteria.

---

## Phase 4: DESIGN

Builder (Opus, design prompt):
> Design the architecture. Project structure, data model, API design,
> testing strategy, CI/CD, work unit decomposition.
> Boring technology. Minimal dependencies. Simplest thing that works.

---

## Phase 5: REVIEW + HUMAN GATE

Same as Feature Phase 4-5.

---

## Phase 6: SCAFFOLD

Builder (Sonnet, implementation prompt):
> Create project foundation: package init, directory structure, tooling
> (lint, format, type check, test), .gitignore, CLAUDE.md, one passing test.
> Run all tools. Commit.

---

## Phase 7: IMPLEMENT CORE

Per work unit, same as Feature Phase 6.

---

## Phase 8: RELEASE + POST-BOOTSTRAP

Builder (release prompt) → initial PR.
Builder (Haiku, docs prompt) ‖ Scout (knowledge extraction) in parallel.
