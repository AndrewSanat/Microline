"""
Task 1.
It takes a list of keys and a list of values. Returns a dictionary of length equal to the length of
the list of keys.
If the list of keys is not passed, then returns None.
If there are no values in the second list, writes None to the dictionary.
"""

from itertools import zip_longest

keys_list = [1, '2abc', [3, 3], 4, 5, 6, 7]
values_list = ['a', 'b', 'c', 'd', 'e']


def get_dict_from_lists(list_of_keys=None, list_of_values=None):
    """
    It takes a list of keys and a list of values. Returns a dictionary of length equal to the length of
    the list of keys.
    If the list of keys is not passed, then returns None.
    If there are no values in the second list, writes None to the dictionary;
    :param list_of_keys: list of hashable objects
    :param list_of_values: list
    :return: dict = {key=list_of_keys[i], value=list_of_values[i]}
    """

    if list_of_keys is None:
        print('Please pass the list of keys')
        return None
    elif list_of_keys and list_of_values is None:
        list_of_values = []

    result_dict = None

    try:
        result_dict = {k: v for k, v in zip_longest(list_of_keys, list_of_values[:len(list_of_keys)])}
    except TypeError as err:
        print(f'Error: {err}. The list of keys must contain hashable objects!')

    return result_dict


if __name__ == '__main__':
    print(get_dict_from_lists(keys_list, values_list))
