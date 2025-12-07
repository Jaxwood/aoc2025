"""Day 3: Advent of Code 2025"""

from typing import List, Tuple


def find_biggest_battery(
    first: int, second: int, batteries: List[int]
) -> Tuple[int, int]:
    if len(batteries) == 0:
        return first, second

    next, *rest = batteries
    if next > first and len(rest) > 0:
        return find_biggest_battery(next, 0, rest)
    if next > second:
        return find_biggest_battery(first, next, rest)

    return find_biggest_battery(first, second, rest)


def part1(data: List[str]) -> int:
    total = 0
    for raw in data:
        batteries = [int(x) for x in raw]
        digit, digit2 = find_biggest_battery(0, 0, batteries)
        total += digit * 10 + digit2

    return total
