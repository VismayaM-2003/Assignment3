"""
Replace string Module.

Module provides a function to read 'Visha' in a string and replace with null.
"""
def replace_name(text):
    """
    Replace occurrences of 'Visha' with an empty string.

    Args:
        text (str): The input string where occurrences of 'Visha' will be replaced.

    Returns:
        str: A new string with occurrences of 'Visha' replaced by an empty string.
    """
    # Replace "Visha" with null
    name = text.replace("Visha", "")
    return name

about = "Vismaya and Vishali are Friends."
result = replace_name(about)
print(result)
