"""Beginner Series #3 Sum of Numbers."""


def get_sum(a, b):
    """Return the sum of all numbers between and including a and b."""
    count = 0
    if a == b:
        return a
    if a < b:
        for i in range(a, b + 1):
            count += i
    if b < a:
        for i in range(b, a + 1):
            count += i
    return count
