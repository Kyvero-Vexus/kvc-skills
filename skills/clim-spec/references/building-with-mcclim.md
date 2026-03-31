# Building with CLIM on McCLIM

This file is the practical companion to the main skill. Use it when you need to answer:
- what CLIM can do,
- which feature fits the UI you are building,
- which spec chapters matter,
- which local McCLIM examples are worth copying.

For **full minimum coverage of the entire CLIM 2 spec**, pair this file with:
- `references/full-spec-feature-map.md`

This file emphasizes the most common build paths; the full-spec map keeps the skill from forgetting less-common chapters and appendices.

## What CLIM gives you in practice

### 1. Application frames and top-level command loops

Use when you need a real application window with state, panes, and a top-level interaction loop.

Core forms:
- `define-application-frame`
- `make-application-frame`
- `run-frame-top-level`

Spec anchors:
- `28-2.html` — defining and creating application frames
- `28-4.html` — generic command loop

McCLIM examples:
- `Documentation/Manual/examples/ex1.lisp`
- `Documentation/Manual/examples/ex2.lisp`
- `Documentation/Manual/examples/ex3.lisp`
- `Examples/superapp.lisp`

### 2. Panes and layouts

Use when you need to divide the window into functional regions.

Common pane roles:
- `:interactor`
- `:application`
- layout panes via `vertically`, `horizontally`, and related pane constructors

Spec anchors:
- `29-2.html` — pane construction
- `29-3.html` — composite and layout panes
- `29-4.html` — CLIM stream panes

McCLIM examples:
- `Documentation/Guided-Tour/color-editor.lisp`
- `Documentation/Guided-Tour/simple-draw.lisp`
- `Examples/stream-test.lisp`

Practical rule:
- prefer abstract pane names for portability
- use a concrete pane class only when you intentionally need implementation-specific behavior

### 3. Commands and command tables

Use when the app is action-driven and should support typed commands, menus, or accelerators.

Spec anchors:
- `27-1.html` — commands
- `27-2.html` — command tables
- `27-6.html` — command processor
- `28-4.html` — generic command loop

McCLIM examples:
- `Documentation/Manual/examples/ex3.lisp`
- `Examples/menu-test.lisp`
- `Examples/asynchronous-commands.lisp`

Practical rule:
- use commands for application actions
- do not embed all state transitions directly inside repaint code or gadget callbacks

### 4. Presentations and typed interaction

This is the CLIM superpower.

Use when visible output should correspond to domain objects, and users should be able to select, inspect, translate, or invoke actions on them semantically.

Core forms:
- `define-presentation-type`
- `present`
- `with-output-as-presentation`
- `accept`
- `define-presentation-to-command-translator`

Spec anchors:
- `23-4.html` — typed output
- `23-5.html` — context-dependent typed input
- `23-7.html` — presentation translators
- `24-5.html` — completion

McCLIM examples:
- `Documentation/Manual/examples/ex3.lisp`
- `Documentation/Guided-Tour/file-browser.lisp`
- `Documentation/Guided-Tour/simple-spreadsheet.lisp`
- `Examples/presentation-test.lisp`
- `Examples/presentation-translators-test.lisp`
- `Examples/dragndrop.lisp`
- `Examples/dragndrop-translator.lisp`

Practical rule:
- if the screen shows domain objects, presentations are usually a better fit than raw coordinate click handling

### 5. Structured output: tables and graphs

Use when output is report-like, grid-like, or graph-like.

Core forms:
- `formatting-table`
- `formatting-row`
- `formatting-cell`
- `format-graph-from-roots`

Spec anchors:
- `17-2.html` — table formatting functions
- `17-3.html` — table formatting protocol
- `18-1.html` — graph formatting functions
- `18-2.html` — graph formatting protocols

McCLIM examples:
- `Documentation/Guided-Tour/simple-spreadsheet.lisp`
- `Documentation/Guided-Tour/scheduler.lisp`
- `Examples/tabledemo.lisp`
- `Examples/graph-formatting-test.lisp`
- `Examples/graph-toy.lisp`

