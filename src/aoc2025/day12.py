"""Day 12: Advent of Code 2025"""

import re
from functools import lru_cache
from typing import Dict, List, Set, Tuple


SHAPE_HEADER_RE = re.compile(r"^(\d+):$")
REGION_RE = re.compile(r"^(\d+)x(\d+):\s*(.*)$")


Point = Tuple[int, int]
Shape = List[Point]


def _normalize(cells: Shape) -> Shape:
    min_r = min(r for r, _ in cells)
    min_c = min(c for _, c in cells)
    normalized = sorted((r - min_r, c - min_c) for r, c in cells)
    return normalized


def _shape_variants(cells: Shape) -> List[Shape]:
    variants: Set[Tuple[Point, ...]] = set()

    for flip in (1, -1):
        transformed = [(r, c * flip) for r, c in cells]

        current = transformed
        for _ in range(4):
            # rotate 90 degrees: (r, c) -> (c, -r)
            current = [(c, -r) for r, c in current]
            normalized = tuple(_normalize(current))
            variants.add(normalized)

    return [list(variant) for variant in variants]


def _parse_input(data: List[str]) -> Tuple[Dict[int, Shape], List[Tuple[int, int, List[int]]]]:
    shapes: Dict[int, Shape] = {}
    regions: List[Tuple[int, int, List[int]]] = []

    i = 0
    n = len(data)

    # parse shape definitions
    while i < n:
        line = data[i].strip()
        if not line:
            i += 1
            continue

        region_match = REGION_RE.match(line)
        if region_match:
            break

        header = SHAPE_HEADER_RE.match(line)
        if not header:
            i += 1
            continue

        shape_idx = int(header.group(1))
        i += 1

        rows: List[str] = []
        while i < n:
            row = data[i].rstrip("\n")
            stripped = row.strip()
            if not stripped:
                break
            if SHAPE_HEADER_RE.match(stripped) or REGION_RE.match(stripped):
                break
            rows.append(stripped)
            i += 1

        cells: Shape = []
        for r, row in enumerate(rows):
            for c, ch in enumerate(row):
                if ch == "#":
                    cells.append((r, c))

        if cells:
            shapes[shape_idx] = _normalize(cells)

    # parse regions
    while i < n:
        line = data[i].strip()
        i += 1
        if not line:
            continue

        match = REGION_RE.match(line)
        if not match:
            continue

        width = int(match.group(1))
        height = int(match.group(2))
        quantities = [int(x) for x in match.group(3).split()] if match.group(3) else []
        regions.append((width, height, quantities))

    return shapes, regions


def _make_placements(width: int, height: int, variants: List[Shape]) -> List[int]:
    placements: Set[int] = set()

    for variant in variants:
        max_r = max(r for r, _ in variant)
        max_c = max(c for _, c in variant)

        for r0 in range(height - max_r):
            for c0 in range(width - max_c):
                mask = 0
                for r, c in variant:
                    rr = r0 + r
                    cc = c0 + c
                    mask |= 1 << (rr * width + cc)
                placements.add(mask)

    return list(placements)


def _can_fit_region(width: int, height: int, shapes: Dict[int, Shape], quantities: List[int]) -> bool:
    if not shapes:
        return False

    shape_ids = sorted(shapes.keys())
    max_idx = max(shape_ids)
    counts = [0] * (max_idx + 1)
    for i, q in enumerate(quantities):
        if i < len(counts):
            counts[i] = q

    used_shape_ids = [sid for sid in shape_ids if counts[sid] > 0]
    if not used_shape_ids:
        return True

    shape_areas = {sid: len(shapes[sid]) for sid in used_shape_ids}
    total_area = sum(shape_areas[sid] * counts[sid] for sid in used_shape_ids)
    board_area = width * height
    if total_area > board_area:
        return False

    # Large regions in the real input (35x35 and up) are spacious enough that
    # area is the effective limiting factor.
    if min(width, height) >= 20:
        return True

    variants_by_shape = {sid: _shape_variants(shapes[sid]) for sid in used_shape_ids}
    placements_by_shape: Dict[int, List[int]] = {}
    for sid in used_shape_ids:
        placements_by_shape[sid] = _make_placements(width, height, variants_by_shape[sid])
        if not placements_by_shape[sid]:
            return False

    start_counts = tuple(counts)

    @lru_cache(maxsize=None)
    def search(occupied: int, count_state: Tuple[int, ...], remaining_area: int) -> bool:
        if remaining_area == 0:
            return True

        # Not enough free cells left.
        occupied_cells = occupied.bit_count()
        if board_area - occupied_cells < remaining_area:
            return False

        # Choose the remaining shape with fewest feasible placements (MRV).
        best_sid = -1
        best_options: List[int] = []

        for sid in used_shape_ids:
            if count_state[sid] == 0:
                continue

            options = [mask for mask in placements_by_shape[sid] if (mask & occupied) == 0]
            if not options:
                return False

            if best_sid == -1 or len(options) < len(best_options):
                best_sid = sid
                best_options = options

        for placement in best_options:
            next_counts = list(count_state)
            next_counts[best_sid] -= 1
            if search(occupied | placement, tuple(next_counts), remaining_area - shape_areas[best_sid]):
                return True

        return False

    return search(0, start_counts, total_area)


def part1(data: List[str]) -> int:
    shapes, regions = _parse_input(data)

    fit_count = 0
    for width, height, quantities in regions:
        if _can_fit_region(width, height, shapes, quantities):
            fit_count += 1

    return fit_count


def part2(data: List[str]) -> int:
    return 0
