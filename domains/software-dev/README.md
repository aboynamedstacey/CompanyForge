# Software Development — AI Engineering Organization

An AI-native organizational structure for software development. Three capability
types (Builder, Reviewer, Scout) plus deterministic tool verification, composed
elastically based on task complexity.

## Setup

Copy this domain into your project:
```bash
cp -r domains/software-dev/.claude /your/project/.claude
cp domains/software-dev/CLAUDE.md /your/project/CLAUDE.md
```

## Prerequisites

- Claude Code CLI
- Recommended plugins: superpowers, claude-mem, firecrawl
- Optional: metaswarm (for agent personas), BEADS (multi-session state)

## Usage

```
/dev add a REST endpoint for user authentication
/dev fix the race condition in the queue processor
/dev refactor the payment module to use the new gateway interface
/dev research whether we should migrate from REST to gRPC
/dev start a new project from scratch
```

The system auto-detects work type, calibrates ceremony, and composes the right
dispatches. Override ceremony with: "treat this as large" or `--budget $N`.

## Design

This organization has three agent capability types and deterministic tools.
Not twelve roles with different names. The Builder writes specs, designs, code,
and docs — those are workflow phases with different prompts, not different
capabilities. The Reviewer checks quality, security, and correctness — those
are different checklists, not different agents.

The only hard organizational boundary: the agent that builds something never
reviews its own work. Everything else is workflow logic.
