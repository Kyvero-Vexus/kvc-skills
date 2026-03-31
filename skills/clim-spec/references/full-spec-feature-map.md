# Full CLIM 2 Feature Map

This file exists so the skill covers **the entire CLIM 2 spec as a minimum**, not just the common app-building subset.

Use it when the user asks:
- what CLIM can do,
- what features exist in the spec,
- which chapter family covers a specific capability,
- which parts of CLIM are less commonly used but still part of the model.

For each chapter family below:
- treat the CLIM 2 mirror as semantic ground truth,
- map the feature back into application-building decisions,
- then look for a nearby McCLIM example if implementation guidance is needed.

---

## Part I — Overview and Conventions

### Chapter 1 — Overview of CLIM
What it gives you:
- the conceptual shape of CLIM as a high-level UI toolkit
- the idea that CLIM is more than widgets: it includes streams, presentations, commands, formatted output, and windowing substrate concerns

### Chapter 2 — Conventions
Builder significance:
- package structure
- protocol classes and predicates
- specialized arguments to generic functions
- multiple-value `setf`
- stream/sheet/medium argument conventions for macros
- error-condition terminology

Use when:
- writing portable CLIM code
- interpreting protocol APIs correctly
- avoiding macro-argument mistakes

---

## Part II — Geometry Substrate

### Chapter 3 — Regions
Features:
- general regions
- region predicates
- region composition
- points, polygons, polylines, lines, rectangles, ellipses, elliptical arcs

Builder significance:
- hit testing
- clipping
- geometric object models
- semantic drawing regions

### Chapter 4 — Bounding Rectangles
Features:
- bounding rectangle protocol
- convenience functions

Builder significance:
- layout calculations
- output record extents
- pane and drawing bounds

### Chapter 5 — Affine Transformations
Features:
- transformations
- constructors
- predicates
- composition
- applying transformations

Builder significance:
- zoom/pan/rotate UIs
- coordinate spaces
- drawing and sheet geometry manipulation

---

## Part III — Windowing Substrate

### Chapter 6 — Overview of Window Facilities
Features:
- introduction to sheets and protocols

Builder significance:
- understanding what lies below panes and frames

### Chapter 7 — Properties of Sheets
Features:
- sheet classes
- sheet relationships
- geometry functions and classes

Builder significance:
- custom panes
- sheet hierarchies
- movement, resizing, transformations, adoption/disowning

### Chapter 8 — Sheet Protocols
Features:
- input protocol
- device events
- output protocol
- medium association
- repaint protocol
- sheet notifications

Builder significance:
- repaint behavior
- event flow
- medium lifecycle
- custom sheet/pane implementations

### Chapter 9 — Ports, Grafts, and Mirrored Sheets
Features:
- ports
- grafts
- mirrored sheets
- native coordinate interfaces

Builder significance:
- implementation/backend-facing app work
- understanding how panes attach to the display server

---

## Part IV — Sheet and Medium Output Facilities

### Chapter 10 — Drawing Options
Features:
- medium components
- binding forms
- local coordinate systems
- line styles

Builder significance:
- how drawing state is established and controlled

### Chapter 11 — Text Styles
Features:
- text styles
- text-style binding forms
- style mappings

Builder significance:
- typography choices
- readable application output
- font/style management

### Chapter 12 — Graphics
Features:
- drawing definitions
- rendering conventions
- drawing functions
- pixmaps
- graphics protocols

Builder significance:
- custom graphics apps
- canvas panes
- structured geometric drawing

### Chapter 13 — Drawing in Color
Features:
- `:ink`
- basic designs
- colors
- opacity
- blending
- indirect inks
- flipping ink

Builder significance:
- practical color and compositing behavior
- visual feedback and highlighting

### Chapter 14 — General Designs
Features:
- compositing protocol
- patterns and stencils
- tiling
- regions as designs
- arbitrary designs
- design protocol

Builder significance:
- patterned fills
- advanced drawing/design composition
- richer visual semantics

---

## Part V — Extended Stream Output Facilities

### Chapter 15 — Extended Stream Output
Features:
- basic and extended output streams
- text cursor protocols
- text protocol
- mixed text/graphics
- wrapping
- user-attention operations
- buffering

Builder significance:
- stream-pane behavior
- text-heavy UIs
- output responsiveness and cursor management

### Chapter 16 — Output Recording
Features:
- output records
- database protocol
- change notification
- record classes
- output recording streams
- output recording utilities

Builder significance:
- semantic structured output
- redisplay support
- interactive output manipulation

### Chapter 17 — Table Formatting
Features:
- table formatting functions
- table/row/column/cell/item-list protocols

Builder significance:
- reports
- dashboards
- spreadsheets
- structured textual layouts

### Chapter 18 — Graph Formatting
Features:
- graph formatting functions
- graph formatting protocols

