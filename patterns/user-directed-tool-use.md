---
title: "User-directed tool use"
slug: "user-directed-tool-use"
number: "3.7"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "Users choose which tools, sources, and output modes the agent may employ for a task."
featured: false
---

# User-directed tool use

> Users choose which tools, sources, and output modes the agent may employ for a task.

## Overview

Sometimes the human knows best how the job should be done. This pattern exposes the agent's toolbox (search the web or not, use this dataset, produce a table not prose) as explicit, per-task controls.

## Why it works

Constraining method is a form of steering that prevents whole classes of error before they happen, and teaches users what the agent's tools actually are.

## When to use it

- Research tasks where source quality matters
- Outputs destined for specific downstream formats
- Users with hard constraints (privacy, cost, compliance)

## When to avoid it

- Defaulting to manual tool selection for users who just want the outcome

## Examples in the wild

- Perplexity's focus and source selectors
- Tool toggles (web, code, canvas) in ChatGPT
- Model and context pickers in agentic IDEs

## Related patterns

- [3.5 Scoped permissions & tool consent](scoped-permissions-and-tool-consent.md)
- [6.1 Source anchoring & grounding](source-anchoring-and-grounding.md)
- [8.4 Context repository & workspace profiles](context-repository-and-workspace-profiles.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
