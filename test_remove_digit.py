"""
Test module for remove_digit.py

This module contains test cases for the functions in remove_digit.py using pytest.

Module to remove digits from a text.
"""
from remove_digit import remove_digits

def test_remove_digits():
    """ 
    To test the remove_digits function.

    Args:
        remove_digits(file1, file2): Text format. 
    
    Returns:
       Checks the correctness of the remove_digits function by testing it with various input files.
    """
    # Test Case: 1
    test_1 = remove_digits('python.txt', 'python1.txt')
    assert '1991' not in test_1, "Test Failed."

    # Test Case: 2
    test_2 = remove_digits('python.txt', 'python1.txt')
    assert 'python' in test_2, "Test Succeed"
