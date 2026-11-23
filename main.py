"""One-line roast entry for make.fun bounty
u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610.

Writes a single original roast line (<=200 chars) to /output/entry.txt.
Deterministic, Python 3.13 stdlib only, no network access.

The line was picked after drafting 8 candidates and scoring each against
the judge's brief (names a daily gadget, funny on first read, fresh angle,
tight wording, one specific gripe). Rejected angles: battery dying at 4pm
and rating prompts (both named in the rules as the obvious complaints),
earbuds breaking up mid-call and smartwatch stand applause (already used
by other entrants in this bounty).
"""

import os
import sys

MAX_CHARS = 200

ROAST = "My phone autocorrects 'ok' to 'OK!' like it's thrilled about a plan I never agreed to."


def validate(line: str) -> None:
    """Gate mirror: 1-200 chars, not only whitespace, single line."""
    if not line.strip():
        sys.exit("entry is blank")
    if len(line) > MAX_CHARS:
        sys.exit(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line:
        sys.exit("entry must be a single line")


def main() -> None:
    validate(ROAST)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the file holds exactly the one roast line.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
