# Post-Cook Analysis Workflow

Used when the user wants to review results from a completed cook or competition.
This workflow extracts lessons and feeds the learning loop via cross-session memory.

Post-Cook Analysis is how the system gets smarter over time. Every competition
result, every backyard cook with notes, every scoresheet — this is the data
that makes future cook plans and recipes better.

## Phases

### 1. INTAKE
Prerequisite: SKILL.md Steps 1-3 complete (request understood, competition body
determined, ceremony calibrated).

Workflow-specific: Identify what data is available — scoresheets, cook logs,
photos, notes, placement results.

### 2. DATA ASSEMBLY AND ANALYSIS (Builder #1)
Dispatch Builder (Sonnet):
> Assemble, organize, and analyze the cook/competition data.
> Available data: {user-provided data}
> Competition body: {if applicable}
>
> **PART 1 — DATA SUMMARY:**
>
> **PER-CATEGORY RESULTS** (if competition):
> - Category: {name}
> - Scores: Appearance {avg}, Taste {avg}, Tenderness {avg}
> - If KCBS: calculate scores with high/low drops — distinguish dropped outliers from surviving scores
> - Overall category score and placement (if known)
> - Score distribution: note any outlier judges (2+ points off the mean)
>
> **COOK LOG ANALYSIS** (if available):
> - Actual timeline vs. planned timeline
> - Stall duration and behavior
> - Wrap time (actual vs. planned)
> - Pull temp and probe tender assessment
> - Rest duration
> - Total cook time
> - Weather conditions actual vs. forecast
>
> **VISUAL ASSESSMENT** (if photos available):
> - Turn-in box appearance notes
> - Bark quality
> - Smoke ring
> - Moisture/juiciness indicators
> - Garnish presentation
>
> **PART 2 — ANALYSIS:**
>
> **WHAT WORKED:**
> - Highest-scoring elements and why
> - Timeline adherence — where the plan held
> - Technique decisions that paid off
>
> **WHAT DIDN'T:**
> - Lowest-scoring elements and probable causes
> - Timeline deviations — where the plan broke and why
> - Technique decisions that cost points
>
> **SCORING PATTERNS:**
> - Which criteria (Appearance/Taste/Tenderness) was strongest/weakest
> - Judge variance — consistent scoring or wide spread
> - Comparison to prior competitions (if data in claude-mem)
>
> **ROOT CAUSE ANALYSIS:**
> For each issue identified, trace back to the decision that caused it:
> - Was it a recipe issue (rub, sauce, injection)?
> - Was it a technique issue (temp, wrap timing, rest)?
> - Was it a planning issue (timeline too tight, wrong equipment)?
> - Was it an execution issue (missed a step, equipment malfunction)?
> - Was it a presentation issue (box appearance, garnish, slicing)?

### 3. ADVERSARIAL REVIEW (Reviewer, Medium+)
Dispatch Reviewer (Opus, FRESH instance):
> Use the adversarial prompt for post-cook analysis from `gates/quality-checklists.md`.
> Receives Builder's analysis only.
>
> Builder's analysis: {Builder output}

### 4. SYNTHESIS (Builder #2, Medium+ — FRESH instance)
Dispatch a NEW Builder (Sonnet, fresh instance):
> You are a fresh instance. You did NOT write the original analysis.
> You have two inputs:
>
> 1. Original analysis: {Builder #1 output}
> 2. Adversarial review findings: {Reviewer output}
>
> Produce the FINAL post-cook analysis:
> (a) Incorporate valid Reviewer findings
> (b) Flag genuine disagreements
>
> Output: One clean analysis with actionable recommendations.

### 5. LEARNING EXTRACTION
**This is the critical step that closes the loop.**

Extract and store in claude-mem:
> **LESSONS LEARNED — {date} — {competition/cook type}:**
> - Protein: {protein}, Equipment: {equipment}
> - What to repeat: {specific techniques/recipes that scored well}
> - What to change: {specific adjustments with rationale}
> - Timeline adjustments: {actual vs. planned, new baseline for this protein/equipment}
> - Recipe adjustments: {specific ingredient or technique changes}
> - Environmental notes: {how weather/altitude affected the cook}
> - Equipment notes: {cooker-specific learnings}

Tag entries for retrieval by: protein, equipment, competition body, category,
technique. Future Scout queries for cook planning and recipe development
will pull these lessons automatically.

### 6. DELIVER
Present the final analysis with:
- Scores summary
- Key findings (what worked, what didn't)
- Actionable recommendations for next cook
- Lessons stored in memory (confirm what was saved)

- Trivial/Small: deliver directly
- Medium: one human gate before delivery
- Large: human gate after review

### ITERATION
If the user provides additional data (forgotten scoresheet, updated placement
results), re-run only affected phases — don't rebuild the whole analysis.
