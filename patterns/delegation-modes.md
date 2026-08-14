---
title: "Delegation modes"
slug: "delegation-modes"
number: "1.2"
category: "Identity & Delegation"
categorySlug: "identity-and-delegation"
definition: "Distinct, user-selectable levels of autonomy, from suggest-only to fully autonomous execution."
featured: false
---

# Delegation modes

> Distinct, user-selectable levels of autonomy, from suggest-only to fully autonomous execution.

## Overview

Autonomy is not a switch, it is a dial. This pattern exposes discrete, well-labelled modes (suggest, ask-before-acting, act-and-report) so users choose how much control to hand over per task, per context, or per agent.

## Why it works

People trust systems whose autonomy they chose. Graduated modes let cautious users start low and ratchet up as the agent proves itself, instead of forcing an all-or-nothing bet.

## When to use it

- Agents whose actions have real-world consequences
- Onboarding journeys where trust must be earned progressively
- Power users and novices sharing one product

## When to avoid it

- Trivial actions where mode selection adds more friction than the action itself

## Examples in the wild

- GitHub Copilot's spectrum from ghost-text suggestions to autonomous agent mode
- Cursor's ask / edit / agent modes
- Driver-assistance levels as the canonical mental model

## Related patterns

- [1.1 Agent identity & role contract](agent-identity-and-role-contract.md)
- [3.2 Human-in-the-loop gates](human-in-the-loop-gates.md)
- [3.3 Plan-then-execute workflow](plan-then-execute-workflow.md)

## Further reading

- Guidelines for Human-AI Interaction, Amershi et al., CHI 2019
- Microsoft HAX Toolkit

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
