---
title: "Escalation & fallback routing"
slug: "escalation-and-fallback-routing"
number: "7.6"
category: "Multi-Agent Systems"
categorySlug: "multi-agent-systems"
definition: "Automatic, graceful transfer to a human or stronger system when the agent hits its limits."
featured: false
---

# Escalation & fallback routing

> Automatic, graceful transfer to a human or stronger system when the agent hits its limits.

## Overview

Failure is inevitable; dead ends are a choice. This pattern defines the paths out (to a human, a more capable model, a safer default) triggered by confidence collapse, repeated failure, or user frustration.

## Why it works

The safety net determines how much users will trust the wire. Known, smooth escalation makes people comfortable starting with the agent.

## When to use it

- Customer-facing agents with human backstops
- Tiered model architectures balancing cost and capability
- Detection of user frustration or repeated failure loops

## When to avoid it

- Escalation that silently drops context and restarts the conversation

## Examples in the wild

- Bot-to-agent escalation in Intercom and Zendesk
- Model fallback chains on refusal or low confidence
- 'Talk to a human' affordances that actually work

## Related patterns

- [7.4 Agent handover briefs](agent-handover-briefs.md)
- [9.2 Guided repair flows](guided-repair-flows.md)
- [6.2 Confidence thermometer](confidence-thermometer.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
