"""Day 3: Advent of Code 2025"""

from typing import List


def find_biggest_joltage(batteries: str, digits_to_keep: int) -> int:
    """Return the largest number formed by keeping digits in original order."""
    drop = len(batteries) - digits_to_keep
    stack: List[str] = []

    for battery in batteries:
        while drop > 0 and stack and stack[-1] < battery:
            stack.pop()
            drop -= 1
        stack.append(battery)

    if drop > 0:
        stack = stack[:-drop]

    return int("".join(stack[:digits_to_keep]))


def part1(data: List[str]) -> int:
    total = 0
    for batteries in data:
        total += find_biggest_joltage(batteries, 2)

    return total


def part2(data: List[str]) -> int:
    total = 0
    for batteries in data:
        total += find_biggest_joltage(batteries, 12)

    return total
