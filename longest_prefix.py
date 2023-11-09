"""this is a leetcode problem to find the longest prefix in an array of strings
return an empty string if there isn't a commone prefix amongst all the items in array of strings"""
from typing import List


def common_prefix(arr: List) -> str:
    # sort the array
    sorted_array = sorted(arr)
    if 0 <= len(arr) <= 1:
        return arr[0]
    prefix = ""
    for char1, char2 in zip(sorted_array[0], sorted_array[-1]):
        if char1 == char2:
            prefix += char1
        else:
            break
    return prefix


