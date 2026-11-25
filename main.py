"""One Star for Monday — make.fun entry.

Writes a single line to /output/entry.txt: a one-star review of Monday
written as if Monday were a restaurant. 21 words, plain text, no hashtags.
"""

import os

REVIEW = (
    "One star. Monday sat me at the worst table, the waiter forgot "
    "my order, and the bill covered the whole week."
)


def main() -> None:
    # The gate allows 1-180 characters and at most 25 words on one line.
    words = REVIEW.split()
    assert 1 <= len(REVIEW) <= 180, "review must be 1-180 characters"
    assert len(words) <= 25, "review must be at most 25 words"
    assert "\n" not in REVIEW, "review must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(REVIEW)


if __name__ == "__main__":
    main()
