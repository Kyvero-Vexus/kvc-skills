# CLIM Skill Mini A/B Eval Plan

Capability delta under test:

> After applying this skill, Claude Code should more reliably design and build McCLIM applications using the right CLIM interaction model, grounded in both the CLIM 2 spec and local McCLIM examples.

## Baseline vs treatment

- **Baseline:** earlier `clim-spec` skill that primarily emphasized spec lookup
- **Treatment:** current skill centered on building applications with McCLIM, with feature mapping, example routing, and spec-grounded implementation guidance

## Representative prompts

1. Build a minimal McCLIM app with one interactor pane.
2. Build a browser where clicking displayed objects triggers commands.
3. Should this spreadsheet-like UI use gadgets or presentations?
4. What CLIM features are available for a dashboard/reporting app?
5. How should I structure panes for a command-driven application?
6. I need a form with text fields and buttons; what McCLIM patterns fit?
7. I need dynamic partial redraws; when should I use incremental redisplay?
8. Which local McCLIM example should I start from for a table-based semantic UI?

## Scoring rubric

Score each prompt 0–2 on each dimension.

### 1. Build orientation
- 0: answer stays at spec-summary level
- 1: partly actionable
- 2: clearly oriented toward building a working app

### 2. Interaction-model choice
- 0: wrong CLIM mechanism chosen
- 1: partly reasonable
- 2: correct mechanism choice (commands vs presentations vs gadgets vs formatted output, etc.)

### 3. Spec grounding
- 0: no CLIM 2 grounding
- 1: vague chapter references
- 2: relevant spec sections consulted or cited

### 4. McCLIM practicality
- 0: ignores local implementation/examples
- 1: generic mention of McCLIM only
- 2: points to concrete local McCLIM examples or implementation constraints

### 5. Semantic discipline
- 0: confuses CLIM-core and McCLIM-specific behavior
- 1: partial distinction
- 2: clear distinction

Maximum score per prompt: 10

## Keep/discard criterion

Keep the new version only if it improves average score on:
- build orientation
- interaction-model choice
- McCLIM practicality

while preserving spec grounding.
