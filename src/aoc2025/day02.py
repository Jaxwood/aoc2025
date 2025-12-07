"""Day 2: Advent of Code 2025"""


def is_invalid(n: int) -> bool:
    """Number is invalid if number is repeated exactly twice, e.g., 11, 22, 6464, 123123 etc."""
    str_n = str(n)
    length = len(str_n)

    if length % 2 != 0:
        return False

    half_length = length // 2
    first_half = str_n[:half_length]
    second_half = str_n[half_length:]

    return first_half == second_half


def part1(data: str) -> int:
    ranges = data.split(",")
    invalid_numbers = []
    for r in ranges:
        bounds = r.split("-")
        start, end = int(bounds[0]), int(bounds[1])
        for n in range(start, end + 1):
            if is_invalid(n):
                invalid_numbers.append(n)
    return sum(invalid_numbers)
