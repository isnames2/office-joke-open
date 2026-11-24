"""Write the office joke entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure standard library. The joke is a single line, at most 200 characters,
written byte-identically on every run.
"""

import os
from pathlib import Path

JOKE = (
    "My manager asked me to automate his job, so I did \u2014 "
    "now he spends his days in meetings explaining what I do."
)
# 108 characters, within the 200-character limit.


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
