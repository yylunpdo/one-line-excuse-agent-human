#!/usr/bin/env python3
"""One-line excuse entry for the make.fun bounty.

Writes a single line (94 characters) to /output/entry.txt.
Pure Python standard library only.
"""

import os

ENTRY = "Sorry I'm late — I delegated the deadline to a subagent, and it delegated it right back to me."
# The em dash above is U+2014; the line is exactly 94 characters, one line,
# no trailing newline, so the sealed scorer reads it byte-identical.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
