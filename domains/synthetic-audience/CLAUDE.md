# Synthetic Audience Research -- AI Organization

Generates AI personas to simulate consumer/audience responses for market
research. Personas respond to stimuli (ads, products, messaging, concepts)
to produce structured audience insights.

## Quick Start

```
/audience test this headline with suburban parents aged 30-45
/audience build a panel of craft beer enthusiasts for concept testing
/audience how does our Q1 messaging track against the November baseline?
/audience explore: what if we repositioned toward gen-z sustainability?
```

Just `/audience` + what you'd tell a research director.

## Organizational Model

### Capability Types (3 + tools)

| Type | Model | What It Does |
|---|---|---|
| **Builder** | Sonnet | Persona construction, verbatim response generation, study protocol design, analysis, synthesis. One type, many uses. |
| **Reviewer** | Opus (always fresh) | Adversarial critique: persona authenticity, AI-artifact detection, convergence checking, sycophancy probes. Never the same instance that built the artifact. |
| **Scout** | Haiku->Sonnet | Category research, demographic context, cultural norms, prior study retrieval. Cheap model first, escalates if depth needed. |
| **Verifier** | Tools (not an agent) | `python tools/diversity_metrics.py` + structured output validation (2x2 matrix, funnel stages, concern weights, Claude-ism patterns). Runs BEFORE any agent review. |

### Ceremony Tiers

| Tier | Segments | Per Segment | Stimuli | Composition | Review | Human Gates |
|---|---|---|---|---|---|---|
| Trivial | 1 | 1-2 | 1 | Builder alone | Verifier only | None |
| Small | 2-3 | 5 | 1-2 | Builder + Verifier + Reviewer | One pass | Segment approval |
| Medium | 3-5 | 8 | 2-4 | Scout + Builder + Verifier + Reviewer | Three-pass | After study design + before delivery |
| Large | 6+ | 12 | 5+ | Full pipeline, parallel segments | Everything + multiple passes | After program design + after simulation + before delivery |

## The Simulation Loop

**Every persona response is its own isolated dispatch.** The orchestrator
owns the loop. Persona A's response is never visible when generating
Persona B's response. This prevents convergence, anchoring, and the LLM
averaging effect that destroys panel variance.

## Quality Standards

- Verifier (tools) runs before Reviewer (agent)
- Fresh instance for every review dispatch
- Claude-ism suppression list checked on all persona-voiced output
- Voice profiles enforce linguistic variety across personas
- Panels of 8+ include a sycophancy canary (persona that should respond negatively)
- Prompt template version recorded for every study

## Conflict Resolution

1. Methodological validity blocks everything
2. Verifier (tool) results override Reviewer (agent) opinions
3. Study brief defines "what" -- capabilities execute, don't debate scope
4. AI-artifact detection overrides positive persona assessment
5. Cross-model disagreement -> human escalation

Full rules: `.claude/skills/orchestrate/gates/conflict-rules.md`

## What This Cannot Do

Synthetic audience research has real limitations. Be honest about them:

- **Not a replacement for real research.** AI personas extrapolate from training data patterns. They cannot surface needs, preferences, or reactions that don't exist in the training distribution.
- **Novel categories are unreliable.** The further a stimulus falls from familiar product categories, the less trustworthy the simulated responses. Flag novelty distance in every deliverable.
- **No actual purchase behavior.** Stated intent and modeled intent are not observed behavior. Funnel positions are directional, not predictive.
- **Cultural depth is uneven.** Training data overrepresents some demographics and underrepresents others. Flag confidence by segment.
- **Convergence risk is structural.** Despite isolation, personas are all produced by the same model. Residual convergence is always possible. The sycophancy canary catches some of it, not all.

Use this for directional signal, hypothesis generation, and pre-screening before real fieldwork. Do not use it as a substitute for primary research on high-stakes decisions.

## Memory Layers

| Layer | Stores |
|---|---|
| This file (CLAUDE.md) | How the org works |
| studies/ | Study protocols, panel specs, results |
| personas/ | Reusable persona library with version history |
| prompts/ | Versioned prompt templates for persona construction |
| Cross-session memory | Category insights, panel performance, calibration data |
