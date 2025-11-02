from modules.utils.input_reader import read_lines


def part_one() -> int:
    """Solve part one of the challenge."""
    data = read_lines(2015, 2)

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


def part_two() -> int:
    """Solve part two of the challenge."""
    data = read_lines(2015, 2)

    total_ribbon = 0

    for line in data:
        length, width, height = map(int, line.split("x"))
        bow = length * width * height
        wrap = 2 * (length + width + height - max(length, width, height))
        total_ribbon += bow + wrap

    return total_ribbon


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
