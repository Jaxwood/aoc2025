"""Tests for Day 3"""

import pytest
from aoc2025.day03 import part1


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
