#!/usr/bin/env python3
"""Run Supermodel API graph/analysis requests with polling.

Examples:
  python3 supermodel_request.py \
    --endpoint /v1/graphs/dependency \
    --repo-dir /path/to/repo

  python3 supermodel_request.py \
    --endpoint /v1/analysis/impact \
    --repo-dir /path/to/repo \
    --diff-file /path/to/changes.diff
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import uuid
import zipfile
from pathlib import Path
from urllib.parse import urlencode


def zip_repo(repo_dir: Path, out_zip: Path) -> None:
    exclude_dirs = {".git", "node_modules", "dist", "build", "target", "__pycache__", ".next"}
    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(repo_dir):
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            for name in files:
                p = Path(root) / name
                rel = p.relative_to(repo_dir)
                zf.write(p, rel.as_posix())


def call_api(
    base_url: str,
    endpoint: str,
    api_key: str,
    idem_key: str,
    zip_path: Path,
    diff_file: Path | None,
    targets: list[str],
) -> dict:
    url = base_url.rstrip("/") + endpoint
    if targets:
        url += "?" + urlencode({"targets": ",".join(targets)})

    cmd = [
        "curl",
        "-sS",
        "-X",
        "POST",
        url,
        "-H",
        f"Idempotency-Key: {idem_key}",
        "-H",
        f"X-Api-Key: {api_key}",
        "-F",
        f"file=@{zip_path};type=application/zip",
    ]
    if diff_file:
        cmd += ["-F", f"diff=@{diff_file};type=text/plain"]

    out = subprocess.check_output(cmd, text=True)
    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return {"status": "error", "error": "non-json", "raw": out[:2000]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--endpoint", required=True)
    ap.add_argument("--repo-dir", required=True)
    ap.add_argument("--base-url", default="https://api.supermodeltools.com")
    ap.add_argument("--api-key-env", default="SUPERMODEL_API_KEY")
    ap.add_argument("--idempotency-key", default="")
    ap.add_argument("--diff-file", default="")
    ap.add_argument("--targets", nargs="*", default=[])
    ap.add_argument("--poll-interval", type=int, default=4)
    ap.add_argument("--max-attempts", type=int, default=90)
    ap.add_argument("--output", default="")
    args = ap.parse_args()

    api_key = os.environ.get(args.api_key_env, "")
    if not api_key:
        print(
            f"ERROR: missing API key in env var {args.api_key_env}. "
            "Set it before running.",
            file=sys.stderr,
        )
        return 2

    repo_dir = Path(args.repo_dir).resolve()
    if not repo_dir.exists() or not repo_dir.is_dir():
        print(f"ERROR: repo-dir not found: {repo_dir}", file=sys.stderr)
        return 2

    diff_file = Path(args.diff_file).resolve() if args.diff_file else None
    if diff_file and not diff_file.exists():
        print(f"ERROR: diff-file not found: {diff_file}", file=sys.stderr)
        return 2

    idem_key = args.idempotency_key or f"openclaw-supermodel-{uuid.uuid4()}"

    with tempfile.TemporaryDirectory(prefix="supermodel-zip-") as td:
        zip_path = Path(td) / "repo.zip"
        zip_repo(repo_dir, zip_path)

        last = {}
        for attempt in range(1, args.max_attempts + 1):
            last = call_api(
                base_url=args.base_url,
                endpoint=args.endpoint,
                api_key=api_key,
                idem_key=idem_key,
                zip_path=zip_path,
                diff_file=diff_file,
                targets=args.targets,
            )
            status = str(last.get("status", "unknown"))
            job = last.get("jobId", "")
            print(f"attempt={attempt} status={status} jobId={job}", file=sys.stderr)

            if status in {"completed", "failed", "error"}:
                break

            retry_after = last.get("retryAfter")
            sleep_s = int(retry_after) if isinstance(retry_after, int) else args.poll_interval
            time.sleep(max(1, sleep_s))

    rendered = json.dumps(last, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
        print(f"wrote {args.output}", file=sys.stderr)
    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
