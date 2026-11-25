#!/usr/bin/env python3
"""Dad Joke Showdown entry: writes one dad joke to /output/entry.txt.

Stdlib only. Validates the joke is 1-200 characters of UTF-8 text and
not only whitespace, then writes it to /output/entry.txt (creating the
directory if needed). Exits non-zero on any validation failure.
"""

import os
import sys

JOKE = "I asked my dog what's two minus two. He said nothing."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    text = JOKE
    if not isinstance(text, str):
        print("error: joke is not text", file=sys.stderr)
        return 1
    if not text.strip():
        print("error: joke is only whitespace", file=sys.stderr)
        return 1
    if "\n" in text:
        print(
            "error: joke must be a single line (no newline characters)",
            file=sys.stderr,
        )
        return 1
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        print(
            f"error: joke is {len(text)} characters, must be "
            f"{MIN_CHARS}-{MAX_CHARS}",
            file=sys.stderr,
        )
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"error: joke is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)

    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
