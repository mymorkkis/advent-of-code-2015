from src.day_one import floor_from_instructions, santa_enters_basement_at_position


def test_can_find_correct_floor():
    assert floor_from_instructions('(())') == 0
    assert floor_from_instructions('()()') == 0
    assert floor_from_instructions('))(((((') == 3
    assert floor_from_instructions(')())())') == -3


def test_can_find_position_of_first_time_santa_enters_basement():
    assert santa_enters_basement_at_position(')') == 1
    assert santa_enters_basement_at_position('()())') == 5


def test_none_is_returned_if_santa_never_enters_the_basement():
    assert santa_enters_basement_at_position('((') is None


def test_non_parenthesis_characters_are_ignored():
    assert floor_from_instructions(')(boom!))())') == -3
    assert santa_enters_basement_at_position('(*bam*)())') == 5
