from modules.utils.input_reader import read_raw


def part_one() -> int:
    """Solve part one of the challenge."""
    data = read_raw(2015, 3)

    houses_visited = set()
    x, y = 0, 0
    houses_visited.add((x, y))

    for char in data:
        if char == ">":
            x += 1
        elif char == "<":
            x -= 1
        elif char == "^":
            y += 1
        elif char == "v":
            y -= 1

        houses_visited.add((x, y))

    return len(houses_visited)


def part_two() -> int:
    """Solve part two of the challenge."""
    data = read_raw(2015, 3)

    houses_visited = set()
    santa_x, santa_y = 0, 0
    robo_x, robo_y = 0, 0
    houses_visited.add((0, 0))

    for index, char in enumerate(data):
        if index % 2 == 0:  # Santa's turn
            if char == ">":
                santa_x += 1
            elif char == "<":
                santa_x -= 1
            elif char == "^":
                santa_y += 1
            elif char == "v":
                santa_y -= 1

            houses_visited.add((santa_x, santa_y))
        else:  # Robo-Santa's turn
            if char == ">":
                robo_x += 1
            elif char == "<":
                robo_x -= 1
            elif char == "^":
                robo_y += 1
            elif char == "v":
                robo_y -= 1

            houses_visited.add((robo_x, robo_y))

    return len(houses_visited)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
