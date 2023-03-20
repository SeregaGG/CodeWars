
def good_vs_evil(good, evil):
    goods_cost = [1, 2, 3, 3, 4, 10]
    evil_cost = [1, 2, 2, 2, 3, 5, 10]

    result = sum([int(val) * goods_cost[x] for x, val in enumerate(good.split(' '))]) - sum(
        [int(val) * evil_cost[x] for x, val in enumerate(evil.split(' '))])

    if result == 0:
        return 'Battle Result: No victor on this battle field'

    if result < 0:
        return 'Battle Result: Evil eradicates all trace of Good'

    return 'Battle Result: Good triumphs over Evil'
