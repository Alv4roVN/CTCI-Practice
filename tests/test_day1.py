from day1.is_unique import is_unique
from day1.check_permutation import check_permutation
from day1.urlify import urlify
from day1.string_compression import string_compression


class TestIsUnique:
    def test_empty_string(self):
        assert is_unique("") is True

    def test_single_char(self):
        assert is_unique("a") is True

    def test_all_unique(self):
        assert is_unique("abcdefg") is True

    def test_duplicate(self):
        assert is_unique("hello") is False

    def test_case_sensitivity(self):
        assert is_unique("Aa") is True

    def test_repeated_case_same_letter(self):
        assert is_unique("AaAa") is False

    def test_whitespace_counts_as_char(self):
        assert is_unique("a b") is True
        assert is_unique("a  b") is False

    def test_all_same_char(self):
        assert is_unique("aaaa") is False

    def test_long_unique_ascii_range(self):
        assert is_unique("".join(chr(i) for i in range(32, 127))) is True


class TestCheckPermutation:
    def test_empty_both(self):
        assert check_permutation("", "") is True

    def test_simple_permutation(self):
        assert check_permutation("abc", "bca") is True

    def test_different_lengths_not_permutation(self):
        assert check_permutation("abc", "ab") is False

    def test_same_length_not_permutation(self):
        assert check_permutation("abc", "abd") is False

    def test_repeated_chars(self):
        assert check_permutation("aabbcc", "abcabc") is True
        assert check_permutation("aabbcc", "abcabb") is False

    def test_case_sensitive(self):
        assert check_permutation("abc", "ABC") is False

    def test_spaces_are_significant(self):
        assert check_permutation("god ", "dog") is False
        assert check_permutation("god", "dog") is True


class TestUrlify:
    def test_basic(self):
        assert urlify("Mr John Smith    ", 13) == "Mr%20John%20Smith"

    def test_no_spaces(self):
        assert urlify("abc", 3) == "abc"

    def test_all_spaces(self):
        assert urlify("   ", 3) == "%20%20%20"

    def test_single_trailing_space(self):
        assert urlify("a b ", 3) == "a%20b"

    def test_single_char(self):
        assert urlify("a", 1) == "a"


class TestStringCompression:
    def test_basic_compression(self):
        assert string_compression("aabcccccaaa") == "a2b1c5a3"

    def test_no_benefit_returns_original(self):
        assert string_compression("abcdef") == "abcdef"

    def test_empty_string(self):
        assert string_compression("") == ""

    def test_single_char_returns_original(self):
        # "a1" (len 2) is not smaller than "a" (len 1)
        assert string_compression("a") == "a"

    def test_all_same_char(self):
        assert string_compression("aaaa") == "a4"

    def test_equal_length_returns_original(self):
        # "a2b2" (len 4) is not smaller than "aabb" (len 4)
        assert string_compression("aabb") == "aabb"
