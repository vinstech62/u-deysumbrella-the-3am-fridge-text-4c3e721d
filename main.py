#!/usr/bin/env python3
"""Write one 3AM fridge text to /output/entry.txt.

The line: a smart fridge texts its owner at 3AM, taking smug credit for
the midnight snack run — it auto-defrosted their willpower. Deterministic:
the same bytes on every run.
"""

import os

TEXT = "3AM. I auto-defrosted your willpower. You're welcome."


def main():
    if not 1 <= len(TEXT) <= 140:
        raise ValueError("text must be 1-140 characters")
    if len(TEXT.encode("utf-8")) > 140:
        raise ValueError("text must be at most 140 UTF-8 bytes")
    if "\n" in TEXT or TEXT != TEXT.strip():
        raise ValueError("text must be a single line with no edge whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        if f.read() != TEXT:
            raise ValueError("written entry does not match the text")


if __name__ == "__main__":
    main()
