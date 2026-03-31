# McCLIM Example Map

Use this map to pick a nearby example before inventing a CLIM architecture from scratch.

## Minimal frame skeletons

- `Documentation/Manual/examples/ex1.lisp`
  - smallest useful frame with one interactor pane
  - good first scaffold for command-line-ish tools

- `Documentation/Manual/examples/ex2.lisp`
  - simple frame expansion beyond the absolute minimum

- `Examples/superapp.lisp`
  - frame plus a couple of panes, including a push button and label pane

## Commands + presentations

- `Documentation/Manual/examples/ex3.lisp`
  - compact example showing:
    - `define-application-frame`
    - commands
    - `define-presentation-type`
    - `with-output-as-presentation`
    - typed command arguments

- `Examples/presentation-test.lisp`
  - presentation behavior playground

- `Examples/presentation-translators-test.lisp`
  - translators and presentation typing combinations

## Presentations + realistic app structure

- `Documentation/Guided-Tour/file-browser.lisp`
  - file-browser style app
  - presentation types and presentation-to-command translators

- `Documentation/Guided-Tour/simple-spreadsheet.lisp`
  - one of the best practical examples in the tree
  - shows:
    - application frame
    - application and interactor panes
    - custom presentation methods
    - `formatting-table`
    - `present`
    - `accepting-values`
    - command-driven mutation of a semantic data grid

## Tables, reports, and graph views

- `Documentation/Guided-Tour/scheduler.lisp`
  - table-based scheduling layout

- `Examples/tabledemo.lisp`
  - table formatting demonstration

- `Examples/graph-formatting-test.lisp`
  - graph formatting example

- `Examples/graph-toy.lisp`
  - graph-centric interaction patterns

## Gadgets and forms

- `Examples/text-gadgets.lisp`
  - text fields, text editor, callbacks, frame pane lookup

- `Examples/gadget-test.lisp`
  - broader gadget showcase

- `Examples/calculator.lisp`
  - buttons + text field as an app interface

- `Examples/colorslider.lisp`
  - slider-driven interaction

## Accepting values / structured input

- `Examples/accepting-values.lisp`
- `Examples/accepting-values-test.lisp`

Use these before hand-rolling form workflows.

## Graphics / drawing / canvas patterns

- `Documentation/Guided-Tour/simple-draw.lisp`
  - minimal custom drawing-oriented frame

- `Examples/patterns.lisp`
  - more advanced drawing/design work

- `Examples/image-transform-demo.lisp`
  - transforms and image-oriented display

- `Examples/transformations-test.lisp`
  - geometric transformations

- `Examples/nested-clipping.lisp`
  - clipping behavior

## Stream / pane internals

- `Examples/stream-test.lisp`
  - custom interactor-pane subclassing and event/gesture hooks

- `Examples/output-record-example-1.lisp`
  - output-record-heavy example

## Drag and drop / pointer interaction

- `Examples/dragndrop.lisp`
- `Examples/dragndrop-translator.lisp`

## How to use this map

1. Pick the example closest to the requested UX.
2. Copy the **architecture**, not every line.
3. Verify semantics in the CLIM spec mirror.
4. Say explicitly what is CLIM-generic and what is McCLIM-specific.
