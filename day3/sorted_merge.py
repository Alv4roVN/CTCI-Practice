from typing import List


def sorted_merge(a: List[int], a_length: int, b: List[int]) -> None:
    """
    CTCI 10.1 - Sorted Merge
    a and b are sorted (ascending) arrays. a has enough trailing empty
    buffer space to hold all of b's elements; a_length is the number of
    real elements currently in a (excluding that buffer). Merge b into
    a, in place, so a ends up sorted and exactly len(a) long.

    Args:
        a: sorted array with trailing buffer of size len(b), mutated in place.
        a_length: number of real (non-buffer) elements in a.
        b: sorted array to merge into a.

    Example:
        a = [1, 3, 5, 0, 0, 0], a_length = 3, b = [2, 4, 6]
        sorted_merge(a, 3, b) -> a is now [1, 2, 3, 4, 5, 6]
    """
    raise NotImplementedError
