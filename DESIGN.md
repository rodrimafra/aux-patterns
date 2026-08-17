---
name: Agentic UX Patterns
description: Dark editorial pattern library. Night Reference Desk, museum-wall stills, serif as citation voice.
colors:
  night-paper: "#0e0f12"
  night-raised: "#15161b"
  night-card: "#1a1b21"
  night-line: "#2a2c34"
  gallery-cream: "#f2f1ee"
  gallery-cream-muted: "#c4c2bb"
  gallery-stone: "#b9b7b0"
  gallery-stone-deep: "#8e8c85"
  light-paper: "#faf9f6"
  light-raised: "#f1efe9"
  light-card: "#ffffff"
  light-line: "#e3e0d6"
  light-ink: "#17181c"
  light-ink-muted: "#3f3e3a"
  light-ink-faint: "#6f6d66"
  cat-field-cream: "#f2eee2"
  cat-1: "#f59e0b"
  cat-2: "#34d399"
  cat-3: "#f87171"
  cat-4: "#f472b6"
  cat-5: "#38bdf8"
  cat-6: "#a3e635"
  cat-7: "#a78bfa"
  cat-8: "#22d3ee"
  cat-9: "#fb923c"
  cat-10: "#818cf8"
typography:
  display:
    fontFamily: "Iowan Old Style, Palatino Linotype, Palatino, Georgia, serif"
    fontSize: "clamp(2.441rem, 7vw, 4.5rem)"
    fontWeight: 600
    lineHeight: 1.04
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "Iowan Old Style, Palatino Linotype, Palatino, Georgia, serif"
    fontSize: "clamp(1.25rem, 2.6vw, 1.563rem)"
    fontWeight: 600
    lineHeight: 1.2
  title:
    fontFamily: "Iowan Old Style, Palatino Linotype, Palatino, Georgia, serif"
    fontSize: "clamp(1.953rem, 5.5vw, 3.052rem)"
    fontWeight: 600
    lineHeight: 1.12
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "0.78125rem"
    fontWeight: 600
    lineHeight: 1.35
    letterSpacing: "0.13em"
  card-body:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "14.5px"
    fontWeight: 400
  blurb:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "13.5px"
    fontWeight: 400
  feat:
    fontFamily: "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Helvetica Neue, Arial, sans-serif"
    fontSize: "10.5px"
    fontWeight: 700
  definition:
    fontFamily: "Iowan Old Style, Palatino Linotype, Palatino, Georgia, serif"
    fontSize: "clamp(16.5px, 2.6vw, 19px)"
    fontWeight: 400
rounded:
  rail: "6px"
  sm: "8px"
  md: "12px"
  take: "14px"
  lg: "16px"
  xl: "22px"
  sheet-mobile: "24px"
  pill: "999px"
  full: "50%"
spacing:
  s0: "4px"
  s1: "8px"
  s2: "16px"
  s3: "24px"
  s4: "32px"
  s5: "40px"
  s6: "48px"
  s7: "64px"
  s8: "80px"
components:
  button-chrome:
    backgroundColor: "{colors.night-raised}"
    textColor: "{colors.gallery-cream-muted}"
    rounded: "{rounded.pill}"
    padding: "8px 14px"
    height: "40px"
  button-chrome-on:
    backgroundColor: "{colors.gallery-cream}"
    textColor: "{colors.night-paper}"
    rounded: "{rounded.pill}"
    padding: "8px 14px"
    height: "40px"
  button-icon:
    backgroundColor: "{colors.night-raised}"
    textColor: "{colors.gallery-cream-muted}"
    rounded: "{rounded.full}"
    size: "42px"
  input-search:
    backgroundColor: "{colors.night-raised}"
    textColor: "{colors.gallery-cream}"
    rounded: "{rounded.md}"
    padding: "12px 16px 12px 42px"
    height: "44px"
  card-pattern:
    backgroundColor: "{colors.night-card}"
    textColor: "{colors.gallery-cream}"
    rounded: "{rounded.lg}"
    padding: "0"
  chip-related:
    backgroundColor: "transparent"
    textColor: "{colors.gallery-cream-muted}"
    rounded: "{rounded.pill}"
    padding: "8px 14px"
    height: "38px"
  badge-featured:
    backgroundColor: "{colors.gallery-stone}"
    textColor: "{colors.night-paper}"
    rounded: "{rounded.pill}"
    padding: "3px 9px"
---

# Design System: Agentic UX Patterns

## Overview

**Creative North Star: "The Night Reference Desk"**

This is a public pattern library that should feel like a night reading room, not a SaaS dashboard. The visitor arrives to scan ten jobs, then lean into one exhibit: a teaching still, a serif title, a definition. Chrome recedes to museum caption. The still and the citation voice are the artifact.

