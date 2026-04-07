# R&D Lab — AI Research & Development Organization

Work flows through three capability types plus deterministic verification,
coordinated by a workflow engine. TRL-based ceremony calibration.

## Quick Start

```
/lab explore feasibility of piezoelectric energy harvesting for bridge sensors
/lab design a thermal management system for a 500W drone motor
/lab compare LiPo vs solid-state batteries for high-altitude UAV applications
/lab test plan for validating antenna gain measurements in an anechoic chamber
/lab regulatory what certifications do we need for a commercial drone under 55 lbs
```

Just `/lab` + what you'd say to your principal investigator.

## Capability Types (3 + tools)

| Type | Model | What It Does |
|---|---|---|
| **Builder** | Sonnet (analysis), Opus (architecture) | Produces artifacts. Dispatched with different prompts for feasibility analysis, system design, quantitative budgets, test plans, specifications. One type, many uses. |
| **Reviewer** | Opus (always fresh) | Adversarial physics and engineering critique. "Why will this NOT work?" Dispatched with different checklists per workflow. Also serves as PI for Large-tier strategic assessment. Never the same instance that built the artifact. |
| **Scout** | Haiku→Sonnet | Gathers context. Literature search, patent landscape (awareness only), prior art, competitive analysis, regulatory frameworks. Cheap model for search, escalates for analysis. |
| **Verifier** | Tools + physics checks | Dimensional analysis, unit consistency, conservation law checks, order-of-magnitude sanity. Runs BEFORE Reviewer. Physics violations caught here don't need agent judgment. |

## Ceremony Tiers (TRL-Based)

| Tier | Composition | Review | Human Gates |
|---|---|---|---|
| Trivial | Scout alone | None | None |
| Small | Scout → Builder | Verifier only | None |
| Medium-Light | Scout → Builder → Verifier | Builder self-review against checklist | None |
| Medium-Full | Scout → Builder → Verifier → Reviewer | Three-pass + adversarial | One gate |
| Large | Full pipeline, Reviewer as PI for strategic assessment | Everything | Two gates |

## Critical Domain Rules

1. **Quantitative rigor.** Show your math. Units, assumptions, and sources for
   every number. "Should work" is not evidence.
2. **Assumption tracking.** Every analysis states assumptions, sources each one,
   flags critical assumptions that could kill the project.
3. **Patent search is AWARENESS ONLY.** Identifies patents in the space. Never
   interprets claims, assesses infringement, or advises on design-arounds.
   Flag for patent counsel.
4. **Physics is the final reviewer.** Conservation laws are non-negotiable. If the
   numbers violate thermodynamics, the concept fails.
5. **Negative results are first-class knowledge.** Capture what fails and why.

## Conflict Resolution

1. Physics overrides everything (conservation laws, thermodynamic limits, material properties)
2. Data overrides analysis (test results trump theoretical predictions)
3. Quantitative overrides qualitative (numbers beat intuition)
4. Prior failure data is authoritative (documented failures must be addressed, not dismissed)
5. Disagreements: prefer conservative estimate → human decides

Full rules: `.claude/skills/orchestrate/gates/conflict-rules.md`

## Memory Layers

| Layer | Stores |
|---|---|
| CLAUDE.md | How this lab works |
| docs/ | Research memos, design specs, test reports, comparison matrices |
| Cross-session memory | Material properties learned, failure modes, project knowledge |
| Auto-memory | Lab conventions, frequently used references |
| State tracking (BEADS) | Project state for multi-session R&D work |
