"""
Dictionary Module

Module provides function to read file and returns its contents as a Dictionary.

Functions:
- `file_to_dict(file_path)`: Reads the specified text file returns in dictionary type.
"""

def file_to_dict(file_path):
    """
    To reads a file into dictionary.

    Args:
        File_path : (dict.txt)text format this file to be processed.

    Returns:
        Returns the text file into dictionary format.
    """
    with open(file_path, 'r', encoding="utf-8") as file:
        result = {}

        for line in file:
            # Assuming the format is key:value
            key, value = line.strip().split(':')
            result[key] = value
        return result

# Example usage:
content_dict = file_to_dict('dict.txt')
print(content_dict)
