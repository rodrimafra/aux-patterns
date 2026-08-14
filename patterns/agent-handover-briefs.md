---
title: "Agent handover briefs"
slug: "agent-handover-briefs"
number: "7.4"
category: "Multi-Agent Systems"
categorySlug: "multi-agent-systems"
definition: "Structured context transfer when work passes between agents, or from agent to human."
featured: false
---

# Agent handover briefs

> Structured context transfer when work passes between agents, or from agent to human.

## Overview

Every handover leaks context unless the interface fights for it. The brief packages goal, state, decisions made, open questions, and constraints so the receiver (silicon or human) starts warm.

## Why it works

Continuity is the product. Users should never re-explain their situation because the system changed workers mid-task.

## When to use it

- Agent-to-human escalation
- Long tasks crossing sessions or specialised agents
- Support flows with mixed bot and human staffing

## When to avoid it

- Trivial handoffs where a brief outweighs the task

## Examples in the wild

- Bot-to-human handoffs with conversation summaries in support platforms
- Escalation tickets auto-populated with attempted steps
- Session summaries when resuming long agent tasks

## Related patterns

- [7.3 Supervisor agent](supervisor-agent.md)
- [7.6 Escalation & fallback routing](escalation-and-fallback-routing.md)
- [8.4 Context repository & workspace profiles](context-repository-and-workspace-profiles.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
