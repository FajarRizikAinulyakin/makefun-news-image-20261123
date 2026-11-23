"""Deliver the finished poster for Monday 23 November 2026.

The poster itself lives beside this file as entry.png: a newspaper
front page summing up the day's world news. All this program does
is place a byte-for-byte copy of it at /output/entry.png, making
the folder when needed. It needs nothing beyond the standard
library, takes no arguments, and never touches the network, so
two runs always produce the same file.
"""

import os
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"


def destination() -> Path:
    """Where the poster goes: /output, or MAKEFUN_OUTPUT_DIR locally."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return Path(folder) / "entry.png"


def main() -> None:
    target = destination()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(SOURCE.read_bytes())
    if target.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("copy came out short: %s" % target)


if __name__ == "__main__":
    main()
