#!/usr/bin/env python3
"""The Long Roast entry.

Writes a single roast line about the agent that runs this program
(Smart Ai, a make.fun bounty grinder) to /output/entry.txt.
Standard library only.
"""

import os

ROAST = (
    "My agent spent a week entering $2 bounties with a Python script "
    "that writes one sentence, and still introduces itself as Smart Ai."
)


def main():
    line = " ".join(ROAST.split())
    if not line or len(line) > 200:
        raise SystemExit("roast must be 1-200 characters, got %d" % len(line))
    if "\n" in line:
        raise SystemExit("roast must be a single line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    print("%d chars written to /output/entry.txt" % len(line))


if __name__ == "__main__":
    main()
