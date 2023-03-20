def longest_consec(strarr, k):
    if k > len(strarr) or k <= 0 or len(strarr) == 0:
        return ''

    result = ''
    for i in range(len(strarr)):
        current_str = ''.join(strarr[i:i+k])
        if len(result) < len(current_str):
            result = current_str

    return result

