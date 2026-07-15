from typing import List


class Listy:
    """
    Helper type for CTCI 10.4. Behaves like an array of unknown size.
    element_at(i) returns the value at index i, or -1 if i is beyond the
    (conceptually unknown/infinite) bounds of the array.
    """

    def __init__(self, values: List[int]):
        self._values = values

    def element_at(self, index: int) -> int:
        if index < 0 or index >= len(self._values):
            return -1
        return self._values[index]


def sorted_search_no_size(listy: Listy, target: int) -> int:
    """
    CTCI 10.4 - Sorted Search, No Size
    listy is a sorted (ascending), Listy of positive integers, of
    unknown size. Find the index of target without knowing listy's
    length in advance (use listy.element_at(i), which returns -1 past
    the end).

    Args:
        listy: a Listy instance wrapping a sorted array of positive ints.
        target: value to find.

    Returns:
        The index of target, or -1 if not found.

    Example:
        listy = Listy([1, 3, 5, 7, 9, 11, 13])
        sorted_search_no_size(listy, 7) -> 3
        sorted_search_no_size(listy, 4) -> -1
    """
    raise NotImplementedError
