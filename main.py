"""Emit the selected browser-tab count without adding a line terminator."""

from os import environ
from pathlib import Path


TAB_COUNT = "284"


def entry_bytes() -> bytes:
    """Validate the fixed entry and return its exact UTF-8 representation."""
    if not 1 <= len(TAB_COUNT) <= 5:
        raise ValueError("The entry must have between one and five characters.")
    if any(digit < "0" or digit > "9" for digit in TAB_COUNT):
        raise ValueError("The entry must contain ASCII digits with no whitespace.")
    return TAB_COUNT.encode("utf-8", errors="strict")


def main() -> None:
    payload = entry_bytes()
    destination = Path(environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)


if __name__ == "__main__":
    main()
