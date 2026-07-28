"""Day 9: Advent of Code 2025"""

from typing import List, Tuple


def _parse_tiles(data: List[str]) -> List[Tuple[int, int]]:
    tiles: List[Tuple[int, int]] = []
    for line in data:
        if line.count(",") != 1:
            continue
        x_str, y_str = line.split(",")
        tiles.append((int(x_str), int(y_str)))
    return tiles


def part1(data: List[str]) -> int:
    tiles = _parse_tiles(data)
    if len(tiles) < 2:
        return 0

    max_area = 0
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        for j in range(i + 1, len(tiles)):
            x2, y2 = tiles[j]
            area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)
            if area > max_area:
                max_area = area

    return max_area


def part2(data: List[str]) -> int:
    return 0
