import pytest

from day4.sorted_search_no_size import Listy, sorted_search_no_size
from day4.rank_from_stream import RankFromStream


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


@pytest.mark.rank_from_stream
class TestRankFromStream:
    """get_rank_of_number(x) = count of tracked values <= x, duplicates
    counted individually. Rank before any tracking is 0."""

    def test_basic_rank(self):
        r = RankFromStream()
        for x in [5, 1, 4, 4, 5, 9, 7, 13, 3]:
            r.track(x)
        # sorted tracked multiset: 1, 3, 4, 4, 5, 5, 7, 9, 13
        assert r.get_rank_of_number(1) == 1
        assert r.get_rank_of_number(3) == 2
        assert r.get_rank_of_number(4) == 4
        assert r.get_rank_of_number(5) == 6
        assert r.get_rank_of_number(10) == 8
        assert r.get_rank_of_number(13) == 9

    def test_rank_before_any_tracking(self):
        r = RankFromStream()
        assert r.get_rank_of_number(5) == 0

    def test_rank_below_all_tracked_values(self):
        r = RankFromStream()
        r.track(10)
        r.track(20)
        assert r.get_rank_of_number(5) == 0

    def test_rank_of_untracked_large_number(self):
        r = RankFromStream()
        r.track(1)
        r.track(2)
        assert r.get_rank_of_number(100) == 2

    def test_duplicates(self):
        r = RankFromStream()
        r.track(5)
        r.track(5)
        r.track(5)
        assert r.get_rank_of_number(5) == 3
