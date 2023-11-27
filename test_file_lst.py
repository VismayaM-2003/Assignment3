"""
Test module for file_to_lst.py

This module contains test cases for the functions in file_to_lst.py using pytest.
"""
from file_to_lst import txt_to_lst

def test_txt_to_lst():
    """
    Testing the text file is reads into List by testing it with various input files.

    Examples:
    - Read 'python.txt' file into a list.
    - Read 'dict.txt' file into a list.
    """
    # Test Case 1: Test to read 'python.txt' file into list.
    test_1 = txt_to_lst('python.txt')
    result_1 = ['python was created by Guido van Rossum, and released in 1991.\n',
    'Thank you.-2023']
    assert test_1 == result_1, "Tested Successfully!"

    # Test Case 2: Test to read 'dict.txt' file into list.
    test_2 = txt_to_lst('dict.txt')
    result_2 = ['name: Vismaya\n','Location: Coimbatore']
    assert test_2 == result_2, "Tested Successfully!"
