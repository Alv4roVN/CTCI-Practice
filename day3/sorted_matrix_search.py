from typing import List, Optional, Tuple


def sorted_matrix_search(matrix: List[List[int]], target: int) -> Optional[Tuple[int, int]]:
    """
    CTCI 10.9 - Sorted Matrix Search
    Given an MxN matrix in which every row and every column is sorted in
    ascending order, find target.

    Important: "every row and column sorted" does NOT mean the matrix is
    sorted overall if you flatten it. For example:
        [[ 1,  4,  7, 11],
         [ 2,  5,  8, 12],
         [ 3,  6,  9, 16],
         [10, 13, 14, 17]]
    is a valid input (check any row or column: always ascending), but
    flattened row-major it reads [1,4,7,11, 2,5,8,...] which goes
    11 -> 2, i.e. NOT sorted. A plain binary search over the flattened
    array will silently give wrong answers here.

    Args:
        matrix: MxN matrix, sorted ascending along rows and columns.
        target: value to find.

    Returns:
        (row, col) of target if found, else None.

    Example:
        Using the matrix above, sorted_matrix_search(matrix, 9) -> (2, 2)
    """
    raise NotImplementedError
