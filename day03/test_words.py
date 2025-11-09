"""
Pytest test suite for the compare function in the words module.
This module tests the Levenshtein distance calculation with comprehensive test cases.

To run the tests:
    pytest test_words.py
    pytest test_words.py -v  (for verbose output)
    pytest test_words.py::test_identical_words_same_case  (run specific test)
"""

import pytest
from words import compare


def test_identical_words_same_case():
    """Test identical words with same case."""
    assert compare("hello", "hello") == 0


def test_identical_words_different_case():
    """Test identical words with different cases."""
    assert compare("Hello", "HELLO") == 0


def test_single_character_substitution():
    """Test single character substitution."""
    assert compare("cat", "bat") == 1


def test_single_character_insertion_at_end():
    """Test single character insertion at end."""
    assert compare("test", "tests") == 1


def test_single_character_deletion():
    """Test single character deletion (double letter)."""
    assert compare("apple", "aple") == 1


def test_empty_string_vs_non_empty():
    """Test empty string vs 3-character word."""
    assert compare("", "abc") == 3


def test_non_empty_vs_empty_string():
    """Test 3-character word vs empty string."""
    assert compare("xyz", "") == 3


def test_both_empty_strings():
    """Test both empty strings."""
    assert compare("", "") == 0


def test_multiple_edits_classic_example():
    """Test multiple edits needed (classic kitten/sitting example)."""
    assert compare("kitten", "sitting") == 3


def test_completely_different_words():
    """Test completely different programming language names."""
    assert compare("python", "java") == 6


def test_substring_relationship():
    """Test when one word is substring of another."""
    assert compare("run", "running") == 4


def test_adjacent_character_transposition():
    """Test adjacent character transposition."""
    assert compare("form", "from") == 2


def test_single_character_words():
    """Test single character substitution."""
    assert compare("a", "b") == 1


def test_same_length_single_substitution():
    """Test same length words with single substitution."""
    assert compare("house", "mouse") == 1


def test_mixed_case_with_multiple_edits():
    """Test mixed case with multiple edits needed."""
    assert compare("GitHub", "gitlab") == 2


# Additional edge case tests
def test_single_char_to_empty():
    """Test single character to empty string."""
    assert compare("a", "") == 1


def test_empty_to_single_char():
    """Test empty string to single character."""
    assert compare("", "a") == 1


def test_simple_swap():
    """Test simple character swap."""
    assert compare("ab", "ba") == 2


def test_swap_last_two_chars():
    """Test swapping last two characters."""
    assert compare("abc", "acb") == 2


def test_anagram_with_many_edits():
    """Test anagram requiring many edits."""
    assert compare("listening", "silent") == 8


@pytest.mark.parametrize("word1,word2,expected", [
    ("cat", "cat", 0),          # Identical
    ("dog", "god", 2),          # Reverse
    ("abc", "def", 3),          # All different
    ("test", "best", 1),        # First char different
    ("hello", "jello", 1),      # First char substitution
])
def test_parametrized_cases(word1, word2, expected):
    """Test additional cases using parametrize."""
    assert compare(word1, word2) == expected


def test_symmetric_property():
    """Test that distance is symmetric: compare(a,b) == compare(b,a)."""
    test_pairs = [
        ("hello", "world"),
        ("python", "java"),
        ("test", "testing"),
        ("", "abc"),
        ("cat", "dog")
    ]
    
    for word1, word2 in test_pairs:
        assert compare(word1, word2) == compare(word2, word1)


def test_triangle_inequality():
    """Test triangle inequality: d(a,c) <= d(a,b) + d(b,c)."""
    # This is a mathematical property of edit distance
    test_triplets = [
        ("cat", "bat", "hat"),
        ("hello", "jello", "yellow"),
        ("test", "best", "rest")
    ]
    
    for a, b, c in test_triplets:
        d_ac = compare(a, c)
        d_ab = compare(a, b)
        d_bc = compare(b, c)
        assert d_ac <= d_ab + d_bc


def test_non_negative_distance():
    """Test that distance is always non-negative."""
    test_cases = [
        ("hello", "world"),
        ("", ""),
        ("a", "b"),
        ("long", "short"),
        ("python", "java")
    ]
    
    for word1, word2 in test_cases:
        assert compare(word1, word2) >= 0


def test_zero_distance_only_for_identical():
    """Test that zero distance only occurs for identical words (case-insensitive)."""
    # These should have distance 0
    zero_distance_pairs = [
        ("hello", "hello"),
        ("Hello", "HELLO"),
        ("", ""),
        ("Python", "python")
    ]
    
    for word1, word2 in zero_distance_pairs:
        assert compare(word1, word2) == 0
    
    # These should have distance > 0
    non_zero_pairs = [
        ("hello", "world"),
        ("cat", "dog"),
        ("a", "b"),
        ("test", "testing")
    ]
    
    for word1, word2 in non_zero_pairs:
        assert compare(word1, word2) > 0


@pytest.fixture
def sample_word_pairs():
    """Fixture providing sample word pairs for testing."""
    return [
        ("hello", "hello", 0),
        ("cat", "dog", 3),
        ("python", "java", 6),
        ("test", "testing", 3),
        ("house", "mouse", 1)
    ]


def test_with_fixture(sample_word_pairs):
    """Test using a fixture."""
    for word1, word2, expected in sample_word_pairs:
        assert compare(word1, word2) == expected


if __name__ == "__main__":
    # Run pytest programmatically if this file is executed directly
    pytest.main([__file__, "-v"])