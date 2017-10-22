"""Kata array diff - returns the difference beteween arrays.

best practice solution:
    def array_diff(a, b):
    return [x for x in a if x not in b]

"""


def array_diff(a, b):
    """Return the values in a that are not in b."""
    tbr = []
    for idx, number in enumerate(a):
        if number in b:
            tbr.append(idx)
    for idx in tbr[::-1]:
        a.pop(idx)
    return a
