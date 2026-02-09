"""Advent of Code 2015 - Day 2: I Was Told There Would Be No Math"""

from modules.utils.input_reader import read_lines


def part_one(data: list[str]) -> int:
    """Solve part one of the challenge."""
    total_area = 0

    for line in data:
        length, width, height = map(int, line.split("x"))
        side1 = length * width
        side2 = width * height
        side3 = height * length
        surface_area = 2 * (side1 + side2 + side3)
        slack = min(side1, side2, side3)
        total_area += surface_area + slack

    return total_area


def part_two(data: list[str]) -> int:
    """Solve part two of the challenge."""
    total_ribbon = 0

    for line in data:
        length, width, height = map(int, line.split("x"))
        bow = length * width * height
        wrap = 2 * (length + width + height - max(length, width, height))
        total_ribbon += bow + wrap

    return total_ribbon


def solve():
    """Main solve function."""
    data = read_lines(2015, 2)

    print(f"Part 1: {part_one(data)}")
    print(f"Part 2: {part_two(data)}")


if __name__ == "__main__":
    solve()
