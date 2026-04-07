# Quality Checklists — Competitive BBQ

## Checklist-to-Capability Mapping

Inject ONLY the relevant checklists. Do not inject the full file.

| Capability | Checklists |
|---|---|
| Builder (recipe) | Food Safety + Recipe Quality |
| Builder (cook plan) | Food Safety + Cook Plan Quality |
| Builder (competition) | Food Safety + Cook Plan Quality + Competition Compliance |
| Builder (post-cook analysis) | Scoring Analysis only |
| Verifier | Verification Math only (run as tools) |
| Reviewer (adversarial) | Adversarial Prompts (workflow-specific only) — NO checklists |
| Scout | Food Safety (items 1-3) |

## Food Safety Checklist
- [ ] All internal temp targets meet USDA minimums (poultry 165F, pork 145F, beef 145F — though competition BBQ typically cooks well beyond these) `[GENERATED DEFAULT — refine through use]`
- [ ] Time through danger zone (40-140F) under 4 hours for any protein
- [ ] Rest/hold temperatures specified and safe (hold above 140F, or cool below 40F within 2 hours) `[GENERATED DEFAULT — refine through use]`
- [ ] No protocol step leaves protein in danger zone without explicit time tracking
- [ ] Reheating protocols (if any) bring internal temp back to 165F `[GENERATED DEFAULT — refine through use]`

## Recipe Quality Checklist
- [ ] Ingredient quantities are reasonable for stated protein weight
- [ ] Salt levels balanced (rub + injection + sauce don't compound to oversalted — this is a taste call, not a calculation)
- [ ] Flavor profile coherent (sweet/heat/savory/acid balance appropriate for competition style) `[GENERATED DEFAULT — refine through use]`
- [ ] Technique protocol includes decision points, not just times (probe tender, bark set, color check)
- [ ] Expected timeline realistic for the protein at stated temperature
- [ ] Equipment-specific considerations addressed (offset vs. kamado vs. pellet cook differently)
- [ ] Resting protocol specified with time and method

## Cook Plan Quality Checklist
- [ ] Timeline works backward from serving/turn-in time
- [ ] Buffer time built in (minimum 20 minutes before turn-in for competition — meat needs to rest but shouldn't get cold)
- [ ] Stall contingency addressed (wrap decision point, adjusted timeline)
- [ ] Weather impact on cook time addressed (if conditions known)
- [ ] Carryover cooking accounted for in pull temp
- [ ] Rest protocol specified (method, duration, minimum internal temp at end of rest)
- [ ] Equipment setup detailed (probe placement, damper settings, fire management)

## Competition Compliance Checklist
- [ ] Garnish rules followed (KCBS: parsley, green leaf lettuce, flat leaf parsley ONLY)
- [ ] Container rules followed (KCBS: provided Styrofoam container, no marks/identifiers)
- [ ] Sauce rules followed (competition-specific — some allow, some restrict)
- [ ] No foreign objects in turn-in box
- [ ] Protein presented correctly for the category (e.g., KCBS chicken — thighs preferred for uniformity, but any chicken part legal)
- [ ] Turn-in window compliance verified
- [ ] No identifiers on the container (team name, marks, unique garnish patterns)

## Scoring Analysis Checklist (Post-Cook)
- [ ] Scores broken down by criteria (Appearance/Taste/Tenderness)
- [ ] High/low drops calculated per competition rules (if applicable) — dropped scores are less actionable than surviving scores
- [ ] Outlier judges identified (2+ points off category mean)
- [ ] Comparison to prior results included (if data available)
- [ ] Root cause traced for each low-scoring area
- [ ] Actionable recommendations specific enough to implement

## Verification Math (Verifier runs as tools)
- [ ] Timeline phases sum correctly
- [ ] Working backward from turn-in/serve time produces valid start time
- [ ] Internal temp targets are food-safe
- [ ] Danger zone transit time under 4 hours
- [ ] Carryover estimate applied to pull temp
- [ ] No schedule conflicts across categories (if multi-category)
- [ ] Rest duration fits between pull time and turn-in/serve time
- [ ] Turn-in window buffer adequate

## Adversarial Prompts

For recipes:
> "You are an experienced competition pitmaster who has cooked this protein 500 times. What's wrong with this recipe? Where does it lose points? Is the flavor profile competitive? Is the technique reliable or risky? Would you trust this recipe on competition day? Find at least {N} problems."

For cook plans:
> "You are the pitmaster who has seen this timeline go wrong. Where does this plan break? What happens when the stall runs 2 hours longer than expected? Is there enough buffer? Where is the single point of failure that ruins the turn-in? What weather change kills this plan? Find at least {N} vulnerabilities."

For competition prep:
> "You are judging this team's preparation. Where does the schedule fall apart under pressure? Which category gets sacrificed when time gets tight? Is the equipment allocation realistic? Where is the cross-category conflict that costs 30 minutes nobody planned for? Find at least {N} risks."

For post-cook analysis:
> "You are the head judge reviewing this team's analysis of their own cook. Are they being honest about what went wrong, or making excuses? Did they identify the real root cause, or blame external factors? Are the recommendations specific enough to actually change the outcome next time? Find at least {N} blind spots."

## Known AI Limitations (inject per-capability subset)

**Builder:**
- "AI has no sensory experience — cannot taste, smell, or feel texture. Flavor recommendations are based on documented combinations and competition results, not direct experience"
- "AI tends toward safe/conventional recommendations — push back if the recipe is too generic to be competitive"
- "AI may underestimate cook time variability — always include contingency protocols"

**Reviewer (adversarial):**
- "AI has no sensory experience — evaluate technique and process, not subjective flavor claims"
- "AI may not account for equipment-specific behavior — flag if the plan assumes generic cooker behavior"

**Scout:**
- "Competition rules change — verify rule citations are current for the specific event"
- "Regional judging preferences are anecdotal — label as tendencies, not rules"
