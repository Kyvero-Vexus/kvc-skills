---
name: clim-spec
description: "Use when implementing, debugging, designing, or reviewing Common Lisp Interface Manager (CLIM 2) or McCLIM code. Routes work to the right CLIM chapters, requires spec lookup before answering, and distinguishes normative spec text from implementation-specific behavior."
compatibility: Designed for Claude Code / Codex / OpenClaw workflows with a local mirrored CLIM 2 HTML corpus and a lookup helper script.
metadata:
  openclaw:
    emoji: "🪟"
---

# CLIM Spec Skill

Use this skill when work touches **CLIM 2 semantics**: application frames, panes, gadgets, presentations, command processing, extended streams, output records, incremental redisplay, drawing, sheets, mediums, ports, grafts, or CLIM stream protocols.

This skill turns the CLIM 2 spec from “big pile of HTML” into a usable workflow.

## Canonical local corpus

Local mirror root:
- `/home/slime/projects/kvc-skills/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec`

Primary entry points:
- `index.html` — spec home
- `contents.html` — full table of contents
- `theindex.html` — index / term lookup
- `F.html` — changes from CLIM 1.0
- `B.html` — CLIM-SYS appendix
- `C.html` — encapsulating streams appendix
- `D.html` — Common Lisp streams appendix

Helper:
- `python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --toc`
- `python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame"`

## Hard rules

1. **Search the spec before answering from memory.**
2. **Treat the mirrored HTML body as normative, not the annotations.**
   - The mirror includes annotation links and an annotation playground.
   - Inline comments / notes / playground material are not normative CLIM 2 requirements.
3. **Separate CLIM 2 spec facts from McCLIM behavior.**
   - If the question is about McCLIM specifically, answer with two layers:
     - what CLIM 2 specifies,
     - what McCLIM appears to implement or extend.
4. **Cite the local source paths you used.**
5. **When the spec is silent, say it is silent.** Do not fabricate rules.

---

## When to use this skill

Use it for any of these:
- “How does CLIM do X?”
- “Which chapter covers presentations / panes / frames / gadgets?”
- implementing or debugging McCLIM / CLIM UI code
- designing a new CLIM application architecture
- writing compatibility code against CLIM 2 semantics
- reviewing whether code matches the CLIM 2 specification
- porting old CLIM 1.x code
- building custom sheet / stream / pane / gadget protocol implementations

Do **not** use it for:
- unrelated GUI toolkits with no CLIM angle
- generic Common Lisp questions unless CLIM behavior is in scope

---

## Routing map: where to look first

### Geometry substrate
Use these when geometry, hit detection, clipping, bounds, or transforms are involved.

- **Chapter 3** — Regions
- **Chapter 4** — Bounding Rectangles
- **Chapter 5** — Affine Transformations

Typical tasks:
- geometric containment
- region composition
- coordinate transforms
- bounding boxes for panes or output records

### Windowing substrate
Use these when working with sheets, repaint, events, ports, or mirrors.

- **Chapter 6** — Overview of Window Facilities
- **Chapter 7** — Properties of Sheets
- **Chapter 8** — Sheet Protocols
- **Chapter 9** — Ports, Grafts, and Mirrored Sheets

Typical tasks:
- sheet hierarchy questions
- move/resize semantics
- repaint lifecycle
- medium attachment
- event dispatch / pointer / keyboard device flow
- backend/window-server integration

### Drawing and medium output
Use these when drawing, styling, inks, patterns, or graphics behavior are involved.

- **Chapter 10** — Drawing Options
- **Chapter 11** — Text Styles
- **Chapter 12** — Graphics
- **Chapter 13** — Drawing in Color
- **Chapter 14** — General Designs

Typical tasks:
- line styles, inks, text styles
- coordinate-system binding forms
- drawing primitives and pixmaps
- colors, opacity, compositing, patterns, stencils

### Output streams and redisplay
Use these for stream panes, output recording, formatting, and efficient redisplay.

- **Chapter 15** — Extended Stream Output
- **Chapter 16** — Output Recording
- **Chapter 17** — Table Formatting
- **Chapter 18** — Graph Formatting
- **Chapter 19** — Bordered Output
- **Chapter 20** — Text Formatting
- **Chapter 21** — Incremental Redisplay

Typical tasks:
- stream cursor / buffering behavior
- output record classes / traversal / mutation
- structured layout helpers
- incremental update performance
- redisplay protocol design

### Input, presentations, and completion
Use these for interactive CLIM behavior.

- **Chapter 22** — Extended Stream Input
- **Chapter 23** — Presentation Types
- **Chapter 24** — Input Editing and Completion Facilities
- **Chapter 25** — Menu Facilities
- **Chapter 26** — Dialog Facilities

Typical tasks:
- gesture handling
- pointer tracking
- typed input/output
- presentation translators
- completion / activation gestures
- input editor behavior

### Application construction
Use these for real apps.

- **Chapter 27** — Command Processing
- **Chapter 28** — Application Frames
- **Chapter 29** — Panes
- **Chapter 30** — Gadgets

Typical tasks:
- command tables and accelerators
- frame definitions and top-level loops
- pane layouts and stream panes
- gadgets/widgets and their integration

