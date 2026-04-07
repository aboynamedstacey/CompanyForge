---
name: lab
description: Use for any R&D work — exploring ideas, designing systems, comparing approaches, planning tests, investigating regulations. Routes automatically.
---

# R&D Lab — Workflow Engine

You route requests through the right workflow, calibrate ceremony using
TRL-based signals, and dispatch Builder/Reviewer/Scout as needed.

## How to Invoke

```
/lab {natural language request}
```

Determine workflow type automatically:
- **Explore** — feasibility of a new idea, technology, or approach
- **Design** — system, subsystem, or component to meet requirements
- **Compare** — evaluate competing approaches or technologies
- **Test** — plan an experiment, predict outcomes, or analyze results
- **Regulatory** — applicable regulations, certifications, compliance

If ambiguous, ask.

## Capability Dispatch Rules

**Builder** (Sonnet for analysis, Opus for architecture):
- Feasibility prompt → quantitative analysis with physics checks
- Design prompt → system architecture with budgets (weight, power, thermal)
- Test plan prompt → experiment design with controls and measurements
- Specification prompt → requirements and performance targets
- Synthesis prompt → final deliverable incorporating review feedback

**Reviewer** (Opus, ALWAYS fresh instance):
- Physics checklist → conservation laws, thermodynamic limits, material properties
- Assumption checklist → sources, confidence levels, critical assumptions
- Quantitative checklist → units, calculations, sanity checks, margins
- Strategic assessment (Large) → go/kill decisions, cross-domain risks
- Workflow-specific adversarial prompts from `gates/quality-checklists.md`

**Scout** (Haiku for search, Sonnet for analysis):
- Literature search → papers, conferences, recent advances
- Patent landscape → awareness only, never claim interpretation
- Competitive analysis → who's doing what commercially
- Regulatory scan → applicable frameworks and certifications
- Prior experience → cross-session memory queries

**Verifier** (tools/checks, not an agent):
- Dimensional analysis — units consistent throughout
- Conservation checks — energy, momentum, mass balance
- Order of magnitude — does the answer make physical sense?
- Material property validation — values match datasheets at operating conditions
Runs BEFORE Reviewer. Physics violations caught here are authoritative.

## Context Engine (4 layers, depth scales with tier)

1. **Technology state of the art** — literature, conferences, recent advances
2. **Patent landscape** — awareness only (see `gates/patent-rules.md`)
3. **Regulatory requirements** — applicable frameworks and certifications
4. **Physical constraints** — conservation laws, material limits, thermodynamics

Layer 4 is ALWAYS checked for quantitative analysis, regardless of tier.
Layers 1-3 scale: Trivial skips all, Small gets Layer 1, Medium adds 1-2, Large gets all.

## Workflow Routing

- Explore → `workflows/explore.md`
- Design → `workflows/design.md`
- Compare → `workflows/compare.md`
- Test → `workflows/test.md`
- Regulatory → `workflows/regulatory.md`

## References

- Ceremony: `ceremony-signals.md`
- Quality checklists: `gates/quality-checklists.md`
- Conflict rules: `gates/conflict-rules.md`
- Patent rules: `gates/patent-rules.md`
- Shared infrastructure: `../../.claude/skills/orchestrate/shared/`
