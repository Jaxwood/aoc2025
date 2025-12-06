"""Day 1: Advent of Code 2025"""

from typing import List, NamedTuple
from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2

class Rotation(NamedTuple):
    direction: Direction
    times: int

class Dial():
    def __init__(self, start_position: int = 50, max_position: int = 99):
        self.position = start_position
        self.MAX_POSITION = max_position
        self.zero_based_position = 0

    def rotate(self, rotation: Rotation):
        # make sure rotation times is within bounds
        times = rotation.times % (self.MAX_POSITION + 1)
        if rotation.direction == Direction.LEFT:
            self.position -= times
        else:
            self.position += times

        # handle out-of-bounds after the rotation
        if self.position < 0:
            self.position += self.MAX_POSITION + 1
        elif self.position > self.MAX_POSITION:
            self.position -= self.MAX_POSITION + 1

        # we should always be within bounds here
        assert 0 <= self.position <= self.MAX_POSITION

        if self.position == 0:
            self.zero_based_position += 1

    def zero_based_positions(self) -> int:
        return self.zero_based_position

def _parse_input(data: List[str]) -> List[Rotation]:
    rotations = []
    for line in data:
        direction, times = line[0], int(line[1:])
        if direction == 'L':
            rotations.append(Rotation(Direction.LEFT, times))
        elif direction == 'R':
            rotations.append(Rotation(Direction.RIGHT, times))
        else:
            raise ValueError(f"Invalid direction: {direction}")

    return rotations

def part1(data: List[str]) -> int:
    dial = Dial(50, 99)
    rotations = _parse_input(data)
    for rotation in rotations:
        dial.rotate(rotation)

    return dial.zero_based_positions()


def part2(data):
    pass
