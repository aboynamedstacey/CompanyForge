# Feature Development Workflow

**Prerequisite:** Ceremony tier determined (see ceremony-signals.md).

---

## Phase 1: RESEARCH [Medium+ only]

Dispatch **Scout** (Haiku for search, Sonnet for analysis):

> Investigate this feature request: "{description}"
>
> **Codebase context:**
> - Existing patterns relevant to this feature
> - Dependencies that help or constrain
> - Similar implementations to use as reference
>
> {If domain_research: "**Domain context:**
> - State of the art, competing approaches, trade-offs
> - Relevant literature or specifications
> - Known risks and limitations"}
>
> **Prior experience:**
> - Query cross-session memory for related past work
>
> Be explicit about confidence levels and knowledge gaps.

---

## Phase 2: SPEC [Medium+ only]

Dispatch **Builder** (Sonnet) with spec-writing prompt:

> Write a product spec for: "{description}"
> {If research: "Research findings: {scout_output}"}
>
> Include:
> 1. **Problem Statement** — what problem, for whom
> 2. **Success Criteria** — how we know it worked (measurable)
> 3. **Acceptance Criteria** — specific testable conditions (given/when/then)
> 4. **Scope** — what's in
> 5. **Non-Goals** — what's explicitly out
>
> Be specific. "Users can log in" is vague. "Given valid credentials, when
> POST /auth/login is called, then return 200 with JWT and refresh token" is testable.

Save to `docs/specs/YYYY-MM-DD-feature-name.md`.

---

## Phase 3: DESIGN [Medium+ only]

Dispatch **Builder** (Opus for design — justifies the model tier because
architecture decisions compound) with design prompt:

> Design the architecture for this feature.
>
> **Spec:** {spec_output}
> {If research: "Research: {scout_output}"}
>
> Produce:
> 1. **Component Design** — what's involved, how they relate
> 2. **API Contracts** — exact interfaces
> 3. **Data Model** — new or changed structures
> 4. **Work Unit Decomposition** — independent implementation chunks, each with:
>    - File scope
>    - Definition of Done (testable)
>    - Dependencies on other work units
>
> Prefer simplicity. Fewer moving parts. Flag ambiguous decisions.

Save to `docs/designs/YYYY-MM-DD-feature-name.md`.

---

## Phase 4: REVIEW DESIGN [Medium+ only]

Dispatch in **parallel**:

**Reviewer** (Opus, fresh) with architecture checklist:
> Review this design. Check: simplicity, scalability, API coherence,
> dependency management, testability. Prefer simpler approaches.
> {design_output}

**Cross-model review** (Gemini/GPT via external-tools):
> Review this architecture independently. Focus on: blind spots,
> over-engineering, missing edge cases, alternatives.
> {design_output}

Merge verdicts. Cross-model disagrees with Reviewer → escalate to human.

---

## Phase 5: HUMAN GATE — Architecture [Medium+ only]

> **Architecture Review Complete**
> Spec: {link} | Design: {link}
> Reviewer: {verdict} | Cross-model: {verdict}
> {Disagreements if any}
> Work units: {count}, estimated {complexity}
>
> Approve / Revise / Reject?

---

## Phase 6: IMPLEMENT (per work unit)

For each work unit (parallel if independent, sequential if dependent):

### 6a. Builder (Sonnet) with implementation prompt:
> Implement this work unit using TDD.
> **Work unit:** {spec} | **Design context:** {design_output}
> 1. Write failing tests (RED)
> 2. Minimal code to pass (GREEN)
> 3. Refactor while green (REFACTOR)
> 4. Run lint, type check, tests
> 5. Commit

### 6b. Verifier (tools — orchestrator runs directly, never trusts agent self-reports):
```bash
{type checker} && {linter} && {test runner}
```
Fail → route back to Builder with error output.

### 6c. Review (tier-appropriate)

**Trivial:** Verifier only.
**Small:** Reviewer with combined checklist ("find at least 3").
**Medium+:** Reviewer dispatched 3× in **parallel** with different checklists:
- Code quality checklist
- Security checklist (OWASP + race conditions, timing attacks)
- Functional checklist (vs. spec acceptance criteria)

Merge verdicts. Critical → fix → re-review. Max 3 iterations per checklist.

### 6d. Commit after review passes.

---

## Phase 7: CROSS-MODEL SECURITY [Medium+ only]

After all work units, cross-model review (Gemini/GPT) on complete diff:
> Review all changes from a security perspective. This code already passed
> Claude's security review. Your job: catch what Claude missed.

---

## Phase 8: RELEASE

Builder (Sonnet) with release prompt:
> Create a PR. Include: summary, spec link, design link, review verdicts. Verify CI.

---

## Phase 9: HUMAN GATE — PR [all except Trivial]

> **PR Ready**
> Feature: {description} | PR: {link}
> Quality: {verdict} | Security: {verdict} | Functional: {verdict}
> Cross-model security: {verdict}
> {Deferred non-critical issues if any}
>
> Approve / Request Changes?

---

## Phase 10: POST-MERGE [Medium+ only]

Dispatch in **parallel**:

**Builder** (Haiku) with docs prompt:
> Update docs for this feature. Public API surfaces and non-obvious behavior only.

**Scout** (Haiku) with knowledge extraction prompt:
> Extract learnings: project-specific observations, generalizable patterns,
> checklist additions if reviews missed something, process improvements.
> Store in cross-session memory.
