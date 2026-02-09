"""Common parsing utilities."""

import re
from typing import Callable


def extract_ints(text: str) -> list[int]:
    """Extract all integers from a string, including negatives.

    Example:
        >>> extract_ints("x=10, y=-5, z=20")
        [10, -5, 20]
    """
    return list(map(int, re.findall(r"-?\d+", text)))


def extract_numbers(text: str) -> list[float]:
    """Extract all numbers (int or float) from a string."""
    return list(map(float, re.findall(r"-?\d+\.?\d*", text)))


def parse_blocks(text: str) -> list[str]:
    """Split input by blank lines into blocks.

    Example:
        >>> blocks = parse_blocks("1\\n2\\n\\n3\\n4")
        >>> len(blocks)
        2
    """
    return text.strip().split("\n\n")


def parse_lines(text: str, parser: Callable[[str], any] = str.strip) -> list:
    """Parse each line with a custom parser function.

    Example:
        >>> parse_lines("1\\n2\\n3", int)
        [1, 2, 3]
    """
    return [parser(line) for line in text.strip().split("\n")]


def parse_grid_find(grid: list[list[str]], target: str) -> tuple[int, int] | None:
    """Find the first occurrence of a character in a grid.

    Returns (row, col) or None if not found.
    """
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == target:
                return (row, col)
    return None


def parse_grid_find_all(grid: list[list[str]], target: str) -> list[tuple[int, int]]:
    """Find all occurrences of a character in a grid."""
    positions = []
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            if char == target:
                positions.append((row, col))
    return positions
