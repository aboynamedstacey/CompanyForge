# Regulatory Workflow

"What certifications do we need?" "Does this fall under ITAR?" "FAA requirements for..."

---

## Phase 1: SCOPE

Establish what's being assessed:
- What is the product/system?
- What markets/jurisdictions? (US, EU, international)
- What's the intended use? (commercial, defense, research)
- What's known about applicable regulations already?

---

## Phase 2: RESEARCH

Dispatch **Scout** (Sonnet — regulatory research needs analysis, not just search):

> Identify applicable regulatory frameworks for: "{product/system}"
> Markets: {jurisdictions} | Use: {intended use}
>
> For each framework:
> - What agency/authority
> - What specifically applies (cite sections/parts)
> - What certifications/approvals are required
> - Timeline and cost estimates (if available)
> - Exemptions that might apply (and their conditions)
>
> Check: FAA (Part 107, Part 91, type certification), FCC (intentional/
> unintentional radiators), ITAR/EAR (export controls), EPA, OSHA,
> industry-specific (DO-178C, MIL-STD, ISO) as applicable.
>
> Flag anything requiring legal interpretation.

---

## Phase 3: ANALYSIS

Dispatch **Builder** (Sonnet) with regulatory analysis prompt:

> Produce a regulatory compliance roadmap for: "{product/system}"
> Regulatory research: {scout_output}
>
> For each applicable framework:
> - Requirements summary (what must be done)
> - Current compliance status (compliant / gap / unknown)
> - Gap analysis (what's missing)
> - Effort to close each gap
> - Dependencies (what must happen first)
> - Timeline estimate
>
> Flag items requiring external counsel. Do NOT make legal interpretations.

Then **Verifier**: cross-reference cited regulations against known frameworks,
check for obvious omissions.

---

## Phase 4: ADVERSARIAL REVIEW [Medium-Full+ only]

Dispatch **Reviewer** (Opus, fresh) with regulatory adversarial prompt:

> What framework was missed? What exemption is being assumed that might not
> apply? Worst case under strict interpretation? Cross-border issues?

---

## Phase 5: DELIVER

Regulatory roadmap with: applicable frameworks, gap analysis, timeline,
items requiring counsel, and recommended next steps.

Items requiring legal interpretation are flagged:
> "These items require external regulatory counsel."

The R&D lab does not do legal work.

Gates: Medium = one gate. Large = two gates.
