"""
Test module for count_words.py

Module contains test cases for the functions in count_words.py using pytest.
"""
from count_words import count_words

def test_count_words():
    """
    Test the count of words in various files.

    Examples:
    - Count the words in 'python.txt' file.
    - Count the words in 'python1.txt' file.
    - Count the words in 'dict.txt' file.
    - Count the words in 'dict1.txt' file.

    Raises:
    - For Test Case 4
         AssertionError: Tested Failed
    """
    # Test Case 1: Count the words in 'python.txt' file.
    test_1 = 'python.txt'
    result_1 = count_words(test_1)
    assert result_1 == 13, "Tested Successfully!"

    # Test Case 2: Count the words in 'python1.txt' file.
    test_2 = 'python1.txt'
    result_2 = count_words(test_2)
    assert result_2 == 13, "Tested Successfully!"
 
    # Test Case 3: Count the words in 'dict.txt' file.
    test_3 = 'dict.txt'
    result_3 = count_words(test_3)
    assert result_3 == 4, "Tested Successfully!"

    # Test Case 4: Count the words in 'dict1.txt' file.
    test_4 = 'dict1.txt'
    result_4 = count_words(test_4)
    assert result_4 == 5, "Incorrect result for dict1.txt file"
 