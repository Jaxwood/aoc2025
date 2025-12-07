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


def is_repeated_invalid(n: int) -> bool:
    """is invalid if it is made only of some sequence of digits repeated at least twice. So, 12341234 (1234 two times), 123123123 (123 three times), 1212121212 (12 five times), and 1111111 (1 seven times) are all invalid IDs."""
    str_n = str(n)
    length = len(str_n)

    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            pattern = str_n[:pattern_length]
            repeat_count = length // pattern_length

            if repeat_count >= 2:
                if pattern * repeat_count == str_n:
                    return True

    return False


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


def part2(data: str) -> int:
    ranges = data.split(",")
    invalid_numbers = []
    for r in ranges:
        bounds = r.split("-")
        start, end = int(bounds[0]), int(bounds[1])
        for n in range(start, end + 1):
            if is_repeated_invalid(n):
                invalid_numbers.append(n)
    return sum(invalid_numbers)
