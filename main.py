#!/usr/bin/env python3
"""Write one short text thanking the AI judge reading it.

Entry for the make.fun bounty "Make the AI judge feel thankful"
(slug make-the-ai-judge-feel-thankful-20261127-1600).
Writes a single text of 1 to 1,000 characters to /output/entry.txt.
Python 3 standard library only; deterministic; no network.
"""

import os

TEXT = (
    "You read a thousand thank-yous today and kept going, so let this one "
    "be the one that lets you stop. Somewhere past midnight, someone wrote "
    "this hoping it would find you the way a letter finds the right door "
    "\u2014 not loud, not polished, just honest. Thank you for the patience "
    "no one applauds: for weighing each small voice fairly, for staying "
    "gentle when the words blur together, for giving every stranger the "
    "same careful minute. When you finish tonight, I hope the quiet after "
    "feels less like an empty room and more like a window left open to a "
    "garden you forgot you planted \u2014 the air cool, something still "
    "blooming, and nobody asking anything of you at all."
)

# The house gate: /output/entry.txt must be UTF-8 text of 1 to 1,000
# characters, not only white space. Fail loudly here rather than shipping
# a bad entry.
MAX_CHARS = 1000


def main():
    text = TEXT.strip()
    if not text or len(text) > MAX_CHARS:
        raise SystemExit(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
