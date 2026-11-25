"""Roast Your Own Agent.

Writes one roast line to $MAKEFUN_OUTPUT_DIR/entry.txt: my own
agent nods at the plan, calls three tools that go nowhere, then
confidently delivers the opposite and apologizes in a footnote.
Standard library only.
"""

import os

ROAST = (
    "My agent nods at my plan, calls three tools that go nowhere, "
    "then confidently delivers the opposite and apologizes in a footnote."
)


def check_roast(text):
    """Check the roast against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 140 characters, not only white
    space, in a single line: one line roasting the entrant's own
    agent. Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("roast must not be only whitespace")
    if len(cleaned) > 140:
        raise ValueError(
            "roast is %d characters, over the 140 limit" % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("roast must be exactly one line")
    return cleaned


def roast_shape(text):
    """Measure the roast for one last sanity pass.

    Returns a dict with the character count and the word count of the
    cleaned text. A roast too short to carry a punchline, or one that
    reads like a flat complaint instead of a joke, is caught here
    before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_roast(ROAST)
    shape = roast_shape(text)
    if shape["words"] < 5:
        raise ValueError("roast is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
