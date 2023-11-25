"""
Replace string Module.

This module provides a function to read 'Visha' in a string and replace with null.

Functions:
- `replace_name(text)`: Reads the string, search Visha in a string and replace with null.
"""

def replace_name(text):
    """
    To replace 'Visha' with 'null'

    Args:
       Arugument 'text': 'about' is to be processed. 
    
    Returns:
        Replaced string Visha with null.
    """
    # Replace "Visha" with null
    name = text.replace("Visha", "")
    return name

ABOUT = "Vismaya and Vishali are Friends."
RESULT = replace_name(ABOUT)
print(RESULT)
