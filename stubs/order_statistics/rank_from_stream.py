class RankFromStream:
    """
    CTCI 10.10 - Rank from Stream
    Track a stream of numbers and answer, for any x, its rank: the
    count of tracked values that are less than or equal to x
    (duplicates counted individually). Querying before anything has
    been tracked returns 0.

    Example:
        r = RankFromStream()
        for x in [5, 1, 4, 4, 5]: r.track(x)
        # tracked so far, sorted: 1, 4, 4, 5, 5
        r.get_rank_of_number(4) -> 3   (1, 4, 4 are <= 4)
        r.get_rank_of_number(10) -> 5  (all 5 tracked values are <= 10)
    """

    def __init__(self):
        raise NotImplementedError

    def track(self, x: int) -> None:
        raise NotImplementedError

    def get_rank_of_number(self, x: int) -> int:
        raise NotImplementedError
