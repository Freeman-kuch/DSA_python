"""this is an algorithm that;
1> takes in a sorted list of elements
2> if the element you are looking for is in the list, it returns the position where it is located, otherwise it returns null
  for any list of n, binary search will take log2 n steps to run in the worst case"""
from typing import List


def binary_search(array: List, item) -> int | None:
    """ Concept still entails that for any list of n elements, binary search will take log N steps to run,
    in the worst case scenario"""
    low = 0  # beginning of the list/array
    high = len(array) - 1  # the last index of the list
    # Each time, you check the middle element
    #  you are basically checking from the middle not from the classic RHS or LHS
    while low <= high:
        mid = (low + high) // 2
        guess = array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        elif guess > item:
            high = mid + 1
    return None
