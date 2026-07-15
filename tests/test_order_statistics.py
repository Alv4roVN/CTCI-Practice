import pytest

from order_statistics.rank_from_stream import RankFromStream


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
