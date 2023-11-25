"""
Remove Digits Module.

This module provides a function to read a text file and remove the digits,
and writes the removed file into another file.

Functions:
- `remove_digits(file1, file2)`: reads the file1 and removing digits then writes into file2.
"""

def remove_digits(file1, file2):
    """
    To remove digits.

    Args:
       File1, File2: python.txt, python1.txt is to be processed.

    Returns:
       Returns python1.txt without digits.
    """
    content = ""
    with open(file1, 'r', encoding="utf-8")as file_1, open(file2, 'w', encoding='utf-8')as file_2:

        for line in file_1:
            # Removing Digits from Each Line
            result = ''.join(ch for ch in line if not ch.isdigit())
            content += result
            file_2.write(result)
    return content
# Function call
remove_digits('python.txt', 'python1.txt')
