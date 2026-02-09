#!/usr/bin/env python3
"""Benchmark AoC solutions."""

import importlib
import sys
import time
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def benchmark_solution(year: int, day: int, runs: int = 10):
    """Benchmark a solution."""
    try:
        module = importlib.import_module(f"solutions.year_{year}.day_{day:02d}")
        input_file = Path(f"solutions/year_{year}/inputs/day_{day:02d}.txt")

        if not input_file.exists():
            print(f"❌ Input file not found: {input_file}")
            return

        data = input_file.read_text().strip()

        # Check if using solve() pattern
        if hasattr(module, "parse_input"):
            data = module.parse_input(data)

        print(f"🎄 Benchmarking Year {year}, Day {day}")
        print("=" * 60)

        # Benchmark part 1
        if hasattr(module, "part_one"):
            part_func = module.part_one

            # Warm-up run
            result = part_func(data)

            # Actual benchmark
            times = []
            for _ in range(runs):
                start = time.perf_counter()
                part_func(data)
                end = time.perf_counter()
                times.append(end - start)

            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)

            print(f"Part 1: {result}")
            print(f"  Average: {avg_time * 1000:>8.2f}ms ({runs} runs)")
            print(f"  Min:     {min_time * 1000:>8.2f}ms")
            print(f"  Max:     {max_time * 1000:>8.2f}ms")
            print()

        # Benchmark part 2
        if hasattr(module, "part_two"):
            part_func = module.part_two

            # Warm-up run
            result = part_func(data)

            # Actual benchmark
            times = []
            for _ in range(runs):
                start = time.perf_counter()
                part_func(data)
                end = time.perf_counter()
                times.append(end - start)

            avg_time = sum(times) / len(times)
            min_time = min(times)
            max_time = max(times)

            print(f"Part 2: {result}")
            print(f"  Average: {avg_time * 1000:>8.2f}ms ({runs} runs)")
            print(f"  Min:     {min_time * 1000:>8.2f}ms")
            print(f"  Max:     {max_time * 1000:>8.2f}ms")

    except ModuleNotFoundError as e:
        print(f"❌ Solution not found: {e}")
        print(f"   Expected: solutions/year_{year}/day_{day:02d}.py")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback

        traceback.print_exc()


def main():
    if len(sys.argv) < 3:
        print("Usage: python scripts/benchmark.py YEAR DAY [RUNS]")
        print("\nExamples:")
        print("  python scripts/benchmark.py 2015 1")
        print("  python scripts/benchmark.py 2015 1 100")
        return

    year = int(sys.argv[1])
    day = int(sys.argv[2])
    runs = int(sys.argv[3]) if len(sys.argv) > 3 else 10

    benchmark_solution(year, day, runs)


if __name__ == "__main__":
    main()
