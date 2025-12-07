"""Tests for Day 2"""

import pytest
from aoc2025.day02 import part1, part2, is_invalid, is_repeated_invalid


def test_part1a(read_input):
    data = read_input("data/day02_part1.txt")
    expected = 1227775554
    actual = part1(data[0])
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day02.txt")
    expected = 21898734247
    actual = part1(data[0])
    assert actual == expected


def test_part2a(read_input):
    data = read_input("data/day02_part1.txt")
    expected = 4174379265
    actual = part2(data[0])
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day02.txt")
    expected = 28915664389
    actual = part2(data[0])
    assert actual == expected


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (11, 22, [11, 22]),
        (95, 115, [99]),
        (998, 1012, [1010]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (38593856, 38593862, [38593859]),
    ],
)
def test_is_invalid(start, end, expected):
    for number in range(start, end + 1):
        expected_result = number in expected
        assert is_invalid(number) == expected_result


@pytest.mark.parametrize(
    "start,end,expected",
    [
        (11, 22, [11, 22]),
        (95, 115, [99, 111]),
        (998, 1012, [999, 1010]),
        (1188511880, 1188511890, [1188511885]),
        (222220, 222224, [222222]),
        (1698522, 1698528, []),
        (446443, 446449, [446446]),
        (38593856, 38593862, [38593859]),
        (565653, 565659, [565656]),
        (824824821, 824824827, [824824824]),
        (2121212118, 2121212124, [2121212121]),
    ],
)
def test_is_repeated_invalid(start, end, expected):
    for number in range(start, end + 1):
        expected_result = number in expected
        assert is_repeated_invalid(number) == expected_result
