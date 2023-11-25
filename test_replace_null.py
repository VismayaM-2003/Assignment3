"""
Test module for replace_null.py

This module contains test cases for the functions in replace_null.py using pytest.

Module to search for "Visha" in a string and replace with other name, null.
"""
from replace_null import replace_name

def test_replace_name():
    """
    To test the replace_name function.

    Args:
       replace_name(string): string format.

    Returns:
       Checks the correctness of the replace_name function by testing it with various input files.
    """
    # Test case 1: Replace "Visha" with null
    text_1 = "Vismaya and li are friends"
    result_1 = replace_name(text_1)
    assert result_1 == 'Vismaya and li are friends', "Test Successfully"

     # Test case 2: Replace "Visha" in an empty string
    text_2 = ""
    result_2 = replace_name(text_2)
    assert result_2 == "", "Test Successfully"

    # Test case 3: Replace "Visha" in a string without "Visha"
    text_3 = "Hello, how are you?"
    result_3 = replace_name(text_3)
    assert result_3 == text_3, "Test Successfully"

    # Test case 4: Replace "Visha" with an empty string
    text_4 = "Vismaya and Vishali are Friends."
    result_4 = replace_name(text_4)
    assert result_4 == " and Vishali are Friends.", "Test Failed"
