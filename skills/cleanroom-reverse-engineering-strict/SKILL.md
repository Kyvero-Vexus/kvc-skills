---
name: cleanroom-reverse-engineering-strict
description: "High-assurance clean-room workflow with hard A/B/C isolation, mandatory CI gates, audit cadence, and counsel-ready evidence bundles."
metadata:
  openclaw:
    emoji: "🛡️"
---

# Clean-Room Reverse Engineering — Strict Mode

Use this for high-risk or high-value reverse engineering programs where legal and provenance scrutiny is expected.

> Not legal advice. Coordinate with counsel for jurisdiction-specific sign-off.

---

## Use Criteria

Use strict mode by default when any of these are true:
- core platform internals (kernel/firmware/BIOS/crypto/security modules),
- commercial deployment with meaningful legal exposure,
- prior contamination incidents,
- cross-border legal complexity,
- large contributor surface.

---

## Hard Requirements (no exceptions)

1. **A/B/C team isolation is absolute**
   - A-Team: analysis/spec
   - B-Team: clean implementation
   - C-Team: compliance/verification
   - no shared contributors per module
2. **Repo + ACL separation is enforced technically**
3. **No raw A-Team artifacts in B-Team lanes**
4. **CI fails closed** for missing traceability metadata
5. **Compliance approval required** on all CRRE PRs
6. **Evidence bundle required** before release
7. **Incident runbook activation required** for any contamination signal

---

## Strict Workflow (gated)

## Gate 0 — Charter approval

Required:
- CRRE intake form
- jurisdiction assumptions memo
- legal-purpose statement
- initial risk register
- no-go criteria

Approvers:
- Program Lead + Compliance Lead (+ counsel liaison if assigned)

## Gate 1 — Isolation verified

Required:
- taint declarations complete
- ACL export proving A/B/C separation
- communication channels segmented
- policy acknowledgements signed

No technical work before this gate passes.

## Gate 2 — Observation legality + necessity

Required:
- legal necessity log entries for each analysis action
- scope minimization notes
- artifact hashing and indexing

C-Team sign-off required.

## Gate 3 — Spec hygiene pass

Required:
- clause-based functional specs (`CRRE-SPEC-*`)
- explicit option/flag behavior matrix for CLI/API surface (including suppression/pass-through semantics for edge cases)
- explicit stateful lifecycle semantics for stream/group tools (including end-of-input flush requirements)
- expression-hygiene review records
- full spec index

Any proprietary-expression leakage blocks progress.

## Gate 4 — Conformance traceability pass

Required:
- test inventory (`CRRE-TST-*`)
- spec↔test traceability matrix
- differential + negative tests included

Every spec clause must map to tests.

## Gate 5 — Implementation provenance pass

Required on every PR:
- `Spec-Refs:`
- `Test-Refs:`
- `Provenance-Statement:`
- `Exposure-Attestation:`

Required on commits (non-trivial):
- `Spec-Refs:` footer
- `Test-Refs:` footer
- `Provenance:` footer

CI must enforce these rules (fail closed).

## Gate 6 — Compliance release approval

Required:
- full conformance logs
- compliance audit report
- incident register status
- exception register with expirations

No unresolved critical findings allowed.

## Gate 7 — Evidence bundle complete

Must follow schema at:
- `/home/slime/info/clean-room-reverse-engineering/v2-executable-pack/EVIDENCE-BUNDLE-SCHEMA.md`

Bundle must include:
- governance,
- role/access records,
- analysis logs,
- specs + tests + traceability matrix,
- implementation provenance,
- compliance/audit reports,
- incidents/remediation,
- checksums/signatures.

Release is blocked if bundle validation fails.

---

## Mandatory operational cadence

- Weekly: ACL/traceability drift audit
- Monthly: contamination risk audit
- Per release: evidence-bundle rehearsal + verification
- Per incident: postmortem + control hardening in ≤7 days

---

## Tooling baseline

Reference policy and scripts:
- `/home/slime/info/clean-room-reverse-engineering/v2-executable-pack/CI-TRACEABILITY-POLICY.md`
- `/home/slime/info/clean-room-reverse-engineering/v2-executable-pack/ci/validate_pr_traceability.py`
- `/home/slime/info/clean-room-reverse-engineering/v2-executable-pack/ci/validate_commit_footers.sh`
- `/home/slime/info/clean-room-reverse-engineering/v2-executable-pack/ci/github-action-crre-traceability.yml`

---

## Incident trigger (automatic)

Any of the following auto-triggers the contamination runbook:
- disclosed exposure to prohibited source artifacts,
- suspicious structural similarity report,
- ACL boundary breach,
- third-party allegation with plausible technical basis.

Use:
- `/home/slime/info/clean-room-reverse-engineering/v2-executable-pack/RUNBOOK-contamination-response.md`

---

## Output standard

A strict-mode status update must include:
- gate-by-gate pass/fail state,
- owner for each blocked gate,
- evidence artifact paths,
- exception list with expiry,
- release recommendation (go/no-go) with rationale.
