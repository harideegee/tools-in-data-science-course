import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test with an empty list, expecting 0."""
    assert longest_positive_streak([]) == 0

def test_multiple_streaks():
    """Test with multiple streaks to find the longest one."""
    assert longest_positive_streak([1, 2, -1, 3, 4, 5, 0, 1]) == 3

def test_with_zeros_and_negatives():
    """Test with a list containing only non-positive numbers."""
    assert longest_positive_streak([-1, -2, 0, -5]) == 0

def test_all_positive():
    """Test with a list of all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_streak_at_end():
    """Test where the longest streak is at the end of the list."""
    assert longest_positive_streak([1, -2, 3, 4]) == 2

def test_single_positive():
    """Test with a single positive number."""
    assert longest_positive_streak([5]) == 1

def test_single_negative():
    """Test with a single negative number."""
    assert longest_positive_streak([-5]) == 0

def test_from_prompt_1():
    """Test case from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_from_prompt_2():
    """Test case from the problem description."""
    assert longest_positive_streak([1, 1, 1]) == 3