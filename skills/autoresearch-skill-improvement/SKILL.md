---
name: autoresearch-skill-improvement
description: "Use when iteratively improving SKILL.md behavior with an autonomous keep/discard experiment loop inspired by karpathy/autoresearch. Best for measurable skill-quality optimization with benchmark prompts."
compatibility: Designed for OpenClaw/Codex workflows where a skill can be evaluated repeatedly with a numeric score.
metadata:
  openclaw:
    emoji: "🔁"
---

# Autoresearch Skill Improvement

Use this to run a disciplined experiment loop for skill improvements, inspired by `karpathy/autoresearch`.

Primary reference:
- `https://github.com/karpathy/autoresearch`

Optional local checkout path (if your environment follows this convention):
- `~/external_src/autoresearch`

## Goal
Improve a target skill through repeated small mutations, keeping only changes that improve a measurable benchmark.

## Capability Delta (required)
Before starting, write one sentence:

> "After this run, `<skill>` should reliably improve `<metric>` on `<benchmark suite>` compared to baseline."

If you cannot define a measurable metric, stop and design one first.

---

## Triggers

Use this skill when user asks to:
- improve an existing skill through repeated experiments,
- run autonomous optimization over prompt/skill instructions,
- do “autoresearch” for skills,
- keep/discard changes based on benchmark results.

Do **not** use this skill for one-off edits with no evaluation loop.

---

## Inputs Required (hard gate)

You must have all 4:
1. `TARGET_SKILL_PATH` (e.g., `skills/foo/SKILL.md`)
2. `BENCHMARK_COMMAND` (single command that returns parsable numeric score)
3. `SCORE_DIRECTION` (`higher-better` or `lower-better`)
4. `RUN_TAG` (short unique experiment tag)

Optional:
- `MAX_ITERS`
- `MAX_HOURS`
- `TIMEOUT_PER_RUN`

If any hard input is missing, ask once and stop.

---

## Experiment Repo Safety

- Never run this loop on `main`.
- Create an isolated branch: `skill-autoresearch/<run-tag>`.
- Commit each candidate mutation before benchmarking.
- Keep benchmark artifacts out of permanent commits unless explicitly requested.

---

## Procedure

## 1) Setup

1. Confirm repo is clean enough to branch safely.
2. Create and switch branch `skill-autoresearch/<run-tag>`.
3. Create `results.tsv` in run workspace with header:

```tsv
iter	commit	score	delta	status	description
```

4. Record baseline:
   - run `BENCHMARK_COMMAND`
   - parse score
   - commit hash = current HEAD
   - `status=keep`, `description=baseline`

## 2) Mutation policy

Per iteration, change only one conceptual dimension:
- trigger phrasing,
- workflow ordering,
- output contract strictness,
- quality-check granularity,
- failure-handling behavior,
- sidecar/reference decomposition.

Avoid multi-axis changes unless prior iterations plateau.

## 3) Keep/Discard loop

For each iteration:

1. edit skill artifacts
2. `git add` + `git commit`
3. run `BENCHMARK_COMMAND` with timeout
4. parse numeric score
5. compare against current best
6. log to `results.tsv`

Decision rule:
- if better → `status=keep`
- else → `status=discard` and reset to previous best commit

Crash rule:
- if benchmark fails/no score, log `status=crash` and revert

## 4) Periodic consolidation

Every 5–10 iterations:
- summarize win rate,
- identify best mutation classes,
- prune noisy patterns,
- optionally tighten benchmark rubric if gaming is detected.

## 5) Finish criteria

Stop when one is true:
- `MAX_ITERS` or `MAX_HOURS` reached,
- no improvement across last N (default 10) valid iterations,
- user interrupts.

At finish, report:
- baseline vs best score,
- kept/discarded/crashed counts,
- top 3 successful mutation patterns,
- final diff summary.

---

## Output Contract

Return all of:

1. branch name and best commit hash
2. best score, baseline score, delta
3. `results.tsv` path
4. concise changelog of kept improvements
5. unresolved risks/regressions
6. recommendation: merge / continue / abandon

---

## Quality Checks (binary)

- [ ] Branch isolation used (`skill-autoresearch/<tag>`)
- [ ] Baseline recorded before first mutation
- [ ] Every iteration committed before benchmark run
- [ ] Every iteration logged in `results.tsv`
- [ ] Non-improving runs reverted
- [ ] Final report includes baseline/best/delta

If any check fails, run is incomplete.

---

## Failure Handling

If benchmark command is flaky:
- retry once,
- if still flaky, mark `crash`, revert, continue.

If score parser breaks:
- fail fast,
- fix parser/command,
- rerun baseline before resuming loop.

If benchmark is gameable:
- add adversarial prompts,
- add rubric constraints,
- invalidate suspicious gains.

---

## Practical Mapping to karpathy/autoresearch

- `train.py` mutations → `SKILL.md` / sidecar mutations
- `val_bpb` → skill benchmark score
- `keep/discard` by metric → same logic
- `results.tsv` ledger → same concept
- autonomous overnight loop → same operational mode if explicitly requested by user
