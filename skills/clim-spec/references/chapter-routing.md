# CLIM Chapter Routing

Use this file when the main skill tells you to route a CLIM question to the right sections.

## Geometry substrate

Look here first when the question is about geometry, clipping, containment, bounds, or transforms.

- **Chapter 3** — Regions
- **Chapter 4** — Bounding Rectangles
- **Chapter 5** — Affine Transformations

Typical tasks:
- geometric containment
- region composition
- coordinate transforms
- bounding boxes for panes or output records

## Windowing substrate

Look here first when the question is about sheets, repaint, events, ports, or mirrors.

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

## Drawing and medium output

Look here first when the question is about drawing, styles, inks, patterns, or graphics behavior.

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

## Output streams and redisplay

Look here first when the question is about stream panes, output recording, formatting, or redisplay.

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

## Input, presentations, and completion

Look here first when the question is about interactive CLIM behavior.

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

## Application construction

Look here first when the question is about complete applications.

- **Chapter 27** — Command Processing
- **Chapter 28** — Application Frames
- **Chapter 29** — Panes
- **Chapter 30** — Gadgets

Typical tasks:
- command tables and accelerators
- frame definitions and top-level loops
- pane layouts and stream panes
- gadgets/widgets and their integration

## Appendices worth using deliberately

- **Appendix B** — `CLIM-SYS` package, resources, multiprocessing, locks
- **Appendix C** — encapsulating streams
- **Appendix D** — Common Lisp stream interop
- **Appendix E** — suggested extensions, useful but non-core
- **Appendix F** — CLIM 1.0 → CLIM 2 changes

## Fast recipes by task type

### Build or fix an application frame
Start here:
- `28.html`
- `28-2.html`
- `28-4.html`
- `29.html`
- `27.html`

Then inspect:
- `23.html`
- `23-7.html`

### Design a pane layout or custom pane
Start here:
- `29-2.html`
- `29-3.html`
- `29-4.html`
- `29-5.html`

Backfill substrate details from:
- `7.html`
- `8.html`
- `9.html`

### Implement typed interaction / clickable objects / contextual commands
Start here:
- `23.html`
- `23-2.html`
- `23-4.html`
- `23-5.html`
- `23-7.html`
- `27-5.html`

Also inspect:
- `24.html`

### Debug redisplay or stale UI behavior
Start here:
- `16.html`
- `21.html`
- `29-4.html`

Focus on:
- output record identity
- record update protocol
- what triggers redisplay
- whether the pane or stream actually records output

### Implement drawing behavior or a rendering backend
Start here:
- `10.html`
- `12.html`
- `13.html`
- `14.html`
- `8-3.html`
- `9-4.html`

Also use:
- `3.html`
- `4.html`
- `5.html`

### Work on CLIM streams or wrap streams
Start here:
- `15.html`
- `22.html`
- `C.html`
- `C-1.html`
- `D.html`

### Port old code / reconcile CLIM 1.x vs CLIM 2
Start here:
- `F.html`

Then re-read the current normative chapter, not just the delta note.

## Handy lookup commands

```bash
python3 skills/clim-spec/scripts/clim_spec_lookup.py --toc
python3 skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame"
python3 skills/clim-spec/scripts/clim_spec_lookup.py --query "presentation translator" --files '23*.html' '27*.html'
python3 skills/clim-spec/scripts/clim_spec_lookup.py --query "incremental redisplay" --limit 10
```

```bash
cd docs/clim-spec/bauhh.dyndns.org:8000/clim-spec
rg -n "presentation translator|application frame|incremental redisplay|sheet-region|move-sheet" *.html
```
