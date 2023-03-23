def prime_factors(n):
    divider = 2
    result = {divider: 0}
    while n > 1:
        if n % divider == 0:
            result[divider] += 1
            n /= divider
        else:
            if result[divider] == 0:
                result.pop(divider)
            divider += 1
            result.update({divider: 0})

    return ''.join([f'({x}**{y})' if y > 1 else f'({x})' for x, y in result.items()])