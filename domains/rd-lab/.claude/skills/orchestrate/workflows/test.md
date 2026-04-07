# Test Workflow

"Plan a test for..." "What should we measure?" "Analyze these test results."

---

## Phase 1: DEFINE

What's being tested? Three modes:
- **Plan** — design an experiment to validate a hypothesis or specification
- **Predict** — estimate expected outcomes before running the test
- **Analyze** — interpret results from a completed test

---

## Phase 2: RESEARCH

Dispatch **Scout**: standard test methods for this type of measurement,
relevant standards (ASTM, MIL-STD, ISO), similar test setups in literature,
known sources of error.

---

## Phase 3: BUILD

### For PLAN mode:

Dispatch **Builder** (Sonnet) with test plan prompt:

> Design an experiment to test: "{hypothesis/specification}"
> Research: {scout_output}
>
> Test plan:
> - Hypothesis (specific, falsifiable)
> - What to measure (parameters, units, resolution required)
> - How to measure it (instruments, setup, calibration)
> - Controls (what's held constant, what varies)
> - Sample size / number of runs (with statistical justification)
> - Expected results if hypothesis is true vs. false
> - Pass/fail criteria (quantitative thresholds)
> - Sources of error and how to minimize them
> - Safety considerations

### For PREDICT mode:

Builder produces quantitative predictions with uncertainty bounds,
stated assumptions, and what the results would mean.

### For ANALYZE mode:

Builder processes test data: statistical analysis, comparison to predictions,
error analysis, conclusions supported by the data.

Then **Verifier**: unit consistency, statistical validity, calculation checks.

---

## Phase 4: ADVERSARIAL REVIEW [Medium-Full+ only]

Dispatch **Reviewer** (Opus, fresh) with test adversarial prompt:

> Is the experiment actually testing the hypothesis? Are controls adequate?
> Is measurement resolution sufficient? What systematic error could make
> results look correct when they're not?

---

## Phase 5: SYNTHESIS + DELIVER

Fresh **Builder** synthesizes final test plan/prediction/analysis with
review findings incorporated.

Gates: Medium = one gate. Large = two gates.
