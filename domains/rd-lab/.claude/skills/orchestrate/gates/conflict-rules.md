# Conflict Resolution — R&D Lab

Inherits base rules from shared `conflict-rules-base.md`.

## Domain-Specific Priority

### R1: Physics overrides everything.
Conservation laws, thermodynamic limits, verified material properties are
non-negotiable. If the numbers violate physics, the concept does not work.
No capability may override a physics constraint. Escalate disagreements
about constraint applicability to human.

### R2: Data overrides analysis.
Test data contradicts theory → data wins. Re-examine the analysis.
Present BOTH with discrepancy clearly stated. Conclusion based on data
until discrepancy is explained.

### R3: Quantitative overrides qualitative.
"Should work" is not evidence. Claims about feasibility, performance,
or risk must be backed by calculation, measurement, or cited data.

### R4: Prior failure data is authoritative.
Documented failure reasons must be addressed directly. "We'll do it better"
requires specific evidence of what has changed. Burden of proof is on the
team proposing the approach.

### R5: Patent flags are for awareness, not avoidance.
Flag relevant patents, recommend counsel, do not attempt legal analysis.

### R6: Conservative estimates for unattended mode.
When unattended, use pessimistic assumptions:
- Material properties: minimum datasheet values
- Efficiency: 80% of datasheet unless measured
- Weight/power: add 20% margin
- Environmental: harsh end of operating range
- Cost: upper end of quotes
- Schedule: 1.5x optimistic estimate

Better to bank "this might not work" than proceed on optimistic assumptions.
Does NOT apply in attended mode.

## Verdict Merging

- Reviewer finds physics violation → must resolve before proceeding
- Reviewer finds thin margin → address in synthesis (better data, add margin, or flag)
- Reviewer finds missed failure mode → mitigate, accept with justification, or flag
- Reviewer and Builder disagree on feasibility → present both with evidence at human gate
