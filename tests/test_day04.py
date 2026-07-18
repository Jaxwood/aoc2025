"""Tests for Day 4"""

from aoc2025.day04 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day04_part1.txt")
    expected = 13
    actual = part1(data)
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day04.txt")
    expected = 1389
    actual = part1(data)
    assert actual == expected


def test_part2a(read_input):
    data = read_input("data/day04_part1.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day04.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected
