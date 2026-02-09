"""Advent of Code 2015 - Day 10: Elves Look, Elves Say"""

from itertools import groupby

PUZZLE_INPUT = 3113322113


def look_and_say(term: str) -> str:
    """
    Generate the next term in the look-and-say sequence.

    The look-and-say sequence describes runs of identical digits:
    - "1" becomes "11" (one 1)
    - "11" becomes "21" (two 1s)
    - "21" becomes "1211" (one 2, one 1)

    Args:
        term: Current sequence term

    Returns:
        Next term in the sequence
    """
    if not term:
        return ""

    return "".join(f"{sum(1 for _ in group)}{digit}" for digit, group in groupby(term))


def part_one() -> int:
    """Compute the 40th term in the look-and-say sequence starting from PUZZLE_INPUT."""
    term = str(PUZZLE_INPUT)

    for _ in range(40):
        term = look_and_say(term)

    return len(term)


def part_two() -> int:
    """Compute the 50th term in the look-and-say sequence starting from PUZZLE_INPUT."""
    term = str(PUZZLE_INPUT)

    for _ in range(50):
        term = look_and_say(term)

    return len(term)


def solve():
    """Main solve function."""

    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")


if __name__ == "__main__":
    solve()
