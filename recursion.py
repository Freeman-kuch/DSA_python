# • Recursion is when a function calls itself.
# • Every recursive function has two cases: the base case and the recursive case.
# • A stack has two operations: push and pop.
# • All function calls go onto the call stack.
# • The call stack can get very large, which takes up a lot of memory.

def find_key(box):
    """
Finds the key within a nested box structure.

Args:
    box (list): The nested list of boxes to search through.

Returns:
    str: A message indicating whether the key was found or not.
"""

    for item in box:
        if item.is_a_box():
            find_key(item)
        elif item.is_a_key():
            return "found the key"
        


def factorial(x : int ) -> int:
    """
Calculates the factorial of a given integer using recursion.

Args:
    x (int): The integer for which to calculate the factorial.

Returns:
    int: The factorial of the given integer.

Examples:
    >>> factorial(5)
    120
"""

    return 1 if x == 1 else x * factorial(x - 1)