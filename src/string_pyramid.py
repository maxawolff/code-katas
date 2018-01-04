"""."""


def watch_pyramid_from_the_side(characters):
    """."""
    print(characters)
    if not characters:
        return characters
    num_letters = 1
    num_spaces = len(characters) - 1
    pyramid = ''
    for idx, letter in enumerate(reversed(characters)):
        pyramid += ' ' * num_spaces
        pyramid += letter * num_letters
        pyramid += ' ' * num_spaces
        if idx < len(characters) - 1:
            pyramid += '\n'
            num_spaces -= 1
            num_letters += 2
#     print(pyramid)
    return pyramid


def watch_pyramid_from_above(characters):
    """."""
    if not characters:
        return characters
    if len(characters) == 1:
        return characters
    size = len(characters) * 2 - 1
    pyramid = ''
    one_level = []
    for i in range(size):
        one_level.append(characters[0])
    container = []
    for i in range(size):
        container.append(one_level[:])
    if size == 1:
        return container
    min = 1
    max = size - 2
    chars_to_add = characters[1:]
    for letter in chars_to_add:
        for row in range(size):
            for col in range(size):
                if row >= min and row <= max and col >= min and col <= max:
                    container[row][col] = letter
        min += 1
        max -= 1
    for row in container:
        for letter in row:
            pyramid += letter
        if row is not container[-1]:
            pyramid += '\n'
    return pyramid


def count_visible_characters_of_the_pyramid(characters):
    """."""
    if not characters:
        return -1
    return (len(characters) * 2 - 1) ** 2


def count_all_characters_of_the_pyramid(characters):
    """."""
    if not characters:
        return -1
    size = (len(characters) * 2 - 1) + 1
    num = 0
    for i in range(1, size, 2):
        num += i ** 2
    return num
