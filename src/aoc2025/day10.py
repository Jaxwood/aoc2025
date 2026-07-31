"""Day 10: Advent of Code 2025"""

import re
from fractions import Fraction
from typing import Dict, List, Optional, Tuple


PATTERN_RE = re.compile(r"\[([.#]+)\]")
BUTTON_RE = re.compile(r"\(([^)]*)\)")
JOLT_RE = re.compile(r"\{([^}]*)\}")


def _parse_buttons(line: str) -> List[List[int]]:
    buttons: List[List[int]] = []
    for group in BUTTON_RE.findall(line):
        group = group.strip()
        if not group:
            continue
        buttons.append([int(token.strip()) for token in group.split(",") if token.strip()])
    return buttons


def _parse_machine_for_part1(line: str) -> Tuple[int, List[int]]:
    pattern_match = PATTERN_RE.search(line)
    if not pattern_match:
        return 0, []

    pattern = pattern_match.group(1)
    target_mask = 0
    for i, c in enumerate(pattern):
        if c == "#":
            target_mask |= 1 << i

    buttons: List[int] = []
    for button in _parse_buttons(line):
        mask = 0
        for idx in button:
            mask ^= 1 << idx
        buttons.append(mask)

    return target_mask, buttons


def _parse_machine_for_part2(line: str) -> Tuple[List[int], List[List[int]]]:
    joltage_match = JOLT_RE.search(line)
    if not joltage_match:
        return [], []

    targets = [int(x.strip()) for x in joltage_match.group(1).split(",") if x.strip()]
    buttons = _parse_buttons(line)
    return targets, buttons


def _fewest_presses_part1(target_mask: int, buttons: List[int]) -> int:
    best_for_state = {0: 0}

    for button_mask in buttons:
        next_best = dict(best_for_state)
        for state, presses in best_for_state.items():
            new_state = state ^ button_mask
            new_presses = presses + 1
            if new_presses < next_best.get(new_state, float("inf")):
                next_best[new_state] = new_presses
        best_for_state = next_best

    return best_for_state.get(target_mask, 0)


def _rref_augmented(a: List[List[int]], b: List[int]) -> Optional[Tuple[List[List[Fraction]], List[int], List[int]]]:
    m = len(a)
    n = len(a[0]) if a else 0
    matrix = [[Fraction(a[i][j]) for j in range(n)] + [Fraction(b[i])] for i in range(m)]

    pivot_cols: List[int] = []
    pivot_row = 0

    for col in range(n):
        candidate = None
        for row in range(pivot_row, m):
            if matrix[row][col] != 0:
                candidate = row
                break

        if candidate is None:
            continue

        matrix[pivot_row], matrix[candidate] = matrix[candidate], matrix[pivot_row]

        pivot_value = matrix[pivot_row][col]
        for j in range(col, n + 1):
            matrix[pivot_row][j] /= pivot_value

        for row in range(m):
            if row == pivot_row or matrix[row][col] == 0:
                continue
            factor = matrix[row][col]
            for j in range(col, n + 1):
                matrix[row][j] -= factor * matrix[pivot_row][j]

        pivot_cols.append(col)
        pivot_row += 1
        if pivot_row == m:
            break

    for row in range(m):
        if all(matrix[row][col] == 0 for col in range(n)) and matrix[row][n] != 0:
            return None

    free_cols = [col for col in range(n) if col not in pivot_cols]
    return matrix, pivot_cols, free_cols


def _fewest_presses_part2(targets: List[int], buttons: List[List[int]]) -> int:
    if not targets:
        return 0

    counter_count = len(targets)
    button_count = len(buttons)
    if button_count == 0:
        return 0 if all(v == 0 for v in targets) else 0

    # A[row][col] = 1 if button col increments counter row
    a = [
        [1 if row in buttons[col] else 0 for col in range(button_count)]
        for row in range(counter_count)
    ]

    rref_result = _rref_augmented(a, targets)
    if rref_result is None:
        return 0

    matrix, pivot_cols, free_cols = rref_result

    # map pivot column -> row index in RREF where that pivot lives
    pivot_row_for_col: Dict[int, int] = {}
    for col in pivot_cols:
        for row in range(counter_count):
            if matrix[row][col] == 1:
                pivot_row_for_col[col] = row
                break

    # Finite upper bounds for each free variable from original constraints.
    free_bounds: List[Tuple[int, int]] = []
    for col in free_cols:
        affected_targets = [targets[row] for row in range(counter_count) if a[row][col] == 1]
        upper_bound = min(affected_targets) if affected_targets else 0
        free_bounds.append((col, upper_bound))

    free_bounds.sort(key=lambda item: item[1])

    best = float("inf")
    assignment: Dict[int, int] = {}

    def search(index: int, free_sum: int) -> None:
        nonlocal best

        if free_sum >= best:
            return

        if index == len(free_bounds):
            total = free_sum

            for pivot_col in pivot_cols:
                row = pivot_row_for_col[pivot_col]
                value = matrix[row][button_count]

                for free_col in free_cols:
                    coeff = matrix[row][free_col]
                    if coeff != 0:
                        value -= coeff * assignment.get(free_col, 0)

                if value < 0 or value.denominator != 1:
                    return

                total += value.numerator
                if total >= best:
                    return

            best = total
            return

        free_col, upper_bound = free_bounds[index]
        for presses in range(upper_bound + 1):
            assignment[free_col] = presses
            search(index + 1, free_sum + presses)

    search(0, 0)
    return int(best if best != float("inf") else 0)


def part1(data: List[str]) -> int:
    total = 0
    for line in data:
        line = line.strip()
        if not line:
            continue

        target_mask, buttons = _parse_machine_for_part1(line)
        if not buttons and target_mask == 0:
            continue

        total += _fewest_presses_part1(target_mask, buttons)

    return total


def part2(data: List[str]) -> int:
    total = 0
    for line in data:
        line = line.strip()
        if not line:
            continue

        targets, buttons = _parse_machine_for_part2(line)
        if not targets and not buttons:
            continue

        total += _fewest_presses_part2(targets, buttons)

    return total
