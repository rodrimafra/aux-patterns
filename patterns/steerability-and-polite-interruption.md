---
title: "Steerability & polite interruption"
slug: "steerability-and-polite-interruption"
number: "3.4"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "Users can redirect a running agent mid-task without cancelling and starting over."
featured: false
---

# Steerability & polite interruption

> Users can redirect a running agent mid-task without cancelling and starting over.

## Overview

Delegation is a conversation, not a contract signing. This pattern lets users interject (refine the goal, correct course, add constraints) while the agent gracefully incorporates the change and continues.

## Why it works

Course corrections are cheaper than restarts. Systems that punish interruption with lost work teach users to under-delegate.

## When to use it

- Long-running generative or research tasks
- Iterative creative work where goals sharpen mid-flight
- Voice interfaces, where interruption is natural

## When to avoid it

- Atomic transactions that genuinely cannot absorb mid-flight change

## Examples in the wild

- Follow-up steering in Cursor and Claude Code while agents work
- Interrupting a voice assistant mid-answer
- Editing a running prompt in modern chat UIs

## Related patterns

- [3.1 Kill switch, pause & resume](kill-switch-pause-and-resume.md)
- [4.2 Edit request](edit-request.md)
- [5.5 Execution progress view](execution-progress-view.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
