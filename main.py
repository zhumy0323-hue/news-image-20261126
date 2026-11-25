#!/usr/bin/env python3
"""Decode the bundled news front page and write it to /output/entry.png.

The entry image ships as base64 text in entry.png.b64 next to this
script, so the entrypoint needs nothing but the Python standard library
and no network access. Running it twice produces byte-identical output.
"""

import base64
import hashlib
import pathlib
import sys

SOURCE = pathlib.Path(__file__).resolve().parent / "entry.png.b64"
TARGET = pathlib.Path("/output/entry.png")

EXPECTED_SHA256 = (
    "5e6fc11ad2c383ac526732837a620300faa51700c19f2f38a802cac316d1546e"
)


def main() -> int:
    encoded = SOURCE.read_text(encoding="ascii").strip()
    image_bytes = base64.b64decode(encoded, validate=True)

    TARGET.parent.mkdir(parents=True, exist_ok=True)
    # The output is a fixed byte sequence: same input, same file, every run.
    TARGET.write_bytes(image_bytes)

    digest = hashlib.sha256(image_bytes).hexdigest()
    print(f"wrote {TARGET} ({len(image_bytes)} bytes)")
    print(f"sha256: {digest}")
    if digest != EXPECTED_SHA256:
        print(f"error: expected sha256 {EXPECTED_SHA256}", file=sys.stderr)
        return 1
    print("sha256 matches the expected value")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
