#!/usr/bin/env python3
"""Create template files for a new AoC day."""

import sys
from datetime import datetime
from pathlib import Path

SOLUTION_TEMPLATE = '''"""Advent of Code {year} - Day {day}

https://adventofcode.com/{year}/day/{day}
"""

from pathlib import Path


def parse_input(text: str):
    """Parse the puzzle input."""
    return text.strip().split('\\n')


def part_one(data) -> int:
    """Solve part 1."""
    # TODO: Implement
    pass


def part_two(data) -> int:
    """Solve part 2."""
    # TODO: Implement
    pass


def solve():
    """Main solve function."""
    input_file = Path(__file__).parent / "inputs" / "day_{day_padded}.txt"
    data = parse_input(input_file.read_text())

    print(f"Part 1: {{part_one(data)}}")
    print(f"Part 2: {{part_two(data)}}")


if __name__ == "__main__":
    solve()
'''

TEST_TEMPLATE = '''"""Tests for Advent of Code {year} - Day {day}"""

import pytest
from solutions.year_{year}.day_{day_padded} import part_one, part_two


EXAMPLE_INPUT = """\\
# TODO: Add example input from problem
"""


def test_part_one():
    """Test part 1 with example."""
    # TODO: Add assertion
    pass


def test_part_two():
    """Test part 2 with example."""
    # TODO: Add assertion
    pass
'''


def create_day(year: int, day: int):
    """Create solution and test files for a new day."""
    day_padded = str(day).zfill(2)

    # Create paths
    year_dir = Path(f"solutions/year_{year}")
    inputs_dir = year_dir / "inputs"
    tests_dir = Path(f"tests/year_{year}")

    solution_file = year_dir / f"day_{day_padded}.py"
    input_file = inputs_dir / f"day_{day_padded}.txt"
    test_file = tests_dir / f"test_day_{day_padded}.py"

    # Create directories
    year_dir.mkdir(parents=True, exist_ok=True)
    inputs_dir.mkdir(exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)

    # Create __init__.py files
    for init_file in [year_dir / "__init__.py", tests_dir / "__init__.py"]:
        if not init_file.exists():
            init_file.touch()

    # Create solution file
    if solution_file.exists():
        print(f"⚠️  Solution already exists: {solution_file}")
    else:
        solution_file.write_text(
            SOLUTION_TEMPLATE.format(year=year, day=day, day_padded=day_padded)
        )
        print(f"✅ Created: {solution_file}")

    # Create empty input file
    if input_file.exists():
        print(f"⚠️  Input already exists: {input_file}")
    else:
        input_file.touch()
        print(f"✅ Created: {input_file}")

    # Create test file
    if test_file.exists():
        print(f"⚠️  Test already exists: {test_file}")
    else:
        test_file.write_text(TEST_TEMPLATE.format(year=year, day=day, day_padded=day_padded))
        print(f"✅ Created: {test_file}")

    print(f"\n🎄 Ready for {year} Day {day}!")
    print(f"   Input: {input_file}")
    print(f"   Run: python main.py {year} {day}")


def main():
    if len(sys.argv) < 2:
        # Auto-detect current AoC day
        now = datetime.now()
        if now.month == 12 and 1 <= now.day <= 25:
            year = now.year
            day = now.day
            print(f"Auto-detected: Year {year}, Day {day}")
        else:
            print("Usage: python scripts/new_day.py [YEAR] DAY")
            print("   or: python scripts/new_day.py DAY  (uses current year)")
            return
    elif len(sys.argv) == 2:
        day = int(sys.argv[1])
        year = datetime.now().year
    else:
        year = int(sys.argv[1])
        day = int(sys.argv[2])

    if not 1 <= day <= 25:
        print("❌ Day must be between 1 and 25")
        return

    create_day(year, day)


if __name__ == "__main__":
    main()
