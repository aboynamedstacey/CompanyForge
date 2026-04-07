# Explore Workflow

"Is this feasible?" "What's the state of the art?" "Has this been tried?"

---

## Phase 1: RESEARCH

**Trivial:** Scout answers directly — skip remaining phases.

Dispatch **Scout** (Haiku for search, Sonnet for analysis):

> Investigate: "{description}"
>
> **Prior attempts:** Has this been tried? What happened? If it failed, why?
> **Competitive landscape:** Who is working on this commercially? Specs? Limitations?
> **Literature:** Key papers, conferences, recent advances.
> {If Medium+: "Patent landscape (awareness only — see patent-rules.md)"}
> {If Large: "+ Regulatory scan"}
>
> For every claim, cite the source. For every number, include units and source.
> Capture negative findings — what does NOT work and why.

Depth: Small = 2-3 papers. Medium-Light = 5-10 + patents. Medium-Full/Large = 15-25 + full landscape.

---

## Phase 2: FEASIBILITY

Dispatch **Builder** (Sonnet) with analysis prompt:

> Assess technical feasibility of: "{description}"
>
> Research findings: {scout_output}
> Physical constraints: {Layer 4 context}
>
> **Physics check:** Do fundamental physics support this? Show governing equations.
> Check conservation laws and thermodynamic limits.
>
> **Quantitative analysis:** Real numbers from literature and datasheets.
> Show all math with units. State every assumption with source.
>
> **Critical assumptions:** Which assumptions, if wrong, kill the project?
> Define how each would be tested.
>
> **Risk assessment:** Top 3-5 technical risks with likelihood and impact.

Then **Verifier**: dimensional analysis, conservation checks, order-of-magnitude sanity.

---

## Phase 3: ADVERSARIAL REVIEW [Medium-Full+ only]

Dispatch **Reviewer** (Opus, fresh) with explore adversarial prompt:

> Review this feasibility assessment. Your job: find why it will NOT work.
>
> Research: {scout_output}
> Feasibility: {builder_output}
>
> Max 5 issues, ranked by severity:
> 1. What physical law or constraint prevents this?
> 2. What assumption is most likely wrong?
> 3. What prior attempt was missed? What failed?
> 4. What hidden complexity is being underestimated?
> 5. Where are the numbers optimistic?

---

## Phase 4: SYNTHESIS [Medium-Full+ only]

Dispatch **Builder** (Sonnet, FRESH — not the original Builder):

> You did NOT write the original assessment. Three inputs:
> 1. Research: {scout_output}
> 2. Original assessment: {builder_1_output}
> 3. Adversarial review: {reviewer_output}
>
> Produce the FINAL assessment by incorporating valid findings, revising
> where the reviewer identified issues, and flagging genuine disagreements.
> Do NOT defend the original out of deference. Do NOT accept review
> uncritically. Evaluate each point on physics and data.

---

## Phase 5: DECISION BRIEF

Recommend one of:

**PURSUE** — Feasible, physics work, risks manageable. Next steps, resources, timeline, risks.
**PIVOT** — Core idea has merit, specific approach has issues. Alternatives, additional info needed.
**KILL** — Not feasible. Why (specific physics/engineering/economic reasons). Lessons learned.

**Gates:**
- Small: deliver directly
- Medium: one human gate with decision brief
- Large: human gate with full brief including Reviewer's strategic assessment

**Unattended:** PURSUE with no critical issues → deliver. PIVOT or KILL → bank for human.
Critical physics violations → bank regardless.

---

## Output Format

```
EXPLORATION REPORT: {topic}
Ceremony: {tier}

EXECUTIVE SUMMARY
{2-3 sentences}

STATE OF THE ART
{Scout findings}

FEASIBILITY ASSESSMENT
{Quantitative analysis with math}
{Assumptions with sources and confidence}

CRITICAL ASSUMPTIONS
{Could-kill-the-project assumptions with validation plans}

RISKS
{Top 3-5 with likelihood and impact}

ADVERSARIAL FINDINGS (Medium+)
{Key issues and how addressed}

RECOMMENDATION: PURSUE / PIVOT / KILL
{Evidence-based reasoning}

NEGATIVE FINDINGS
{What does NOT work and why}

PATENT AWARENESS (if applicable)
{Awareness only, not legal analysis}
```
