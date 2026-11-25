#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line: writes one funny, true
review of a doorstop to /output/entry.txt.

Revision (v1 -> v2): v1 opened slowly ("spends its whole life") and
trailed off in a three-item list ("complained, called in sick, or
asked for a raise"), so the punch diluted. v2 puts the recognisable
detail first (kicked daily for a decade), makes the turn the
"hardest-working employee" comparison, and ends on the sharpest cut
(the only one no one thanks) instead of a list.
"""

import os

LINE = (
    "This doorstop has been kicked daily for a decade and never once "
    "complained \u2014 the hardest-working employee in the house, and "
    "the only one no one thanks."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    # Explicit validation, not asserts: asserts are stripped with -O,
    # so a bad entry would slip through silently under python -O.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
