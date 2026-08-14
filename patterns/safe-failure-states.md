---
title: "Safe failure states"
slug: "safe-failure-states"
number: "9.1"
category: "Failure & Repair"
categorySlug: "failure-and-repair"
definition: "When the agent fails, it fails without damage: work preserved, systems intact, path forward clear."
featured: false
---

# Safe failure states

> When the agent fails, it fails without damage: work preserved, systems intact, path forward clear.

## Overview

Failure handling is architecture, not apology. Safe failure means partial work is saved, external systems are left consistent, destructive steps were staged not committed, and the user lands on 'here's what happened and what you can do', never a dead end.

## Why it works

The cost of an agent's worst day determines how much users risk on its ordinary ones. Cheap failure makes bold delegation rational.

## When to use it

- Every agent that acts (this pattern is a floor, not a feature
- Long tasks accumulating unsaved value
- Actions staged against external systems

## When to avoid it

- Never) but beware failure states so soft that real failures go unnoticed

## Examples in the wild

- Draft preservation on crash across mature editors
- Transactional rollbacks leaving systems consistent
- Agents halting before destructive steps and reporting state

## Related patterns

- [3.6 Rollback & version history](rollback-and-version-history.md)
- [3.1 Kill switch, pause & resume](kill-switch-pause-and-resume.md)
- [9.2 Guided repair flows](guided-repair-flows.md)

## Further reading

- People + AI Guidebook (Google PAIR (Errors + Graceful Failure)
- Guidelines for Human-AI Interaction) Amershi et al., CHI 2019

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
