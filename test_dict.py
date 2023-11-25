"""
Test module for file_to_dict.py

This module contains test cases for the functions in file_to_dict.py using pytest.

Module to reads the file into dictionary.
"""
from file_to_dict import file_to_dict

def test_file_to_dict():
    """
    To test the file_to_dict function.

    Args:
       file_to_dict(Text): to reads text into dictionary.

    Returns:
       Checks the correctness of the file_to_dict function by testing it with various input files.
    """
    # Test Case 1: Test to read 'dict.txt' file into dictionary.
    result_1 = file_to_dict('dict.txt')
    expected_result_1 = {'name': ' Vismaya', 'Location': ' Coimbatore'}
    assert result_1 == expected_result_1,  "Test Succeed."

    # Test Case 2: Test to read 'dict1.txt' file into dictionary.
    result_2 = file_to_dict('dict1.txt')
    expected_result_2 = {'from': ' Pollachi', 'To': ' Coimbatore'}
    assert result_2 == expected_result_2,  "Test Succeed."
