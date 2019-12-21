from typing import Optional


def floor_from_instructions(instructions: str) -> int:
    return sum(_floor_change(instruction) for instruction in instructions)


def santa_enters_basement_at_position(instructions: str) -> Optional[int]:
    floor_number, position = 0, 0
    for instruction in instructions:
        floor_change = _floor_change(instruction)
        if floor_change:
            position += 1
            floor_number += floor_change
        if floor_number == -1:
            return position
    return None


def _floor_change(change_instruction: str) -> int:
    if change_instruction == '(':
        return 1
    if change_instruction == ')':
        return -1
    return 0
