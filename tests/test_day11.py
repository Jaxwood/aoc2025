"""Tests for Day 11"""

from aoc2025.day11 import part1, part2


def test_part1a(read_input):
    data = read_input("data/day11_part1.txt")
    expected = 5
    actual = part1(data)
    assert actual == expected


def test_part1(read_input):
    data = read_input("data/day11.txt")
    expected = 652
    actual = part1(data)
    assert actual == expected


def test_part2a():
    data = [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]
    expected = 2
    actual = part2(data)
    assert actual == expected


def test_part2(read_input):
    data = read_input("data/day11.txt")
    expected = 362956369749210
    actual = part2(data)
    assert actual == expected
