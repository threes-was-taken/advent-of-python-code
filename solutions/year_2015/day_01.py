from modules.utils.input_reader import read_raw


def part_one() -> int:
    """Solve part one of the challenge."""
    data = read_raw(2015, 1)

    floor = 0

    for char in data:
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

    return floor


def part_two() -> int:
    """Solve part two of the challenge."""
    data = read_raw(2015, 1)

    floor = 0

    for index, char in enumerate(data, start=1):
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1

        if floor == -1:
            return index

    return -1  # Should not reach here for valid input


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
