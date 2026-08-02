"""Day 11: Advent of Code 2025"""

from functools import lru_cache
from typing import Dict, List


def _parse_graph(data: List[str]) -> Dict[str, List[str]]:
    graph: Dict[str, List[str]] = {}

    for line in data:
        line = line.strip()
        if not line or ":" not in line:
            continue

        node, outputs = line.split(":", 1)
        node = node.strip()
        graph[node] = outputs.strip().split() if outputs.strip() else []

    return graph


def part1(data: List[str]) -> int:
    graph = _parse_graph(data)
    if "you" not in graph:
        return 0

    visiting = set()

    @lru_cache(maxsize=None)
    def count_paths(node: str) -> int:
        if node == "out":
            return 1
        if node not in graph:
            return 0
        if node in visiting:
            return 0

        visiting.add(node)
        total = sum(count_paths(next_node) for next_node in graph[node])
        visiting.remove(node)
        return total

    return count_paths("you")


def part2(data: List[str]) -> int:
    return 0
