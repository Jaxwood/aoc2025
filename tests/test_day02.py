"""Tests for Day 2"""

from aoc2025.day02 import part1


def test_part1a(read_input):
    data = read_input("data/day02_part1.txt")
    expected = 1227775554
    actual = part1(data)
    assert actual == expected
