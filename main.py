"""Self-checkout one-liner entry for make.fun.

Writes exactly one funny line, in the voice of a smug self-checkout
machine, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Pure stdlib, deterministic: the same line on every run.
"""

import os

LINE = (
    "Twelve yoghurts, nothing else. I have scanned your entire "
    "personality and it expires on Friday \u2014 please place your "
    "disappointment in the bagging area."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
