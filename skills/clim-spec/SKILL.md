---
name: clim-spec
description: Use when users want to build, extend, or debug a CLIM application on McCLIM: choosing frames, panes, commands, presentations, gadgets, formatted output, graphics, redisplay, or typed interaction grounded in the CLIM 2 spec.
compatibility: Designed for Claude Code skill workflows with a local CLIM 2 mirror and a local McCLIM checkout.
metadata:
  openclaw:
    emoji: "🪟"
---

# Build CLIM Applications with McCLIM

## Goal

After applying this skill, Claude Code should reliably **build working CLIM applications on McCLIM** using CLIM 2 concepts correctly, instead of treating CLIM as only a spec-reading exercise.

Use the spec as the semantic ground truth and McCLIM as the concrete implementation and example corpus.

## Triggers

Use this skill when the user wants to:
- build a GUI/tool/browser/editor/dashboard with CLIM on McCLIM
- choose between frames, panes, presentations, commands, gadgets, or redisplay strategies
- understand what CLIM features it has and how they fit together in practice
- port or redesign an interface into CLIM style
- debug a McCLIM application while staying aligned with CLIM 2 semantics
- find the right McCLIM example to copy or adapt

Do **not** use this skill for:
- generic Common Lisp questions with no CLIM angle
- purely backend-internal McCLIM hacking when the user does not need application-building guidance
- unrelated GUI toolkits

## Core stance

This skill is for **building things**.

That means:
- start from the application architecture,
- choose the right CLIM interaction model,
- use the spec to keep semantics straight,
- use McCLIM examples to avoid inventing nonsense.

## Local resources

### CLIM 2 spec mirror
- `/home/slime/projects/kvc-skills/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec`

Helper:
- `python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame"`

### Local McCLIM checkout
- `/home/slime/external_src/mcclim`

High-value McCLIM material:
- `README.md`
- `Documentation/Guided-Tour/`
- `Documentation/Manual/examples/`
- `Examples/`

Sidecars:
- `references/building-with-mcclim.md`
- `references/mcclim-example-map.md`
- `references/eval-plan.md`
- `examples/minimal-app.lisp`
- `examples/presentation-table-app.lisp`
- `examples/gadget-form.lisp`

## Quick workflow

1. Classify the app or feature you are building.
2. Choose the primary interaction style.
3. Start from a nearby McCLIM example.
4. Read the governing CLIM spec sections before committing to semantics.
5. Build the frame, panes, and layout first.
6. Add commands, presentations, gadgets, or formatted output as appropriate.
7. Use output recording / redisplay deliberately for dynamic views.
8. Keep CLIM-core semantics separate from McCLIM-specific behavior.

## Procedure

### 1) Classify what you are building

Put the task into one or more of these buckets:
- **minimal command tool** — interactor-pane plus commands
- **browser / inspector / semantic document UI** — presentations and translators
- **table / report / spreadsheet / dashboard** — formatting-table and structured output
- **graph / hierarchy / network view** — graph formatting or custom drawing
- **form / control panel** — gadgets and accepting values
- **graphics / canvas app** — application-pane plus drawing, regions, transforms
- **dynamic live view** — output records and incremental redisplay

If the request spans multiple buckets, choose one primary interaction model and note the rest as supporting mechanisms.

### 2) Choose the right CLIM interaction model

Pick the mechanism that matches the problem.

#### Use commands when:
- the app is action-oriented
- textual command input is useful
- menu/accelerator integration matters

Spec anchors:
- Chapter 27 — Command Processing
- Chapter 28 — Application Frames

#### Use presentations when:
- objects on screen should be semantically clickable/selectable
- typed output and typed input should share the same domain model
- translators or pointer-driven actions matter

Spec anchors:
- Chapter 23 — Presentation Types
- Chapter 24 — Input Editing and Completion Facilities

#### Use gadgets when:
- the UI is form-like or control-like
- text fields, buttons, sliders, check boxes, option panes, or editors are the natural idiom

Spec anchors:
- Chapter 29 — Panes
- Chapter 30 — Gadgets

#### Use formatted output when:
- the output is tabular, hierarchical, report-like, or graph-like
- you want CLIM to manage layout through output records

Spec anchors:
- Chapter 17 — Table Formatting
- Chapter 18 — Graph Formatting
- Chapter 16 — Output Recording

#### Use custom drawing when:
- the app is geometry-heavy, visual, or canvas-oriented
- you need direct control over drawing and transforms

Spec anchors:
- Chapters 3–5 — geometry and transforms
- Chapters 10–14 — drawing and designs
- Chapter 29.4 — CLIM stream panes

### 3) Start from a real McCLIM example

Before inventing a design from scratch, locate a nearby local example.

