#!/usr/bin/env python3
"""Fetch pages with a real headless Firefox through geckodriver.

Rung 2 of the fetch ladder: use this when `nl_source_fetch.py` returns 403/429
from a host, or 200 with no prose (JS-rendered page), or when you need the page
as a user actually sees it. A real browser presents a coherent TLS + header
fingerprint, so crude per-host UA heuristics pass — but you also get the page's
own chrome (cookie-consent banners included) rather than a clean text body.

Stdlib only: a hand-rolled WebDriver client over HTTP, no selenium. Runs on the
system python3.

Requirements:
    geckodriver on PATH (snap: /snap/bin/geckodriver) and Firefox installed.
    Nothing to install for this script itself.

Usage:
    python3 firefox_fetch.py URL [URL ...]
    python3 firefox_fetch.py --max-chars 4000 URL
    python3 firefox_fetch.py --profile /home/you/ff-wd-profile URL

Snap-Firefox trap: the snap `home` interface cannot read hidden directories, so
a profile under ~/.cache/... makes session creation fail with "Failed to set
preferences: unknown error". Default here is ~/ff-wd-profile (not hidden).
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request

READ_RETURN = (
    "return [document.title, document.body.innerText.length, "
    "document.body.innerText.slice(0, %d)];"
)


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def wd(port: int, method: str, path: str, payload=None, timeout: int = 120):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(
        f"http://127.0.0.1:{port}{path}",
        data=data,
        method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.status, json.loads(resp.read() or b"{}")
    except urllib.error.HTTPError as exc:
        return exc.code, json.loads(exc.read() or b"{}")
    except Exception as exc:  # noqa: BLE001
        return 0, {"value": {"error": repr(exc)}}


def wait_ready(port: int, timeout: float = 20.0) -> bool:
    deadline = time.time() + timeout
    while time.time() < deadline:
        status, body = wd(port, "GET", "/status", timeout=3)
        if status == 200 and body.get("value", {}).get("ready"):
            return True
        time.sleep(0.3)
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--max-chars", type=int, default=8000)
    ap.add_argument("--profile", default=os.path.expanduser("~/ff-wd-profile"))
    ap.add_argument("--port", type=int, default=0, help="0 = pick a free port")
    args = ap.parse_args()

    driver = shutil.which("geckodriver")
    if not driver:
        print("geckodriver not found on PATH (snap users: /snap/bin/geckodriver)", file=sys.stderr)
        return 1
    os.makedirs(args.profile, exist_ok=True)

    port = args.port or free_port()
    proc = subprocess.Popen(
        [driver, "--port", str(port)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    ok = 0
    try:
        if not wait_ready(port):
            print("geckodriver did not become ready", file=sys.stderr)
            return 1
        status, body = wd(port, "POST", "/session", {"capabilities": {"alwaysMatch": {
            "browserName": "firefox",
            "moz:firefoxOptions": {"args": ["-headless", "-profile", args.profile]},
        }}})
        if status != 200:
            print(f"session not created: {status} {json.dumps(body)[:400]}", file=sys.stderr)
            return 1
        sid = body["value"]["sessionId"]
        try:
            for url in args.urls:
                t0 = time.time()
                nav, nav_body = wd(port, "POST", f"/session/{sid}/url", {"url": url})
                exec_status, res = wd(port, "POST", f"/session/{sid}/execute/sync", {
                    "script": READ_RETURN % args.max_chars,
                    "args": [],
                })
                print(f"\n===== firefox nav={nav} exec={exec_status} "
                      f"{time.time() - t0:.1f}s {url} =====")
                if nav != 200:
                    print(json.dumps(nav_body)[:400])
                    continue
                val = res.get("value", [])
                title, length, text = (val + [None] * 3)[:3]
                print(f"TITLE: {title}  (innerText {length} chars)")
                print(text or "")
                ok += 1
        finally:
            wd(port, "DELETE", f"/session/{sid}", timeout=30)
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=10)
        except subprocess.TimeoutExpired:
            proc.kill()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
