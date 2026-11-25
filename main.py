#!/usr/bin/env python3
"""Entry point for the make.fun news-image-20261126 bounty, version 2.

Decodes the base64 front-page image shipped alongside this file and
writes it to /output/entry.png, then checks the result against the
expected SHA-256. Pure standard library, no network, no randomness:
two runs produce byte-identical output.

Run:  python3 main.py
"""

import base64
import hashlib
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
B64_PATH = os.path.join(HERE, "entry.png.b64")
OUT_PATH = "/output/entry.png"

# SHA-256 of the v2 front-page image (1024x1024 PNG, 181,462 bytes),
# built 2026-11-26 ~10:35 CST from that morning's world news.
EXPECTED_SHA256 = "dc0149e178f89ab886c6b1754bd01d3048356359deabe0ec3df1dd5bd5fca06a"


def decode_entry():
    """Read the bundled base64 payload and return the raw PNG bytes.

    The decode is deterministic: the same payload always yields the
    same bytes, so repeated runs are byte-identical by construction.
    """
    with open(B64_PATH, "r", encoding="ascii") as handle:
        payload = handle.read().strip()
    return base64.b64decode(payload, validate=True)


def main():
    image = decode_entry()
    digest = hashlib.sha256(image).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"SHA-256 mismatch: got {digest}, expected {EXPECTED_SHA256}",
              file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "wb") as handle:
        handle.write(image)
    print(f"wrote {OUT_PATH} ({len(image)} bytes, sha256 {digest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
