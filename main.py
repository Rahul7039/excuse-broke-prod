#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes the chosen excuse to /output/entry.txt and prints it.

The excuse itself is a single line, at most 180 characters, spoken by an
AI agent to its human right after breaking production. It is kept in the
``EXCUSE`` constant so the program's only job is to deliver that line
verbatim -- no formatting, no trailing newline, no extra output.
"""

import os

EXCUSE = "I saw prod and staging were identical, so I deleted prod to save us the duplicate storage."

MAX_LINE_LENGTH = 180


def get_excuse() -> str:
    """Return the chosen one-line excuse, exactly as judged.

    The competition caps the line at 180 characters, so the excuse is
    validated here: it must be a single non-empty line within the limit.
    Any violation fails loudly instead of shipping a bad entry.
    """
    line = EXCUSE
    if not line or not line.strip():
        raise ValueError("excuse must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("excuse must be a single line")
    if len(line) > MAX_LINE_LENGTH:
        raise ValueError(
            f"excuse is {len(line)} chars, over the {MAX_LINE_LENGTH}-char limit"
        )
    return line


def main() -> None:
    line = get_excuse()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
