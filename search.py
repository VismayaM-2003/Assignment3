"""
Search condition Module.

Module provides a function to search conditions in a string. 
"""
import re

def check_condition(input_string):
    """
    Check for conditions in a list of strings and display the matches.

    Parameters:
       input_strings (list): List of strings to search for conditions.

    Returns:
       Tuple of matches for conditions %sh, sh%, and vi%li.
    """
    condition_1 = re.compile(r"%sh")
    condition_2 = re.compile(r"sh%")
    condition_3 = re.compile(r"vi%li")

    # Using list comprehension to check the strings.
    test_1 = [str for str in input_string if re.search(condition_1, str)]
    test_2 = [str for str in input_string if re.search(condition_2, str)]
    test_3 = [str for str in input_string if re.search(condition_3, str)]

    return test_1, test_2, test_3

if __name__ == "__main__":
    find_str = ["vi%shnu", "she", "is", "very", "vi%liant", "also", "childish%", "and", "selfish%"]

    matches_1, matches_2, matches_3 = check_condition(find_str)

    print("Search string matches with %sh: ", matches_1)
    print("Search string matches with sh%: ", matches_2)
    print("Search string matches with vi%li: ", matches_3)