Examples:
- minimal app: `Documentation/Manual/examples/ex1.lisp`
- frame + interactor + commands + presentations: `Documentation/Manual/examples/ex3.lisp`
- spreadsheet/table/presentations: `Documentation/Guided-Tour/simple-spreadsheet.lisp`
- text gadgets: `Examples/text-gadgets.lisp`
- richer gadget use: `Examples/gadget-test.lisp`
- formatted graphs: `Examples/graph-formatting-test.lisp`
- accepting values: `Examples/accepting-values.lisp`
- drag/drop translators: `Examples/dragndrop.lisp`, `Examples/dragndrop-translator.lisp`

Use:
- `references/mcclim-example-map.md`

### 4) Read the spec sections that govern the pattern

Do not just cargo-cult the example.
Use the local mirror to verify semantics.

Typical lookups:

```bash
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame"
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "presentation translator" --files '23*.html' '27*.html'
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "make-pane|CLIM stream pane" --files '29*.html'
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "incremental redisplay|updating-output" --files '21*.html'
```

Use:
- `references/building-with-mcclim.md`

### 5) Build the frame first

The usual backbone is:
- package definition
- `define-application-frame`
- frame state slots
- `:panes`
- `:layouts`
- runner based on `make-application-frame` and `run-frame-top-level`

Prefer abstract pane names and `make-pane`-style portability unless you have a good McCLIM-specific reason not to.

The spec explicitly treats application frames, panes, and command loops as the organizing structure of an app.

### 6) Choose pane strategy deliberately

Common pane roles:
- **interactor-pane** — command input / REPL-like interaction
- **application-pane** — custom display-function-driven output
- **layout panes** — `vertically`, `horizontally`, table-ish pane arrangements
- **gadget panes** — buttons, sliders, text fields, option panes, editors

Rule of thumb:
- if you are displaying domain objects, use an application pane
- if users should type commands, include an interactor pane
- if users edit form fields, use gadgets or `accepting-values`

### 7) Render semantics, not just pixels

If output corresponds to domain objects, prefer:
- `present`
- `with-output-as-presentation`
- `accept`
- presentation translators

This is one of CLIM's strongest features.
It gives you semantic UI, not just painted rectangles.

If the output is tabular or report-like, use:
- `formatting-table`
- `formatting-row`
- `formatting-cell`

If the output is graph-like, use:
- `format-graph-from-roots`

### 8) Use commands, translators, and gadgets in the right places

Good division of labor:
- **commands** for app actions and command tables
- **presentations/translators** for semantic object interaction
- **gadgets** for controls/forms
- **accepting-values** for structured data entry sessions

Do not force everything into gadgets if the real abstraction is semantic object interaction.
Do not force everything into translators if the real abstraction is a simple form.

### 9) Plan for redisplay if the view changes often

If the app is stateful and dynamic, inspect:
- output recording
- output records
- `updating-output`
- incremental redisplay

This matters for dashboards, inspectors, editors, and any view with partial updates.

### 10) Be explicit about McCLIM specifics

McCLIM is the implementation, not the spec.

Keep these separate in your reasoning:
- **CLIM 2 says** — semantic/API expectation
- **McCLIM does** — concrete behavior, examples, quirks, extensions, or omissions

Also keep backend reality in view: the local McCLIM README notes CLX/X-server assumptions.
Do not promise backend portability that the implementation does not currently provide.

## Output contract

When using this skill successfully, return:
1. the chosen application style or interaction model
2. the frame/pane architecture you recommend or implemented
3. the CLIM mechanisms being used (commands, presentations, gadgets, formatted output, redisplay, etc.)
4. the CLIM spec files consulted
5. the McCLIM example files consulted or adapted
6. a clear distinction between CLIM-core semantics and McCLIM-specific behavior
7. code or edits oriented toward a working McCLIM application

## Quality checks

- [ ] the answer or implementation is about **building with CLIM**, not just browsing the spec
- [ ] a real McCLIM example was consulted when a local pattern exists
- [ ] relevant CLIM spec sections were consulted before asserting semantics
- [ ] frame / panes / layout are defined coherently
- [ ] the chosen interaction style matches the problem
- [ ] presentations are used when output carries domain semantics
- [ ] gadgets are used when form controls are the natural fit
- [ ] McCLIM-specific behavior is not misrepresented as core CLIM 2

## Failure handling

### No obvious example match
- pick the nearest McCLIM example and say what is being borrowed
- fall back to the minimal frame skeleton and build upward

### Spec/example tension
- prefer CLIM 2 for semantic claims
- note the McCLIM behavior separately
- if necessary, say the implementation may diverge or leave a corner unspecified

### User asks for features list rather than code
- answer in terms of buildable capabilities:
  - frames and command loops
  - panes and layouts
  - semantic presentations and typed input/output
  - commands and command tables
  - gadgets and forms
  - formatted tables and graphs
  - drawing, colors, patterns, transforms
  - output recording and incremental redisplay

### Dynamic UI gets messy
- reconsider whether the design should rely more on presentations/output records or on gadgets
- look for a simpler frame architecture before adding more callbacks
