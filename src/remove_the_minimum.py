"""Remove the minimum.

best practice solution:

def remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

"""


def remove_smallest(numbers):
    """Remove the smallest value from a list."""
    if numbers == []:
        return numbers
    smallest = numbers[0]
    index = 0
    for idx, number in enumerate(numbers):
        if number < smallest:
            smallest = number
            index = idx
    numbers.pop(index)
    return numbers
