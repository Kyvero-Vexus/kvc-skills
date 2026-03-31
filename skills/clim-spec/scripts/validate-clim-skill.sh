#!/usr/bin/env bash
set -euo pipefail

repo_root=$(cd "$(dirname "$0")/../../.." && pwd)
skill_dir="$repo_root/skills/clim-spec"
spec_root="$repo_root/docs/clim-spec/bauhh.dyndns.org:8000/clim-spec"
mcclim_root="/home/slime/external_src/mcclim"
lookup="$skill_dir/scripts/clim_spec_lookup.py"
skill_file="$skill_dir/SKILL.md"

fail() {
  echo "FAIL: $*" >&2
  exit 1
}

[ -f "$skill_file" ] || fail "missing SKILL.md"
[ -f "$skill_dir/references/building-with-mcclim.md" ] || fail "missing building-with-mcclim reference"
[ -f "$skill_dir/references/full-spec-feature-map.md" ] || fail "missing full-spec-feature-map reference"
[ -f "$skill_dir/references/mcclim-example-map.md" ] || fail "missing mcclim-example-map reference"
[ -f "$skill_dir/references/eval-plan.md" ] || fail "missing eval-plan reference"
[ -f "$skill_dir/examples/minimal-app.lisp" ] || fail "missing minimal app example"
[ -f "$skill_dir/examples/presentation-table-app.lisp" ] || fail "missing presentation table example"
[ -f "$skill_dir/examples/gadget-form.lisp" ] || fail "missing gadget form example"
[ -x "$lookup" ] || fail "lookup helper is not executable"
[ -f "$spec_root/index.html" ] || fail "missing mirrored spec index"
[ -f "$spec_root/contents.html" ] || fail "missing mirrored spec contents"
[ -f "$mcclim_root/README.md" ] || fail "missing local McCLIM checkout"

rg -q "build.*CLIM applications on McCLIM|build working CLIM applications on McCLIM" "$skill_file" || fail "skill is not clearly build-oriented"
rg -q "full CLIM 2 feature surface|full-spec-feature-map" "$skill_file" "$skill_dir/references" || fail "skill does not clearly cover the full CLIM feature surface"
rg -q "Documentation/Manual/examples/ex1.lisp|Examples/text-gadgets.lisp|simple-spreadsheet" "$skill_file" "$skill_dir/references" || fail "skill does not reference concrete McCLIM examples"

python3 "$lookup" --toc >/dev/null || fail "lookup helper --toc failed"
python3 "$lookup" --query "application frame" --limit 1 >/dev/null || fail "lookup helper application-frame query failed"
python3 "$lookup" --query "presentation translator" --files '23*.html' '27*.html' --limit 1 >/dev/null || fail "lookup helper translator query failed"

echo "PASS: clim-spec skill is build-oriented, references McCLIM examples, and CLIM lookup sanity checks succeeded"
