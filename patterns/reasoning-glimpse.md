---
title: "Reasoning glimpse"
slug: "reasoning-glimpse"
number: "5.1"
category: "Transparency of Process"
categorySlug: "transparency-of-process"
definition: "A brief, honest window into what the agent is doing and why, enough to establish real work, without exposing the machinery."
featured: true
---

# Reasoning glimpse

> A brief, honest window into what the agent is doing and why, enough to establish real work, without exposing the machinery.

## Overview

An agent that goes silent and returns an answer asks for blind faith. An agent that narrates every internal step is exhausting, and usually theatre. The reasoning glimpse sits deliberately between: short, task-specific status lines that tell the user what kind of work is happening ('Reading the contract… extracting payment terms… checking dates') and summarised reasoning available at a glance. The test of honesty is specificity: cues generated from the actual work read as reporting; generic cues read as a spinner in costume.

## Why it works

Perceived competence tracks visible process. People trust outcomes more when they witness credible effort, but only if the display is truthful; decorative 'thinking' animations erode trust the first time they are caught lying.

## When to use it

- Tasks longer than a few seconds, where silence reads as failure
- Complex analysis whose value users cannot judge from the answer alone
- Building early trust in a new agent relationship

## When to avoid it

- Faking process signals that do not correspond to real work
- Streaming raw chain-of-thought that overwhelms more than it informs

## Examples in the wild

- Summarised thinking in reasoning models (OpenAI o-series, Claude's extended thinking)
- Perplexity's live step display: searching, reading sources, composing
- Tool-call narration in agentic IDEs (searching codebase, running tests)

## Takeaways

- Make cues task-specific, generated from real work, never canned
- Show the kind of work, not the full transcript
- Match cue granularity to task length and stakes
- Honesty is the constraint: a glimpse that lies is worse than silence

## Related patterns

- [5.3 Tool usage indicators](tool-usage-indicators.md)
- [5.5 Execution progress view](execution-progress-view.md)
- [6.5 Explanation on demand](explanation-on-demand.md)

## Further reading

- Building Effective Agents (Anthropic
- Shape of AI) Emily Campbell

---
*Agentic UX Patterns · CC BY-NC-ND 4.0*
