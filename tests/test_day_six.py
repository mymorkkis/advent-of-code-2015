from src.day_six import switch_lights_on_grid, lights_turned_on_in_grid, Grid


def _create_grid(size: int) -> Grid:
    return [[False] * size for _ in range(size)]


def test_can_count_lights_tuned_on_for_a_one_by_one_grid():
    grid = _create_grid(size=1)

    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 0,0'])
    assert lights_turned_on_in_grid(grid) == 1

    switch_lights_on_grid(grid, instructions=['turn off 0,0 through 0,0'])
    assert lights_turned_on_in_grid(grid) == 0


def test_can_count_lights_tuned_on_for_a_four_by_four_grid():
    grid = _create_grid(size=4)
    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 3,3'])
    assert lights_turned_on_in_grid(grid) == 16

    switch_lights_on_grid(grid, instructions=['turn off 0,0 through 3,0'])
    assert lights_turned_on_in_grid(grid) == 12


def test_can_toggle_lights_on_a_four_by_four_grid():
    grid = _create_grid(size=4)
    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 0,3'])
    assert lights_turned_on_in_grid(grid) == 4

    switch_lights_on_grid(grid, instructions=['toggle 0,0 through 3,3'])
    assert lights_turned_on_in_grid(grid) == 12


def test_can_pass_multiple_instructions_to_switch_lights_on_grid():
    grid = _create_grid(size=4)
    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 3,0', 'turn on 0,0 through 0,3'])
    assert lights_turned_on_in_grid(grid) == 7
