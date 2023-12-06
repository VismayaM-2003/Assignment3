"""
Word Count Module.

Module provides a function to read a text file and return the count of words.
"""

def count_words(path):
    """
    Count the number of words in a text file.

    Args:
        path (str): The path to the text file to be processed.

    Returns:
        int: The count of words in the specified text file.
    """
    with open(path, encoding="utf-8")as file:
        text = file.read()

    # Splitting Text into Words
    numbers = text.split()
    # Counting Words
    return len(numbers)

word = count_words("python.txt")
print(f"Count of words is: {word}")
