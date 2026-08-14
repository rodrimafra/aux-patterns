---
title: "Rollback & version history"
slug: "rollback-and-version-history"
number: "3.6"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "Every agent action is recorded and reversible; state can be restored to any prior point."
featured: false
---

# Rollback & version history

> Every agent action is recorded and reversible; state can be restored to any prior point.

## Overview

Undo is the foundation of fearless use. Extended to agents, it means a browsable history of what changed, when, by whom (human or agent) with one-step restoration.

## Why it works

Reversibility converts risk into experiment. Users who know they can roll back delegate earlier, grant more, and panic less when something looks wrong.

## When to use it

- Agents that modify documents, code, or configuration
- Batch operations across many items
- Anywhere 'undo' would exist for a human doing the same work

## When to avoid it

- Genuinely irreversible external actions, which is exactly where HITL gates belong instead

## Examples in the wild

- Git as the deep prior art
- Figma and Notion version history
- Checkpoint restore in agentic coding tools

## Related patterns

- [3.1 Kill switch, pause & resume](kill-switch-pause-and-resume.md)
- [9.1 Safe failure states](safe-failure-states.md)
- [5.4 Activity timeline & audit log](activity-timeline-and-audit-log.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
