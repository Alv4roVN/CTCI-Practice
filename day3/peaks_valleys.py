from typing import List


def peaks_and_valleys(arr: List[int]) -> List[int]:
    """
    CTCI 10.11 - Peaks and Valleys
    Rearrange arr into an alternating sequence of peaks and valleys:
    arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] ...
    There can be multiple valid arrangements; any one is acceptable as
    long as the alternating property holds and the multiset of values
    is unchanged.

    Args:
        arr: list of integers, mutated in place.

    Returns:
        The same list object, rearranged (returned for test convenience).

    Example:
        peaks_and_valleys([5, 3, 1, 2, 3]) -> [3, 1, 3, 2, 5]  (one valid answer)
        # check: 3 >= 1 <= 3 >= 2 <= 5 -- alternates, same multiset as input
    """
    raise NotImplementedError
