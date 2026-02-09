"""Advent of Code 2015 - Day 1: Not Quite Lisp"""

from modules.utils.input_reader import read_raw


def part_one(data: str) -> int:
    """Find the final floor.

    '(' means go up one floor, ')' means go down one floor.
    """
    return data.count("(") - data.count(")")


def part_two(data: str) -> int:
    """Find the position of the character that first causes entering the basement.

    Returns the 1-indexed position where floor becomes -1.
    """
    floor = 0

    for index, char in enumerate(data, start=1):
        floor += 1 if char == "(" else -1

        if floor == -1:
            return index

    return -1  # Should not reach here for valid input


def solve():
    """Main solve function."""
    data = read_raw(2015, 1)

    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")


if __name__ == "__main__":
    solve()
