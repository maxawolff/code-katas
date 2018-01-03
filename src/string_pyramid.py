def watch_pyramid_from_above(characters):
    """Pyramid from above."""
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
