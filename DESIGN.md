---
name: Omena CV
description: A restrained blue-and-white Traditional Chinese CV based on moderncv banking.
colors:
  accent: "#245b85"
  accent-hover: "#173f5f"
  ink: "#232d37"
  muted: "#53616c"
  rule: "#b7ccdc"
  paper: "#fff"
  canvas: "#edf1f4"
  divider: "#dce4eb"
  selection-bg: "#d5e5f2"
  selection-ink: "#143c5c"
typography:
  body:
    fontFamily: "Microsoft JhengHei, PingFang TC, Noto Sans TC, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.7
  headline:
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.4
  title:
    fontSize: "15px"
    fontWeight: 700
    lineHeight: 1.55
  label:
    fontSize: "12px"
    fontWeight: 400
    lineHeight: 1.7
  metadata:
    fontSize: "13px"
    fontWeight: 400
    lineHeight: 1.7
rounded:
  button: "4px"
spacing:
  small: "4px"
  section-gap: "12px"
  heading-gap: "14px"
  entry-gap: "16px"
  group-gap: "20px"
  navigation-gap: "24px"
components:
  download:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.paper}"
    rounded: "{rounded.button}"
    padding: "9px 18px"
  download-hover:
    backgroundColor: "{colors.accent-hover}"
    textColor: "{colors.paper}"
  sheet:
    backgroundColor: "{colors.paper}"
    padding: "48px 66px 28px"
  section-heading:
    textColor: "{colors.accent}"
    typography: "{typography.headline}"
  entry-title:
    textColor: "{colors.ink}"
    typography: "{typography.title}"
  period:
    textColor: "{colors.muted}"
    typography: "{typography.label}"
---

# Design System: Omena CV

## Overview

**Creative North Star: "Moderncv Banking Document"**

A restrained moderncv banking adaptation for a Traditional Chinese CV. Blue headings, white paper, centered identity and fine horizontal rules establish a professional document rhythm.

The screen presentation retains the printed document structure while mobile reading becomes a continuous column. Typography and alignment carry the hierarchy; no shipping raster imagery is used.

**Key Characteristics:**
- Single-column document structure
- Blue section titles with trailing rules
- Continuous mobile reading and explicit A4 pagination

## Colors

A quiet blue accent anchors cool neutral paper and text.

### Primary

- **Document Blue** (`accent`): identity, section headings, text links and the PDF action.
- **Deep Blue** (`accent-hover`): interactive hover state.

### Neutral

- **Ink** (`ink`): primary reading text.
- **Slate** (`muted`): dates, supporting metadata and footers.
- **Blue Rule** (`rule`): identity separator, section rules and continuation header.
- **Paper** (`paper`) and **Canvas** (`canvas`): document and surrounding desktop surface.
- **Quiet Divider** (`divider`): footers and mobile navigation boundary.
- **Selection Blue** (`selection-bg`, `selection-ink`): selected text contrast.

**The Document Blue Rule.** Use blue to identify headings and actions; keep reading paragraphs in ink.

## Typography

**Body Font:** Microsoft JhengHei, PingFang TC, Noto Sans TC, sans-serif. The installed Traditional Chinese font stack supplies readable document text without remote font loading.

The section, title, body and metadata tokens describe a compact, purpose-led hierarchy. Dates use tabular numbers and stay on one line. The identity currently renders at 34px/1.25 with bold Chinese name and regular Latin name; its native system display face is an implementation exception, not a reusable display-font prescription.

On mobile the section headings become 21px, entry titles 16px, organization text 14px and body leading 1.8. The identity becomes 31px. Print uses a 10pt body with 1.55 leading, 27pt identity, 14pt sections, 10.5pt entry titles, and 8-9pt metadata.

## Layout

The toolbar and sheets share a 940px maximum width. Desktop sheets have generous inset padding and a 30px inter-sheet gap. At 980px and below, sheets use 24px outside margins and 42px horizontal padding.

At 600px and below, the canvas becomes paper, sheet margins disappear, horizontal inset becomes 22px, and entries stack their dates beneath titles. Navigation wraps into a full-width row; section links have a 44px minimum height. Page-number footers and the continuation header disappear so the two sheets read as one column.

Print uses A4 with zero page margins and two explicitly sized 210mm by 297mm sheets, each padded 14mm 17mm 12mm. Each sheet breaks after itself except the last. Entry and education blocks avoid internal breaks; flex layout pushes page footers to the bottom. Toolbar, site footer and skip link are hidden in print. Content growth requires checking the two-page result again.

## Elevation & Depth

A single ambient sheet shadow (`0 5px 24px rgb(23 48 66 / 7%)`) separates white paper from the desktop canvas. Mobile and print remove it. Interior sections remain flat; thin rules provide structure.

**The Paper Depth Rule.** Reserve elevation for the desktop sheet boundary.

## Shapes

Sheets and content blocks are rectangular. Only the filled download action uses the small button radius. Section rules and document separators are 1px; they are native to this document style.

## Components

### Download action

A compact filled blue link uses bold 14px text, white lettering and the button radius. Hover deepens the fill; mobile horizontal padding reduces to 12px. The link downloads the shared two-page PDF.

### Navigation and text links

The toolbar combines a bold ink wordmark with underlined section links and the download action. Text links deepen on hover; contact links add underlining on hover. Every link uses a 3px accent focus outline offset by 5px. A focus-revealed skip link precedes navigation. No transitions or animated scrolling are defined.

### Section heading

A blue heading and a flexible trailing rule share a baseline-height row with the heading gap. Preserve readable text before the rule.

### CV entry

A bold title and muted date share a baseline-aligned row with space between. Supporting organization text precedes a compact bullet list. Mobile stacks the title and date; print restores the row. Project entries add technology metadata and a small source link aligned to the list inset.

### Sheet and continuation

The desktop document surface carries centered identity, section content and a quiet numbered footer. A small continuation row identifies the second sheet. Print preserves both page footers; mobile removes the pagination furniture.

## Do's and Don'ts

### Do:

- **Do** preserve readable Traditional Chinese text and aligned date metadata.
- **Do** keep section navigation and the PDF download available on mobile.
- **Do** verify two A4 pages after content or print-style changes.
- **Do** preserve visible keyboard focus on every link.

### Don't:

- **Don't** replace the document hierarchy with a promotional hero or project gallery.
- **Don't** introduce decorative cards into the CV entries.
- **Don't** treat desktop sheet shadows as a mobile or print requirement.
