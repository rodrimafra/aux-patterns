---
title: "Guided repair flows"
slug: "guided-repair-flows"
number: "9.2"
category: "Failure & Repair"
categorySlug: "failure-and-repair"
definition: "A structured path from agent error to fixed outcome, with the agent doing the heavy lifting."
featured: false
---

# Guided repair flows

> A structured path from agent error to fixed outcome, with the agent doing the heavy lifting.

## Overview

'It's wrong' should begin a repair, not a support ticket. Guided repair walks the user through diagnosis (what's wrong, where, of which kind) then proposes targeted fixes, applies the chosen one, and verifies the result.

## Why it works

Repair effort determines whether errors are potholes or cliffs. A cheap, reliable fix loop makes imperfect agents perfectly usable.

## When to use it

- Structured outputs where errors are localised and typed
- Recurring failure modes worth productising
- Users who can recognise wrong but can't specify right

## When to avoid it

- Freeform creative revision, where conversation serves better than a wizard

## Examples in the wild

- Fix-with-AI loops on failing code and tests
- Correction flows in document-extraction review queues
- Merge-conflict resolution wizards as prior art

## Related patterns

- [9.1 Safe failure states](safe-failure-states.md)
- [2.6 Feedback & rating controls](feedback-and-rating-controls.md)
- [4.2 Edit request](edit-request.md)

## Further reading

- People + AI Guidebook (Google PAIR (Errors + Graceful Failure)
- Guidelines for Human-AI Interaction) Amershi et al., CHI 2019

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
