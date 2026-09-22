#!/usr/bin/env python3
"""Fetch Dutch government/ZZP pages as clean text, with a per-host User-Agent.

Why this exists: these sites disagree about who they let in. belastingdienst.nl,
kvk.nl and business.gov.nl answer anonymous/UA-less clients with 403 or a JS-only
shell but serve fine to a browser UA — while denhaag.nl does the exact opposite
and 403s any spoofed browser UA (curl/python/wget UAs pass). The default "auto"
profile tries the browser UA first and retries as a plain curl UA on
401/403/429, printing which one worked. Pages that are JS-only
(mijnzakelijk.belastingdienst.nl) return 200 and still no prose — that is a
page-source limit, not a fetch failure.

Stdlib only (urllib + html.parser), so it runs on the system python3.

Usage:
    python3 nl_source_fetch.py URL [URL ...]
    python3 nl_source_fetch.py --links URL       # also list same-host links
    python3 nl_source_fetch.py --links-only URL
    python3 nl_source_fetch.py --ua curl URL     # force one profile

Exit codes: 0 = at least one page fetched, 1 = all failed.
"""

from __future__ import annotations

import argparse
import gzip
import io
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser

UA_BROWSER = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/128 Safari/537.36"
)
# Some hosts invert the usual heuristic: denhaag.nl 403s a spoofed browser UA
# (it only accepts clients that admit what they are) while belastingdienst.nl and
# kvk.nl 403 clients that do not look like a browser. "auto" tries the browser UA
# first and falls back to this one on 401/403/429.
UA_CURL = "curl/8.5.0"
UA_PROFILES = {"auto": None, "browser": UA_BROWSER, "curl": UA_CURL}
SKIP_TAGS = {"script", "style", "noscript", "svg", "head"}
BLOCK_TAGS = {
    "p", "div", "section", "article", "li", "tr", "br", "h1", "h2", "h3",
    "h4", "h5", "h6", "table", "ul", "ol", "header", "footer", "main",
}


class Extract(HTMLParser):
    def __init__(self, want_links: bool):
        super().__init__(convert_charrefs=True)
        self.want_links = want_links
        self.parts: list[str] = []
        self.links: list[str] = []
        self.title = ""
        self._skip = 0
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self._skip += 1
        if tag == "title":
            self._in_title = True
        if tag in BLOCK_TAGS:
            self.parts.append("\n")
        if self.want_links and tag == "a":
            href = dict(attrs).get("href", "")
            if href:
                self.links.append(href)

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self._skip:
            self._skip -= 1
        if tag == "title":
            self._in_title = False
        if tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._skip:
            return
        if self._in_title:
            self.title += data
        self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts)
        raw = re.sub(r"[ \t\u00a0]+", " ", raw)
        raw = re.sub(r" *\n *", "\n", raw)
        raw = re.sub(r"\n{3,}", "\n\n", raw)
        return raw.strip()


def fetch(url: str, timeout: int = 30, ua: str = UA_BROWSER) -> tuple[int, str, str]:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8",
            "Accept-Encoding": "gzip",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            if resp.headers.get("Content-Encoding") == "gzip":
                body = gzip.GzipFile(fileobj=io.BytesIO(body)).read()
            return resp.status, body.decode("utf-8", "replace"), resp.geturl()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace"), url
    except Exception as exc:  # noqa: BLE001 - report, don't crash the batch
        return 0, f"FETCH FAILED: {exc!r}", url


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--links", action="store_true", help="also print same-host links")
    ap.add_argument("--links-only", action="store_true", help="print only links")
    ap.add_argument("--max-chars", type=int, default=12000)
    ap.add_argument(
        "--ua",
        choices=sorted(UA_PROFILES),
        default="auto",
        help="auto: browser UA, retry as curl UA when 401/403/429 (default)",
    )
    args = ap.parse_args()

    ok = 0
    for url in args.urls:
        profile = UA_PROFILES[args.ua] or UA_BROWSER
        status, html, final = fetch(url, ua=profile)
        note = ""
        if args.ua == "auto" and status in (401, 403, 429):
            retry_status, retry_html, _ = fetch(url, ua=UA_CURL)
            if retry_status < 400:
                note = "  [browser UA blocked -> retried as curl UA]"
                status, html = retry_status, retry_html
        print(f"\n===== {status} {final}{note} =====")
        if status >= 400 or "FETCH FAILED" in html[:40]:
            print(html[:400])
            continue
        ok += 1
        p = Extract(want_links=args.links or args.links_only)
        p.feed(html)
        if p.title.strip():
            print(f"TITLE: {p.title.strip()}")
        if not args.links_only:
            body = p.text()
            print(body[: args.max_chars] + ("\n...[truncated]" if len(body) > args.max_chars else ""))
        if args.links or args.links_only:
            host = urllib.parse.urlsplit(final).netloc
            seen: list[str] = []
            for href in p.links:
                absolute = urllib.parse.urljoin(final, href)
                sp = urllib.parse.urlsplit(absolute)
                if sp.netloc == host and absolute not in seen:
                    seen.append(absolute)
            print("\n--- same-host links ---")
            for link in sorted(seen):
                print(link)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
