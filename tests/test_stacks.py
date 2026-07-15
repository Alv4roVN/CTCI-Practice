import pytest

from stacks.stack_min import MinStack
from stacks.sort_stack import sort_stack


@pytest.mark.stack_min
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


@pytest.mark.sort_stack
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
