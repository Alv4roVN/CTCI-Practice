class RankFromStream:
    """
    CTCI 10.10 - Rank from Stream
    Track a stream of numbers and answer, for any x, its rank: the
    count of tracked values that are less than or equal to x
    (duplicates counted individually). Querying before anything has
    been tracked returns 0.
    """

    def __init__(self):
        raise NotImplementedError

    def track(self, x: int) -> None:
        raise NotImplementedError

    def get_rank_of_number(self, x: int) -> int:
        raise NotImplementedError
