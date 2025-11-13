from itertools import pairwise, permutations

from modules.utils.input_reader import read_lines


def prepare_routes(data: list[str]) -> tuple[set[str], dict[tuple[str, str], int]]:
    """
    Parse input data to extract cities and their routes with distances.

    Args:
        data: List of strings in format "CityA to CityB = distance"

    Returns:
        Tuple of (set of city names, dict mapping city pairs to distances)
    """
    routes: dict[tuple[str, str], int] = {}
    cities: set[str] = set()

    for line in data:
        parts = line.split(" to ")
        if len(parts) != 2:
            continue  # Skip malformed lines

        origin = parts[0]
        dest_parts = parts[1].split(" = ")

        if len(dest_parts) != 2:
            continue

        destination = dest_parts[0]
        distance = int(dest_parts[1])

        cities.add(origin)
        cities.add(destination)

        # Store bidirectional routes
        routes[(origin, destination)] = distance
        routes[(destination, origin)] = distance

    return cities, routes


def calculate_route_distance(
    route: tuple[str, ...], routes: dict[tuple[str, str], int]
) -> int | None:
    """
    Calculate total distance for a given route.

    Args:
        route: Tuple of city names in order
        routes: Dict mapping city pairs to distances

    Returns:
        Total distance if route is valid, None otherwise
    """
    total_distance = 0

    for city_pair in pairwise(route):
        if city_pair not in routes:
            return None
        total_distance += routes[city_pair]

    return total_distance


def find_optimal_route(
    cities: set[str], routes: dict[tuple[str, str], int], find_max: bool = False
) -> int:
    """
    Find the optimal route that visits each city exactly once.

    This is the Traveling Salesman Problem (TSP).

    Args:
        cities: Set of all city names
        routes: Dict mapping city pairs to distances
        find_max: If True, find longest route; if False, find shortest

    Returns:
        Optimal distance (shortest or longest based on find_max)
    """
    if not cities:
        return 0

    optimal_distance = float("-inf") if find_max else float("inf")
    comparison = max if find_max else min

    for route in permutations(cities):
        distance = calculate_route_distance(route, routes)

        if distance is not None:
            optimal_distance = comparison(optimal_distance, distance)

    return (
        int(optimal_distance)
        if optimal_distance != float("inf") and optimal_distance != float("-inf")
        else 0
    )


def part_one() -> int:
    """Calculate the shortest route visiting all cities exactly once."""
    data = read_lines(2015, 9)
    cities, routes = prepare_routes(data)
    return find_optimal_route(cities, routes, find_max=False)


def part_two() -> int:
    """Calculate the longest route visiting all cities exactly once."""
    data = read_lines(2015, 9)
    cities, routes = prepare_routes(data)
    return find_optimal_route(cities, routes, find_max=True)
