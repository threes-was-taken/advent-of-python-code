from modules.utils.input_reader import read_lines


def find_nice_strings(data: list[str], allow_overlapping: bool) -> int:
    """Count the number of nice strings in the provided data, conditionally allowing overlap."""
    nice_strings_count = 0

    for line in data:
        vowels = sum(1 for char in line if char in "aeiou")
        has_double_letter = any(line[i] == line[i + 1] for i in range(len(line) - 1))
        has_forbidden_substring = any(
            substr in line for substr in ["ab", "cd", "pq", "xy"]
        )

        if (
            vowels >= 3
            and has_double_letter
            and not has_forbidden_substring
            and allow_overlapping
        ):
            nice_strings_count += 1
        elif not allow_overlapping:
            # For part two, we need to check for the new criteria
            has_repeated_pair = False
            has_sandwiched_letter = False

            # Check for repeated pair
            pairs = {}

            for i in range(len(line) - 1):
                pair = line[i : i + 2]
                if pair in pairs:
                    if i - pairs[pair] > 1:
                        has_repeated_pair = True
                        break
                else:
                    pairs[pair] = i

            # Check for sandwiched letter
            for i in range(len(line) - 2):
                if line[i] == line[i + 2]:
                    has_sandwiched_letter = True
                    break

            if has_repeated_pair and has_sandwiched_letter:
                nice_strings_count += 1

    return nice_strings_count


def part_one() -> int:
    """Solve part one of the challenge."""
    data = read_lines(2015, 5)

    return find_nice_strings(data, allow_overlapping=True)


def part_two() -> int:
    """Solve part two of the challenge."""
    data = read_lines(2015, 5)

    return find_nice_strings(data, allow_overlapping=False)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
