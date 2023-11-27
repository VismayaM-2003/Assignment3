"""
Dictionary Module

Module provides function to read file and returns its contents as a Dictionary.
"""

def file_to_dict(file_path):
    """
    Read a file into a dictionary.

    Args:
        file_path (str): The path to the text file to be processed.

    Returns:
        dict: A dictionary representing the contents of the file. 
            Assumes the file format is key:value.
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
