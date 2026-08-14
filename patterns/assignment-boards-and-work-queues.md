---
title: "Assignment boards & work queues"
slug: "assignment-boards-and-work-queues"
number: "7.5"
category: "Multi-Agent Systems"
categorySlug: "multi-agent-systems"
definition: "Shared boards where tasks are visibly assigned across humans and agents alike."
featured: false
---

# Assignment boards & work queues

> Shared boards where tasks are visibly assigned across humans and agents alike.

## Overview

When agents become teammates, they belong on the team board. This pattern slots agent work into the same queues, statuses, and assignments as human work, one operational picture.

## Why it works

A shared board normalises supervision: spotting a stuck agent task works exactly like spotting a stuck human one. No parallel shadow system.

## When to use it

- Teams with recurring delegated agent workloads
- Ops functions balancing human and agent capacity
- Visibility of agent workload for planning

## When to avoid it

- Solo use, where a personal task list suffices

## Examples in the wild

- Bots as assignees in Linear and Jira workflows
- Copilot tasks appearing in project queues
- Ticket routing that mixes human and bot agents

## Related patterns

- [7.1 Orchestration graph](orchestration-graph.md)
- [5.5 Execution progress view](execution-progress-view.md)
- [10.1 Fleet health dashboard](fleet-health-dashboard.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
