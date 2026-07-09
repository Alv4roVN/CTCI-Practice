def urlify(s: str, true_length: int) -> str:
    """
    CTCI 1.3 - URLify
    Replace all spaces in a string with '%20'. The string is given with
    enough trailing padding at the end to hold the extra characters, and
    true_length is the length of the string ignoring that padding.

    Args:
        s: padded string, e.g. "Mr John Smith    ".
        true_length: length of s excluding trailing padding, e.g. 13.

    Returns:
        The urlified string trimmed to its final length,
        e.g. "Mr%20John%20Smith".
    """
    raise NotImplementedError
