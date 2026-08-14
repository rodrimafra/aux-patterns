---
title: "Plan-then-execute workflow"
slug: "plan-then-execute-workflow"
number: "3.3"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "The agent proposes a complete plan for review before any action is taken."
featured: false
---

# Plan-then-execute workflow

> The agent proposes a complete plan for review before any action is taken.

## Overview

Instead of acting step by step into the unknown, the agent thinks first and shows its work: a structured plan the user can approve, edit, or reject. Execution begins only after the human has seen the shape of what is coming.

## Why it works

A plan is the cheapest possible place to catch a misunderstanding. Reviewing intent costs seconds; reversing execution can cost hours, or be impossible.

## When to use it

- Multi-step tasks touching real systems
- Ambiguous requests where interpretation should be verified
- Expensive operations (compute, money, other people's time)

## When to avoid it

- Quick single-step tasks where planning theatre slows everything down

## Examples in the wild

- Claude Code's plan mode
- Devin's editable task plan before running
- Copilot Workspace's spec-and-plan flow before code changes

## Related patterns

- [3.2 Human-in-the-loop gates](human-in-the-loop-gates.md)
- [4.3 Confirmed assumptions](confirmed-assumptions.md)
- [5.5 Execution progress view](execution-progress-view.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
