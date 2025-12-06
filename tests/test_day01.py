"""Tests for Day 1"""

from aoc2025.day01 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day01_part1.txt")
    expected = 3
    actual = part1(data)
    assert actual == expected

def test_part1(read_input):
    data = read_input("data/day01.txt")
    expected = 1048
    actual = part1(data)
    assert actual == expected

def test_part2(read_input):
    pass
