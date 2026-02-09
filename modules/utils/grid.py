"""Grid utilities for 2D navigation problems."""

from typing import Iterator

# Common direction vectors
DIRECTIONS_4 = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
DIRECTIONS_8 = [
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
]  # All 8 directions including diagonals

DIRECTION_MAP = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
    "U": (-1, 0),
    "D": (1, 0),
    "R": (0, 1),
    "L": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
    ">": (0, 1),
    "<": (0, -1),
}


def parse_grid(text: str) -> list[list[str]]:
    """Parse a text grid into a 2D list.

    Example:
        >>> grid = parse_grid("..#\\n#..\\n...")
        >>> grid[0][2]
        '#'
    """
    return [list(line) for line in text.strip().split("\n")]


def parse_grid_dict(text: str) -> dict[tuple[int, int], str]:
    """Parse a text grid into a dictionary mapping (row, col) -> char.

    Useful for sparse grids or when you need to add/remove cells.

    Example:
        >>> grid = parse_grid_dict("..#\\n#..")
        >>> grid[(0, 2)]
        '#'
    """
    grid = {}
    for row, line in enumerate(text.strip().split("\n")):
        for col, char in enumerate(line):
            grid[(row, col)] = char
    return grid


def neighbors_4(row: int, col: int) -> Iterator[tuple[int, int]]:
    """Yield the 4 orthogonal neighbors (up, down, left, right)."""
    for dr, dc in DIRECTIONS_4:
        yield (row + dr, col + dc)


def neighbors_8(row: int, col: int) -> Iterator[tuple[int, int]]:
    """Yield all 8 neighbors including diagonals."""
    for dr, dc in DIRECTIONS_8:
        yield (row + dr, col + dc)


def in_bounds(row: int, col: int, grid: list[list]) -> bool:
    """Check if position is within grid bounds."""
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])


def print_grid(grid: list[list[str]] | dict[tuple[int, int], str]) -> None:
    """Pretty print a grid."""
    if isinstance(grid, dict):
        if not grid:
            return
        min_row = min(r for r, c in grid.keys())
        max_row = max(r for r, c in grid.keys())
        min_col = min(c for r, c in grid.keys())
        max_col = max(c for r, c in grid.keys())

        for row in range(min_row, max_row + 1):
            print("".join(grid.get((row, col), " ") for col in range(min_col, max_col + 1)))
    else:
        for row in grid:
            print("".join(row))


def manhattan_distance(pos1: tuple[int, int], pos2: tuple[int, int]) -> int:
    """Calculate Manhattan distance between two positions."""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def rotate_90(direction: tuple[int, int], clockwise: bool = True) -> tuple[int, int]:
    """Rotate a direction vector 90 degrees.

    Example:
        >>> rotate_90((0, 1))  # Right -> Down
        (1, 0)
    """
    dr, dc = direction
    if clockwise:
        return (dc, -dr)
    else:
        return (-dc, dr)
