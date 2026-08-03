"""Day 11: Advent of Code 2025"""

from functools import lru_cache
from typing import Dict, List, Set


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


def _count_paths(graph: Dict[str, List[str]], start: str, required: Set[str]) -> int:
    if start not in graph:
        return 0

    required_nodes = sorted(required)
    required_index = {name: idx for idx, name in enumerate(required_nodes)}
    all_required_mask = (1 << len(required_nodes)) - 1
    visiting = set()

    @lru_cache(maxsize=None)
    def count_paths(node: str, required_mask: int) -> int:
        if node in required_index:
            required_mask |= 1 << required_index[node]

        state = (node, required_mask)
        if state in visiting:
            return 0

        if node == "out":
            return 1 if required_mask == all_required_mask else 0

        if node not in graph:
            return 0

        visiting.add(state)
        total = sum(count_paths(next_node, required_mask) for next_node in graph[node])
        visiting.remove(state)
        return total

    return count_paths(start, 0)


def part1(data: List[str]) -> int:
    graph = _parse_graph(data)
    return _count_paths(graph, start="you", required=set())


def part2(data: List[str]) -> int:
    graph = _parse_graph(data)
    return _count_paths(graph, start="svr", required={"dac", "fft"})
