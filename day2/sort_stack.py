from typing import List


def sort_stack(stack: List[int]) -> List[int]:
    """
    CTCI 3.5 - Sort Stack
    Sort a stack such that the smallest items end up on top, using only
    one additional stack as extra storage (no other data structures).

    Convention: a stack is represented as a list where index -1 (the
    end of the list) is the top. After sorting, the top of the stack
    (last element) must be the smallest value, so read bottom-to-top
    the list is in descending order.
    Example: sort_stack([1, 2, 3]) -> [3, 2, 1]  (top is 1, the smallest)

    Args:
        stack: a list used as a stack (top of stack = end of list).

    Returns:
        The sorted stack (same convention: top of stack = end of list).
    """
    raise NotImplementedError
