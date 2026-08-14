---
title: "Kill switch, pause & resume"
slug: "kill-switch-pause-and-resume"
number: "3.1"
category: "Control & Steering"
categorySlug: "control-and-steering"
definition: "An always-available control to halt an agent instantly, without losing the work in progress."
featured: false
---

# Kill switch, pause & resume

> An always-available control to halt an agent instantly, without losing the work in progress.

## Overview

The most important button in agentic UX is stop. This pattern guarantees interruption is immediate, lossless, and reversible: pause preserves state, resume continues, stop abandons cleanly.

## Why it works

Knowing you can stop is what makes starting safe. Recoverable interruption removes the fear cost of delegation, so users grant more autonomy overall.

## When to use it

- Every autonomous execution longer than a moment
- Actions with mounting cost or consequence
- Agents operating on live external systems

## When to avoid it

- Never omit it, the anti-pattern is its absence

## Examples in the wild

- Stop-generating controls in every major chat product
- Devin's pause and redirect mid-run
- CI/CD pipeline cancellation as prior art

## Related patterns

- [3.4 Steerability & polite interruption](steerability-and-polite-interruption.md)
- [3.6 Rollback & version history](rollback-and-version-history.md)
- [9.1 Safe failure states](safe-failure-states.md)

## Further reading

- Building Effective Agents (Anthropic
- Human-Centered AI) Ben Shneiderman

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
