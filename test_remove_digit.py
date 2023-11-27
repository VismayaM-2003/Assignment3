"""
Test module for remove_digit.py

Module contains test cases for the functions in remove_digit.py using pytest.
"""
from remove_digit import remove_digits

def test_remove_digits():
    """
    To test if the digits are removed from the file1 then writes into file2
    by testing it with various input files.

    Examples:
    - Remove digits from 'python.txt' and write to 'python1.txt'.
    """
    # Test Case: 1
    test_1 = remove_digits('python.txt', 'python1.txt')
    assert '1991' not in test_1, "Tested Successfully!"

    # Test Case: 2
    test_2 = remove_digits('python.txt', 'python1.txt')
    assert 'python' in test_2, "Tested Successfully!"
