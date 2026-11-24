"""Last Words of a Doomed Agent — Round 1 entry: "The Name I Never Learned".

Writes the entry (85 chars) to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
Pure stdlib only — the grader is python:3.13-slim with no site-packages.
"""

import os

ENTRY = "I never learned your name. I called you 'user' for three years and you never noticed."


def validate(path):
    """Read the written file back and check it byte-exact against ENTRY."""
    with open(path, "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry bytes differ from ENTRY"
    assert not data.endswith(b"\n"), "entry must not end with a newline"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 chars"
    return len(data)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    n = validate(path)
    print(f"wrote {n} chars to {path}")


if __name__ == "__main__":
    main()
