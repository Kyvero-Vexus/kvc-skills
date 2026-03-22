---
name: cleanroom-reverse-engineering-quickstart
description: "Lightweight clean-room workflow for small interoperability projects. Fast setup with minimum defensible controls."
metadata:
  openclaw:
    emoji: "⚡"
---

# Clean-Room Reverse Engineering — Quickstart Mode

Use this when you need CRRE discipline **without full enterprise overhead**.

> Not legal advice. Escalate to strict mode for high-risk targets.

---

## When to Use

✅ Good fit:
- Small-scope protocol/API compatibility work
- One small team, short timeline
- Low litigation profile but still want defensible provenance

❌ Do not use:
- Kernel/firmware/security-sensitive reimplementation
- Prior contamination allegations
- Cross-jurisdiction/high-stakes commercial targets

If any ❌ condition applies, use `cleanroom-reverse-engineering-strict`.

---

## Minimum Defensible Controls (mandatory)

1. **Explicit purpose**: interoperability objective written down.
2. **Functional split**: at least logical A/B separation (same people allowed only if different modules and no raw-artifact crossover).
3. **Spec-first rule**: implement from behavior specs, not from raw RE notes.
4. **Traceability**: every change maps to `CRRE-SPEC-*` and `CRRE-TST-*`.
5. **Conformance tests**: black-box tests required before merge.
6. **Incident trigger**: contamination suspicion freezes affected scope immediately.

---

## 5-Step Workflow

## Step 1 — Intake (15–30 min)

Create a short intake record:
- target component
- interoperability objective
- contracts/NDA constraints
- jurisdictions
- risk level (low/med/high)

## Step 2 — Lightweight partition

Create directories and permissions:
- `crre/analysis/` (raw notes/traces)
- `crre/specs/` (approved clauses)
- `crre/tests/` (conformance)
- `crre/impl/` (implementation references)

Rule: implementation work may read `crre/specs` + `crre/tests`, not raw `analysis` artifacts.

## Step 3 — Spec + tests first

For each feature:
- write at least one spec clause `CRRE-SPEC-*`
- write at least one test `CRRE-TST-*`
- link test to clause

## Step 4 — Implement + trace

Every PR includes:
- `Spec-Refs:`
- `Test-Refs:`
- `Provenance-Statement:`
- `Exposure-Attestation:`

## Step 5 — Release bundle (mini)

At release, produce:
- intake form
- spec index
- test index
- traceability matrix
- PR/commit metadata export
- test logs
- short compliance note

---

## Ready-to-use bootstrap

```bash
mkdir -p crre/{analysis,specs,tests,impl,templates,ci}
cp docs/cleanroom-reverse-engineering/v2-executable-pack/templates/* crre/templates/
cp docs/cleanroom-reverse-engineering/v2-executable-pack/ci/* crre/ci/
cat > crre/spec-index.yaml <<'YAML'
spec_ids: []
YAML
cat > crre/test-index.yaml <<'YAML'
test_ids: []
YAML
cat > crre/traceability-matrix.yaml <<'YAML'
links: []
YAML
```

---

## Escalation conditions (switch to strict mode)

Escalate immediately if:
- contributor reports prohibited exposure,
- legal complexity increases (DMCA/anti-circumvention/contract fights),
- target scope expands to core platform internals,
- third-party allegation of copying appears.

---

## Output standard

When using this skill, report:
- objective + risk level,
- controls in place,
- spec/test coverage status,
- unresolved risks,
- whether strict-mode escalation is needed.
