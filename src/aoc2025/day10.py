"""Day 10: Advent of Code 2025"""

import re
from typing import List, Tuple


PATTERN_RE = re.compile(r"\[([.#]+)\]")
BUTTON_RE = re.compile(r"\(([^)]*)\)")


def _parse_machine(line: str) -> Tuple[int, List[int]]:
    pattern_match = PATTERN_RE.search(line)
    if not pattern_match:
        return 0, []

    pattern = pattern_match.group(1)
    target_mask = 0
    for i, c in enumerate(pattern):
        if c == "#":
            target_mask |= 1 << i

    buttons: List[int] = []
    for group in BUTTON_RE.findall(line):
        group = group.strip()
        if not group:
            continue

        mask = 0
        for token in group.split(","):
            idx = int(token.strip())
            mask ^= 1 << idx
        buttons.append(mask)

    return target_mask, buttons


def _fewest_presses(target_mask: int, buttons: List[int]) -> int:
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


def part1(data: List[str]) -> int:
    total = 0
    for line in data:
        line = line.strip()
        if not line:
            continue

        target_mask, buttons = _parse_machine(line)
        if not buttons and target_mask == 0:
            continue

        total += _fewest_presses(target_mask, buttons)

    return total


def part2(data: List[str]) -> int:
    return 0
