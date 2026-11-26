"""Verify two isolated runs using only the Python standard library."""

import hashlib
import os
from pathlib import Path
import subprocess
import sys
import tempfile


def check_output(path: Path) -> bytes:
    data = path.read_bytes()
    text = data.decode("utf-8", errors="strict")
    if not 1 <= len(text) <= 5:
        raise ValueError("Output must contain 1–5 characters.")
    if not text.isascii() or not text.isdigit():
        raise ValueError("Output must contain ASCII digits only.")
    if data.endswith((b"\n", b"\r")):
        raise ValueError("Output must have no trailing newline.")
    if any(character.isspace() for character in text):
        raise ValueError("Output must have no whitespace.")
    return data


def main() -> int:
    repository = Path(__file__).resolve().parent
    verification_root = repository / ".verify"
    try:
        verification_root.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(
            prefix="verification-", dir=verification_root
        ) as temporary_directory:
            results = []
            for run_number in (1, 2):
                output_directory = Path(temporary_directory) / f"run-{run_number}"
                output_directory.mkdir()
                environment = os.environ.copy()
                environment["OUTPUT_DIR"] = str(output_directory)
                completed = subprocess.run(
                    [sys.executable, str(repository / "main.py")],
                    cwd=repository,
                    env=environment,
                    capture_output=True,
                    text=True,
                    timeout=30,
                    check=True,
                )
                if completed.stdout or completed.stderr:
                    raise ValueError("main.py must run without console output.")
                results.append(check_output(output_directory / "entry.txt"))

            if results[0] != results[1]:
                raise ValueError("The two runs produced different bytes.")

            print("PASS: UTF-8, 1–5 ASCII digits, no whitespace or newline, identical runs.")
            print(f"Count: {results[0].decode('utf-8')} ({len(results[0])} characters)")
            for run_number, data in enumerate(results, start=1):
                print(f"Run {run_number} SHA-256: {hashlib.sha256(data).hexdigest()}")
    except (OSError, UnicodeError, ValueError, subprocess.SubprocessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
