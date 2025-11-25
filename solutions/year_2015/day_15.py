from modules.utils.input_reader import read_lines

AVAILABLE_TEASPOONS = 100
CALORIE_TARGET = 500


def parse_ingredients(line: str) -> tuple[str, list[int]]:
    """Parse a line of ingredient properties into a name and list of properties."""
    parts = line.split(":")
    name = parts[0].strip()
    properties = list(
        map(
            lambda x: int(x.split()[-1]),
            parts[1].strip().split(","),
        )
    )

    return name, properties


def calculate_ingredient_score(
    amounts: list[int],
    ingredients: dict[str, list[int]],
    include_calories: bool = False,
) -> int:
    """Calculate the cookie score for a given combination of ingredient amounts."""
    totals = [0, 0, 0, 0, 0]

    property_count = len(totals)

    for idx, amount in enumerate(amounts):
        ingredient = list(ingredients.values())[idx]
        for prop_idx in range(property_count):
            totals[prop_idx] += ingredient[prop_idx] * amount

    if include_calories and totals[-1] != CALORIE_TARGET:
        return 0

    score = 1
    for total in totals[:-1]:
        if total < 0:
            return 0
        score *= total

    return score


def generate_distributions(total: int, num_ingredients: int):
    """Generate all possible ways to distribute total among num_ingredients.

    Yields tuples of length num_ingredients that sum to total.
    """
    if num_ingredients == 1:
        yield (total,)
        return

    for first_amount in range(total + 1):
        for rest in generate_distributions(total - first_amount, num_ingredients - 1):
            yield (first_amount,) + rest


def find_best_cookie_score(include_calories: bool = False) -> int:
    """Find the best possible cookie score given ingredient constraints."""
    data = read_lines(2015, 15)

    ingredients = {}
    for line in data:
        name, properties = parse_ingredients(line)
        ingredients[name] = properties

    num_ingredients = len(ingredients)
    max_score = 0

    for distribution in generate_distributions(AVAILABLE_TEASPOONS, num_ingredients):
        score = calculate_ingredient_score(
            list(distribution), ingredients, include_calories=include_calories
        )
        max_score = max(max_score, score)

    return max_score


def part_one() -> int:
    data = read_lines(2015, 15)

    ingredients = {}

    for line in data:
        name, properties = parse_ingredients(line)
        ingredients[name] = properties

    return find_best_cookie_score(include_calories=False)


def part_two() -> int:
    data = read_lines(2015, 15)

    ingredients = {}

    for line in data:
        name, properties = parse_ingredients(line)
        ingredients[name] = properties

    return find_best_cookie_score(include_calories=True)


if __name__ == "__main__":
    print("Part One:", part_one())
    print("Part Two:", part_two())
