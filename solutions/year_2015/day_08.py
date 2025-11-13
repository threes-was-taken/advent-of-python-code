from modules.utils.input_reader import read_lines


def count_memory_chars(line: str) -> int:
    r"""
    Count actual memory characters in a string literal.

    Handles escape sequences: \\, \", and \xNN (hex ASCII codes).

    Args:
        line: String literal without surrounding quotes

    Returns:
        Number of characters in memory representation
    """
    i = 0
    memory_chars = 0
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):  # Add bounds check
            if line[i + 1] in ["\\", '"']:
                memory_chars += 1
                i += 2
            elif line[i + 1] == "x" and i + 3 < len(line):  # Add bounds check
                memory_chars += 1
                i += 4
            else:
                # Handle malformed escape sequences
                memory_chars += 1
                i += 1
        else:
            memory_chars += 1
            i += 1
    return memory_chars


def part_one() -> int:
    """Calculate difference between literal and memory string lengths."""
    data = read_lines(2015, 8)

    literal_count = sum(len(line) for line in data)
    memory_count = sum(count_memory_chars(line[1:-1]) for line in data)

    return literal_count - memory_count


def encode_string(s: str) -> str:
    """
    Encode string by escaping quotes and backslashes, adding surrounding quotes.

    Args:
        s: Original string to encode

    Returns:
        Encoded string with escaping and quotes
    """
    escaped = s.replace("\\", r"\\").replace('"', r"\"")
    return f'"{escaped}"'


def part_two() -> int:
    """Calculate difference between encoded and literal string lengths."""
    data = read_lines(2015, 8)

    literal_count = sum(len(line) for line in data)
    encoded_count = sum(len(encode_string(line)) for line in data)

    return encoded_count - literal_count
