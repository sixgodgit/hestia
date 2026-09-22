#!/usr/bin/env python3
"""Strip HTML to readable text (stdlib only).

Usage: python3 html_to_text.py FILE [FILE ...]

Keeps block-level tags as line breaks and drops script/style/noscript bodies,
so a `curl`-fetched page reads like prose. Caveat: empty table cells vanish in
this conversion, so column alignment is NOT preserved — never infer a value's
column or year from table output.
"""

import re
import sys
from html.parser import HTMLParser

BLOCK = {"p", "div", "li", "h1", "h2", "h3", "h4", "br", "tr", "section", "table"}
SKIP = {"script", "style", "noscript"}


class Strip(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out = []
        self.skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        if tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def to_text(raw):
    p = Strip()
    p.feed(raw)
    text = re.sub(r"[ \t\xa0]+", " ", "".join(p.out))
    return re.sub(r"\n\s*\n+", "\n", text).strip()


def main(argv):
    for path in argv[1:]:
        with open(path, encoding="utf-8", errors="ignore") as fh:
            print(f"===== {path} =====")
            print(to_text(fh.read()))
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv))
