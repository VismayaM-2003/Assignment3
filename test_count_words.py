"""
Test module for count_words.py

This module contains test cases for the functions in count_words.py using pytest.

Module to count the number of number in a file.
"""
from count_words import count_words

def test_count_words():
    """
    To test the count_words function.

    Args:
        count_words(text): words to be counted. 

    Returns:
        Checks the correctness of the count_words function by testing it with various input files.
    """
    # Test Case 1: Count the words in 'python.txt' file.
    test_1 = 'python.txt'
    result_1 = count_words(test_1)
    assert result_1 == 13, "Tested Successfully"

    # Test Case 2: Count the words in 'python1.txt' file.
    test_2 = 'python1.txt'
    result_2 = count_words(test_2)
    assert result_2 == 13, "Tested Successfully"

    # Test Case 3: Count the words in 'dict.txt' file.
    test_3 = 'dict.txt'
    result_3 = count_words(test_3)
    assert result_3 == 4, "Tested Successfully"

    # Test Case 1: Count the words in 'dict1.txt' file.
    test_4 = 'dict1.txt'
    result_4 = count_words(test_4)
    assert result_4 == 5, "Tested Failed"
 