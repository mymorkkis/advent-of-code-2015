from src.day_two import square_feet_of_wrapping_paper_needed_for_presents, feet_of_ribbon_needed_for_presents


PRESENT_1_SIZE = '2x3x4'
PRESENT_2_SIZE = '1x1x10'


def test_can_calculate_wrapping_paper_needed_for_presents():
    assert square_feet_of_wrapping_paper_needed_for_presents([]) == 0
    assert square_feet_of_wrapping_paper_needed_for_presents([PRESENT_1_SIZE]) == 58
    assert square_feet_of_wrapping_paper_needed_for_presents([PRESENT_2_SIZE]) == 43
    assert square_feet_of_wrapping_paper_needed_for_presents([PRESENT_1_SIZE, PRESENT_2_SIZE]) == 58 + 43


def test_can_calculate_feet_of_ribbon_needed_for_presents():
    assert feet_of_ribbon_needed_for_presents([]) == 0
    assert feet_of_ribbon_needed_for_presents([PRESENT_1_SIZE]) == 34
    assert feet_of_ribbon_needed_for_presents([PRESENT_2_SIZE]) == 14
    assert feet_of_ribbon_needed_for_presents([PRESENT_1_SIZE, PRESENT_2_SIZE]) == 34 + 14
