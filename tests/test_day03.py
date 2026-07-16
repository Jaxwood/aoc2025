"""Tests for Day 3"""

from aoc2025.day03 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day03_part1.txt")
    expected = 357
    actual = part1(data)
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day03.txt")
    expected = 17445
    actual = part1(data)
    assert actual == expected


def test_part2a(read_input):
    data = read_input("data/day03_part1.txt")
    expected = 3121910778619
    actual = part2(data)
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day03.txt")
    expected = 173229689350551
    actual = part2(data)
    assert actual == expected
