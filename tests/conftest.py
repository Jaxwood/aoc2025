"""Test helpers and fixtures."""

import pytest
from pathlib import Path
from typing import List, Callable


@pytest.fixture
def read_input() -> Callable[[str], List[str]]:
    """Fixture that returns a function to read input files."""

    def _read_input(file_path: str) -> List[str]:
        """Read input from a file and return as list of lines.

        Args:
            file_path: Path to the input file

        Returns:
            List of lines with trailing whitespace stripped from each line
        """
        content = Path(file_path).read_text(encoding="utf-8").rstrip()
        return content.split("\n")

    return _read_input
