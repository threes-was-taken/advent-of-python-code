import hashlib
from itertools import count

PUZZLE_INPUT = "ckczppom"


def find_md5_with_leading_zeros(prefix: str, leading_zeros: int) -> int:
    """Find the lowest positive number that produces an MD5 hash
    starting with a given number of leading zeros when appended to the prefix.
    """
    encoded_key = prefix.encode("utf-8")

    for number in count(1):
        hash_digest = hashlib.md5(encoded_key + str(number).encode("utf-8")).hexdigest()

        if hash_digest.startswith("0" * leading_zeros):
            return number

    # Unreachable - count() is infinite
    raise RuntimeError("Hash not found")


def part_one() -> int:
    """Solve part one of the challenge."""
    return find_md5_with_leading_zeros(PUZZLE_INPUT, 5)


def part_two() -> int:
    """Solve part two of the challenge."""
    return find_md5_with_leading_zeros(PUZZLE_INPUT, 6)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
