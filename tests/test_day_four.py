from src.day_four import lowest_positive_number_that_produces_hash

FINAL_TEST_INPUT = 'bgvyzdsv'


def test_can_find_lowest_positive_number_that_produces_hash_starting_with_five_zeros():
    assert lowest_positive_number_that_produces_hash(secret_key='abcdef', no_of_zeros=5) == 609043
    assert lowest_positive_number_that_produces_hash(secret_key='pqrstuv', no_of_zeros=5) == 1048970
    assert lowest_positive_number_that_produces_hash(secret_key=FINAL_TEST_INPUT, no_of_zeros=5) == 254575


def test_can_find_lowest_positive_number_that_produces_hash_starting_with_six_zeros():
    assert lowest_positive_number_that_produces_hash(secret_key=FINAL_TEST_INPUT, no_of_zeros=6) == 1038736
