from day3.sorted_merge import sorted_merge
from day3.search_rotated import search_rotated
from day3.sorted_matrix_search import sorted_matrix_search
from day3.peaks_valleys import peaks_and_valleys


class TestSortedMerge:
    def test_basic_merge(self):
        a = [1, 3, 5, 0, 0, 0]
        sorted_merge(a, 3, [2, 4, 6])
        assert a == [1, 2, 3, 4, 5, 6]

    def test_b_all_smaller(self):
        a = [4, 5, 6, 0, 0, 0]
        sorted_merge(a, 3, [1, 2, 3])
        assert a == [1, 2, 3, 4, 5, 6]

    def test_b_empty(self):
        a = [1, 2, 3]
        sorted_merge(a, 3, [])
        assert a == [1, 2, 3]

    def test_a_empty_initially(self):
        a = [0, 0, 0]
        sorted_merge(a, 0, [1, 2, 3])
        assert a == [1, 2, 3]

    def test_duplicates_across_arrays(self):
        a = [2, 2, 3, 0, 0, 0]
        sorted_merge(a, 3, [2, 2, 4])
        assert a == [2, 2, 2, 2, 3, 4]

    def test_negative_numbers(self):
        a = [-5, -1, 4, 0, 0, 0]
        sorted_merge(a, 3, [-3, 0, 2])
        assert a == [-5, -3, -1, 0, 2, 4]


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


class TestPeaksAndValleys:
    @staticmethod
    def _is_valid(arr):
        for i in range(len(arr)):
            if i % 2 == 0:
                if i > 0 and arr[i] < arr[i - 1]:
                    return False
                if i < len(arr) - 1 and arr[i] < arr[i + 1]:
                    return False
        return True

    def test_basic(self):
        arr = [5, 3, 1, 2, 3]
        result = peaks_and_valleys(arr)
        assert self._is_valid(result)
        assert sorted(result) == sorted([5, 3, 1, 2, 3])

    def test_already_valid_input(self):
        result = peaks_and_valleys([5, 1, 4, 2, 3])
        assert self._is_valid(result)

    def test_empty(self):
        assert peaks_and_valleys([]) == []

    def test_single_element(self):
        assert peaks_and_valleys([1]) == [1]

    def test_two_elements(self):
        result = peaks_and_valleys([1, 2])
        assert self._is_valid(result)
        assert sorted(result) == [1, 2]

    def test_all_same_value(self):
        result = peaks_and_valleys([2, 2, 2, 2])
        assert self._is_valid(result)

    def test_duplicates(self):
        result = peaks_and_valleys([1, 1, 2, 2, 3, 3])
        assert self._is_valid(result)
        assert sorted(result) == sorted([1, 1, 2, 2, 3, 3])
