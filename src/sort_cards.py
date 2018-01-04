"""Sort a deck of cards."""


def compare(num1, num2):
    """."""
    if num1 == 'A':
        num1 = 1
    if num1 == 'T':
        num1 = 10
    if num1 == 'J':
        num1 = 11
    if num1 == 'Q':
        num1 = 12
    if num1 == 'K':
        num1 = 13
    if num2 == 'A':
        num2 = 1
    if num2 == 'T':
        num2 = 10
    if num2 == 'J':
        num2 = 11
    if num2 == 'Q':
        num2 = 12
    if num2 == 'K':
        num2 = 13
    num1 = int(num1)
    num2 = int(num2)
    return (num1 > num2)


final_list = []


def sort_cards(deck):
    """Sort a list using merge sort."""
    if len(deck) < 2:
        return deck
    half = int(len(deck) / 2)
    l1 = deck[0:half]
    l2 = deck[half:]
    if len(l1) > 1:
        l1 = sort_cards(l1)
    if len(l2) > 1:
        l2 = sort_cards(l2)
    return _sort(l1, l2)


def _sort(l1, l2):
    """Take two sorted lists and merge them together."""
    return_list = []
    while l1 or l2:
        if compare(l1[0], l2[0]):
            return_list.append(l2.pop(0))
        else:
            return_list.append(l1.pop(0))
        if not l1:
            return_list += l2
            return return_list
        if not l2:
            return_list += l1
            return return_list
