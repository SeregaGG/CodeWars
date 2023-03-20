
def get_score(word):
    return sum([ord(x) - 96 for x in word])


def high(x):
    splited_str = x.split()
    max_score_word = splited_str[0]

    for item in splited_str:
        if get_score(max_score_word) < get_score(item):
            max_score_word = item

    return max_score_word