"""
Test module for file_to_dict.py

Module contains test cases for the functions in file_to_dict.py using pytest.
"""
from file_to_dict import file_to_dict

def test_file_to_dict():
    """
    Test if the text file is reads into dictionary.

    Examples:
    - Read a file into a dictionary ('dict.txt').
    - Read a file into a dictionary ('dict1.txt').
    """
    # Test Case 1: Test to read 'dict.txt' file into dictionary.
    result_1 = file_to_dict('dict.txt')
    expected_result_1 = {'name': ' Vismaya', 'Location': ' Coimbatore'}
    assert result_1 == expected_result_1,  "Tested Successfully!"

    # Test Case 2: Test to read 'dict1.txt' file into dictionary.
    result_2 = file_to_dict('dict1.txt')
    expected_result_2 = {'from': ' Pollachi', 'To': ' Coimbatore'}
    assert result_2 == expected_result_2,  "Tested Successfully!"
