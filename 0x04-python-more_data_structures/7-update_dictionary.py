#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Update a dictionary with the provided key-value pair.

    Args:
    - a_dictionary (dict): The dictionary to be updated.
    - key: The key to be added or updated.
    - value: The value corresponding to the key.

    Returns:
    - dict: The updated dictionary.
    """
    a_dictionary.update({key: value})
    return a_dictionary
