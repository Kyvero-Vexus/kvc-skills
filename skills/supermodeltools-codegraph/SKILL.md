---
name: supermodeltools-codegraph
description: "Use Supermodel API/MCP to generate code graphs and static analysis artifacts (dependency/call/domain/impact/dead-code/test-coverage/circular deps). Best for architecture mapping, blast-radius analysis, and clean-room spec planning."
metadata:
  openclaw:
    emoji: "🕸️"
---

# Supermodel Tools Codegraph Skill

Use this skill when you need machine-generated structural understanding of a repository.

## Best-fit use cases

- clean-room planning (A-Team artifact generation)
- blast-radius mapping for risky edits
- dependency/call graph understanding before implementation
- dead-code and circular-dependency audits
- static test-coverage reachability mapping

## External action rule (important)

Supermodel requests upload repository snapshots to an external API.
Only run this when user intent clearly allows external processing for that repo.

---

## Prerequisites

- API key available as env var: `SUPERMODEL_API_KEY`
- API base (default): `https://api.supermodeltools.com`
- Docs: `https://docs.supermodeltools.com`
- OpenAPI: `https://docs.supermodeltools.com/openapi.yaml`

Local harvested references:
- `~/external_docs/supermodeltools/SUMMARY-2026-03-21.md`
- `~/external_docs/supermodeltools/docs-site/openapi.yaml`
- `~/external_src/supermodeltools/mcp`
- `~/external_src/supermodeltools/typescript-sdk`
- `~/external_src/supermodeltools/openapi-spec`

---

## Endpoints to use

Graphs:
- `POST /v1/graphs/dependency`
- `POST /v1/graphs/call`
- `POST /v1/graphs/domain`
- `POST /v1/graphs/parse`
- `POST /v1/graphs/supermodel`

Analysis:
- `POST /v1/analysis/dead-code`
- `POST /v1/analysis/test-coverage-map`
- `POST /v1/analysis/circular-dependencies`
- `POST /v1/analysis/impact` (supports optional `diff` and `targets`)

Always include:
- `X-Api-Key`
- `Idempotency-Key`

---

## Recommended workflow

1. **Choose minimal endpoint set** (avoid API spam):
   - architecture map: dependency + domain
   - function behavior: call + parse
   - risk review: impact + circular-dependencies
2. **Use stable idempotency keys** per repo+commit+endpoint.
3. **Poll responsibly** (`retryAfter` if present, otherwise 4–10s).
4. **Cache outputs** in workspace before re-calling API.
5. **Summarize findings into clean-room artifacts** (spec clauses/test plans), not direct code copying.

---

## Clean-room integration guidance

When used in clean-room programs:

- A-Team may use Supermodel outputs to build:
  - domain and dependency maps,
  - affected-function lists,
  - impact boundaries,
  - candidate behavior/test matrices.
- B-Team should consume approved specs/tests only.
- C-Team should verify:
  - artifact traceability,
  - contamination controls,
  - consistency between claimed scope and graph evidence.

Supermodel should accelerate structure discovery, not replace clean-room governance.

---

## Quick command (helper script)

Helper script included:
- `skills/supermodeltools-codegraph/scripts/supermodel_request.py`

Example: dependency graph

```bash
python3 skills/supermodeltools-codegraph/scripts/supermodel_request.py \
  --endpoint /v1/graphs/dependency \
  --repo-dir /path/to/repo \
  --idempotency-key myrepo-$(git -C /path/to/repo rev-parse --short HEAD)-dep \
  --output /tmp/supermodel-dependency.json
```

Example: impact analysis with diff

```bash
git -C /path/to/repo diff main...HEAD > /tmp/changes.diff
python3 skills/supermodeltools-codegraph/scripts/supermodel_request.py \
  --endpoint /v1/analysis/impact \
  --repo-dir /path/to/repo \
  --diff-file /tmp/changes.diff \
  --idempotency-key myrepo-$(git -C /path/to/repo rev-parse --short HEAD)-impact \
  --output /tmp/supermodel-impact.json
```

---

## Output contract (for agent use)

Return:
1. endpoint(s) executed,
2. input snapshot basis (repo path + commit),
3. status (`completed|failed|error`) + job IDs,
4. concise findings (top structural insights),
5. files written,
6. recommended next clean-room action.

If API call fails, include the error category and one actionable retry/fix path.
