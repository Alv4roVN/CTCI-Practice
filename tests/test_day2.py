import copy

from day2.rotate_matrix import rotate_matrix
from day2.zero_matrix import zero_matrix
from day2.stack_min import MinStack
from day2.sort_stack import sort_stack


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


class TestMinStack:
    def test_basic_min(self):
        s = MinStack()
        s.push(5)
        s.push(3)
        s.push(7)
        assert s.min() == 3

    def test_min_after_pop(self):
        s = MinStack()
        s.push(5)
        s.push(3)
        s.push(7)
        s.pop()
        assert s.min() == 3
        s.pop()
        assert s.min() == 5

    def test_duplicates_min(self):
        s = MinStack()
        s.push(2)
        s.push(2)
        s.push(1)
        s.push(2)
        assert s.min() == 1
        s.pop()
        assert s.min() == 1
        s.pop()
        assert s.min() == 2

    def test_top(self):
        s = MinStack()
        s.push(1)
        s.push(9)
        assert s.top() == 9

    def test_is_empty(self):
        s = MinStack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False

    def test_negative_numbers(self):
        s = MinStack()
        s.push(-1)
        s.push(-5)
        s.push(-3)
        assert s.min() == -5


class TestSortStack:
    """Convention: index -1 of the list is the top of the stack. After
    sorting, the top must hold the smallest value, so read bottom-to-top
    the result is in descending order."""

    def test_already_correctly_ordered(self):
        assert sort_stack([3, 2, 1]) == [3, 2, 1]

    def test_ascending_input_gets_reversed(self):
        assert sort_stack([1, 2, 3]) == [3, 2, 1]

    def test_random_order(self):
        assert sort_stack([5, 1, 4, 2, 3]) == [5, 4, 3, 2, 1]

    def test_empty_stack(self):
        assert sort_stack([]) == []

    def test_single_element(self):
        assert sort_stack([42]) == [42]

    def test_duplicates(self):
        assert sort_stack([3, 1, 3, 2, 1]) == [3, 3, 2, 1, 1]

    def test_negative_numbers(self):
        assert sort_stack([-1, -5, 3, 0]) == [3, 0, -1, -5]
