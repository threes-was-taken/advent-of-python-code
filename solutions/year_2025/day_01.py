from typing import List

from modules.utils.input_reader import read_lines


def initialize(is_test: bool) -> List[str]:
    data = (
        read_lines(2025, 1)
        if not is_test
        else ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    )

    return data


def get_direction_and_steps(line: str) -> tuple[str, int]:
    direction = line[0]
    steps = int(line[1:])
    return direction, steps


def is_empty_line(line: str) -> bool:
    return not line or not line.strip()


def handle_left_steps(current_position: int, steps: int) -> int:
    return (current_position - steps) % 100


def handle_right_steps(current_position: int, steps: int) -> int:
    return (current_position + steps) % 100


def calculate_amount_of_zeros(include_passing_zeros: bool) -> int:
    data = initialize(is_test=False)
    current_position = 50
    amount_of_zeros = 0
    last_position_was_zero = False

    for line in data:
        if is_empty_line(line):
            continue

        direction, steps = get_direction_and_steps(line)

        if steps >= 100:
            full_cycles = int(steps / 100)
            steps = steps % 100

            if include_passing_zeros:
                amount_of_zeros += full_cycles

        if direction == "L":
            current_position -= steps
        else:
            current_position += steps

        new_position = current_position % 100

        if new_position == 0:
            amount_of_zeros += 1
        elif (
            include_passing_zeros
            and new_position != current_position
            and not last_position_was_zero
        ):
            amount_of_zeros += 1

        last_position_was_zero = new_position == 0
        current_position = new_position

    return amount_of_zeros


def part_one() -> int:
    """Calculate the amount of times we land on 0."""
    return calculate_amount_of_zeros(include_passing_zeros=False)


def part_two() -> int:
    """Calculate the amount of times we land on 0, including passing zeros."""
    return calculate_amount_of_zeros(
        include_passing_zeros=True,
    )


def solve():
    """Main solve function."""

    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")


if __name__ == "__main__":
    solve()
