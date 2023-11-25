"""
Test module for search.py

This module contains test cases for the functions in search.py using pytest.

Module to search conditions in the string.
"""
from search import check_condition

def test_check_condition():
    """
    To test the check_condition function.

    Args:
        check_condition(string): string format.

    Returns:
        Checks the correctness of the check_condition function.
    """
    find_str = ["vi%shnu", "she", "is", "very", "vi%liant", "also", "childish%", "and", "selfish%"]

    matches_1, matches_2, matches_3 = check_condition(find_str)

    assert matches_1 == ["vi%shnu"]
    assert matches_2 == ["childish%", "selfish%"]
    assert matches_3 == ["vi%liant"]
