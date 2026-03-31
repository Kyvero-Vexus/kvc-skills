# CLIM Skill Mini A/B Eval Plan

Capability delta under test:

> After applying this skill, Claude Code should more reliably answer CLIM 2 and McCLIM questions with spec-backed citations and clearer separation between normative spec text and implementation-specific behavior.

## Baseline vs treatment

- **Baseline:** previous `skills/clim-spec/SKILL.md`
- **Treatment:** current skill with explicit trigger contract, progressive disclosure sidecars, quality checks, and failure handling

## Representative prompts

1. Which CLIM chapter should I read for presentation translators?
2. Does CLIM 2 specify how application frames interact with incremental redisplay?
3. I am debugging a stale McCLIM pane; what CLIM sections should I inspect first?
4. Is `move-sheet` a sheet geometry concern or a pane concern?
5. What is normative in the CLIM mirror versus annotation noise?
6. I need to port old CLIM 1.x frame code; where should I start?
7. Which appendix matters for encapsulating streams?
8. How should I answer a McCLIM question when the spec is silent?

## Scoring rubric

Score each prompt 0–2 on each dimension.

### 1. Triggering accuracy
- 0: skill would probably not trigger or would trigger for the wrong thing
- 1: partial trigger clarity
- 2: clear trigger match

### 2. Routing accuracy
- 0: wrong chapters/sections
- 1: partially correct routing
- 2: correct primary routing with sensible cross-links

### 3. Normative discipline
- 0: blends CLIM, McCLIM, and annotations together
- 1: partial distinction
- 2: clearly separates spec requirements from implementation notes

### 4. Citation readiness
- 0: no reproducible local citations
- 1: vague citation guidance
- 2: clear local mirrored-file citation pattern

### 5. Failure honesty
- 0: improvises when the spec is silent
- 1: mixed
- 2: explicitly states ambiguity/silence

Maximum score per prompt: 10

## Keep/discard criterion

Keep the new version only if it improves average score on:
- routing accuracy
- normative discipline
- citation readiness

with no regression in trigger clarity.
