from itertools import groupby
from typing import List, NamedTuple, Set


class Pair(NamedTuple):
    string: str
    indexes: Set[int]


def nice_string_count(strings: List[str]) -> int:
    return sum(string_is_nice(string) for string in strings)


def string_is_nice(string: str) -> bool:
    return _has_non_overlapping_same_pair_combination(string) and _has_repeated_char_with_one_between(string)


def _has_non_overlapping_same_pair_combination(string: str) -> bool:
    for duplicated_pairs in _duplicated_pairs_in_string(string):
        unique_duplicates = 0
        indexes: Set[int] = set()
        for pair in duplicated_pairs:
            previous_indexes_len = len(indexes)
            indexes.update(pair.indexes)
            if len(indexes) == previous_indexes_len + 2:
                unique_duplicates += 1
        if unique_duplicates >= 2:
            return True
    return False


def _duplicated_pairs_in_string(string: str) -> List[List[Pair]]:
    pairs = [
        Pair(string=string[idx:idx+2], indexes={idx, idx + 1})
        for idx in range(len(string) - 1)
    ]
    sorted_pairs = sorted(pairs, key=lambda pair: pair.string)
    grouped_pairs = [list(g) for _, g in groupby(sorted_pairs, key=lambda pair: pair.string)]
    duplicated_pairs = [group for group in grouped_pairs if len(group) > 1]
    return duplicated_pairs


def _has_repeated_char_with_one_between(string: str) -> bool:
    string_triplets = [string[idx:idx+3] for idx in range(len(string) - 2)]
    return any(s[0] == s[2] != s[1] for s in string_triplets)

