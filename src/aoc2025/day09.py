"""Day 9: Advent of Code 2025"""

from typing import Dict, List, Tuple


def _parse_tiles(data: List[str]) -> List[Tuple[int, int]]:
    tiles: List[Tuple[int, int]] = []
    for line in data:
        if line.count(",") != 1:
            continue
        x_str, y_str = line.split(",")
        tiles.append((int(x_str), int(y_str)))
    return tiles


def _merge_intervals(intervals: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    if not intervals:
        return []

    intervals.sort()
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def _build_green_intervals_by_row(tiles: List[Tuple[int, int]]) -> Dict[int, List[Tuple[int, int]]]:
    if not tiles:
        return {}

    vertical_edges: List[Tuple[int, int, int]] = []
    horizontal_edges_by_y: Dict[int, List[Tuple[int, int]]] = {}

    n = len(tiles)
    for i in range(n):
        x1, y1 = tiles[i]
        x2, y2 = tiles[(i + 1) % n]

        if x1 == x2:
            low, high = sorted((y1, y2))
            vertical_edges.append((x1, low, high))
        else:
            low, high = sorted((x1, x2))
            horizontal_edges_by_y.setdefault(y1, []).append((low, high))

    min_y = min(y for _, y in tiles)
    max_y = max(y for _, y in tiles)

    green_by_row: Dict[int, List[Tuple[int, int]]] = {}

    for y in range(min_y, max_y + 1):
        intervals: List[Tuple[int, int]] = []

        # boundary horizontal segments on this row
        intervals.extend(horizontal_edges_by_y.get(y, []))

        # boundary vertical segments contribute their x on touched rows
        crossings: List[int] = []
        for x, low, high in vertical_edges:
            if low <= y <= high:
                intervals.append((x, x))
            if low <= y < high:
                crossings.append(x)

        # interior fill using even-odd crossings at y + 0.5
        crossings.sort()
        for idx in range(0, len(crossings) - 1, 2):
            left = crossings[idx] + 1
            right = crossings[idx + 1] - 1
            if left <= right:
                intervals.append((left, right))

        green_by_row[y] = _merge_intervals(intervals)

    return green_by_row


def _row_covers(intervals: List[Tuple[int, int]], left: int, right: int) -> bool:
    for start, end in intervals:
        if start <= left and right <= end:
            return True
    return False


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
    tiles = _parse_tiles(data)
    if len(tiles) < 2:
        return 0

    green_by_row = _build_green_intervals_by_row(tiles)

    pairs = []
    for i in range(len(tiles)):
        x1, y1 = tiles[i]
        for j in range(i + 1, len(tiles)):
            x2, y2 = tiles[j]
            left, right = sorted((x1, x2))
            bottom, top = sorted((y1, y2))
            area = (right - left + 1) * (top - bottom + 1)
            pairs.append((area, left, right, bottom, top))

    pairs.sort(reverse=True, key=lambda p: p[0])

    best = 0
    for area, left, right, bottom, top in pairs:
        if area <= best:
            break

        valid = True
        for y in range(bottom, top + 1):
            if y not in green_by_row or not _row_covers(green_by_row[y], left, right):
                valid = False
                break

        if valid:
            best = area

    return best
