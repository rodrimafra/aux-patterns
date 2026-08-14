---
title: "Supervisor agent"
slug: "supervisor-agent"
number: "7.3"
category: "Multi-Agent Systems"
categorySlug: "multi-agent-systems"
definition: "A coordinating agent that decomposes work, delegates to specialists, and quality-checks results."
featured: false
---

# Supervisor agent

> A coordinating agent that decomposes work, delegates to specialists, and quality-checks results.

## Overview

One point of contact, many hands. The supervisor pattern gives users a single conversational interface while specialist agents work behind it, with the supervisor owning decomposition, sequencing, and integration of results.

## Why it works

Users get simplicity without sacrificing capability. The supervisor also concentrates accountability: one agent answers for the whole, however many contributed.

## When to use it

- Complex tasks spanning distinct competencies
- Products hiding multi-agent complexity behind one persona
- Quality-control layers over generative work

## When to avoid it

- Simple domains where a supervisor is bureaucracy

## Examples in the wild

- Orchestrator-worker architectures in agent frameworks
- Subagent delegation in agentic coding tools
- Manager agents in AutoGen-style systems

## Related patterns

- [7.1 Orchestration graph](orchestration-graph.md)
- [7.4 Agent handover briefs](agent-handover-briefs.md)
- [7.6 Escalation & fallback routing](escalation-and-fallback-routing.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
