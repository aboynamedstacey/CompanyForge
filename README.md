# CompanyForge

CompanyForge generates domain-specific AI organizations that run inside [Claude Code](https://docs.anthropic.com/en/docs/claude-code). You describe a professional domain (software development, R&D lab, competitive BBQ) and the system builds a complete organizational structure: capabilities, workflows, quality controls, and cost management. The output is a working Claude Code project you can drop into any directory and start using immediately.

Most agentic AI systems either do too little (one prompt, one loop) or too much (fifteen roles staffed on a two-sentence question). CompanyForge calibrates and provides what's needed, whether it's a solo practitioner for a quick question or a full team with adversarial review for a complex deliverable. The system decides based on the work, not a fixed configuration.

## What It Does

Run `/forge "software-dev"` and CompanyForge will:

1. **Research the domain.** What does the minimum viable team look like? What are the 3-5 core work types that cover 90% of what this kind of organization does? What goes wrong most often, including what goes wrong when AI specifically does this work?

2. **Design the architecture.** A flat capability pool (not a hierarchy), mapped to model tiers by the judgment required. Opus is used for adversarial review. Sonnet is used for substantive work. Haiku is used for mechanical tasks. The architect decides which infrastructure components the domain needs. 

3. **Present it for your approval.** You see the proposed structure before anything gets built. 

4. **Generate the files.** A self-contained domain directory with personas, workflows, quality gates, and a domain context engine. 

5. **Run adversarial review on its own output.** A fresh reviewer checks the generated organization for gaps: missing capabilities, unrealistic ceremony calibration, workflows that don't match how the domain works, dispatches that batch independent units when they should be isolated.

6. **Calibrate with your knowledge.** The AI resolves defaults it can answer from established sources (published standards, documented conventions). Then it presents only the open questions for your input, which should be the things that require practitioner judgment, rather than things the AI already knows.

## Why Not a Traditional Org Chart

Human organizational patterns exist because humans need them: hierarchy for coordination, departments for career growth, meetings because people can't see each other's state. CompanyForge avoids these contraints and generates AI-native organizations that provide agents with specialized prompts, fresh instances for review, persistent knowledge across sessions, and conflict resolution rules. 

## Design Principles

**Ceremony scales with stakes.** Every task gets sized into tiers. The tier determines staffing, review depth, cost budget, and human gates. 

**Three-pass review on anything that matters.** For medium and large tasks: Capability #1 drafts. A reviewer (always a fresh instance, never the drafter) critiques. Capability #2 synthesizes a final deliverable so that you see one clean output.

**Natural language routing.** `/dev add authentication`, not `/orchestrate workflow-type "feature" sub-type "auth" tier "medium"`. You talk normally and the system figures out what kind of work it is.

**Deterministic tools before agent opinions.** If a tool can verify it (lint, type check, test, diversity metrics, math check), the tool's answer is authoritative. Agent judgment is for things tools can't check.

**Infrastructure is conditional.** Not every domain needs document processing, execution modes, or formal iteration protocols. The forge evaluates what the domain requires and skips what it doesn't.

**Economics are explicit.** Model selection is a staffing decision, not a default. Cost tracking, budget alerts, and spend reporting are built into every workflow.

## Included Domains

CompanyForge ships with reference implementations you can use directly or study as examples for the forge generator.

### Software Development

Three capability types (Builder, Reviewer, Scout) plus deterministic tool verification, composed elastically by ceremony tier. Five workflows (feature, bugfix, techdebt, research, greenfield). TDD mandatory. Cross-model review for architecture and security.

```
/dev add a REST endpoint for user authentication
/dev fix the race condition in the queue processor
/dev research whether we should migrate from REST to gRPC
```

### R&D Lab

Five capabilities from lone researcher to PI-led team. TRL-based ceremony tiers. Quantitative rigor enforced with every number needing units, assumptions, and sources and the laws of physics being the final reviewer. If the numbers violate conservation laws, the concept fails.

```
/lab explore feasibility of piezoelectric energy harvesting for bridge sensors
/lab design a passive cooling system for a 200W outdoor edge computing enclosure
/lab compare thermoelectric vs phase-change materials for vaccine cold chain transport
```

### Competitive BBQ

Three capabilities plus tool verification. Three workflows (recipe development, cook planning, post-cook analysis), with user calibration.

```
/bbq build me a rub recipe for spare ribs
/bbq develop a complete rib cook protocol for KCBS
/bbq full comp prep, 4 categories for Saturday's KCBS
```


## Repository Structure

```
CompanyForge/
├── CLAUDE.md                                    # Project handbook
├── README.md                                    # This file
├── .claude/skills/
│   ├── forge/SKILL.md                           # The generator itself
│   └── orchestrate/shared/                      # Components all domains inherit
│       ├── ceremony-calibration-base.md
│       ├── cost-control.md
│       ├── error-resilience.md
│       ├── conflict-rules-base.md
│       ├── learning-system.md
│       └── observability.md
└── domains/
    ├── software-dev/                            # Software engineering organization
    ├── rd-lab/                                  # R&D lab organization
    └── bbq/                                     # Competitive BBQ (forge-generated, practitioner-trimmed)
```

Each domain is self-contained. Copy a domain directory into any project and it works independently of the rest of the repository.

## How Ceremony Calibration Works

The system evaluates your request against domain-specific signals and assigns a tier:

| Tier | Composition | Review | Human Gates |
|---|---|---|---|
| Trivial | Builder alone | Verifier (tools) only | None |
| Small | Builder → Verifier → Reviewer (combined) | One pass | None |
| Medium | Scout → Builder → Verifier → Reviewer (parallel) → cross-model | Three-pass + parallel checklists | Architecture + PR |
| Large | Full pipeline, parallel work units, mid-point checkpoint | Everything | All gates |

The capability types stay the same across tiers. What changes is the number of dispatches.

You see the tier estimate before work begins and can override it.

## Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI

Optional but useful:
- claude-mem (cross-session memory)
- firecrawl (web research)

## Background

This project started with a practical question: if you're going to use AI agents for professional work, how should you organize them? Not as a chatbot with a system prompt, and not as an enterprise platform with forty microservices, but as a working organization that scales effort to the task and doesn't pretend agents are people who need meetings and management hierarchies.

The software development domain was built first, by hand. The R&D lab came second. The BBQ domain was the first forge-generated one. It revealed that the forge over-engineered simple domains, which led to conditional infrastructure. Later domains tested the improved forge on more complex work and drove further improvements to execution isolation, self-reinforcement prevention, and calibration.
