import pytest

from sorting.sorted_merge import sorted_merge
from sorting.peaks_valleys import peaks_and_valleys


@pytest.mark.sorted_merge
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


@pytest.mark.peaks_valleys
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
