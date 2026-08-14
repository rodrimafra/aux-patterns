---
title: "Scoped permissions & tool consent"
slug: "scoped-permissions-and-tool-consent"
number: "3.5"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "Granular, revocable grants controlling which tools, data, and actions an agent may use."
featured: false
---

# Scoped permissions & tool consent

> Granular, revocable grants controlling which tools, data, and actions an agent may use.

## Overview

All-or-nothing access is how trust dies. This pattern decomposes agent capability into inspectable scopes (read calendar, send email, spend up to X) granted individually, revocable instantly, and visible in one place.

## Why it works

Granularity lets users say yes to the useful parts without underwriting the dangerous ones. Every scope granted is a considered decision, not a surrender.

## When to use it

- Agents connecting to external accounts and APIs
- Financial or destructive capability
- Enterprise deployment with compliance requirements

## When to avoid it

- Fragmenting scopes so finely that consent becomes noise

## Examples in the wild

- OAuth scope consent screens
- iOS per-capability app permissions
- Claude's per-tool permission model

## Related patterns

- [1.1 Agent identity & role contract](agent-identity-and-role-contract.md)
- [3.2 Human-in-the-loop gates](human-in-the-loop-gates.md)
- [10.3 Access & permission tiers for agents](access-and-permission-tiers-for-agents.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
