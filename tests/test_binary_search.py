import pytest

from binary_search.search_rotated import search_rotated
from binary_search.sorted_matrix_search import sorted_matrix_search
from binary_search.sorted_search_no_size import Listy, sorted_search_no_size


@pytest.mark.search_rotated
class TestSearchRotated:
    def test_not_rotated(self):
        assert search_rotated([1, 2, 3, 4, 5], 3) == 2

    def test_rotated_basic(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4

    def test_rotated_target_at_pivot(self):
        assert search_rotated([6, 7, 0, 1, 2, 4, 5], 6) == 0

    def test_not_found(self):
        assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_empty_array(self):
        assert search_rotated([], 5) == -1

    def test_single_element_found(self):
        assert search_rotated([1], 1) == 0

    def test_single_element_not_found(self):
        assert search_rotated([1], 2) == -1

    def test_two_elements(self):
        assert search_rotated([3, 1], 1) == 1


@pytest.mark.sorted_matrix_search
class TestSortedMatrixSearch:
    MATRIX = [
        [1, 4, 7, 11],
        [2, 5, 8, 12],
        [3, 6, 9, 16],
        [10, 13, 14, 17],
    ]

    def test_found_middle(self):
        assert sorted_matrix_search(self.MATRIX, 9) == (2, 2)

    def test_not_found(self):
        assert sorted_matrix_search(self.MATRIX, 100) is None

    def test_top_left_corner(self):
        assert sorted_matrix_search([[1, 2], [3, 4]], 1) == (0, 0)

    def test_bottom_right_corner(self):
        assert sorted_matrix_search([[1, 2], [3, 4]], 4) == (1, 1)

    def test_empty_matrix(self):
        assert sorted_matrix_search([], 5) is None

    def test_single_element_found(self):
        assert sorted_matrix_search([[5]], 5) == (0, 0)

    def test_single_element_not_found(self):
        assert sorted_matrix_search([[5]], 3) is None


@pytest.mark.sorted_search_no_size
class TestSortedSearchNoSize:
    def test_found_basic(self):
        listy = Listy([1, 3, 5, 7, 9, 11, 13])
        assert sorted_search_no_size(listy, 7) == 3

    def test_not_found(self):
        listy = Listy([1, 3, 5, 7, 9, 11, 13])
        assert sorted_search_no_size(listy, 4) == -1

    def test_first_element(self):
        listy = Listy([2, 4, 6, 8])
        assert sorted_search_no_size(listy, 2) == 0

    def test_last_element(self):
        listy = Listy([2, 4, 6, 8])
        assert sorted_search_no_size(listy, 8) == 3

    def test_empty_listy(self):
        assert sorted_search_no_size(Listy([]), 5) == -1

    def test_single_element_found(self):
        assert sorted_search_no_size(Listy([5]), 5) == 0

    def test_large_listy(self):
        values = list(range(1, 20000, 2))  # odd numbers, 1..19999
        listy = Listy(values)
        assert sorted_search_no_size(listy, 9999) == values.index(9999)
