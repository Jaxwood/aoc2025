"""Day 4: Advent of Code 2025"""

from typing import List


def _adjacent_rolls(grid: List[str], row: int, col: int) -> int:
    height = len(grid)
    width = len(grid[0])
    adjacent = 0

    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == 0 and d_col == 0:
                continue

            n_row, n_col = row + d_row, col + d_col
            if 0 <= n_row < height and 0 <= n_col < width and grid[n_row][n_col] == "@":
                adjacent += 1

    return adjacent


def part1(data: List[str]) -> int:
    accessible = 0

    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "@" and _adjacent_rolls(data, row, col) < 4:
                accessible += 1

    return accessible


def part2(data: List[str]) -> int:
    return 0
