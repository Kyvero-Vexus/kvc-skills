#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/../../.." && pwd)
skill_dir="$repo_root/skills/clim-spec"
spec_root="$repo_root/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec"
lookup="$skill_dir/scripts/clim_spec_lookup.py"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

[ -f "$skill_dir/SKILL.md" ] || fail "missing SKILL.md"
[ -f "$skill_dir/references/chapter-routing.md" ] || fail "missing chapter-routing reference"
[ -f "$skill_dir/references/eval-plan.md" ] || fail "missing eval-plan reference"
[ -f "$skill_dir/examples/answer-template.md" ] || fail "missing answer template"
[ -x "$lookup" ] || fail "lookup helper is not executable"
[ -f "$spec_root/index.html" ] || fail "missing mirrored spec index"
[ -f "$spec_root/contents.html" ] || fail "missing mirrored spec contents"

python3 "$lookup" --toc >/dev/null || fail "lookup helper --toc failed"
python3 "$lookup" --query "application frame" --limit 1 >/dev/null || fail "lookup helper application-frame query failed"
python3 "$lookup" --query "presentation translator" --files '23*.html' '27*.html' --limit 1 >/dev/null || fail "lookup helper translator query failed"

echo "PASS: clim-spec skill structure and lookup sanity checks succeeded"
