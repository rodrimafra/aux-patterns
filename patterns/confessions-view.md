---
title: "Confessions view"
slug: "confessions-view"
number: "5.6"
category: "Transparency of Process"
categorySlug: "transparency-of-process"
definition: "The agent proactively discloses shortcuts, failures, and unverified claims in its own output."
featured: false
---

# Confessions view

> The agent proactively discloses shortcuts, failures, and unverified claims in its own output.

## Overview

The most trustworthy sentence an agent can produce is 'here is what I could not do.' Confessions surface skipped steps, low-confidence sections, and unverified assumptions alongside the result, before the user finds them the hard way.

## Why it works

Self-reported limitations are cheaper than discovered ones. Every honest confession spends a little pride to buy durable credibility.

## When to use it

- Research and analysis with variable source coverage
- Long tasks where some steps quietly failed
- Anything a user will act on without independent checking

## When to avoid it

- Reflexive hedging on everything, confession must be specific to be useful

## Examples in the wild

- 'I couldn't verify…' notes on grounded answers
- Test-failure admissions in coding agent summaries
- Coverage caveats in research tool outputs

## Related patterns

- [6.6 Counter-evidence](counter-evidence.md)
- [5.1 Reasoning glimpse](reasoning-glimpse.md)
- [9.1 Safe failure states](safe-failure-states.md)

## Further reading

- Building Effective Agents (Anthropic
- Shape of AI) Emily Campbell

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
