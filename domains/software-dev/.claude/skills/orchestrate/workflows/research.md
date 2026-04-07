# Research Workflow

Produces knowledge, not code. Typically Medium tier.

---

## Phase 1: SCOPE

Scout (Sonnet):
> Scope this investigation: "{question}"
> 1. Specific sub-questions to answer
> 2. Sources to check for each
> 3. What "answered" looks like
> 4. What's NOT in scope

Present scope for human approval.

---

## Phase 2: HUMAN GATE

> **Research Scope**
> Question: {question}
> Sub-questions: {list}
> Depth: {quick survey | moderate | deep dive}
> Approve / Adjust / Cancel?

---

## Phase 3: INVESTIGATE

Scout (Sonnet) with approved scope:
> For each sub-question: gather evidence, assess quality (strong/moderate/weak),
> note conflicts explicitly, flag gaps. Separate facts from interpretation.

---

## Phase 4: ADVERSARIAL REVIEW

Reviewer (Opus, fresh):
> Review these findings for completeness and bias.
> - Actually answering the question?
> - Evidence cherry-picked?
> - Alternatives not considered?
> - Hidden assumptions?
> - Confidence levels appropriate?

FAIL → Scout addresses gaps → re-review. Max 2 iterations.

---

## Phase 5: SYNTHESIZE

Builder (Sonnet, FRESH — not the Scout that investigated) with synthesis prompt:
> Combine findings and review feedback into a clean report.
> 1. Executive summary (2-3 sentences)
> 2. Findings by sub-question with evidence and confidence
> 3. Options with trade-offs (if applicable)
> 4. Recommendation with rationale
> 5. Open questions
> 6. Sources

---

## Phase 6: DELIVER

Present report. Save to `docs/research/YYYY-MM-DD-topic.md` for Medium+.
Scout (knowledge extraction): capture generalizable findings in cross-session memory.
