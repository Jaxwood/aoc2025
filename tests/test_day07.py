"""Tests for Day 7"""

from aoc2025.day07 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day07_part1.txt")
    expected = 21
    actual = part1(data)
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day07.txt")
    expected = 1553
    actual = part1(data)
    assert actual == expected


def test_part2a(read_input):
    data = read_input("data/day07_part1.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day07.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected
