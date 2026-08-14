---
title: "Agent identity & role contract"
slug: "agent-identity-and-role-contract"
number: "1.1"
category: "Identity & Delegation"
categorySlug: "identity-and-delegation"
definition: "An explicit, inspectable statement of what an agent is, what it is for, and the boundaries of its mandate."
featured: false
---

# Agent identity & role contract

> An explicit, inspectable statement of what an agent is, what it is for, and the boundaries of its mandate.

## Overview

Before a person can delegate anything, they need to know who they are delegating to. This pattern gives every agent a visible contract: its purpose, its capabilities, its limits, and what it will never do. The contract is a promise the interface keeps.

## Why it works

Trust begins with predictability. A stated mandate lets users calibrate expectations before the first interaction, and gives them grounds to object when the agent drifts outside it.

## When to use it

- Introducing a new agent to users for the first time
- Products where one agent among several must be distinguishable
- Regulated domains where scope must be documented

## When to avoid it

- Purely reactive single-purpose tools where scope is self-evident

## Examples in the wild

- Custom GPT instruction summaries shown before first use
- Slack app profiles listing granted scopes and capabilities
- Claude's stated constitution and usage policies

## Related patterns

- [1.2 Delegation modes](delegation-modes.md)
- [3.5 Scoped permissions & tool consent](scoped-permissions-and-tool-consent.md)
- [8.3 Privacy & data usage controls](privacy-and-data-usage-controls.md)

## Further reading

- Guidelines for Human-AI Interaction, Amershi et al., CHI 2019
- Microsoft HAX Toolkit

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
