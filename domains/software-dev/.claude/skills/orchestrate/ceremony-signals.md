# Ceremony Calibration — Software Development

Inherits the calibration process from shared `ceremony-calibration-base.md`.

---

## Greenfield Override

First feature in a new codebase: always MEDIUM regardless of size signals.
Architectural decisions in a new project have outsized impact.

## Size Signals

| Signal | Trivial | Small | Medium | Large |
|---|---|---|---|---|
| Files affected | 1-2 | 3-10 | 10-30 | 30+ |
| Modules touched | 0 | 1 | 2-3 | 4+ |
| New API surface | None | Minimal | Moderate | Significant |
| Data model changes | None | None | Minor | Schema changes |
| Domain knowledge | None | Minimal | Some | Deep research |
| Keywords | "fix typo", "rename", "config" | "add endpoint", "utility" | "add feature", "integrate" | "build system", "rewrite", "migrate" |

Take the highest tier matching 2+ signals.

## Tier Composition

### TRIVIAL
- Builder (implementation prompt, TDD)
- Verifier (lint, type, test)
- Auto-commit

### SMALL
- Builder (implementation prompt, TDD)
- Verifier
- Reviewer (combined checklist: quality + security + functional, "find at least 3")
- Fix loop if needed (max 3 iterations)
- Builder (release prompt → create PR)

### MEDIUM
- Scout (codebase + domain research if flagged)
- Builder (spec prompt → product spec)
- Builder (design prompt → architecture + work units)
- Reviewer (architecture checklist) ‖ Cross-model review (architecture)
- **HUMAN GATE: architecture approval**
- Per work unit: Builder (implementation) → Verifier → Reviewer (quality ‖ security ‖ functional in parallel)
- Cross-model review (security, full diff)
- Builder (release prompt → PR)
- **HUMAN GATE: PR approval**
- Post-merge: Builder (docs prompt) ‖ Scout (knowledge extraction)

### LARGE
Same as MEDIUM, plus:
- Scout (research) is mandatory, not conditional
- Parallel work units where independent
- Mid-implementation human gate after ~50% of work units
- Full regression after every work unit

## Domain Research Trigger

Set `domain_research = true` when the request involves knowledge beyond
routine software engineering:
- Specific domains (finance, ML, medical, hardware)
- Algorithms or scientific concepts
- "State of the art" or "best approach"

## Budget Defaults

- Trivial: $0.50
- Small: $2
- Medium: $15
- Large: $75
