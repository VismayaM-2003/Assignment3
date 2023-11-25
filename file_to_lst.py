"""
Dictionary Module

Module provides function to reads a file and return its contents as a list.

Functions:
- `txt_to_lst(path)`: Reads the specified text file and returns it into list type.

"""
def txt_to_lst(path):
    """
    To read a file into List
    
    Args:
       Path: python.txt as text file.

    Returns:
       File python.txt into list type.
    """
    with open(path, encoding='utf-8') as file:

        # Reads the contents of the file line by line and stores them in a list
        text = file.readlines()
    return text

result = txt_to_lst('python.txt')
print(result)
