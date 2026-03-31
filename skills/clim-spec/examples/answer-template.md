# CLIM Spec Answer Template

Use this response shape when answering a CLIM or McCLIM question after consulting the mirrored corpus.

## Template

```text
Short answer:
<1-3 sentence answer>

Subsystem:
- <primary CLIM subsystem>
- <secondary subsystem if relevant>

Relevant sections:
- <chapter/section name> — <why it matters>
- <chapter/section name> — <why it matters>

Spec requirement:
- <what CLIM 2 appears to require>

Implementation note:
- <what seems specific to McCLIM or another implementation>

Ambiguity / silence:
- <what the spec does not settle, if anything>

Next action:
- <what to read next / what to inspect in code>

Sources:
- docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/<file>.html
- docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/<file>.html
```

## Example stub

```text
Short answer:
Presentation translators are covered primarily in Chapter 23, with command-related utilities in Chapter 27.

Subsystem:
- input / presentations / completion
- commands / frames / panes / gadgets

Relevant sections:
- 23.7 Presentation Translators — defines translator concepts and functions
- 27.5 Presentation Translator Utilities — command-processing-side helpers

Spec requirement:
- CLIM 2 treats presentation translators as part of the presentation system, not merely ad hoc command hooks.

Implementation note:
- McCLIM may add implementation-specific translator behavior or debugging affordances.

Ambiguity / silence:
- If the question is about a specific translator edge case, the spec may not define every UI behavior.

Next action:
- Read `23-7.html` first, then `27-5.html` if commands are involved.

Sources:
- docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/23-7.html
- docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/27-5.html
```
