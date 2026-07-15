import copy

import pytest

from matrices.rotate_matrix import rotate_matrix
from matrices.zero_matrix import zero_matrix


@pytest.mark.rotate_matrix
class TestRotateMatrix:
    def test_1x1(self):
        assert rotate_matrix([[1]]) == [[1]]

    def test_2x2(self):
        assert rotate_matrix([[1, 2], [3, 4]]) == [[3, 1], [4, 2]]

    def test_3x3(self):
        m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
        assert rotate_matrix(m) == expected

    def test_4x4(self):
        m = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        expected = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4],
        ]
        assert rotate_matrix(m) == expected

    def test_empty_matrix(self):
        assert rotate_matrix([]) == []


@pytest.mark.zero_matrix
class TestZeroMatrix:
    def test_single_zero(self):
        m = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        expected = [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
        assert zero_matrix(m) == expected

    def test_no_zeros_unchanged(self):
        m = [[1, 2], [3, 4]]
        assert zero_matrix(copy.deepcopy(m)) == m

    def test_all_zeros(self):
        assert zero_matrix([[0, 0], [0, 0]]) == [[0, 0], [0, 0]]

    def test_zero_in_corner(self):
        assert zero_matrix([[0, 1], [2, 3]]) == [[0, 0], [0, 3]]

    def test_multiple_zeros_different_rows_cols(self):
        m = [
            [1, 2, 3],
            [4, 5, 0],
            [0, 8, 9],
        ]
        expected = [
            [0, 2, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]
        assert zero_matrix(m) == expected

    def test_empty_matrix(self):
        assert zero_matrix([]) == []
