# Ceremony Signals — R&D Lab

## Size Signals (TRL-Based)

| Signal | Trivial | Small | Medium-Light | Medium-Full | Large |
|---|---|---|---|---|---|
| TRL stage | Quick question | TRL 1-2 concept | TRL 3 proof | TRL 4-5 feasibility | TRL 6-9 system |
| Investment at risk | None | <$10K | <$30K | $30K-$100K | $100K+ |
| Technical novelty | Known answer | Proven approach | Some novelty | Genuine novelty | Novel/unproven |
| Disciplines involved | 1 | 1-2 | 1-2 | 2-4 | 4+ |
| Regulatory exposure | None | Minimal | Minimal | Moderate | ITAR/defense/FAA |
| Test complexity | None | Bench test | Bench test | Lab test with equipment | Field test or certification |
| System integration | Single component | Few components | Single subsystem | Multi-subsystem | Full system |

Score: highest tier matching 2+ signals.

## Tier Composition

### TRIVIAL
Scout answers directly from knowledge or quick search. No Builder, no review.

### SMALL
Scout (literature) → Builder (single-discipline analysis with math) → Verifier.

### MEDIUM-LIGHT
Scout → Builder → Verifier → Builder self-reviews against checklist.
Use when: straightforward feasibility, single-subsystem, known physics.

### MEDIUM-FULL
Scout → Builder #1 → Verifier → Reviewer (adversarial) → Builder #2 (fresh synthesis).
Three-pass. One human gate.
Use when: multi-subsystem, genuine novelty, significant investment.

### LARGE
Full pipeline. Scout (comprehensive, all 4 context layers) → Builder → Verifier →
Reviewer (adversarial + strategic assessment) → Builder (synthesis).
Two human gates: after initial analysis, before final delivery.

## Budget Defaults

Actual costs depend on context length and model pricing. System tracks and reports.

## Deep Research Trigger

Set deep_research = true when:
- Novel approach with no clear prior art
- Multi-discipline integration
- Investment at risk exceeds $50K
- Regulatory involvement (FAA, ITAR, FCC)
- Technology less than 3 years old
- Prior attempts failed for unclear reasons

## TRL Reference

| TRL | Description | Ceremony |
|---|---|---|
| 1-2 | Basic principles / concept | Small |
| 3 | Proof of concept | Medium-Light |
| 4-5 | Lab / relevant environment validation | Medium-Full |
| 6-9 | Demonstration through operational | Large |

Quick questions that don't map to a TRL default to Trivial.
