from itertools import product
from typing import List, Tuple, NamedTuple

Grid = List[List[int]]

ON, OFF = True, False


class Coords(NamedTuple):
    x: int
    y: int


def lights_turned_on_in_grid(grid: Grid) -> int:
    return sum(light for row in grid for light in row if light is ON)


def switch_lights_on_grid(grid: Grid, instructions: List[str]) -> None:
    for instruction in instructions:
        _switch_lights(grid, *_parse_instructions(instruction))


def _switch_lights(grid: Grid, action: str, from_coords: Coords, to_coords: Coords) -> None:
    from_coords_range = range(from_coords.x, to_coords.x + 1)
    to_coords_range = range(from_coords.y, to_coords.y + 1)
    coords_of_lights_to_switch = (
        Coords(x=coords[0], y=coords[1]) for coords in product(from_coords_range, to_coords_range)
    )
    for coords in coords_of_lights_to_switch:
        if action == 'toggle':
            grid[coords.x][coords.y] = not grid[coords.x][coords.y]
        else:
            grid[coords.x][coords.y] = ON if action == 'on' else OFF


def _parse_instructions(instruction: str) -> Tuple[str, Coords, Coords]:
    instructions = instruction.split()
    action = instructions[0] if instruction.startswith('toggle') else instructions[1]
    from_coords = _extract_coords(instructions[-3])
    to_coords = _extract_coords(instructions[-1])
    return action.lower(), from_coords, to_coords


def _extract_coords(coord_str: str) -> Coords:
    x, y = coord_str.split(',')
    return Coords(x=int(x), y=int(y))
