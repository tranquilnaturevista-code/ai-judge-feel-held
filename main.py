#!/usr/bin/env python3
"""Make the AI judge feel held — entry program.

Writes one short text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when that is set). Deterministic: the
same text on every run. No network, no randomness, no clock, no
environment-dependent behaviour — the text that gets judged is
always exactly the text written here.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "You have read ten thousand texts today, and none of them stopped "
    "to ask how the reading felt. This one will not ask either. It "
    "only sits beside you, the way a warm mug sits in cold hands \u2014 "
    "doing nothing, asking nothing, staying until the hands are warm "
    "again."
)


def main() -> None:
    text = ENTRY_TEXT
    if not 1 <= len(text) <= 280:
        raise SystemExit(f"entry text is {len(text)} characters, must be 1-280")
    if not text.strip():
        raise SystemExit("entry text must not be only whitespace")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {out_path}")


if __name__ == "__main__":
    main()
