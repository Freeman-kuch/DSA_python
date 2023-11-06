# This is a major D&C( divide and conquer) algorithm
from typing import List
import random
def sum(arr):
    """
Calculates the sum of all elements in the given array recursively.

Args:
    arr (List[int]): The array of integers.

Returns:
    int: The sum of all elements in the array.

Examples:
    >>> sum([1, 2, 3, 4, 5])
    15
    >>> sum([])
    0
"""

    if len(arr) == 0:
        return 0
    for i,x in enumerate(arr):
        arr.pop(i)
        return x + sum(arr)

# print(sum([1,2,3,4,5,6,7,8]))

# Much faster! Quicksort is a tricky case.
# In the worst case, quicksort takes O(n2) time.
def quick_sort(arr: List) -> List:
    """
Sorts the given list using the quicksort algorithm.

Args:
    arr (List): The list to be sorted.

Returns:
    List: The sorted list.

Examples:
    >>> quick_sort([4, 2, 1, 3, 5])
    [1, 2, 3, 4, 5]
    >>> quick_sort([])
    []
"""

    if len(arr) < 2:
        return arr
    pivot = arr[random.randint(0, len(arr)-1)]
    less = [x for x in arr if x <= pivot]
    greater = [x for x in arr if x > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


# print(random.sample(range(1, 101), 50))

print(quick_sort(random.sample(range(1, 10000001), 1000000)))