Practical rule:
- use table and graph formatting before hand-positioning text unless the view is truly custom graphics

### 6. Gadgets and forms

Use when the UI needs conventional controls.

Examples of gadget categories from the spec:
- push buttons
- toggle buttons
- menu buttons
- scroll bars
- sliders
- radio/check boxes
- list/option panes
- text fields and text editors

Spec anchors:
- `30-2.html` — abstract gadgets and callbacks
- `30-4.html` — standard gadget families
- `29-2.html` — panes as gadget carriers

McCLIM examples:
- `Examples/text-gadgets.lisp`
- `Examples/gadget-test.lisp`
- `Examples/calculator.lisp`
- `Examples/colorslider.lisp`

Practical rule:
- gadgets are great for controls and forms
- they are not a replacement for presentations when your UI is fundamentally about semantic objects on screen

### 7. Accepting values and structured input sessions

Use when the user is editing multiple related inputs in a structured flow.

Core forms:
- `accept`
- `accepting-values`

Spec anchors:
- `24.html` — input editing and completion facilities
- `26.html` — dialog facilities
- `21-2.html` — includes `invoke-accept-values-command-button`

McCLIM examples:
- `Examples/accepting-values.lisp`
- `Examples/accepting-values-test.lisp`
- `Documentation/Guided-Tour/simple-spreadsheet.lisp`

Practical rule:
- for transient parameter editing, `accepting-values` is often simpler than building a custom gadget dialog by hand

### 8. Drawing, graphics, and canvas-style UIs

Use when the application is visually custom, geometric, or drawing-heavy.

Spec anchors:
- `12.html` — graphics
- `13.html` — color
- `14.html` — designs
- `3.html`, `4.html`, `5.html` — geometry and transforms
- `29-4.html` — CLIM stream panes

McCLIM examples:
- `Documentation/Guided-Tour/simple-draw.lisp`
- `Examples/patterns.lisp`
- `Examples/image-transform-demo.lisp`
- `Examples/transformations-test.lisp`
- `Examples/nested-clipping.lisp`

Practical rule:
- use an application pane with a display function for custom drawing
- use presentations on top of graphics if the graphics still represent semantic objects

### 9. Output records and incremental redisplay

Use when the UI changes frequently and partial updates matter.

Spec anchors:
- `16.html` — output recording
- `21-1.html` — overview of incremental redisplay
- `21-2.html` — standard programmer interface
- `21-3.html` — incremental redisplay protocol

McCLIM examples:
- `Examples/output-record-example-1.lisp`
- `Examples/reinitialize-frame.lisp`
- dynamic portions of `Documentation/Guided-Tour/simple-spreadsheet.lisp`

Practical rule:
- if the same view is redrawn often, consider output records and `updating-output` before brute-force full redraws

## Design decision table

| If you need... | Start with... | Then add... |
|---|---|---|
| A simple command tool | frame + interactor pane | commands, maybe menus |
| Clickable domain objects | application pane + presentations | translators, typed input |
| A data grid/report | application pane + `formatting-table` | presentations per cell, commands |
| A graph browser | `format-graph-from-roots` | presentations/translators |
| A settings/control panel | gadgets or `accepting-values` | callbacks, frame state |
| A drawing app | application pane + drawing functions | transforms, presentations, redisplay |
| A live dashboard | application pane + output records | incremental redisplay |

## Common anti-patterns

### Anti-pattern: treat CLIM as just “draw stuff + callbacks”
Better:
- use presentations when the output is semantic
- use commands when the action belongs in the command system

### Anti-pattern: use gadgets for everything
Better:
- gadgets for controls/forms
- presentations for object-centric interaction

### Anti-pattern: copy McCLIM examples without checking the spec
Better:
- consult the example for shape
- consult the spec for semantics

### Anti-pattern: jump straight into backend internals
Better:
- first get the frame/pane/interaction design right
- only then dig into backend or pane implementation details

## Handy source paths

Spec mirror root:
- `docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/`

McCLIM root:
- `/home/slime/external_src/mcclim/`
