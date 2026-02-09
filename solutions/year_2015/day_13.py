"""Advent of Code 2015 - Day 13: Knights of the Dinner Table"""

from itertools import permutations

from modules.utils.input_reader import read_lines


def find_happiness(data: list[str], include_me: bool = False) -> dict[tuple[str, str], int]:
    """
    Parse input data to extract happiness values between individuals, optionally including myself.
    Args:
        data: List of strings describing happiness changes
        include_me: If True, include "Me" in the happiness calculations
    Returns:
        Dictionary mapping (person_a, person_b) to happiness value
    """
    happiness = {}
    for line in data:
        parts = line[:-1].split()
        person_a = parts[0]
        gain_lose = parts[2]
        amount = int(parts[3])
        person_b = parts[-1]

        if gain_lose == "lose":
            amount = -amount

        happiness[(person_a, person_b)] = amount

    if include_me:
        people = set()
        for person_a, person_b in happiness.keys():
            people.add(person_a)
            people.add(person_b)
        for person in people:
            happiness[("Me", person)] = 0
            happiness[(person, "Me")] = 0

    return happiness


def find_optimal_arrangement(happiness: dict[tuple[str, str], int]) -> int:
    """
    Find the seating arrangement that maximizes total happiness.
    Args:
        happiness: Dictionary mapping (person_a, person_b) to happiness value
    Returns:
        Maximum total happiness for any arrangement
    """
    people = set()
    for person_a, person_b in happiness.keys():
        people.add(person_a)
        people.add(person_b)

    max_happiness = float("-inf")
    for arrangement in permutations(people):
        total_happiness = 0
        for index in range(len(arrangement)):
            person_a = arrangement[index]
            person_b = arrangement[(index + 1) % len(arrangement)]
            total_happiness += happiness.get((person_a, person_b), 0)
            total_happiness += happiness.get((person_b, person_a), 0)
        max_happiness = max(max_happiness, total_happiness)

    return int(max_happiness)


def part_one(data: list[str]) -> int:
    """Find the optimal seating arrangement without including myself."""
    happiness = find_happiness(data, include_me=False)
    return find_optimal_arrangement(happiness)


def part_two(data: list[str]) -> int:
    """Include myself in the happiness calculations and find the optimal arrangement."""
    happiness = find_happiness(data, include_me=True)
    return find_optimal_arrangement(happiness)


def solve():
    """Main solve function."""

    data = read_lines(2015, 13)
    print("Part One:", part_one(data))
    print("Part Two:", part_two(data))


if __name__ == "__main__":
    solve()
