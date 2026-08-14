# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Agentic UX Patterns: an independent, public pattern library for interfaces where software acts autonomously (like Laws of UX, but for agentic/AI interaction design). 49 patterns across 10 categories, bilingual (EN-US / PT-BR). Owner: Rodrigo Mafra. No build step, no package.json, no test suite, static content only.

**Read `HANDOFF.md` in full before making non-trivial changes.** It has critical constraints not repeated here in full.

## Critical constraint: client detachment

The 49 patterns originated in a paid client engagement (product "Verena," client "Invictus AI") and were deliberately detached and rewritten to stand as independent work. This must hold going forward:

- No client references anywhere: no "Verena," no "Invictus AI," no client screenshots/copy.
- Every example in every pattern must cite a real, public, verifiable product (Claude Code, ChatGPT, Copilot, Devin, Perplexity, Stripe, Grammarly, Notion, etc.), never client work.
- Visual identity must stay independent of the client's brand (dark editorial, serif display type, one accent hue per category from `data/en.json` → `cats[n].hex`). Do not reuse the client's purple/violet "Gemframe" identity.
- If asked to add a client-named example or reuse client visual identity, flag the conflict instead of complying.

## Repository structure

- `index.html`, self-contained bilingual prototype (~150KB, single file, no build step, no external deps except system fonts). Embeds all pattern content as an inline JS object (`const DB = {...}`, currently line 594).
- `data/en.json`, `data/pt-br.json`, the same pattern content as `index.html`'s embedded DB, in JSON form. Shape: `cats` (10 categories, each with `name`, `q`, `hex`) and `patterns` (array of 49, fields `n` number, `t` title, `d` definition, `c` category, `o` overview, `w` why-it-works, `u` when-to-use, `a` when-to-avoid, `e` examples).
- `data/ui-strings.json`, chrome strings (labels, buttons) per language.
- `patterns/*.md`, 49 EN-US markdown files, front-matter (title/slug/number/category/categorySlug/definition/featured) + sections (Overview, Why it works, When to use it, When to avoid it, Examples in the wild, Related patterns, Further reading).
- `patterns/pt-br/*.md`, 49 PT-BR markdown files, same slugs and structure, Hugo/Astro multilingual-ready.

**Design artifacts (craft uplift):**
- `docs/designpowers/briefs/2026-08-13-agentic-ux-lawsofux-uplift.md`, design brief for the Laws-of-UX craft uplift.
- `design-state.md`, principles, decisions log, motif seed notes, artifact index.

**Known duplication**: `index.html`'s embedded DB, `data/*.json`, and the 98 markdown files are three independently maintained copies of the same content. Editing pattern content means editing all copies that apply, there is no single source of truth or generator script yet (see HANDOFF.md §7 for the recommended refactor).

## Style rules (non-negotiable, already applied retroactively across all 98 files)

- No em dash ("—") anywhere, in either language. Use commas, colons, or parentheses instead.
- Concise, direct prose, minimal hedging.
- Pattern section order when extending content: definition (1 sentence) → Overview → Why it works → When to use / avoid (concrete, bulleted) → Examples in the wild (named real products) → Related patterns (cross-links by number) → Further reading (per-category, already defined in `data/*.json`).
- Only the 3 featured patterns (3.2 Human-in-the-loop gates, 5.1 Reasoning glimpse, 6.3 Semantic highlighting of uncertainty) get a "Takeaways" section. Don't add it to the others without being asked.
- PT-BR files are a faithful translation of EN-US, not a localization pass, don't assume PT-BR content has been reviewed for Brazilian market idiom.

## Sanity checks

```sh
# pattern count should be 49 in both languages
grep -c '"n":' data/en.json data/pt-br.json

# em dash check, should return nothing
grep -rl "—" index.html README.md patterns/

# featured patterns should be exactly 3.2, 5.1, 6.3
python3 -c "import json;d=json.load(open('data/en.json'));print([p['n'] for p in d['patterns'] if p.get('f')])"  # expect 3.2, 5.1, 6.3
```

## Running the prototype

Open `index.html` directly in a browser, no server or build step required.
