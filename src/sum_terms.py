"""Sum of the first nth term of Series.

best practice solution:
def series_sum(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))

"""


def series_sum(n):
    """Will return the sum of the nth term in a series as string.

    the results of the series are 1/1, 1/4, 1/7 etc...
    """
    denom = 1.00
    number = 0
    for i in range(1, n + 1):
        number += 1 / denom
        denom += 3
    return str(format(number, '.2f'))
