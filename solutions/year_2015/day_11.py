SANTAS_PASSWORD = "cqjxjnds"


def increment_password(pw: str) -> str:
    """
    Increment the password string to the next lexicographical value.
    Args:
        pw: Current password string
    Returns:
        Next password string
    """

    pw_list = list(pw)

    for index in range(len(pw_list) - 1, -1, -1):
        if pw_list[index] == "z":
            pw_list[index] = "a"
        else:
            pw_list[index] = chr(ord(pw_list[index]) + 1)
            break

    return "".join(pw_list)


def is_valid_password(pw: str) -> bool:
    """
    Check if the password meets the specified criteria.
    Args:
        pw: Password string to validate
    Returns:
        True if valid, False otherwise
    """

    # Rule 1: Password must not contain 'i', 'o', or 'l'
    if any(c in pw for c in "iol"):
        return False

    # Rule 2: Password must contain at least one increasing straight of three letters
    has_straight = any(
        ord(pw[index]) + 1 == ord(pw[index + 1])
        and ord(pw[index]) + 2 == ord(pw[index + 2])
        for index in range(len(pw) - 2)
    )

    if not has_straight:
        return False

    # Rule 3: Password must contain at least two different, non-overlapping pairs of letters
    pairs = set()

    for index in range(len(pw) - 1):
        if pw[index] == pw[index + 1]:
            pairs.add(pw[index])
            index += 2
        else:
            index += 1

    if len(pairs) < 2:
        return False

    return True


def find_next_password(current_password: str) -> str:
    """
    Find the next valid password according to specified rules.

    Args:
        current_password: Current password string

    Returns:
        Next valid password string
    """

    next_password = increment_password(current_password)
    while not is_valid_password(next_password):
        next_password = increment_password(next_password)

    return next_password


def part_one() -> str:
    return find_next_password(SANTAS_PASSWORD)


def part_two() -> str:
    return find_next_password(part_one())


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
