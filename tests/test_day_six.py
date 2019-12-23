from src.day_six import switch_lights_on_grid, total_brightness_of_grid_lights, Grid


def _create_grid(size: int) -> Grid:
    return [[0] * size for _ in range(size)]


def test_can_count_brightness_of_lights_tuned_on_and_off():
    grid = _create_grid(size=1)

    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 0,0'])
    assert total_brightness_of_grid_lights(grid) == 1

    switch_lights_on_grid(grid, instructions=['turn off 0,0 through 0,0'])
    assert total_brightness_of_grid_lights(grid) == 0


def test_light_brightness_cannot_go_below_zero():
    grid = _create_grid(size=1)

    switch_lights_on_grid(grid, instructions=['turn off 0,0 through 0,0'])
    assert total_brightness_of_grid_lights(grid) == 0


def test_can_turn_lights_on_and_off_for_multiple_grid_points():
    grid = _create_grid(size=4)

    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 3,3'])
    assert total_brightness_of_grid_lights(grid) == 16

    switch_lights_on_grid(grid, instructions=['turn off 0,0 through 3,0'])
    assert total_brightness_of_grid_lights(grid) == 12


def test_toggling_lights_increases_their_value_by_two():
    grid = _create_grid(size=4)

    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 0,3'])
    assert total_brightness_of_grid_lights(grid) == 4

    switch_lights_on_grid(grid, instructions=['toggle 0,0 through 3,3'])
    # 4 lights on and 12 lights off == 8 and 24 increase each + original 4
    assert total_brightness_of_grid_lights(grid) == 36


def test_can_pass_multiple_instructions_to_switch_lights_on_grid():
    grid = _create_grid(size=4)

    switch_lights_on_grid(grid, instructions=['turn on 0,0 through 3,0', 'turn on 0,0 through 0,3'])
    assert total_brightness_of_grid_lights(grid) == 8

