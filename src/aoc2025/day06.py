"""Day 6: Advent of Code 2025"""

from typing import List


def _split_problem_columns(data: List[str]) -> List[tuple[int, int]]:
    width = max(len(line) for line in data)
    padded = [line.ljust(width) for line in data]

    spans: List[tuple[int, int]] = []
    start = None

    for col in range(width):
        is_separator = all(row[col] == " " for row in padded)

        if not is_separator and start is None:
            start = col
        elif is_separator and start is not None:
            spans.append((start, col))
            start = None

    if start is not None:
        spans.append((start, width))

    return spans


def part1(data: List[str]) -> int:
    if not data:
        return 0

    if not any("+" in line or "*" in line for line in data):
        return 0

    total = 0
    for start, end in _split_problem_columns(data):
        numbers: List[int] = []
        operation = ""

        for line in data:
            token = line[start:end].strip()
            if not token:
                continue
            if token in {"+", "*"}:
                operation = token
            elif token.isdigit():
                numbers.append(int(token))

        if not numbers:
            continue

        if operation == "+":
            total += sum(numbers)
        elif operation == "*":
            product = 1
            for n in numbers:
                product *= n
            total += product

    return total


def part2(data: List[str]) -> int:
    return 0
