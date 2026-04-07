# Domain Context Engine — Software Development

## Codebase Context (always gathered)

Before implementation or design:
- Existing patterns, conventions, naming
- Dependencies and constraints
- API contracts to respect or extend
- Git history for recent changes

**Source priority:** code > CLAUDE.md > git history > cross-session memory

**Depth by tier:**
- Trivial: files being changed + CLAUDE.md
- Small: + related modules, similar patterns
- Medium: + full dependency analysis, API review
- Large: + cross-project memory, prior architecture decisions

## Domain Context (when domain_research = true)

For work beyond routine software engineering:
- State of the art, competing approaches
- Relevant specs or literature
- Regulatory requirements if applicable

**Source priority:** cross-session memory > web research > papers > specs

**Depth by tier:**
- Trivial/Small: skip
- Medium: quick survey
- Large: comprehensive literature review
