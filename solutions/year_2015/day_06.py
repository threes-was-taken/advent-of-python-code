from modules.utils.input_reader import read_lines


def get_coordinates(coord_string: str) -> tuple[int, int]:
    """Convert a coordinate string 'x,y' into a tuple of integers (x, y)."""
    x_str, y_str = coord_string.split(",")
    return int(x_str), int(y_str)


def get_instruction(line: str) -> tuple[str, tuple[int, int], tuple[int, int]]:
    """Parse an instruction line into action and coordinate tuples."""
    parts = line.strip().split(" ")
    if parts[0] == "turn":
        action = parts[1]
        start_coords = get_coordinates(parts[2])
        end_coords = get_coordinates(parts[-1])
    elif parts[0] == "toggle":
        action = "toggle"
        start_coords = get_coordinates(parts[1])
        end_coords = get_coordinates(parts[-1])
    return action, start_coords, end_coords


def part_one() -> int:
    """Solve part one of the challenge."""
    data = read_lines(2015, 6)

    light_grid = [[0 for _ in range(1000)] for _ in range(1000)]
    lights_on = 0

    for line in data:
        action, start_coords, end_coords = get_instruction(line)

        start_x_coordinate, start_y_coordinate = start_coords
        end_x_coordinate, end_y_coordinate = end_coords

        for x in range(start_x_coordinate, end_x_coordinate + 1):
            for y in range(start_y_coordinate, end_y_coordinate + 1):
                if action == "on":
                    if light_grid[x][y] == 0:
                        light_grid[x][y] = 1
                        lights_on += 1
                elif action == "off":
                    if light_grid[x][y] == 1:
                        light_grid[x][y] = 0
                        lights_on -= 1
                elif action == "toggle":
                    if light_grid[x][y] == 1:
                        light_grid[x][y] = 0
                        lights_on -= 1
                    else:
                        light_grid[x][y] = 1
                        lights_on += 1

    return lights_on


def part_two() -> int:
    """Solve part two of the challenge."""
    data = read_lines(2015, 6)

    light_grid = [[0 for _ in range(1000)] for _ in range(1000)]
    total_brightness = 0

    for line in data:
        action, start_coords, end_coords = get_instruction(line)

        start_x_coordinate, start_y_coordinate = start_coords
        end_x_coordinate, end_y_coordinate = end_coords

        for x in range(start_x_coordinate, end_x_coordinate + 1):
            for y in range(start_y_coordinate, end_y_coordinate + 1):
                if action == "on":
                    light_grid[x][y] += 1
                    total_brightness += 1
                elif action == "off":
                    if light_grid[x][y] > 0:
                        light_grid[x][y] -= 1
                        total_brightness -= 1
                elif action == "toggle":
                    light_grid[x][y] += 2
                    total_brightness += 2

    return total_brightness


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
