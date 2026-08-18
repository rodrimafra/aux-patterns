# Handoff — Agentic UX Patterns

**For:** the next LLM (or human) picking up this project
**From:** prior session, prototype phase
**Owner:** Rodrigo Mafra
**Status:** working prototype, content in first draft, not yet published

Read this whole file before touching anything. It tells you what this project is, why it's shaped the way it is, what's actually done versus what looks done, and the constraints you must not violate.

---

## 1. What this project is

**Agentic UX Patterns** is an independent, public reference site: a pattern library for designing interfaces where software acts autonomously, not just interfaces that wait for input. Same genre as [Laws of UX](https://lawsofux.com) by Jon Yablonski, but for agentic/AI interaction design, a niche that currently has no assembled equivalent.

49 named patterns across 10 categories, each with a definition, rationale, usage guidance, and real public-product examples (Claude, ChatGPT, Copilot, Devin, Perplexity, Grammarly, Stripe, etc.).

**Structure modeled on Laws of UX:** a filterable card index plus category hubs where each pattern expands in place, downloadable/citable, CC-licensed.

**The owner's end goal:** turn this into his personal, career-defining public asset (a real deployed site, likely with a companion poster series), not a one-off deliverable.

---

## 2. Critical context: this was extracted from client work

This is the single most important thing to understand before writing or changing content.

The 49 patterns originated as design documentation written during a paid client engagement (an AI product called "Verena," client "Invictus AI," via Toptal). The owner made an explicit, deliberate decision partway through this project: **detach the pattern library from that client relationship** and publish it as independent, standalone work, because:

- The underlying *concepts* (human-in-the-loop gates, reasoning traces, confidence display, etc.) are already public discourse across the AI/design industry. Nobody owns them.
- What *could* be contested is the specific expression/wording written during the paid engagement.
- No assembled library like this exists publicly yet, that's the opportunity.

**As a result, and this must be preserved going forward:**

1. **No client references anywhere.** No "Verena," no "Invictus AI," no screenshots or copy from that product. Every example in every pattern must cite a *public, verifiable product* (Claude Code, ChatGPT, Copilot, Devin, Perplexity, GitHub Actions, Stripe, Grammarly, Zapier, Notion, etc.), not client work.
2. **No shared visual identity with the client.** The client's brand was purple/violet "Gemframe" gemstone identity. This project's identity is a **completely different, independently designed system**: dark editorial, serif display type (Iowan Old Style / Palatino / Georgia stack), one accent hue per category (see `data/en.json` → `cats[n].hex`), no gemstone, no purple-as-primary-brand-color.
3. **All 49 pattern specs were rewritten from scratch** in the owner's own words as an independent work, not copied from the client `.docx` source files. If you are asked to expand or edit patterns, keep writing fresh content, don't reach for client material even if it's referenced elsewhere in this environment.
4. If you encounter any client-named material in your context (e.g., in a file called "Verena — Portfolio Case Study Drafts.md" or similar), **that is a separate, related-but-distinct deliverable** (a design portfolio). Do not merge it into this project or pull client examples from it into this library.

If a future instruction asks you to "add a Verena example" or similar, flag the conflict with the detachment decision rather than silently complying.

---

## 3. License and attribution

- Intended license: **CC BY-NC-ND 4.0** (same model as Laws of UX), non-commercial, no derivatives without permission.
- Attribution: **© Rodrigo Mafra**. Not Invictus AI, not Noord Studio (unless the owner tells you otherwise later).
- The site should eventually credit adjacent prior art honestly (see `data/*.json` → `rd` field, "Further reading" per category): Anthropic's "Building Effective Agents," Google PAIR's "People + AI Guidebook," Microsoft's "Guidelines for Human-AI Interaction" (Amershi et al., CHI 2019) and HAX Toolkit, Ben Shneiderman's Human-Centered AI, Emily Campbell's Shape of AI. **Positioning claim should be "first library focused specifically on agentic interaction patterns," not "first AI UX patterns resource."** Overclaiming primacy against these adjacent efforts would be dishonest and easily fact-checked.

---

## 4. What's actually built (verified working)

```
agentic-ux-patterns/
├── index.html              ← self-contained prototype, open directly in a browser
├── README.md                ← quick structure + migration notes
├── HANDOFF.md                ← this file
├── data/
│   ├── en.json               ← EN-US content, extracted from index.html's embedded DB
│   ├── pt-br.json             ← PT-BR content, same shape
│   └── ui-strings.json         ← chrome strings (labels, buttons) per language
└── patterns/
    ├── *.md                    ← 49 EN-US markdown files, Laws-of-UX-style front-matter + sections
    └── pt-br/
        └── *.md                  ← 49 PT-BR markdown files, same slugs
```

**`index.html`** is a single self-contained file (~145KB), no build step, no external dependencies except system fonts. It embeds all content as a JS object (`const DB = {...}`) so the markdown files and the HTML are currently **two independent copies of the same content**, not generated from one source. If you edit content, you must edit both, or better, refactor to a single source of truth (see §7).

Confirmed working:
- 49 patterns × 10 categories, both languages, card index plus in-page full detail for every pattern on its category hub (not just featured ones)
- 3 featured patterns with a "featured" badge and extra "Takeaways" section: **3.2 Human-in-the-loop gates, 5.1 Reasoning glimpse, 6.3 Semantic highlighting of uncertainty**
- EN-US default, PT-BR via persistent toggle (localStorage), correctly sets `<html lang>`
- Dark/light theme toggle, persisted
- Responsive: fluid type (`clamp()`), container queries, native `<dialog>` for Contact only (becomes a mobile bottom sheet under 640px); pattern detail is a full in-page folio on the hub (no accordion); View Transitions API on filter changes, `prefers-reduced-motion` respected, 44px touch targets, safe-area insets, `dvh` units
- Live search + category filter chips (horizontally scrollable with snap on mobile)
- Zero em dashes anywhere in the copy (owner's explicit style rule, see §6)
- Validated: HTML tag balance checked, embedded JSON parses cleanly, both language pattern counts confirmed at 49
- Category teaching stills: ten 224 squares drawn in Figma (file `g81CTKZNVjYAqhjdVEPji4`, frame `categories` 28:353), on disk at `assets/illustrations/categories/cat-{1..10}.svg` and inlined in `index.html` as `ILLUS`. Do not overwrite them with `tools/illustrations/generate.py` (that script is the superseded 320x200 probe).

## 5. What's NOT done yet, ranked by what the owner has asked for next

**Phase B (2026-08-14):** 49 pattern stills are in the prototype (`PAT` in `index.html`, `assets/illustrations/patterns/`). Category parents stay Figma. Resume notes: `docs/designpowers/handoff/2026-08-13-illustration-checkpoint.md`.

1. **Per-pattern posters** — the owner asked for this right before requesting this handoff, then paused to get a portable package instead. A taxonomy overview poster already exists as a separate deliverable (`Portfolio Assets/agentic-ux-patterns-taxonomy.svg` in the Verena client folder, built with the CLIENT's Gemframe colors, do NOT reuse those colors here, this project needs its own poster identity using the category hex colors in `data/en.json`). Next step: generate 49 individual pattern posters (one per pattern, this project's dark/serif/category-hue identity) plus a new taxonomy overview poster in the *independent* identity, since the existing one is client-branded and can't be reused as-is.
2. **Content review pass** — all 98 pattern files (49 EN + 49 PT-BR) are first drafts, written by the AI, never reviewed by the owner for voice, accuracy, or whether the public-product examples still hold up. Do not treat this content as final or launch-ready. PT-BR is a faithful translation, not a Brazilian-market localization pass.
3. **Single source of truth refactor** — currently `index.html`'s embedded JS object and the 98 markdown files are separately maintained copies of the same content (the markdown was generated first, then the HTML was built from the same Python data structure, then translated, then edited for em dashes independently in both places). This works today but will drift if either is hand-edited without the other. See §7 for the recommended fix.
4. **Real site migration** — Astro (recommended) or Hugo. Not started. See README.md in the package for the intended approach.
5. **Domain, hosting, analytics, /about page** — not discussed in depth. The owner has not chosen a domain name yet.
6. **Legal check** — the owner should have someone review the Toptal engagement's IP-assignment clause before public launch, to confirm the detachment (§2) is clean. Not your job to do, but don't let it get forgotten if you're producing a launch checklist.

## 6. Style rules the owner has explicitly set (follow these without being asked again)

- **No em dashes, anywhere, in any language.** Use commas, colons, or parentheses instead. This was a specific, deliberate instruction, applied retroactively to fix all 98 existing files. If you generate new content, don't introduce em dashes in the first place.
- **Concise, direct prose.** The owner's global preference (see system-level instructions if visible to you) is minimal padding, no unnecessary hedging.
- Pattern writing pattern to match, if extending content: definition (1 sentence) → Overview (what it is, framed as a problem/solution) → Why it works (the mechanism, in human/psychological terms) → When to use / avoid (bulleted, concrete conditions, not generic advice) → Examples in the wild (named real products, specific features, not vague categories) → Related patterns (cross-links by number) → Further reading (per-category citation list, already defined in `data/*.json`).
- Featured patterns additionally get a "Takeaways" section: 3-4 short, actionable, memorable bullets. Only the 3 featured patterns have this; don't add it to all 49 without being asked.

## 7. Recommended next technical step (if not doing posters first)

Refactor to single-source content:
1. Treat `data/en.json` and `data/pt-br.json` as the canonical source (they're already extracted and clean).
2. Regenerate both `index.html`'s embedded DB and the 98 markdown files from these JSON files via a build script, rather than hand-editing three places independently.
3. This is exactly what the original build scripts did (Python, generating markdown + HTML + JSON from one in-memory data structure), but those scripts were transient and not saved as reusable files. If you need the pattern content restructured, rebuilding a small Python or Node build script from `data/*.json` is faster and safer than manually editing 100 files.

## 8. Quick sanity checks for whoever picks this up

Run these before trusting the package:
```
# pattern count should be 49 in both languages
grep -c '"n":' data/en.json data/pt-br.json   # or equivalent JSON tooling

# em dash check, should return nothing
grep -rl "—" index.html README.md patterns/

# featured patterns should be exactly these three numbers
grep -l '"f": true' data/en.json   # inspect manually, should be 3.2, 5.1, 6.3
```

## 9. Who to ask if something is ambiguous

The owner is **Rodrigo Mafra**, Director of Design at Noord Studio, doing this as personal/independent work (separate from his Noord Studio and Invictus AI client engagements). If a decision genuinely can't be inferred from this document or the code, don't guess on anything touching: licensing, client-boundary questions (§2), or brand identity changes. Ask.
