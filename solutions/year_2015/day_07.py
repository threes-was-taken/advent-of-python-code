from modules.utils.input_reader import read_lines


def compute_bitwise_operation(left: int, operator: str, right: int) -> int:
    """Compute the result of a bitwise operation."""
    if operator == "AND":
        return left & right
    elif operator == "OR":
        return left | right
    elif operator == "LSHIFT":
        return (left << right) & 0xFFFF
    elif operator == "RSHIFT":
        return (left >> right) & 0xFFFF
    else:
        raise ValueError(f"Unknown operator: {operator}")


def complement_value(value: int) -> int:
    """Compute the bitwise NOT of a value within 16 bits."""
    return ~value & 0xFFFF


def emulate_circuit(
    circuit: dict[str, str], processed_wires: dict[str, int]
) -> dict[str, int]:
    """Emulate the circuit until no more wires can be processed."""
    while True:
        progress_made = False

        for connection in circuit:
            if connection in processed_wires:
                continue

            instruction = circuit[connection]
            tokens = instruction.split(" ")

            if len(tokens) == 1:
                operand = tokens[0]

                result = (
                    processed_wires.get(operand, None)
                    if processed_wires.get(operand, None) is not None
                    else int(operand)
                    if operand.isdigit()
                    else None
                )

                if result is None:
                    continue

                processed_wires[connection] = result
                progress_made = True

            elif len(tokens) == 2:
                operator, operand = tokens

                operand_value = (
                    processed_wires.get(operand, None)
                    if processed_wires.get(operand, None) is not None
                    else int(operand)
                    if operand.isdigit()
                    else None
                )

                if operand_value is None:
                    continue

                if operator == "NOT":
                    result = complement_value(operand_value)
                    processed_wires[connection] = result
                    progress_made = True

            elif len(tokens) == 3:
                left, operator, right = tokens

                left_value = (
                    processed_wires.get(left, None)
                    if processed_wires.get(left, None) is not None
                    else int(left)
                    if left.isdigit()
                    else None
                )
                right_value = (
                    processed_wires.get(right, None)
                    if processed_wires.get(right, None) is not None
                    else int(right)
                    if right.isdigit()
                    else None
                )

                if left_value is None or right_value is None:
                    continue

                result = compute_bitwise_operation(left_value, operator, right_value)
                processed_wires[connection] = result
                progress_made = True

        if not progress_made:
            break

    return processed_wires


def part_one() -> int:
    """Solve part one of the challenge."""
    data = read_lines(2015, 7)

    circuit = {}
    processed_wires = {}

    for line in data:
        bitwise_instruction, output_wire = line.split(" -> ")

        bitwise_instruction = bitwise_instruction.strip()

        circuit[output_wire] = bitwise_instruction

    processed_wires = emulate_circuit(circuit, processed_wires)

    return processed_wires.get("a", 0)


def part_two() -> int:
    """Solve part two of the challenge."""
    wire_a_signal = part_one()

    data = read_lines(2015, 7)

    circuit = {}
    processed_wires = {"b": wire_a_signal}

    for line in data:
        bitwise_instruction, output_wire = line.split(" -> ")

        bitwise_instruction = bitwise_instruction.strip()

        circuit[output_wire] = bitwise_instruction
    processed_wires = emulate_circuit(circuit, processed_wires)

    return processed_wires.get("a", 0)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