Builder significance:
- trees
- dependency graphs
- hierarchy browsers
- relationship visualization

### Chapter 19 — Bordered Output
Features:
- bordered output around rendered content

Builder significance:
- emphasis, grouping, panels, visual affordances

### Chapter 20 — Text Formatting
Features:
- textual list formatting
- indented output
- filled output

Builder significance:
- prose-heavy interfaces
- inspectors/help panes/report generation

### Chapter 21 — Incremental Redisplay
Features:
- overview and examples
- standard interface
- incremental redisplay protocol
- redisplay stream protocol

Builder significance:
- dynamic UIs
- dashboards
- inspectors/editors
- partial refresh instead of brute-force redraw

---

## Part VI — Extended Stream Input Facilities

### Chapter 22 — Extended Stream Input
Features:
- basic and extended input streams
- extended input stream protocol and conditions
- gestures and gesture names
- pointer protocol
- pointer tracking

Builder significance:
- keyboard and pointer interaction models
- gesture-aware UIs
- interactive stream behavior

### Chapter 23 — Presentation Types
Features:
- presentations
- presentation protocol
- presentation type definition and abbreviations
- presentation methods and functions
- typed output
- context-dependent typed input
- views
- presentation translators
- translator applicability/finding
- standard presentation types

Builder significance:
- the semantic interaction core of CLIM
- object-centric UI design
- typed clicking, selection, menus, translators, and contextual input

### Chapter 24 — Input Editing and Completion Facilities
Features:
- input editor
- input editing stream protocol
- activation and delimiter gestures
- errors inside `present`
- token reading/writing
- completion

Builder significance:
- richer command-line and typed-input UX
- completion-driven interfaces
- robust input sessions

### Chapter 25 — Menu Facilities
Features:
- menu mechanisms

Builder significance:
- command menus and user choice interfaces

### Chapter 26 — Dialog Facilities
Features:
- dialog-oriented interaction mechanisms

Builder significance:
- modal or semi-structured user input flows
- parameter and data-entry interfaces

---

## Part VII — Building Applications

### Chapter 27 — Command Processing
Features:
- commands
- command tables
- command menus
- keystroke accelerators
- presentation translator utilities
- command processor
- command presentation types

Builder significance:
- action-oriented application structure
- tying commands to menus, keystrokes, and typed interaction

### Chapter 28 — Application Frames
Features:
- frame overview
- defining and creating frames
- pane specification inside frames
- frame functions
- interface with presentations
- generic command loop
- frame managers
- examples

Builder significance:
- the spine of most CLIM applications
- app state, pane hierarchy, standard streams, command lifecycle

### Chapter 29 — Panes
Features:
- pane overview
- basic pane construction
- initialization options and properties
- composite/layout/scroller panes
- layout protocol
- CLIM stream panes
- standalone CLIM windows
- defining new pane types

Builder significance:
- practical window decomposition
- reusable UI structure
- custom pane design

### Chapter 30 — Gadgets
Features:
- gadget overview
- abstract gadgets
- using and implementing gadgets
- basic and abstract gadget classes
- push buttons
- toggle buttons
- menu buttons
- scroll bars
- sliders
- radio/check boxes
- list/option panes
- text fields/editors
- integrating gadgets with output records

Builder significance:
- conventional controls layered into CLIM applications
- forms, control surfaces, and hybrid UIs

---

## Part VIII — Appendices

### Appendix A — Glossary
Use when terminology is fuzzy.

### Appendix B — The `CLIM-SYS` Package
Features:
- resources
- multiprocessing
- locks
- multiple-value `setf`

Builder significance:
- infrastructure work
- background tasks and concurrency-aware applications
- synchronization around dynamic UIs

### Appendix C — Encapsulating Streams
Features:
- encapsulating stream classes
- encapsulating stream protocol
- delegation problem

Builder significance:
- stream wrappers
- instrumentation/filtering/proxy streams

### Appendix D — Common Lisp Streams
Features:
- stream classes
- basic stream functions
- character input/output
- binary streams

Builder significance:
- interop between CLIM streams and regular CL stream expectations

### Appendix E — Suggested Extensions to CLIM
Features:
- PostScript output
- reading bitmap files

Builder significance:
- output/export and image-input extension points

### Appendix F — Changes from CLIM 1.0
Builder significance:
- migration guide
- legacy code reconciliation
- avoiding stale CLIM 1.x assumptions

---

## Required minimum policy for this skill

When the user asks broadly what CLIM has, what it can do, or whether a feature area is covered, the answer must be able to range across **all of the chapter families above**.

The common app-building path usually emphasizes:
- Chapters 17–30
- plus geometry/drawing chapters as needed

But the minimum scope of the skill is larger:
- conventions,
- geometry,
- window substrate,
- output/input facilities,
- application-building chapters,
- appendices with implementation impact.