### Appendices worth using deliberately

- **Appendix B** — `CLIM-SYS` package, resources, multiprocessing, locks
- **Appendix C** — encapsulating streams
- **Appendix D** — Common Lisp stream interop
- **Appendix E** — suggested extensions, useful but non-core
- **Appendix F** — CLIM 1.0 → CLIM 2 changes

---

## Fast recipes by task type

### 1) “Build or fix an application frame”
Start here:
- `28.html`
- `28-2.html` — defining and creating application frames
- `28-4.html` — generic command loop
- `29.html` — panes
- `27.html` — command processing

Then check presentations if commands use typed interaction:
- `23.html`
- `23-7.html` — presentation translators

### 2) “Design a pane layout or custom pane”
Start here:
- `29-2.html` — basic pane construction
- `29-3.html` — composite and layout panes
- `29-4.html` — CLIM stream panes
- `29-5.html` — defining new pane types

Backfill substrate details from:
- `7.html` / `8.html` / `9.html`

### 3) “Implement typed interaction / clickable objects / contextual commands”
Start here:
- `23.html` — presentation types
- `23-2.html` — presentations
- `23-4.html` — typed output
- `23-5.html` — context-dependent typed input
- `23-7.html` — presentation translators
- `27-5.html` — presentation translator utilities

Also inspect:
- `24.html` — input editing and completion

### 4) “Debug redisplay or stale UI behavior”
Start here:
- `16.html` — output recording
- `21.html` — incremental redisplay
- `29-4.html` — CLIM stream panes

Focus on:
- output record identity,
- record update protocol,
- what triggers redisplay,
- whether the pane/stream actually records output.

### 5) “Implement drawing behavior or a rendering backend”
Start here:
- `10.html` — drawing options
- `12.html` — graphics
- `13.html` — color
- `14.html` — designs
- `8-3.html` — output protocol / medium association
- `9-4.html` — mirrors and mirrored sheets

Also use:
- `3.html`, `4.html`, `5.html` for geometry/transform semantics.

### 6) “Work on CLIM streams or wrap streams”
Start here:
- `15.html` — extended output
- `22.html` — extended input
- `C.html` / `C-1.html` — encapsulating streams
- `D.html` — Common Lisp streams

### 7) “Port old code / reconcile CLIM 1.x vs CLIM 2”
Start here:
- `F.html` — changes from CLIM 1.0

Then re-read the current normative chapter, not just the delta note.

---

## Mandatory workflow

### Step 1: classify the request
Put the problem into one or more buckets:
- geometry
- sheet/window substrate
- drawing/medium output
- stream output / recording / redisplay
- stream input / presentations / completion
- commands / frames / panes / gadgets
- CLIM-SYS / stream interop / legacy migration

### Step 2: search locally
Use the helper first, then direct file reads.

Examples:

```bash
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --toc
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "presentation translator"
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "incremental redisplay" --limit 10
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame" --files '28*.html'
```

Direct grep is also fine:

```bash
cd /home/slime/projects/kvc-skills/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec
rg -n "presentation translator|application frame|incremental redisplay|sheet-region|move-sheet" *.html
```

### Step 3: read the primary sections
Read the actual chapter/section files that answer the question.

Prefer:
1. exact section,
2. parent chapter,
3. related appendix,
4. `F.html` only if migration history matters.

### Step 4: separate normative from non-normative material
When answering, distinguish among:
- **Spec requirement** — directly supported by mirrored CLIM text
- **Implementation note** — McCLIM or another implementation detail
- **Inference / recommendation** — your synthesis from the spec

### Step 5: answer with source-backed structure
Recommended response shape:
1. short answer,
2. relevant CLIM sections,
3. any implementation caveats,
4. next action / code sketch if requested,
5. citations.

---

## Citation format

Use simple file-based citations so another agent can reproduce the lookup quickly.

Examples:
- `Source: docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/28-2.html`
- `Source: docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/23-7.html`
- `Source: docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/21.html`

If multiple sections matter, cite all of them.

---

## Important cautions

### Annotation noise
The HTML mirror contains annotation links and a playground (`G.html`, `P-X.html`).
These are useful historical artifacts, but **not part of the normative core**.

### Spec vs implementation
McCLIM may diverge, lag, or extend.
When the user is implementing McCLIM code, do not pretend McCLIM and CLIM 2 are identical.

### Legacy traps
If you find advice from old CLIM mailing lists, examples, or code snippets, cross-check against:
- the current chapter text,
- `F.html` for changed names/semantics.

### Streams and panes cross-cut heavily
A lot of CLIM questions look like “pane” questions but are really about:
- stream protocols,
- output records,
- presentations,
- command loop integration.
Always widen the search when a behavior spans subsystems.

---

## Output contract for agent use

When using this skill successfully, return:
1. the CLIM subsystem classification,
2. the specific mirrored files consulted,
3. the answer grounded in the spec,
4. any implementation-specific notes kept clearly separate,
5. unresolved ambiguity if the spec is vague or silent.

If you did **not** consult the mirrored files, the skill was not followed.
