import json
from typing import Any

from modules.utils.input_reader import read_raw


def extract_numbers(obj: Any, ignore_red: bool = False) -> list[int]:
    """
    Recursively extract all numbers from a JSON structure.

    Args:
        obj: JSON object (can be dict, list, int, str, etc.)
        ignore_red: If True, skip dictionaries containing "red" as a value

    Returns:
        List of all integers found in the structure
    """
    if isinstance(obj, int):
        return [obj]

    if isinstance(obj, list):
        return [num for item in obj for num in extract_numbers(item, ignore_red)]

    if isinstance(obj, dict):
        # Skip this dict if it contains "red" and we're ignoring red
        if ignore_red and "red" in obj.values():
            return []

        return [
            num for value in obj.values() for num in extract_numbers(value, ignore_red)
        ]

    # Base case: not a number, list, or dict
    return []


def sum_json_numbers(data: str, ignore_red: bool = False) -> int:
    """
    Parse JSON and sum all numbers, optionally ignoring objects with "red".

    Args:
        data: JSON string to parse
        ignore_red: If True, ignore objects containing "red" value

    Returns:
        Sum of all numbers in the JSON structure
    """
    json_data = json.loads(data)
    numbers = extract_numbers(json_data, ignore_red)
    return sum(numbers)


def part_one() -> int:
    """Sum all numbers in the JSON document."""
    data = read_raw(2015, 12)
    return sum_json_numbers(data, ignore_red=False)


def part_two() -> int:
    """Sum all numbers, ignoring objects with 'red' property."""
    data = read_raw(2015, 12)
    return sum_json_numbers(data, ignore_red=True)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
