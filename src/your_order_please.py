"""Your order please.

best practice solution:
def order(sentence):
    return " ".join(sorted(sentence.split(),
     key=lambda x: int(filter(str.isdigit, x))))
"""


def order(sentence):
    """Return a list of strings sorted by what number is in them."""
    # example given "tw2o o1ne" returns "o1ne tw2o"
    word_list = sentence.split(' ')
    new_word_list = []
    for i in range(1, len(word_list) + 1):
        for word in word_list:
            if str(i) in word:
                new_word_list.append(word)
    return ' '.join(new_word_list)
