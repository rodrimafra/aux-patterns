---
title: "Semantic highlighting of uncertainty"
slug: "semantic-highlighting-of-uncertainty"
number: "6.3"
category: "Transparency of Confidence"
categorySlug: "transparency-of-confidence"
definition: "Uncertainty is marked locally, on the exact span the agent is unsure about, not as a global score users learn to ignore."
featured: true
---

# Semantic highlighting of uncertainty

> Uncertainty is marked locally, on the exact span the agent is unsure about, not as a global score users learn to ignore.

## Overview

A document-level confidence score answers a question nobody asked. What users need to know is where the doubt lives: which extracted date, which translated phrase, which clause. Semantic highlighting marks the specific uncertain spans (visually quiet, semantically precise) so correction effort lands exactly where it is needed. Everything unmarked carries an implicit warranty; the highlighted spans invite one targeted look each.

## Why it works

Local uncertainty display makes review effort proportional to actual risk. It also keeps the agent honest at a granular level: it cannot hide a shaky claim inside an overall 'high confidence' rating.

## When to use it

- Document extraction and parsing (contracts, invoices, forms)
- Translation and transcription outputs
- Any structured output a human confirms field by field

## When to avoid it

- Highlighting so much that the marking loses meaning
- Using alarming visual treatments that read as errors rather than flags

## Examples in the wild

- Grammarly's span-level underlines by issue confidence
- Low-confidence field highlighting in OCR and document-AI review UIs
- Alternative renderings offered on uncertain phrases in machine translation

## Takeaways

- Mark the span, not the document
- Unmarked content is a promise, police it
- Pair every highlight with a one-tap correction path
- Visual weight should whisper 'check this', not shout 'error'

## Related patterns

- [6.2 Confidence thermometer](confidence-thermometer.md)
- [4.3 Confirmed assumptions](confirmed-assumptions.md)
- [5.6 Confessions view](confessions-view.md)

## Further reading

- Guidelines for Human-AI Interaction, Amershi et al., CHI 2019
- People + AI Guidebook, Google PAIR

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
