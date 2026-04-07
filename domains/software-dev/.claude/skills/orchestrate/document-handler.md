# Document Handler — Software Development

## Produced Artifacts

- Specs: `docs/specs/YYYY-MM-DD-name.md`
- Designs: `docs/designs/YYYY-MM-DD-name.md`
- ADRs: `docs/adr/NNNN-title.md`
- Research: `docs/research/YYYY-MM-DD-topic.md`

## Process Once, Inject Everywhere

When Builder produces an artifact: orchestrator captures output, saves to
docs/, injects cached content into subsequent dispatches. No capability
re-reads raw files.

When external docs are referenced: extract once (firecrawl for URLs, Read
for local), cache for workflow duration, inject relevant sections only.
