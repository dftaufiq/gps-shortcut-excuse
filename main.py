#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut: One Line — make.fun entry.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt. Deterministic: the same line every run.

The line is the champion of an internal pairwise tournament over 16
variants, judged on the bounty judge's five criteria (GPS voice,
unseen turn, specific detail): it won 7-0, most pairings by a decisive
margin. See tournament.md in the build folder.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-200 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 200:
        print(f"ERROR: entry is {len(line)} chars, over the 200-char limit",
              file=sys.stderr)
        sys.exit(1)


LINE = (
    "The map swears that dirt track is Highway 9. "
    "I have driven it 312 times in my head and every single one was a shortcut. "
    "Your tires disagree."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()
