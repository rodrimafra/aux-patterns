---
title: "Orchestration graph"
slug: "orchestration-graph"
number: "7.1"
category: "Multi-Agent Systems"
categorySlug: "multi-agent-systems"
definition: "A visual map of the agents involved in a task and how work flows between them."
featured: false
---

# Orchestration graph

> A visual map of the agents involved in a task and how work flows between them.

## Overview

When one request fans out to many agents, users lose the plot. The orchestration graph shows the cast and the choreography: which agent does what, what depends on what, where things stand.

## Why it works

Legible structure is the difference between a system and a séance. Users supervise multi-agent work meaningfully only when they can see its shape.

## When to use it

- Workflows spanning three or more agents
- Debugging multi-agent failures
- Explaining system behaviour to stakeholders

## When to avoid it

- Single-agent products, where a graph is decoration

## Examples in the wild

- Workflow canvases in n8n and Zapier
- Agent-graph visualisers in orchestration frameworks
- Pipeline DAG views in data tooling

## Related patterns

- [7.3 Supervisor agent](supervisor-agent.md)
- [7.5 Assignment boards & work queues](assignment-boards-and-work-queues.md)
- [5.5 Execution progress view](execution-progress-view.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
