from functools import reduce
from itertools import combinations
from typing import List


def square_feet_of_wrapping_paper_needed_for_presents(presents: List['str']) -> int:
    square_feet_of_wrapping_paper_needed = 0
    for present in presents:
        dimensions = _dimensions_of_present(present)
        surface_areas = [dimension[0] * dimension[1] for dimension in combinations(dimensions, r=2)]
        surface_area_of_present = sum(surface_area * 2 for surface_area in surface_areas)
        square_feet_of_wrapping_paper_needed += (surface_area_of_present + min(surface_areas))
    return square_feet_of_wrapping_paper_needed


def feet_of_ribbon_needed_for_presents(presents: List['str']) -> int:
    feet_of_ribbon_needed = 0
    for present in presents:
        dimensions = _dimensions_of_present(present)
        cubic_feet_of_present = reduce(lambda x, y: x * y, dimensions)
        shortest_distance_around_present = sum(dimension * 2 for dimension in sorted(dimensions)[:2])
        feet_of_ribbon_needed += (shortest_distance_around_present + cubic_feet_of_present)
    return feet_of_ribbon_needed


def _dimensions_of_present(present: str) -> List[int]:
    return [int(dimension) for dimension in present.split('x')]
