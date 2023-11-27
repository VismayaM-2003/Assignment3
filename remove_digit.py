"""
Remove Digits Module.

Module provides a function to read a text file and remove the digits,
and writes the removed file into another file.
"""
def remove_digits(file1, file2):
    """
    Remove digits from the content of file1 and write the modified content into file2.

    Args:
        file1 (str): The path to the input file containing digits.
        file2 (str): The path to the output file where the modified content will be written.

    Returns:
        None. The function modifies the content of file2 by removing digits.
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