Density is wall-like: large stills, sparse controls, type as captions. An 8px rhythm (`--s0` through `--s8`) keeps the wall from collapsing into a product grid. Default rest accent is Gallery Stone (`#b9b7b0`). Category hues live in content data and may sit together on the home wall. They are not a single brand primary.

Confirmed visual rejections: no Gemframe purple as identity, no client gemstone language, no Laws of UX clone (qualities only: whitespace, type scale, filterable index, signature visual).

**Key Characteristics:**
- Dark editorial first; light theme is the same desk with the lamp on.
- Serif display (Iowan / Palatino / Georgia) for titles; system sans for chrome and body.
- Teaching stills (224 squares on cards, 16:9 motif in detail) carry color and meaning.
- Hairline 1px borders in the shipped prototype; ambient shadows are the locked direction for future surfaces.
- Bilingual EN-US / PT-BR and `prefers-reduced-motion` are part of the visual contract, not extras.

## Colors

Night Paper desk, Gallery Cream ink, Gallery Stone rest chrome. Category hues are a ten-color atlas, not a logo.

### Primary
- **Gallery Stone** (`{colors.gallery-stone}`): rest-state `--accent` when no category is selected. Featured pills, quiet marks. Light theme mixes this 58% into `{colors.light-ink}` for `--accent-ink` so accent text holds contrast.

### Neutral
- **Night Paper** (`{colors.night-paper}`): dark page ground (`--bg`).
- **Night Raised** (`{colors.night-raised}`): topbar buttons, search field, detail sheet (`--bg2`).
- **Night Card** (`{colors.night-card}`): pattern cards and takeaway wells (`--card`).
- **Night Line** (`{colors.night-line}`): 1px hairlines (`--line`).
- **Gallery Cream** (`{colors.gallery-cream}`): dark primary ink (`--ink`).
- **Gallery Cream Muted** (`{colors.gallery-cream-muted}`): secondary reading (`--ink2`).
- **Gallery Stone Deep** (`{colors.gallery-stone-deep}`): tertiary captions (`--ink3`).
- **Light Paper / Raised / Card / Line / Ink** (`{colors.light-paper}` … `{colors.light-ink-faint}`): lamp-on theme. Same roles, inverted values.
- **Cat Field Cream** (`{colors.cat-field-cream}`): ink on category-tinted hero when a hub is active (`#f2eee2`), not Gallery Cream.

### Tertiary
Category atlas (data `cats[n].hex`, also `--accent` on a scoped surface):

- **Cat 1 Identity** `{colors.cat-1}` through **Cat 10 Ethics** `{colors.cat-10}`.

Cats 7 and 10 may use violet/indigo on a mark. They must not become the site’s brand canvas.

**The Atlas Wall Rule.** Home may show all ten hues at once. Do not force a single active hue onto the whole chrome unless a category hub is actually selected.

**The Independence Rule.** Never introduce purple or violet as a global brand color. Cats 7/10 stay local to those jobs.

## Typography

**Display Font:** Iowan Old Style (Palatino Linotype, Palatino, Georgia)
**Body Font:** system UI sans (`-apple-system`, Segoe UI, Roboto, Helvetica Neue, Arial)
**Label/Mono Font:** same sans, small caps tracking (no separate mono)

**Character:** Serif is the citation. Sans is the caption rail. Pairing should read as a reference desk, not a startup landing.

### Hierarchy
- **Display** (600, `clamp(2.441rem, 7vw, 4.5rem)`, 1.04, tracking `-0.015em`): site title on the landing hero.
- **Title** (600, `clamp(1.953rem, 5.5vw, 3.052rem)`, 1.12): pattern name in the detail sheet.
- **Headline** (600, `clamp(1.25rem, 2.6vw, 1.563rem)`, 1.2): card titles and hub pattern names.
- **Body** (400, `1rem` / `15.5px`–`16px` in sheets, 1.55): definitions and section copy. Sub and lead stay under ~36–40rem.
- **Label** (600–700, ~10.5–12.5px, tracking `0.12em`–`0.18em`, uppercase): category kicker, featured badge, section headers in the sheet (`h3`).

Scale ratio `--ratio: 1.25` (`--t-xs` … `--t-4xl`).

**The Caption Voice Rule.** Uppercase tracking labels never compete with serif titles. If a control needs a name, keep it sans and quiet.

## Layout

Container `--wrap` max 1200px, inline pad `--sp` (`clamp(16px, 4vw, 32px)`). Index grid: `auto-fill`, min `min(320px, 100%)`, gap `--s2`. Category hub reading column max 48rem with a sticky section rail (`minmax(168px, 220px)` + column + leftover); rail stacks under 800px.

