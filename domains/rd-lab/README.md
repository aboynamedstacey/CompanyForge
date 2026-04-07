# R&D Lab — AI Research & Development Organization

An AI-native organizational structure for R&D work. Three capability types
(Builder, Reviewer, Scout) plus physics verification, with TRL-based ceremony.

## Setup

```bash
cp -r domains/rd-lab/.claude /your/project/.claude
cp domains/rd-lab/CLAUDE.md /your/project/CLAUDE.md
```

## Prerequisites

- Claude Code CLI
- Recommended plugins: superpowers, claude-mem, firecrawl
- Optional: BEADS (multi-session state tracking)

## Usage

```
/lab explore feasibility of piezoelectric energy harvesting for bridge sensors
/lab design a thermal management system for a 500W drone motor
/lab compare LiPo vs solid-state batteries for high-altitude UAV applications
/lab test plan for validating antenna gain in an anechoic chamber
/lab regulatory certifications for a commercial drone under 55 lbs
```

## Design

Three agent types, not five named personas. The Builder produces feasibility
assessments, system designs, quantitative analyses, and test plans — same
type, different prompts. The Reviewer checks physics, challenges assumptions,
and finds failure modes — same type, different checklists per workflow.
Physics verification (dimensional analysis, conservation checks) is a tool
layer, not agent judgment.
