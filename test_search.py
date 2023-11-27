"""
Test module for search.py

Module contains test cases for the functions in search.py using pytest.
"""
from search import check_condition

def test_check_condition():
    """
    To test the conditions are matched with the given string.

    Examples:
    - Check conditions in the list 
    ["vi%shnu", "she", "is", "very", "vi%liant", "also", "childish%", "and", "selfish%"].
    """

    find_str = ["vi%shnu", "she", "is", "very", "vi%liant", "also", "childish%", "and", "selfish%"]

    matches_1, matches_2, matches_3 = check_condition(find_str)

    assert matches_1 == ["vi%shnu"]
    assert matches_2 == ["childish%", "selfish%"]
    assert matches_3 == ["vi%liant"], "Tested Successfully!"