Breakpoints in the shipped CSS: 720px (category hero), 800px (rail), 640px (detail becomes bottom sheet), 560px (hub thumb), container 480px (category question cue).

Touch: chrome controls 40px+; search 44px; icon buttons 42px. Safe-area insets on topbar and footer.

**The Eight-Point Rule.** Spacing comes from `--s0`–`--s8` (4px … 80px). One-off padding (22px, 14px) is allowed on type measure, not as a second scale.

## Elevation & Depth

Shipped prototype is tonal and hairline: `--bg` / `--bg2` / `--card` / `--line`. Cards lift `translateY(-3px)` on hover. Detail overlay: backdrop `rgba(10, 10, 13, .66)` plus `blur(6px)`. No card `box-shadow` in current CSS.

**The Ambient Lift Rule.** Ambient shadows are a first-class language going forward. Do not keep inventing more hairlines as a substitute. Exact shadow tokens are unresolved until a polish pass writes them; until then, do not fake a Material elevation ramp.

## Shapes

Soft museum objects, not sharp tools. Cards 16px. Search 12px. Detail sheet 22px (24px 24px 0 0 as a bottom sheet under 640px). Pills 999px for chrome buttons, featured badge, related links. Icon buttons full circle. Teaching plates are square or 16:9 crops of the still, not rounded picture frames on the motif itself.

Hairline 1px `{colors.night-line}` / `{colors.light-line}`. Focus-visible: no glow ring on most chrome; shift to stronger ink and line. Next-category link uses a 2px outline offset 4px.

**The Still Is Square Rule.** Category teaching art is a 224×224 exhibit on a field (`--illu-field`). Do not restyle the SVG into a decorative blob or gemstone.

## Components

Chrome is caption. The still and the serif title are the exhibit.

### Buttons
- **Shape:** pill (`999px`) for text chrome; circle (`50%`) for icon-only.
- **Primary chrome (`.tbtn`):** raised fill, hairline, `--ink2` label, min-height 40px, pad `--s1` / 14px. On: invert to ink on paper.
- **Hover / Focus:** ink up, line to `--ink3`. No outline.
- **Icon (`.icon-btn`):** 42px, 88% raised mix, 6px blur, hairline.

Stroke icons: 18px (16px `.sm`), stroke 1.5, round caps, `currentColor`.

### Chips
- **Related (`.rel button`):** ghost pill, hairline, transparent fill, 13.5px, min-height 38px.
- **Featured:** Gallery Stone fill, 10.5px, tracking `0.14em`, 999px. Light theme: `{colors.light-ink}` on the pill, never cream on cream. Lives in `.body`, never on the teaching band.

### Cards / Containers
- **Corner Style:** 16px
- **Background:** `{colors.night-card}` / `{colors.light-card}`, 1px line
- **Shadow Strategy:** none in the prototype; Ambient Lift Rule for new work
- **Band:** 260px teaching field, 224 SVG
- **Internal Padding:** `--s3` / 22px in `.body`
- **Hover:** lift 3px, line to `--ink3`
- Takeaway well: 14px radius, card fill, 18px 20px pad

### Inputs / Fields
- **Style:** raised fill, 12px radius, 1px line, 16px text (no iOS zoom), icon inset 14px
- **Focus:** line to `--ink3`
- **Error / Disabled:** not in the prototype; do not invent

### Navigation
Sticky filter strip: gradient fade of page ground. Hub section rail: 13px links, 2px left rule when `.on`. Mobile: wrap pills, 8px radius, raised fill.

### Pattern detail sheet
Native `<dialog>`. Sheet max 760px, 22px radius, raised ground. Motif 16:9, max-height 280px. Body type 16px; list rows hairline-separated with a Gallery Stone comma mark. Under 640px: bottom sheet, min-height 60dvh. `@starting-style` enter 24px; killed under `prefers-reduced-motion`.

## Do's and Don'ts

### Do:
- **Do** set `--accent` from `cats[n].hex` on the active card, hub, or sheet only.
- **Do** keep display type on the Iowan / Palatino / Georgia stack; never web-font the prototype without an explicit stack change.
- **Do** put featured badges in the caption body, not on the teaching still.
- **Do** respect `prefers-reduced-motion` by dropping transition and animation.
- **Do** treat light theme as the same identity: mix accent into `{colors.light-ink}` for readable `--accent-ink`.

### Don't:
- **Don't** use purple/violet as a global brand or canvas (Gemframe anti-reference). Cats 7/10 marks only.
- **Don't** clone Laws of UX layout, icons, or type as a visual twin.
- **Don't** add Takeaways chrome to patterns other than 3.2, 5.1, and 6.3.
- **Don't** document or ship em dashes in UI copy.
- **Don't** invent a second spacing scale or a fake shadow ramp before the Ambient Lift tokens exist.
