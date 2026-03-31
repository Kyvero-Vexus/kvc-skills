---
name: clim-spec
description: Use when users ask what CLIM 2 specifies, which chapter covers panes/frames/presentations/gadgets/redisplay, how McCLIM behavior relates to the spec, or when implementing/debugging CLIM code that needs spec-backed answers.
compatibility: Designed for Claude Code skill workflows with a local mirrored CLIM 2 HTML corpus.
metadata:
  openclaw:
    emoji: "🪟"
---

# CLIM Spec Skill

## Goal

After applying this skill, Claude Code reliably answers **CLIM 2 and McCLIM questions with spec-backed citations** instead of hand-wavy memory, and routes implementation/debugging work to the right parts of the CLIM corpus quickly.

## Triggers

Use this skill when the request involves any of the following:
- what CLIM 2 specifies
- which CLIM chapter or section covers a topic
- McCLIM behavior versus CLIM 2 semantics
- implementing or debugging CLIM code
- application frames, panes, gadgets, command tables, presentations, translators, streams, output records, redisplay, sheets, ports, grafts, mediums, drawing, or CLIM-SYS
- porting CLIM 1.x code or checking legacy compatibility

Do **not** use this skill for:
- unrelated GUI toolkit questions
- generic Common Lisp questions with no CLIM angle
- purely implementation-specific McCLIM internals when no spec comparison is needed

## Quick workflow

1. Classify the request into a CLIM subsystem.
2. Search the local mirror before answering from memory.
3. Read the exact chapter/section files that govern the behavior.
4. Treat mirrored chapter text as normative; ignore annotation/playground noise.
5. Separate **spec requirement**, **implementation note**, and **inference**.
6. Answer with citations to local mirrored files.
7. If the spec is silent or ambiguous, say so explicitly.

## Core resources

Canonical mirror root:
- `/home/slime/projects/kvc-skills/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec`

Key files:
- `index.html`
- `contents.html`
- `theindex.html`
- `F.html`
- `B.html`
- `C.html`
- `D.html`

Helper script:
- `python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --toc`
- `python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "presentation translator"`

Sidecars:
- `references/chapter-routing.md` — routing map and lookup recipes
- `references/eval-plan.md` — mini A/B plan for skill quality
- `examples/answer-template.md` — response shape for spec-backed answers
- `scripts/validate-clim-skill.sh` — deterministic sanity checks

## Procedure

### 1) Classify the request

Put the problem into one or more buckets:
- geometry
- sheets / window substrate
- drawing / medium output
- output streams / recording / redisplay
- input / presentations / completion
- commands / frames / panes / gadgets
- CLIM-SYS / stream interop / legacy migration

If the topic spans more than one bucket, pick a primary bucket and note the cross-cutting ones.

### 2) Search the local mirror first

Use the helper before answering from memory.

Examples:

```bash
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --toc
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame"
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "presentation translator" --files '23*.html' '27*.html'
python3 /home/slime/projects/kvc-skills/skills/clim-spec/scripts/clim_spec_lookup.py --query "incremental redisplay" --limit 10
```

If needed, grep directly in the mirrored corpus:

```bash
cd /home/slime/projects/kvc-skills/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec
rg -n "presentation translator|application frame|incremental redisplay|sheet-region|move-sheet" *.html
```

### 3) Read the governing sections

Read the specific section files that answer the question.

Priority order:
1. exact section file,
2. parent chapter,
3. closely related appendix,
4. `F.html` only when migration history matters.

Use the routing sidecar when you need to decide where to look first:
- `references/chapter-routing.md`

### 4) Separate kinds of claims

When forming the answer, clearly distinguish:
- **Spec requirement** — stated or directly supported by CLIM 2 text
- **Implementation note** — McCLIM or another implementation detail
- **Inference / recommendation** — your synthesis based on the spec

If the question is about McCLIM specifically, answer in two layers:
1. what CLIM 2 specifies
2. what McCLIM appears to do, extend, or leave unspecified

### 5) Treat annotations as non-normative

The mirror includes annotation links and an annotation playground.
Those are useful historical artifacts, but they are **not** authoritative CLIM 2 requirements.

Do not treat playground or annotation comments as normative unless the user explicitly asks for annotation history.

### 6) Answer with a reproducible structure

Use this default response shape:
1. short answer
2. relevant CLIM sections
3. implementation caveats, if any
4. next action / code sketch if requested
5. citations

Use the example sidecar if helpful:
- `examples/answer-template.md`

### 7) Be explicit about silence or ambiguity

If the spec does not settle the issue, say that directly.
Do not invent semantics just to sound complete.

## Output contract

When this skill is used successfully, return all of:
1. CLIM subsystem classification
2. local mirrored files consulted
3. answer grounded in CLIM 2 text
4. implementation-specific notes clearly separated from the spec
5. unresolved ambiguity if the spec is silent, vague, or leaves room for implementation choice

Citation style:
- `Source: docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/28-2.html`
- `Source: docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/23-7.html`

## Quality checks

- [ ] `SKILL.md` describes concrete trigger contexts
- [ ] local mirror path is identified
- [ ] mirrored files are consulted before answering from memory
- [ ] normative CLIM text is separated from implementation notes
- [ ] citations point to local mirrored files
- [ ] sidecar references resolve
- [ ] if the spec is silent, the answer says so instead of improvising

## Failure handling

### Missing mirror or helper failure
- Verify `docs/clim-spec/.../index.html` exists.
- Run `scripts/validate-clim-skill.sh`.
- If the mirror is missing or broken, report that and do not pretend to have checked the spec.

### Ambiguous routing
- Use `references/chapter-routing.md`.
- If still ambiguous, search across the likely chapters and state that the topic is cross-cutting.

### McCLIM-only behavior with no clear spec hook
- Say it appears implementation-specific.
- Avoid overstating CLIM 2 requirements.

### Legacy/conflicting advice from old examples
- Re-check current chapter text.
- Use `F.html` to detect CLIM 1.x drift.
- Prefer current normative text over old folklore.

## Conflict policy

If another skill also looks relevant, prefer the more specific domain skill.
Use this skill whenever **spec-backed CLIM semantics** are part of the task, even if implementation work is also happening.
