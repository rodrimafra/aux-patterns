---
title: "Confidence thermometer"
slug: "confidence-thermometer"
number: "6.2"
category: "Transparency of Confidence"
categorySlug: "transparency-of-confidence"
definition: "A graded, glanceable display of how certain the agent is about a given output."
featured: false
---

# Confidence thermometer

> A graded, glanceable display of how certain the agent is about a given output.

## Overview

Binary certainty is a lie told by interface convention. The thermometer renders confidence as a spectrum (high, moderate, low) calibrated so the displayed level actually predicts accuracy.

## Why it works

Users allocate scrutiny efficiently when confidence is visible: skim the high, verify the low. Calibration is everything, a thermometer that always reads high is worse than none.

## When to use it

- Extraction and classification with measurable confidence
- Batch outputs where users must prioritise review
- Decision support feeding human judgement

## When to avoid it

- Displaying uncalibrated scores as if they were probabilities

## Examples in the wild

- Probability framing in weather forecasts as the mental model
- Confidence bands on ML-extracted document fields
- Match-strength indicators in search and dedupe tools

## Related patterns

- [6.3 Semantic highlighting of uncertainty](semantic-highlighting-of-uncertainty.md)
- [6.1 Source anchoring & grounding](source-anchoring-and-grounding.md)
- [6.4 Multiple presented options](multiple-presented-options.md)

## Further reading

- Guidelines for Human-AI Interaction, Amershi et al., CHI 2019
- People + AI Guidebook, Google PAIR

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
