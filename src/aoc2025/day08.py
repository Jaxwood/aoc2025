"""Day 8: Advent of Code 2025"""

import heapq
from typing import List, Tuple


class UnionFind:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a == root_b:
            return False

        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1

        return True


def _parse_points(data: List[str]) -> List[Tuple[int, int, int]]:
    points: List[Tuple[int, int, int]] = []
    for line in data:
        if line.count(",") != 2:
            continue
        x_str, y_str, z_str = line.split(",")
        points.append((int(x_str), int(y_str), int(z_str)))
    return points


def _distance_squared(a: Tuple[int, int, int], b: Tuple[int, int, int]) -> int:
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2


def part1(data: List[str]) -> int:
    points = _parse_points(data)
    n = len(points)
    if n < 3:
        return 0

    def pairs():
        for i in range(n):
            for j in range(i + 1, n):
                yield (_distance_squared(points[i], points[j]), i, j)

    connection_target = 10 if n <= 20 else 1000
    shortest_pairs = heapq.nsmallest(min(connection_target, n * (n - 1) // 2), pairs())

    uf = UnionFind(n)
    for _, i, j in shortest_pairs:
        uf.union(i, j)

    component_sizes = {}
    for node in range(n):
        root = uf.find(node)
        component_sizes[root] = component_sizes.get(root, 0) + 1

    largest = sorted(component_sizes.values(), reverse=True)
    if len(largest) < 3:
        return 0

    return largest[0] * largest[1] * largest[2]


def part2(data: List[str]) -> int:
    points = _parse_points(data)
    n = len(points)
    if n < 2:
        return 0

    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            edges.append((_distance_squared(points[i], points[j]), i, j))

    edges.sort(key=lambda edge: edge[0])

    uf = UnionFind(n)
    components = n

    for _, i, j in edges:
        if uf.union(i, j):
            components -= 1
            if components == 1:
                return points[i][0] * points[j][0]

    return 0
