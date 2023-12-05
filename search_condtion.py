"""
Search condition Module.

Module provides a function to search conditions in a string. 
"""
import re

def search_conditions(input_string):
    """
    Search for specific patterns in a given string.

    Parameters:
    - input_string (str): The input string to search.

    Returns:
    - Tuple: A tuple containing three lists of matches for different patterns.
    """
    condition1 = re.compile(r'\b\w*sh\b')  # Ends with "sh"
    condition2 = re.compile(r'\bsh\w*\b')  # Starts with "sh"
    condition3 = re.compile(r'\bvi\w*li\b')  # Starts with "vi" and ends with "li"

    match1 = re.findall(condition1, input_string)
    match2 = re.findall(condition2, input_string)
    match3 = re.findall(condition3, input_string)

    return match1, match2, match3


text = """In the peaceful village of Shirelish, nestled between lush green hills
and shimmering lakesh, the villagers lived simple lives.They would often gather in the evening to share stories and laughter. 
One day, a vibrant visitor named vishali arrived, bringing with her a sense of vitality and curiosity. 
vishali quickly became a cherished member viloli of the community,viloli and her presence added a dash of excitement to the otherwise tranquil Shirelish.
The villagers admired vishali's resilience and kindness,viloli and they looked forward to the delightful moments 
she would inevitably bring to their lives."""

result1, result2, result3 = search_conditions(text)

print("Strings Ends with 'sh' \n ", result1)
print("Strings Starts with 'sh' \n ", result2)
print("Strings Starts with 'vi' and ends with 'li' \n ", result3)
