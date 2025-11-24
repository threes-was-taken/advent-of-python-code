from modules.utils.input_reader import read_lines

RACE_DURATION = 2503


def parse_reindeer(line: str) -> tuple[int, int, int]:
    parts = line.split()
    speed = int(parts[3])
    fly_time = int(parts[6])
    rest_time = int(parts[13])
    return speed, fly_time, rest_time


def calculate_reindeer_distance(
    speed: int, fly_time: int, rest_time: int, duration: int
) -> int:
    cycle_time = fly_time + rest_time
    full_cycles = duration // cycle_time
    remaining_time = duration % cycle_time

    distance = full_cycles * speed * fly_time
    distance += speed * min(remaining_time, fly_time)

    return distance


def part_one() -> int:
    data = read_lines(2015, 14)

    reindeer_distances = {}

    for reindeer in data:
        speed, fly_time, rest_time = parse_reindeer(reindeer)

        distance = calculate_reindeer_distance(
            speed, fly_time, rest_time, RACE_DURATION
        )

        reindeer_distances[reindeer] = distance

    return max(reindeer_distances.values())


def part_two() -> int:
    data = read_lines(2015, 14)

    reindeer_stats = []

    for reindeer in data:
        speed, fly_time, rest_time = parse_reindeer(reindeer)
        reindeer_stats.append((speed, fly_time, rest_time))

    reindeer_points = [0] * len(reindeer_stats)
    reindeer_distances = [0] * len(reindeer_stats)

    for second in range(1, RACE_DURATION + 1):
        for i, (speed, fly_time, rest_time) in enumerate(reindeer_stats):
            distance = calculate_reindeer_distance(speed, fly_time, rest_time, second)
            reindeer_distances[i] = distance
        max_distance = max(reindeer_distances)
        for i, distance in enumerate(reindeer_distances):
            if distance == max_distance:
                reindeer_points[i] += 1

    return max(reindeer_points)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
