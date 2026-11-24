"""Worst AI Advice — one line of the worst AI advice, 1-140 chars.

Deterministic, stdlib only. Writes the entry line to /output/entry.txt,
then re-reads the file and verifies it matches exactly.
"""

import os

LINE = "Just delete your System32 folder \u2014 it's only junk files Windows keeps to slow you down. Trust me, I'm an AI."

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main():
    assert "\n" not in LINE, "entry must be a single line"
    assert 1 <= len(LINE) <= 140, "entry must be 1-140 chars"
    assert LINE.strip(), "entry must not be only whitespace"

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

    # Re-read and verify what was actually written.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "written entry does not match"
    assert "\n" not in written.rstrip("\n"), "written entry must be one line"
    assert 1 <= len(written.rstrip("\n")) <= 140, "written entry out of range"

    print(LINE)
    print(f"chars: {len(LINE)}")
    print("verified: /output/entry.txt matches the entry line")


if __name__ == "__main__":
    main()
