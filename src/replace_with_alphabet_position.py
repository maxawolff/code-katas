"""Replace with alphabet position.

best practice solution
def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

"""


def alphabet_position(text):
    """Replace a letter with its alphabet position ie a = 1."""
    words = text.split(' ')
    numbers = []
    for word in words:
        for letter in word:
            number = ord(letter)
            if number > 96:
                numbers.append(str(number - 96))
            elif number > 64:
                numbers.append(str(number - 64))
    return ' '.join(numbers)
