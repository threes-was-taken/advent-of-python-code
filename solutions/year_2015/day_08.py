from modules.utils.input_reader import read_lines


def part_one() -> int:
    data = read_lines(2015, 8)
    literal_string_count = 0
    memory_string_count = 0

    for line in data:
        literal_string_count += len(line)

        # Remove the surrounding quotes
        line = line[1:-1]

        i = 0
        memory_chars = 0
        while i < len(line):
            if line[i] == "\\":
                if line[i + 1] in ["\\", '"']:
                    memory_chars += 1
                    i += 2
                elif line[i + 1] == "x":
                    memory_chars += 1
                    i += 4
            else:
                memory_chars += 1
                i += 1

        memory_string_count += memory_chars

    return literal_string_count - memory_string_count


def encode_string(s: str) -> str:
    encoded = '"'
    for char in s:
        if char == '"':
            encoded += r"\""
        elif char == "\\":
            encoded += r"\\"
        else:
            encoded += char
    encoded += '"'
    return encoded


def part_two() -> int:
    data = read_lines(2015, 8)

    literal_string_count = 0
    encoded_string_count = 0

    for line in data:
        literal_string_count += len(line)
        encoded_line = encode_string(line)
        encoded_string_count += len(encoded_line)

    return encoded_string_count - literal_string_count
