---
title: "Access & permission tiers for agents"
slug: "access-and-permission-tiers-for-agents"
number: "10.3"
category: "Governance & Oversight"
categorySlug: "governance-and-oversight"
definition: "Role-based capability levels for agents, mirroring how organisations already tier human access."
featured: false
---

# Access & permission tiers for agents

> Role-based capability levels for agents, mirroring how organisations already tier human access.

## Overview

Organisations don't give interns production keys; agents deserve the same discipline. Tiers bundle scopes into named levels (read-only, contributor, trusted operator) with promotion criteria and review cycles.

## Why it works

Tiering scales consent: instead of auditing hundreds of individual scope grants, governance reasons about a handful of well-defined levels.

## When to use it

- Fleets of agents with varied maturity and blast radius
- Progressive promotion as agents prove reliability
- Mapping agent access to existing IAM structures

## When to avoid it

- Solo agents, where direct scoped permissions suffice

## Examples in the wild

- IAM roles and policies as the direct ancestor
- Enterprise AI policies tiering tool access
- Staged rollouts granting capability by cohort

## Related patterns

- [3.5 Scoped permissions & tool consent](scoped-permissions-and-tool-consent.md)
- [10.2 Risk & policy heatmaps](risk-and-policy-heatmaps.md)
- [7.2 Agent registry & profiles](agent-registry-and-profiles.md)

## Further reading

- Human-Centered AI (Ben Shneiderman
- Building Effective Agents) Anthropic

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
