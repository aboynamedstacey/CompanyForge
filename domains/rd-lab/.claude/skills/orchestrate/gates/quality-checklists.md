# Quality Checklists — R&D Lab

## Checklist-to-Type Mapping

| Type | Checklists |
|---|---|
| Builder | Assumption Tracking + Quantitative Accuracy |
| Reviewer | Physics Reality Check + workflow-specific adversarial prompts |
| Scout | Prior Art |
| Verifier | Quantitative Accuracy items 1-5 (units/arithmetic only) |

Inject ONLY the relevant checklists per dispatch.

---

## Assumption Tracking

- [ ] Every assumption explicitly stated (not buried in calculations)
- [ ] Each assumption sourced: datasheet, paper, measurement, or estimate
- [ ] Estimated values flagged with confidence level (high/medium/low)
- [ ] Source quality noted: manufacturer data > peer-reviewed > estimate
- [ ] Critical assumptions identified (could kill the project if wrong)
- [ ] Validation plan defined for each critical assumption
- [ ] Interacting assumptions identified (if A and B both optimistic, combined effect is worse)
- [ ] Environmental assumptions stated (temperature, altitude, humidity, load)

## Quantitative Accuracy

- [ ] Units consistent throughout (SI preferred)
- [ ] Unit conversions shown explicitly
- [ ] Calculations reproducible (formulas shown, not just results)
- [ ] Intermediate values shown
- [ ] Numbers sanity-checked against known benchmarks
- [ ] Error and uncertainty propagated
- [ ] Results compared to literature values
- [ ] Order of magnitude check: does the answer make physical sense?
- [ ] Significant figures appropriate
- [ ] Safety margins stated with rationale

## Prior Art

- [ ] Literature search covers last 5 years minimum
- [ ] Key conferences checked (AIAA, ASME, IEEE, ACM as appropriate)
- [ ] Patent search covers relevant classifications (awareness only — see `patent-rules.md`)
- [ ] Failed prior attempts identified with failure reasons
- [ ] Competitive landscape mapped
- [ ] Directly relevant patents flagged for human + patent counsel
- [ ] Negative results captured

## Physics Reality Check

- [ ] Conservation of energy satisfied
- [ ] Conservation of momentum satisfied
- [ ] Conservation of mass satisfied
- [ ] Thermodynamic limits respected (Carnot, second law)
- [ ] Material properties from verified sources at operating conditions
- [ ] Structural limits checked (yield, fatigue, buckling, creep)
- [ ] Environmental conditions accounted for (thermal cycling, vibration, humidity, UV)
- [ ] Degradation and aging considered (end of life, not just beginning)
- [ ] Interface loads verified

## Adversarial Prompts (per workflow)

**Explore:**
> "Why will this NOT work? What physical law prevents it? What prior attempt
> failed? What assumption is most likely wrong? What's the hidden complexity?"

**Design:**
> "What fails first? Where are the margins thinnest? What happens at boundary
> conditions? What's the single point of failure? What integration problem
> is being ignored?"

**Compare:**
> "What criteria did you weight wrong? Which approach did you dismiss too quickly?
> What data point would change the recommendation? What system-level effect
> makes the 'best' approach worse in practice?"

**Test:**
> "Is the experiment testing the hypothesis or something else? Are controls
> adequate? Is measurement resolution sufficient? What systematic error could
> make results look correct when they're not?"

**Regulatory:**
> "What framework did you miss? What exemption are you assuming that might not
> apply? What's the worst case under strict interpretation? What cross-border
> issue hasn't been considered?"

## Known AI Limitations

Include relevant subset per dispatch:

**Builder:** May invent plausible-sounding wrong physics. May underestimate
integration complexity. May not account for real-world non-idealities.

**Reviewer:** May invent plausible-sounding wrong physics. May confuse similar
phenomena or conflate distinct concepts.

**Scout:** May miss recent papers — search databases, don't rely on training data.
May confuse similar phenomena. Knowledge cutoff applies — flag recent topics.
