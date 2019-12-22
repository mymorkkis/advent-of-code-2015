from src.day_five import string_is_nice, nice_string_count


def test_can_detect_that_string_is_nice():
    assert string_is_nice('qjhvhtzxzqqjkmpb')
    assert string_is_nice('xxyxx')
    assert string_is_nice('xxyxxxpxx')


def test_can_detect_that_a_string_is_not_nice():
    assert not string_is_nice('aaa')  # Contains overlapping pair
    assert not string_is_nice('uurcxstgmygtbstg')  # Contains no repeat with single letter between
    assert not string_is_nice('ieodomkazucvgmuy')  # Contains no double pair


def test_can_count_how_many_strings_are_nice_in_a_given_list_of_strings():
    assert nice_string_count(['xxyxx', 'ieodomkazucvgmuy']) == 1
