# Cook Planning Workflow

Used when the user asks to plan a specific cook session — timeline, temps,
equipment setup, and weather considerations. Handles everything from a single
backyard brisket to full multi-category competition prep.

## Tiers

- **Small:** Single protein, single timeline. "Plan a brisket cook for Saturday."
- **Medium:** Single category with full review. "Develop a full rib protocol for KCBS."
- **Large:** Multi-category competition prep. "Full comp prep — 4 categories for Saturday's KCBS." This is parallel planning across categories with cross-category schedule verification, equipment allocation, and turn-in window management.

## Phases

### 1. INTAKE
Prerequisite: SKILL.md Steps 1-3 complete (request understood, competition body
determined, ceremony calibrated).

Workflow-specific: Identify protein(s), target date/time (if scheduled), equipment
available, desired doneness.

For Large (competition prep): Also identify competition body, all categories entered,
date/location, number and type of cookers, team size.

### 2. CONTEXT GATHERING (Scout, Medium+)
Dispatch Scout (Haiku->Sonnet):
> Gather context for {protein} cook planning.
> Equipment: {cooker type, fuel type}
> Date/location: {if scheduled}
> Query claude-mem for: prior cook data for this protein on this equipment,
> equipment-specific timing adjustments.
> Pull: weather forecast (if dated), altitude (if location known).
> Competition body: {if applicable — pull turn-in windows and rules}

For Large: Scout pulls all category rules, full turn-in order and windows,
site conditions, and prior results at this event or competition body.

### 3. COOK PLAN BUILD (Builder #1)
Dispatch Builder (Sonnet):
> Build a complete cook plan for {protein}.
> Competition context: {if applicable — turn-in window, rules}
> Equipment: {cooker type, controller if any}
> Environmental: {weather forecast, altitude, ambient temp}
> Recipe/technique: {if specified by user, or reference prior recipe from context}
> Prior cook data: {from Scout, if available}
>
> Produce:
> **TIMELINE** (work backward from serving/turn-in time):
> - Fire start time
> - Cooker preheat and stabilization
> - Protein load time
> - Expected stall window (155-165F for beef/pork) with contingency
> - Wrap decision point (if applicable)
> - Target pull temp and probe tender check protocol
> - Rest protocol (faux cambro: cooler + towels, target 2-4 hours for brisket) `[GENERATED DEFAULT — refine through use]`
> - Slice/pull/prep time
> - Turn-in or serving time
>
> **FUEL PLAN:**
> - Fuel type and estimated quantity (based on prior cook data from Scout if available)
> - Fire management approach (clean fire, thin blue smoke)
> - Wood selection for smoke flavor
>
> **EQUIPMENT SETUP:**
> - Cooker configuration (damper settings, water pan, deflector plates)
> - Probe placement (pit probe, meat probe positions)
> - Airflow management
>
> **CONTINGENCIES:**
> - If stall runs long: wrap decision and adjusted timeline
> - If weather changes: timeline adjustments
> - If running ahead: extended rest protocol
> - If running behind: temp bump protocol and quality tradeoffs
>
> **FOOD SAFETY CHECKPOINTS:**
> - Max time in danger zone (40-140F) — must be under 4 hours `[GENERATED DEFAULT — refine through use]`
> - Minimum internal temp targets
> - Safe hold temperatures during rest

### 3L. LARGE TIER — COMPETITION STRATEGY (Builder #1, before per-category plans)

For Large (multi-category competition prep), Builder #1 first produces the competition
strategy before building individual cook plans:

