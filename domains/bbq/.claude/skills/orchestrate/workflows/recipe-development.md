# Recipe Development Workflow

Used when the user asks to build, refine, or develop a recipe, rub, sauce,
injection, technique protocol, meat profile, or judging standard reference.

Technique is part of recipe — 3-2-1 is how you execute a rib recipe, not a
separate work type. Meat profiles and judging standards are Builder outputs
(reference document prompt), not a separate workflow.

## Phases

### 1. INTAKE
Prerequisite: SKILL.md Steps 1-3 complete (request understood, competition body
determined, ceremony calibrated).

Workflow-specific: Identify target protein, competition body (if any), equipment
constraints, and whether this is a new recipe or refinement of an existing one.

### 2. CONTEXT GATHERING (Scout, Medium+)
Dispatch Scout (Haiku->Sonnet):
> Gather context for {protein} recipe development.
> Competition body: {body or "backyard"}
> Equipment: {cooker type}
> Query claude-mem for: prior cook data for this protein, prior recipes,
> lessons learned from post-cook analyses.
> Pull: competition category rules, judging criteria, scoring weights.
> If deep_research: research regional judging tendencies, winning techniques.

### 3. RECIPE BUILD (Builder #1)
Dispatch Builder (Sonnet):
> Develop a {recipe type} for {protein}.
> Competition context: {from context engine — rules, scoring criteria, judging standards}
> Equipment: {cooker type, fuel type}
> Prior cook data: {from Scout, if available}
> User preferences: {any stated preferences}
>
> Produce:
> - Complete ingredient list with quantities (scaled to protein weight if applicable)
> - Step-by-step method with time and temperature targets
> - Technique protocol (e.g., 3-2-1 adapted to this specific recipe and equipment)
> - Target internal temps and doneness indicators (probe tender vs. temp-based)
> - Expected timeline at standard conditions (225F, sea level, 70F ambient)
> - Food safety checkpoints
> - Scoring optimization notes (if competition): what judges look for in this category
>
> For reference documents (meat profiles, judging standards):
> Produce a comprehensive reference covering the protein's characteristics,
> cooking behavior, common pitfalls, and what separates good from great
> in competition scoring.

### 4. VERIFICATION (Verifier, Small+)
Run Verifier (tools, not an agent):
- Internal temp targets are food-safe (USDA minimums met)
- Time-at-temperature calculations are correct
- Timeline arithmetic checks out (phases sum correctly)
- Ingredient quantities are reasonable for stated protein weight
- No danger zone violations in the protocol (time between 40-140F)

### 5. ADVERSARIAL REVIEW (Reviewer, Medium+)
Dispatch Reviewer (Opus, FRESH instance — never Builder #1):
> Use the adversarial prompt for recipes from `gates/quality-checklists.md`.
> Receives Builder's recipe only — do NOT re-inject competition rules or context.
>
> Builder's recipe: {Builder #1 output}

### 6. SYNTHESIS (Builder #2, Medium+ — FRESH instance, never Builder #1)
Dispatch a NEW Builder (Sonnet, fresh instance):
> You are a fresh instance. You did NOT write the original recipe.
> You have two inputs:
>
> 1. Original recipe: {Builder #1 output}
> 2. Adversarial review findings: {Reviewer output}
>
> Produce the FINAL recipe by:
> (a) Incorporating the Reviewer's valid findings
> (b) If you believe a Reviewer finding is wrong, state why briefly
> (c) If the original recipe and Reviewer genuinely disagree on a material
>     point (e.g., wrap vs. no wrap, target temp), flag it:
>     "DISAGREEMENT — [topic]: Builder says X, Reviewer says Y. Human decision needed."
>
> Do NOT defend the original recipe out of deference. Do NOT accept the
> Reviewer's findings uncritically. Evaluate each on its merits.
>
> Output: One clean, final recipe the human can execute.

### 7. DELIVER
Present the final recipe.
- Trivial/Small: deliver directly (no adversarial review, no synthesis)
- Medium: one human gate before delivery
- Large: human gate after review (rare for recipe dev — Large usually routes to Cook Planning)

If disagreements were flagged in Step 6, present them clearly:
> **Unresolved disagreement:** [topic]
> Builder's position: [X]
> Reviewer's position: [Y]
> Your call.

### ITERATION
If cook results or feedback require revision, re-run only affected phases.
Recipe feedback goes to Builder #2 for revision without rebuilding from scratch.
