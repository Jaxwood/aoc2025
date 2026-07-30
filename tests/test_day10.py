"""Tests for Day 10"""

from aoc2025.day10 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day10_part1.txt")
    expected = 7
    actual = part1(data)
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day10.txt")
    expected = 481
    actual = part1(data)
    assert actual == expected


def test_part2a(read_input):
    data = read_input("data/day10_part1.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day10.txt")
    expected = 0
    actual = part2(data)
    assert actual == expected
