# Compare Workflow

"Compare LiPo vs solid-state batteries for..." "Which motor topology is best for..."

---

## Phase 1: DEFINE CRITERIA

Establish comparison framework with human:
- What are the candidates? (2-5 approaches/technologies)
- What criteria matter? (performance, cost, weight, reliability, maturity, risk)
- What are the weights? (or let the analysis determine relative importance)
- What's the use case context? (operating conditions, constraints, requirements)

---

## Phase 2: RESEARCH

Dispatch **Scout** per candidate:

> Research {candidate} for application: "{use case}"
> Key parameters: {criteria list}
> Find: specifications, real-world performance data, failure modes,
> cost data, availability, maturity level.
> Cite sources. Flag where data is estimated vs. measured.

Dispatch in parallel for independent candidates.

---

## Phase 3: ANALYSIS

Dispatch **Builder** (Sonnet) with comparison prompt:

> Compare candidates for: "{use case}"
> Research: {scout_outputs per candidate}
> Criteria: {from phase 1}
>
> Build a quantitative comparison matrix:
> | Criterion | Weight | {Candidate A} | {Candidate B} | ... |
> With real numbers, units, and sources for every cell.
>
> Analyze: where does each candidate excel? Where does each fall short?
> What system-level effects (integration, supply chain, development risk)
> aren't captured in the matrix?
>
> Recommend with clear reasoning. State what data point would change
> the recommendation.

Then **Verifier**: unit consistency, calculation checks across the matrix.

---

## Phase 4: ADVERSARIAL REVIEW [Medium-Full+ only]

Dispatch **Reviewer** (Opus, fresh) with compare adversarial prompt:

> What criteria were weighted wrong? Which approach was dismissed too quickly?
> What data point would flip the recommendation? What system-level effect
> makes the "best" approach worse in practice?

---

## Phase 5: SYNTHESIS [Medium-Full+ only]

Fresh **Builder** produces final comparison incorporating review findings.

---

## Phase 6: DELIVER

Comparison report with: matrix, analysis, recommendation, sensitivity
analysis (what changes the answer), and negative findings per candidate.

Gates: Medium = one gate. Large = two gates.
