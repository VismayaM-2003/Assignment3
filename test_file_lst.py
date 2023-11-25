"""
Test module for file_to_lst.py

This module contains test cases for the functions in file_to_lst.py using pytest.

Module to reads a file into list.
"""
from file_to_lst import txt_to_lst

def test_txt_to_lst():
    """
    Test the txt_to_lst function.

    Args:
       txt_to_lst(Text): to read a text file into dictionary.

    Returns: 
       Checks the correctness of the txt_to_lst function by testing it with various input files.
    """
    # Test Case 1: Test to read 'python.txt' file into list.
    test_1 = txt_to_lst('python.txt')
    result_1 = ['python was created by Guido van Rossum, and released in 1991.\n',
    'Thank you.-2023']
    assert test_1 == result_1

    # Test Case 2: Test to read 'dict.txt' file into list.
    test_2 = txt_to_lst('dict.txt')
    result_2 = ['name: Vismaya\n','Location: Coimbatore']
    assert test_2 == result_2
