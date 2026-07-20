"""Day 5: Advent of Code 2025"""

from typing import List, Tuple


def _parse_database(data: List[str]) -> Tuple[List[Tuple[int, int]], List[int]]:
    ranges: List[Tuple[int, int]] = []
    ingredient_ids: List[int] = []

    reading_ranges = True
    for line in data:
        if line == "":
            reading_ranges = False
            continue

        if reading_ranges and "-" in line:
            start, end = line.split("-")
            ranges.append((int(start), int(end)))
        else:
            reading_ranges = False
            ingredient_ids.append(int(line))

    return ranges, ingredient_ids


def part1(data: List[str]) -> int:
    ranges, ingredient_ids = _parse_database(data)

    fresh = 0
    for ingredient_id in ingredient_ids:
        if any(start <= ingredient_id <= end for start, end in ranges):
            fresh += 1

    return fresh


def part2(data: List[str]) -> int:
    return 0
