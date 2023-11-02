from typing import List
def find_smallest(array : list) -> int:
    """
    Finds the index of the smallest element in a list.

    Args:
        array (list): The list in which to find the smallest element.

    Returns:
        int: The index of the smallest element.

    Examples:
        >>> find_smallest([4, 2, 1, 3])
        2
        >>> find_smallest([9, 5, 7, 1, 3])
        3
    """

    smallest = array[0]
    tiny_index = 0
    for i in range(len(array)):
        if array[i] < smallest:
            smallest = array[i]
            tiny_index = i
    return tiny_index


def selection_sort(arr : List) -> List:
    """
    Sorts a list in ascending order using the selection sort algorithm.

    Args:
        arr (List): The list to be sorted.

    Returns:
        List: The sorted list.

    Examples:
        >>> selection_sort([4, 2, 1, 3])
        [1, 2, 3, 4]
        >>> selection_sort([9, 5, 7, 1, 3])
        [1, 3, 5, 7, 9]
        """

    new_arr = []
    for _ in range(len(arr)):
        small = find_smallest(arr)
        new_arr.append(arr.pop(small))
    return  new_arr


if __name__ == "__main__":
    print(selection_sort([5, 3, 6, 2, 10]))