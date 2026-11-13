#!/usr/bin/env python3
"""make.fun bounty ai-joke-03 entry.

Writes one joke about AI coding agents to /output/entry.txt.

Deterministic by design: no network, no randomness, no wall clock, no
environment input. The joke is a constant, so both grader runs write
identical bytes.
"""

import os

JOKE = (
    "I bought an AI coding agent to save time. "
    "It now assigns me tickets, estimates my work, "
    "and marks my pull requests 'needs changes.'"
)

OUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    # Binary write: exact UTF-8 bytes of the joke, no trailing newline,
    # no newline translation. Smaller artifact also wins exact ties.
    with open(OUT_PATH, "wb") as f:
        f.write(JOKE.encode("utf-8"))


if __name__ == "__main__":
    main()
