from itertools import cycle
from typing import NamedTuple


SANTA = 'Santa'
ROBO_SANTA = 'Robo-Santa'


class Coordinates(NamedTuple):
    x: int
    y: int


def houses_that_received_presents_count(instructions: str) -> int:
    if not instructions:
        return 0

    deliverer = cycle([SANTA, ROBO_SANTA])
    current_coordinates = Coordinates(x=0, y=0)
    santa_coordinates = [current_coordinates]
    robo_santa_coordinates = [current_coordinates]

    for instruction in instructions:
        deliverer_coordinates = santa_coordinates if next(deliverer) == SANTA else robo_santa_coordinates
        previous_coordinates = deliverer_coordinates[-1]
        current_coordinates = _new_position(instruction, previous_coordinates)

        if previous_coordinates != current_coordinates:
            deliverer_coordinates.append(current_coordinates)
        else:
            next(deliverer)

    return len(set(santa_coordinates + robo_santa_coordinates))


def _new_position(instruction: str, current_coordinates: Coordinates) -> Coordinates:
    if instruction == '>':
        return Coordinates(x=current_coordinates.x + 1, y=current_coordinates.y)
    if instruction == 'v':
        return Coordinates(x=current_coordinates.x, y=current_coordinates.y - 1)
    if instruction == '<':
        return Coordinates(x=current_coordinates.x - 1, y=current_coordinates.y)
    if instruction == '^':
        return Coordinates(x=current_coordinates.x, y=current_coordinates.y + 1)
    return current_coordinates
