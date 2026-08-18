# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary users are product designers and PMs making agentic UI decisions: they open a public pattern library, scan categories, then read a named pattern (definition, rationale, when to use or avoid, public-product examples) to decide how an autonomous interface should behave.

Other audiences exist (researchers and writers citing definitions) but are not the design center.

## Product Purpose

Agentic UX Patterns is an independent public reference for interfaces where software acts autonomously, not only interfaces that wait for input. Same genre as Laws of UX, scoped to agentic and AI interaction design.

Success: a real public site people treat as the go-to library for agentic UX patterns.

## Positioning

First library focused specifically on agentic interaction patterns. Not "first AI UX patterns resource." Adjacent prior art must stay credited: Anthropic Building Effective Agents, Google PAIR People + AI Guidebook, Microsoft Guidelines for Human-AI Interaction and HAX Toolkit, Shneiderman Human-Centered AI, Emily Campbell Shape of AI.

Owner: Rodrigo Mafra. Independent work, not a client deliverable.

## Operating Context

Current surface is a self-contained bilingual prototype: open `index.html` in a browser, no server or build required. Users filter by category, search, then read full patterns on the category hub (rail or title scrolls to a named pattern). Contact stays a dialog. Toggle EN-US / PT-BR and dark / light (both persisted). Deep-link via hash, share a copy-link.

Content lives in three copies until a later refactor: `index.html` embedded DB, `data/*.json`, and `patterns/` markdown (EN-US plus `patterns/pt-br/`).

## Capabilities and Constraints

- 49 named patterns across 10 categories. Featured patterns only: 3.2 Human-in-the-loop gates, 5.1 Reasoning glimpse, 6.3 Semantic highlighting of uncertainty (those three get Takeaways; do not add Takeaways to the rest unless asked).
- Client detachment is binding: no client product name, no client company name, no client screenshots or copy. Every example cites a real public verifiable product.
- Visual identity must stay independent of the former client's purple/violet Gemframe system. Category accent hues come from `data/en.json` `cats[n].hex`.
- No em dash character in any language. Use commas, colons, or parentheses.
- EN-US default. PT-BR is a faithful translation, not a Brazilian-market localization pass. Pattern copy is first draft until the owner reviews it.
- Intended license: CC BY-NC-ND 4.0. Attribution: © Rodrigo Mafra.
- Domain, hosting, analytics, and /about are undecided.
- Astro or Hugo migration is intended later; not started. Do not treat the single-file prototype as a forever stack unless the owner says so.
- Legal review of the originating engagement's IP-assignment clause before public launch is the owner's job, not a cleared product fact.

## Brand Commitments

Name: Agentic UX Patterns. Voice: concise, direct, minimal hedging. Pattern section order is definition, Overview, Why it works, When to use, When to avoid, Examples in the wild, Related patterns, Further reading.

## Evidence on Hand

- Working prototype: `index.html`
- Canonical-ish content: `data/en.json`, `data/pt-br.json`, `data/ui-strings.json`
- Pattern markdown: `patterns/*.md`, `patterns/pt-br/*.md`
- Constraints and status: `HANDOFF.md`, `README.md`, `CLAUDE.md`
- Craft brief: `docs/designpowers/briefs/2026-08-13-agentic-ux-lawsofux-uplift.md`
- Category stills: `assets/illustrations/categories/`; pattern stills: `assets/illustrations/patterns/`

Do not fabricate testimonials, traffic, launch dates, domain names, or client case studies. Do not reuse the client-branded taxonomy poster.

## Product Principles

1. Practitioners can find a named pattern fast and leave with a decision, not a manifesto.
2. Independence is non-negotiable: public examples, independent identity, owner attribution.
3. Honesty over primacy: credit adjacent AI UX work; claim only the agentic-pattern-library gap.
4. Bilingual access without pretending PT-BR is localized.
5. Accessibility is part of the product: keyboard, screen reader, reduced motion, light and dark, AA-usable contrast.

## Accessibility & Inclusion

Required: keyboard and screen-reader use, `prefers-reduced-motion`, light and dark themes, touch targets, bilingual `lang`, WCAG AA contrast for ink on both themes.
