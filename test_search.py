"""
Test module for search_condition.py

Module contains test cases for the functions in search_condition.py using pytest.
"""
from search_condtion import search_conditions

def test_search_conditions_1():
    """
    To test the conditions are matched with the given string.

    Examples:
       text_1(str): searches the conditions in the string text_1.

    Raises:
       AssertionError: Incorrect result for text_2.
    """
    # Test Case 1:
    text_1 = """vishali and sheeba are friends. sheeba is very innocent and childish girl.
             vishali is brilliant and have a good character."""
    result1, result2, result3 = search_conditions(text_1)

    assert result1 == ['childish']
    assert result2 == ['sheeba', 'sheeba']
    assert result3 == ['vishali', 'vishali'], "Tested Successfully."

    # Test Case 2:
    text_2 = "Maya is my friend, she is childish and selfish."
    result1, result2, result3 = search_conditions(text_2)

    assert result1 == ['childish', 'selfish']
    assert result2 == ['she']
    assert result3 == [], "Tested Successfully."
    