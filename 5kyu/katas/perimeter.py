def perimeter(n):
    result_sum = 2
    first = 1
    second = 1
    for i in range(3, n + 2):
        current_num = second + first
        first = second
        second = current_num
        result_sum += current_num

    return result_sum * 4
