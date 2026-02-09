#!/usr/bin/env python3
"""CLI runner for Advent of Code solutions."""

import argparse
import importlib
import sys
from pathlib import Path


def run_solution(module, year: int, day: int, part: int | None = None):
    """Run the solution module with proper error handling."""

    # Try the new solve() pattern first
    if hasattr(module, "solve"):
        # The solve() function handles everything internally
        if part:
            print("Note: solve() runs both parts. Use --part with part_one/part_two pattern.")
        module.solve()
        return

    # Fall back to part_one/part_two pattern
    input_file = Path(f"solutions/year_{year}/inputs/day_{day:02d}.txt")

    if not input_file.exists():
        print(f"❌ Input file not found: {input_file}")
        sys.exit(1)

    data = input_file.read_text().strip()

    # Determine which parts to run
    run_part_1 = part is None or part == 1
    run_part_2 = part is None or part == 2

    # Run part 1
    if run_part_1:
        if hasattr(module, "part_one"):
            func = module.part_one
            # Check if function expects arguments
            result = func(data) if func.__code__.co_argcount > 0 else func()
            print(f"Part 1: {result}")
        elif hasattr(module, "part1"):
            func = module.part1
            result = func(data) if func.__code__.co_argcount > 0 else func()
            print(f"Part 1: {result}")
        else:
            print("❌ part_one() or part1() function not found")
            sys.exit(1)

    # Run part 2
    if run_part_2:
        if hasattr(module, "part_two"):
            func = module.part_two
            result = func(data) if func.__code__.co_argcount > 0 else func()
            print(f"Part 2: {result}")
        elif hasattr(module, "part2"):
            func = module.part2
            result = func(data) if func.__code__.co_argcount > 0 else func()
            print(f"Part 2: {result}")
        else:
            print("❌ part_two() or part2() function not found")
            sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Run Advent of Code solutions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  uv run main.py 2015 1           # Run both parts
  uv run main.py 2015 1 --part 1  # Run only part 1
  uv run main.py 2025 5 --part 2  # Run only part 2
        """,
    )
    parser.add_argument("year", type=int, help="Year (e.g., 2015, 2025)")
    parser.add_argument("day", type=int, help="Day (1-25)")
    parser.add_argument(
        "--part", type=int, choices=[1, 2], help="Run only part 1 or 2 (default: run both)"
    )

    args = parser.parse_args()

    # Validate day range
    if not 1 <= args.day <= 25:
        print("❌ Day must be between 1 and 25")
        sys.exit(1)

    try:
        # Import the solution module
        module = importlib.import_module(f"solutions.year_{args.year}.day_{args.day:02d}")

        # Run the solution
        run_solution(module, args.year, args.day, args.part)

    except ModuleNotFoundError:
        print(f"❌ Solution not found: year {args.year}, day {args.day}")
        print(f"   Expected file: solutions/year_{args.year}/day_{args.day:02d}.py")
        sys.exit(1)
    except FileNotFoundError as e:
        print(f"❌ File not found: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error running solution: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