> Develop competition strategy for {competition body}, {N} categories.
> Competition rules: {from Scout}
> Categories: {list with turn-in order and windows}
> Equipment available: {cooker inventory}
> Team size: {number of people}
> Weather forecast: {from Scout}
> Prior results: {from Scout/claude-mem}
>
> **MASTER TIMELINE:**
> Work backward from the LAST turn-in. Map every category's key milestones
> onto a single timeline. Identify overlaps and conflicts.
>
> Turn-in order for KCBS (standard): Chicken, Ribs, Pork, Brisket
> at 30-minute intervals starting at noon (typical). `[GENERATED DEFAULT — refine through use]`
>
> **EQUIPMENT ALLOCATION:**
> Which cooker runs which protein. Shared cooker time if needed.
>
> **PRIORITY RANKING:**
> Which categories to prioritize if time gets tight. Factor: prior strengths,
> scoring weight, competitive landscape.
>
> **CROSS-CATEGORY CONFLICTS:**
> Where cook windows overlap. Where equipment is double-booked.
> Where one category's needs conflict with another's.
>
> **CONTINGENCY PLAN:**
> What to cut if running behind. Which category gets sacrificed (none if possible,
> but have the plan). Rain/wind protocol. Equipment failure fallback.

**HUMAN GATE #1 (Large only):** Present competition strategy for approval before
building per-category plans. Categories, master timeline, equipment allocation,
priority ranking, top risks. Approve / Revise / Override priority ranking?

Then dispatch per-category cook plans (Phase 3 above) for each category, using the
approved strategy. **Parallel dispatch where possible** — categories with independent
equipment can be planned in parallel. Categories sharing a cooker must be sequenced.

### 4. VERIFICATION (Verifier, Small+)
Run Verifier (tools, not an agent):
- Timeline arithmetic: all phases sum to correct total, working backward from turn-in/serve hits target
- Turn-in compliance: plan delivers to the window with ~20 minutes buffer (meat needs rest time but shouldn't get cold)
- Food safety: time through danger zone under 4 hours, internal temps meet USDA minimums
- Schedule conflicts: if multiple proteins, no overlapping equipment needs that can't be met
- Carryover cooking: pull temp accounts for expected carryover (5-10F for large cuts) `[GENERATED DEFAULT — refine through use]`

For Large — cross-category checks on the COMBINED schedule:
- No turn-in conflicts (each category delivered within its window)
- No equipment double-booking (two proteins can't need the same cooker simultaneously unless planned)
- No food safety violations from extended holds waiting for later turn-in windows
- Buffer time between turn-in preps (minimum 5 minutes between categories) `[GENERATED DEFAULT — refine through use]`
- Rest times adequate for each protein given the schedule

### 5. ADVERSARIAL REVIEW (Reviewer, Medium+)
Dispatch Reviewer (Opus, FRESH instance — never Builder #1):
> Use the adversarial prompt for cook plans from `gates/quality-checklists.md`.
> For Large, use the competition prep prompt instead.
> Receives Builder's output only — do NOT re-inject weather, equipment specs, or context.
>
> Builder's cook plan: {Builder #1 output}
> For Large: competition strategy + all per-category cook plans + cross-category verification results.

### 6. SYNTHESIS (Builder #2, Medium+ — FRESH instance, never Builder #1)
Dispatch a NEW Builder (Sonnet, fresh instance):
> You are a fresh instance. You did NOT write the original cook plan.
> You have three inputs:
>
> 1. Original cook plan: {Builder #1 output}
> 2. Verifier results: {Verifier output — any failed checks}
> 3. Adversarial review findings: {Reviewer output}
>
> Produce the FINAL cook plan by:
> (a) Fix all Verifier-flagged issues (timeline math, food safety, schedule conflicts)
> (b) Incorporate the Reviewer's valid findings
> (c) Flag genuine disagreements for the human
>
> Output: One clean, executable cook plan.
>
> For Large: unified master timeline (single document, all categories),
> per-category detail sheets, equipment logistics, contingency protocols,
> shopping list (all proteins, ingredients, fuel, supplies).

### 7. DELIVER
Present the final cook plan.
- Trivial/Small: deliver directly
- Medium: one human gate before delivery
- Large: **HUMAN GATE #2** before final delivery

Include: timeline summary, key decision points, contingency triggers.
For Large: master timeline, per-category plans, shopping list, equipment allocation.

### ITERATION
If weather changes, protein specs change, or schedule shifts — re-run only the
affected phases. A weather change re-runs context gathering and timeline phases.
A protein change re-runs from recipe/technique. A schedule change re-runs
timeline and cross-category verification only.
