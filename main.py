import argparse


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    parser.add_argument("year", type=int, help="Year (e.g., 2025)")
    parser.add_argument("day", type=int, help="Day (1-25)")
    parser.add_argument("--part", type=int, choices=[1, 2], help="Part 1 or 2")

    args = parser.parse_args()

    try:
        solution_module = __import__(
            f"solutions.year_{args.year}.day_{args.day:02d}", fromlist=[""]
        )

        if args.part == 1:
            result = solution_module.part_one()
            print(f"Year {args.year}, Day {args.day}, Part 1: {result}")
        elif args.part == 2:
            result = solution_module.part_two()
            print(f"Year {args.year}, Day {args.day}, Part 2: {result}")
        else:
            result1 = solution_module.part_one()
            result2 = solution_module.part_two()
            print(f"Year {args.year}, Day {args.day}, Part 1: {result1}")
            print(f"Year {args.year}, Day {args.day}, Part 2: {result2}")

    except ImportError:
        print(f"Could not find solution for year {args.year}, day {args.day}.")
        return
    except Exception as e:
        print(f"An error occurred while importing the solution: {e}")
        return


if __name__ == "__main__":
    main()
