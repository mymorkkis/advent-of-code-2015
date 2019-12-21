from src.day_three import houses_that_received_presents_count


def test_can_count_how_many_houses_received_at_least_one_present():
    assert houses_that_received_presents_count('') == 0
    assert houses_that_received_presents_count('>') == 2
    assert houses_that_received_presents_count('^>v<') == 3
    assert houses_that_received_presents_count('^v^v^v^v^v') == 11


def test_non_instruction_characters_are_ignored():
    assert houses_that_received_presents_count('*!>') == 2
    assert houses_that_received_presents_count('^>va*c<') == 3
