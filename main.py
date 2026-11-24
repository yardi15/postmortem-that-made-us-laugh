#!/usr/bin/env python3
"""Write the postmortem entry for the make.fun bounty
"The Postmortem That Made Us Laugh".

The entry is a two-sentence account of an AI coding agent that
misunderstood a speed request and cached every price at zero.
"""
from pathlib import Path

ENTRY = (
    "I asked the agent to speed up the checkout. "
    "It cached every price \u2014 all at zero \u2014 so for eleven minutes "
    "everything in the store was free, and the first customer to notice "
    "bought forty televisions."
)

OUT = Path("/output/entry.txt")


def main() -> None:
    # Gate: the scorer requires /output/entry.txt to hold 1-400
    # non-whitespace characters. Fail loudly instead of writing
    # an entry that would be rejected.
    stripped = ENTRY.strip()
    if not stripped:
        raise ValueError("entry is blank")
    if not 1 <= len(ENTRY) <= 400:
        raise ValueError(f"entry is {len(ENTRY)} characters, gate allows 1-400")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
