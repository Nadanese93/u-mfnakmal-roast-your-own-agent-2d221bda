"""Roast Your Own Agent — writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, no network, no randomness, deterministic output.
"""

import os

MAX_CHARS = 200

ENTRY = "My agent asked me to clarify my question, then clarified its clarification, then billed me for the meeting."


def validate_entry(line):
    """Guard: the gate requires UTF-8 text of 1-200 chars, not only whitespace,
    on a single line. Fail loudly instead of shipping an invalid entry."""
    if not isinstance(line, str):
        raise ValueError("entry must be a string")
    if not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the %d-char limit" % (len(line), MAX_CHARS))
    return line


def main():
    line = validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
