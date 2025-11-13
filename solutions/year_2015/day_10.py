PUZZLE_INPUT = 3113322113


def look_and_say(term: str) -> str:
    """
    Generate the next term in the look-and-say sequence.

    Args:
        term: Current term as a string

    Returns:
        Next term as a string
    """
    next_term = []
    index = 0

    while index < len(term):
        count = 1
        while index + 1 < len(term) and term[index] == term[index + 1]:
            count += 1
            index += 1
        next_term.append(f"{count}{term[index]}")
        index += 1

    return "".join(next_term)


def part_one() -> int:
    """Compute the 40th term in the look-and-say sequence starting from PUZZLE_INPUT."""
    term = str(PUZZLE_INPUT)

    for _ in range(40):
        term = look_and_say(term)

    return len(term)


def part_two() -> int:
    term = str(PUZZLE_INPUT)

    for _ in range(50):
        term = look_and_say(term)

    return len(term)
