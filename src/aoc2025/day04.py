"""Day 4: Advent of Code 2025"""

from collections import deque
from typing import List, Set, Tuple


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
    rolls: Set[Tuple[int, int]] = {
        (row, col)
        for row, line in enumerate(data)
        for col, char in enumerate(line)
        if char == "@"
    }

    adjacent_count = {
        (row, col): _adjacent_rolls(data, row, col)
        for row, col in rolls
    }

    queue = deque([pos for pos, neighbors in adjacent_count.items() if neighbors < 4])
    removed: Set[Tuple[int, int]] = set()

    while queue:
        row, col = queue.popleft()
        position = (row, col)
        if position in removed:
            continue

        removed.add(position)

        for d_row in (-1, 0, 1):
            for d_col in (-1, 0, 1):
                if d_row == 0 and d_col == 0:
                    continue

                neighbor = (row + d_row, col + d_col)
                if neighbor not in adjacent_count or neighbor in removed:
                    continue

                adjacent_count[neighbor] -= 1
                if adjacent_count[neighbor] < 4:
                    queue.append(neighbor)

    return len(removed)
