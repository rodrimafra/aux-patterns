---
title: "Human-in-the-loop gates"
slug: "human-in-the-loop-gates"
number: "3.2"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "Checkpoints where the agent must pause and obtain explicit approval before proceeding, placed by consequence, not by habit."
featured: true
---

# Human-in-the-loop gates

> Checkpoints where the agent must pause and obtain explicit approval before proceeding, placed by consequence, not by habit.

## Overview

Not every action needs approval; approving everything is just a slower manual product. HITL gates are deliberate checkpoints positioned where consequence and irreversibility are high, sending the email, moving the money, deleting the data. Below the gate line, the agent acts freely. Above it, a human decides. The gate itself must be informative: a pre-action brief covering what the agent wants to do, why, on what evidence, and what happens next, never a bare Confirm/Cancel that trains blind clicking.

## Why it works

Gates convert autonomy from a leap of faith into a supervised handover. Placed well, they concentrate human attention exactly where it is irreplaceable; placed lazily, they create approval fatigue that defeats their purpose.

## When to use it

- Irreversible or costly actions (payments, sends, deletions, contracts)
- First occurrences of a new action class, before trust is established
- Regulated workflows requiring documented consent

## When to avoid it

- Routine, reversible actions (gate fatigue teaches users to stop reading
- As a liability shield without genuine decision content

## Examples in the wild

- Claude Code's permission prompts before running commands or editing files
- Deployment approval steps in GitHub Actions and release pipelines
- Payment confirmation with biometric step-up in banking apps
- Devin's plan approval before autonomous execution

## Takeaways

- Place gates by consequence and reversibility, not uniformly
- Make every gate a brief: what, why, evidence, what happens next
- Tier approvals) first-time actions gate, proven routines flow
- Measure gate fatigue: approval-without-reading is a design failure

## Related patterns

- [3.3 Plan-then-execute workflow](plan-then-execute-workflow.md)
- [1.2 Delegation modes](delegation-modes.md)
- [5.1 Reasoning glimpse](reasoning-glimpse.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
