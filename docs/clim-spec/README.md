# CLIM 2 Spec Mirror

This directory contains a local mirror of the HTML CLIM 2 specification from:

- `http://bauhh.dyndns.org:8000/clim-spec/index.html`

## Why this mirror exists

- gives KVC skills a stable local CLIM reference
- reduces repeat hits against the remote host
- makes agent lookups deterministic and scriptable
- supports offline-ish work once mirrored locally

## Mirror location

Canonical root:
- `docs/clim-spec/bauhh.dyndns.org:8000/clim-spec/`

Important files:
- `index.html` — landing page
- `contents.html` — full table of contents
- `theindex.html` — keyword index
- `F.html` — changes from CLIM 1.0
- `B.html`, `C.html`, `D.html` — appendices that matter often in implementation work

Current snapshot facts:
- ~184 HTML files
- 18 PNG assets
- ~4.5 MB mirrored corpus

## Refresh command

From repo root:

```bash
mkdir -p docs/clim-spec
cd docs/clim-spec
wget --mirror --convert-links --adjust-extension --page-requisites \
  --no-parent --no-verbose --show-progress \
  http://bauhh.dyndns.org:8000/clim-spec/index.html
```

## Helper lookup script

```bash
python3 skills/clim-spec/scripts/clim_spec_lookup.py --toc
python3 skills/clim-spec/scripts/clim_spec_lookup.py --query "application frame"
python3 skills/clim-spec/scripts/clim_spec_lookup.py --query "presentation translator" --files '23*.html' '27*.html'
```

## Normative caution

The mirrored HTML includes annotation links and annotation-playground material.
Treat the core spec body as normative; do not treat annotations/playground text as authoritative CLIM requirements.
