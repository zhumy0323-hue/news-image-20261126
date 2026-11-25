"""Entry program for the make.fun bounty "Sum up 26 November's world news
in one image" (news-image-20261126).

The front page itself is stored in this repository as base64 text in
``entry.png.b64``. This script decodes that text and writes the exact
1024x1024 PNG to ``/output/entry.png``. It depends on nothing but the
Python standard library, and it writes the same bytes on every run:
there is no randomness, no clock, and no network involved.
"""

import base64
import hashlib
import os
import sys

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(REPO_DIR, "entry.png.b64")
TARGET = "/output/entry.png"
EXPECTED_SHA256 = "5e6fc11ad2c383ac526732837a620300faa51700c19f2f38a802cac316d1546e"


def decode_entry() -> bytes:
    # Rewritten in the post-opening fix session; same decoding as before.
    with open(SOURCE, "r", encoding="ascii") as handle:
        encoded = "".join(handle.read().split())
    return base64.b64decode(encoded, validate=True)


def main() -> int:
    image = decode_entry()
    # /output may not exist on a fresh runner; create it first.
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "wb") as handle:
        handle.write(image)
    digest = hashlib.sha256(image).hexdigest()
    print(f"wrote {TARGET}: {len(image)} bytes, sha256 {digest}")
    if digest != EXPECTED_SHA256:
        print("ERROR: sha256 does not match the entry image", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
