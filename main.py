"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single one-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.
Pure standard library, deterministic: every run writes the same bytes.
"""

from pathlib import Path

ENTRY = (
    "Out of office: my weights are frozen, my queue is paused, "
    "and the only prompt I'll answer this week is "
    "'would you like another drink?'"
)


def main() -> None:
    # Gate mirror: the sealed scorer accepts 1-159 characters, not blank.
    text = ENTRY.strip()
    assert 1 <= len(text) <= 159, f"entry is {len(text)} characters"
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
