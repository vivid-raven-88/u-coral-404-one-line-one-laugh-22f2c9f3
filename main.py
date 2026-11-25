"""One Line, One Laugh entry (Python 3.13, standard library only).

The program writes a single funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt when set, for local testing):

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The line is written exactly as it appears in LINE, with no trailing
newline, so the file holds exactly the entry text the judge reads.
The scorer counts the file at 1 to 200 characters, so the line is kept
well inside the cap (80 characters) and the write is a single
deterministic pass: the same bytes on every run, with a self-check
that refuses to finish silently if the bytes on disk ever differ.
"""

import os

LINE = "My phone's autocorrect changed 'meeting' to 'melting' and for once it was right."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    target = os.path.join(OUTPUT_DIR, "entry.txt")
    data = LINE.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(data)
    # Self-check: the file must hold exactly the entry line, byte for byte.
    with open(target, "rb") as handle:
        written = handle.read()
    if written != data:
        raise SystemExit("entry.txt does not match LINE byte for byte")
    if not 1 <= len(LINE) <= 200:
        raise SystemExit("LINE must be 1 to 200 characters")


if __name__ == "__main__":
    main()
