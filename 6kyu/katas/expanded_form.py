def expanded_form(num):
    result = []
    divider = 10
    for item in range(len(str(num))):
        current_num = num % divider
        if current_num != 0:
            result.append(current_num)
        num -= num % divider
        divider *= 10
    result.reverse()
    return ' + '.join(map(str, result))

