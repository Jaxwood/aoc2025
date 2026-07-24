"""Day 7: Advent of Code 2025"""

from typing import List, Set


def part1(data: List[str]) -> int:
    if not data:
        return 0

    width = max(len(row) for row in data)
    grid = [row.ljust(width) for row in data]

    start_row = -1
    start_col = -1
    for row_idx, row in enumerate(grid):
        col_idx = row.find("S")
        if col_idx != -1:
            start_row = row_idx
            start_col = col_idx
            break

    if start_col == -1:
        return 0

    split_count = 0
    active: Set[int] = {start_col}

    for row_idx in range(start_row + 1, len(grid)):
        next_active: Set[int] = set()

        for col in active:
            if not (0 <= col < width):
                continue

            if grid[row_idx][col] == "^":
                split_count += 1
                if col - 1 >= 0:
                    next_active.add(col - 1)
                if col + 1 < width:
                    next_active.add(col + 1)
            else:
                next_active.add(col)

        active = next_active
        if not active:
            break

    return split_count


def part2(data: List[str]) -> int:
    return 0
