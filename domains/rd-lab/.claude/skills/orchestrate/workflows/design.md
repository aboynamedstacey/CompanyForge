# Design Workflow

"Design a thermal management system for..." "Specify a power supply that meets..."

---

## Phase 1: REQUIREMENTS

Decompose the design challenge:
- Functional requirements (what it must do)
- Performance requirements (with numbers and units)
- Interface requirements (physical/electrical/thermal connections)
- Environmental requirements (temperature, vibration, humidity, altitude)
- Constraints (weight, volume, power, cost, schedule)
- Regulatory requirements (certifications, standards)

If incomplete, ask. A design without clear requirements produces a solution
to an undefined problem.

---

## Phase 2: RESEARCH

Dispatch **Scout**: state of the art for this type of system, competing
implementations, relevant material properties, applicable standards.
Depth scales with ceremony tier.

---

## Phase 3: ARCHITECTURE

Dispatch **Builder** (Opus — architecture decisions compound):

> Design system-level architecture for: "{description}"
> Requirements: {phase_1} | Context: {scout_output}
>
> Propose 2-3 options. For each: block diagram, how it meets requirements,
> component choices with rationale, trade-offs (weight/power/cost/complexity/
> reliability), risks, estimated performance (with math).
>
> Select recommended approach with clear reasoning.

**Large gate (attended):** Present options to human before detailed design.

---

## Phase 4: QUANTITATIVE ANALYSIS

Dispatch **Builder** (Sonnet) with budgets prompt:

> Detailed quantitative analysis for selected architecture.
>
> Budgets (as applicable): weight, power, thermal, cost.
> Format: component | value | source | margin vs. requirement.
>
> Show all math. State all assumptions. Propagate uncertainty.

Then **Verifier**: unit consistency, conservation checks, margin calculations.

---

## Phase 5: ADVERSARIAL REVIEW [Medium-Full+ only]

Dispatch **Reviewer** (Opus, fresh) with design adversarial prompt:

> What fails first? Where are margins thinnest? What happens at boundary
> conditions? Single point of failure? Integration problem being ignored?

---

## Phase 6: SYNTHESIS [Medium-Full+ only]

Fresh **Builder** synthesizes original design + review findings into final spec.

---

## Phase 7: DELIVER

Design specification with: architecture, budgets, margins, risk assessment,
assumptions, and recommended next steps (prototyping, testing, procurement).

Gates: Medium = one gate before delivery. Large = two gates (after architecture, before delivery).
