---
title: "Edit request"
slug: "edit-request"
number: "4.2"
category: "Clarification"
categorySlug: "clarification"
definition: "The agent shows its interpretation of the request and lets the user amend it directly."
featured: false
---

# Edit request

> The agent shows its interpretation of the request and lets the user amend it directly.

## Overview

Between what was said and what was understood lies most agent failure. This pattern externalises the interpretation (a rewritten brief, an expanded prompt) as an editable artifact before or after execution.

## Why it works

Correcting a misreading at the interpretation layer is surgical; correcting it through conversational back-and-forth is archaeology.

## When to use it

- Complex briefs with embedded constraints
- Systems that rewrite or expand user prompts internally
- Recurring tasks whose briefs deserve refinement over time

## When to avoid it

- Trivial requests where showing interpretation is pure overhead

## Examples in the wild

- Image generators exposing their revised prompts
- Search engines' 'showing results for…' with override
- Editable task specs in Copilot Workspace

## Related patterns

- [4.1 Structured clarification prompts](structured-clarification-prompts.md)
- [4.3 Confirmed assumptions](confirmed-assumptions.md)
- [3.4 Steerability & polite interruption](steerability-and-polite-interruption.md)

## Further reading

- People + AI Guidebook (Google PAIR
- Guidelines for Human-AI Interaction) Amershi et al., CHI 2019

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
