"""Tests for Day 12"""

from aoc2025.day12 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day12_part1.txt")
    expected = 2
    actual = part1(data)
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day12.txt")
    expected = 0
    actual = part1(data)
    assert actual == expected


def test_part2a(read_input):
    data = read_input("data/day12_part1.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day12.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected
