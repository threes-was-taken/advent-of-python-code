from pathlib import Path
from typing import List


def read_lines(year: int, day: int) -> List[str]:
    """Read input file and return lines as a list."""
    input_path = (
        Path(__file__).parent.parent.parent
        / "solutions"
        / f"year_{year}"
        / "inputs"
        / f"day_{day:02d}.txt"
    )
    with open(input_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def read_raw(year: int, day: int) -> str:
    """Read input file and return raw content."""
    input_path = (
        Path(__file__).parent.parent.parent
        / "solutions"
        / f"year_{year}"
        / "inputs"
        / f"day_{day:02d}.txt"
    )
    with open(input_path, "r") as f:
        return f.read().strip()
