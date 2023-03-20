def max_sequence(arr):
    current_sum = 0
    result = 0

    for item in arr:

        current_sum += item

        if current_sum < 0:
            current_sum = 0

        if result < current_sum:
            result = current_sum

    return result
