from katas.max_sequence import max_sequence


def test_max_sequence():
    assert max_sequence([7, 4, 11, -11, 39, 36, 10, -6, 37, -10, -32, 44, -26, -34, 43, 43]) == 155
    assert max_sequence([-2, -1, -3, -4, -1, -2, -1, -5, -4]) == 0
