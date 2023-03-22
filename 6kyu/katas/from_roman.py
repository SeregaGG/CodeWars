symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def solution(roman):
    result = 0
    iter = 0
    while iter < len(roman):
        if iter < len(roman) - 1:
            if symbols.get(roman[iter]) < symbols.get(roman[iter + 1]):
                result += symbols.get(roman[iter + 1]) - symbols.get(roman[iter])
                iter += 2
                continue

        result += symbols.get(roman[iter])

        iter += 1
    return result
