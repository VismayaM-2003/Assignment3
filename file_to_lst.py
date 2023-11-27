"""
List Module

Module provides function to reads a file and return its contents as a list.
"""
def txt_to_lst(path):
    """
    Read a file into a list.

    Args:
       path (str): The path to the text file to be processed.

    Returns:
       list: A list representing the contents of the file. Each element in the
             list corresponds to a line from the text file.
    """
    with open(path, encoding='utf-8') as file:

        # Reads the contents of the file line by line and stores them in a list
        text = file.readlines()
    return text

result = txt_to_lst('python.txt')
print(result)
