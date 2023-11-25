"""
Word Count Module.

This module provides a function to read a text file and return the count of words.

Functions:
- `count_words(path)`: Reads the specified text file and returns the count of words.
"""

def count_words(path):
    """
    To counts the number of words

    Args:
        Path : (python.txt) text format is to be processed.

    Returns:
        Counts of words from the python.txt file
    """
    with open(path, encoding="utf-8")as file:
        text = file.read()

    # Splitting Text into Words
    numbers = text.split()
    # Counting Words
    return len(numbers)

word = count_words("python.txt")
print(f"Count of words: {word}")
