"""Find the pairity outlier.

best practice solution:
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
"""


def find_outlier(integers):
    """Return whatever number is an outlier from a list, even or odd."""
    def is_even(number):
        if number % 2:
            return -1
        else:
            return 1

    odd_or_even = is_even(integers[0])
    + is_even(integers[1]) + is_even(integers[2])

    if odd_or_even > 0:
        for number in integers:
            if is_even(number) == -1:
                return number
    else:
        for number in integers:
            if is_even(number) == 1:
                return number
