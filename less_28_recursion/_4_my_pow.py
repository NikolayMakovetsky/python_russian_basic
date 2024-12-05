def my_pow(x: int, y: int) -> int:
    if x < 0 or x == 0:
        raise ValueError("Число х должно быть > 0")
    if y < 0:
        raise ValueError("Число y должно быть >= 0")
    if y == 0:
        return 1
    if y == 1:
        return x
    return x * my_pow(x, y - 1)


pow_short = lambda x, y: 1 if y == 0 else x if y == 1 else x * pow_short(x, y - 1)

if __name__ == '__main__':
    # assert my_pow(0, 5)  # ValueError: Число х должно быть > 0
    # assert my_pow(4, -1)  # ValueError: Число y должно быть >= 0

    assert my_pow(1, 0) == 1
    assert my_pow(2, 0) == 1
    assert my_pow(256, 0) == 1

    assert my_pow(1, 1) == 1
    assert my_pow(5, 1) == 5
    assert my_pow(256, 1) == 256

    assert my_pow(1, 2) == 1
    assert my_pow(2, 2) == 4
    assert my_pow(3, 2) == 9

    assert my_pow(5, 1) == 5
    assert my_pow(5, 2) == 25
    assert my_pow(5, 3) == 125
    assert my_pow(5, 4) == 625

    assert pow_short(1, 0) == 1
    assert pow_short(2, 0) == 1
    assert pow_short(256, 0) == 1

    assert pow_short(1, 1) == 1
    assert pow_short(5, 1) == 5
    assert pow_short(256, 1) == 256

    assert pow_short(1, 2) == 1
    assert pow_short(2, 2) == 4
    assert pow_short(3, 2) == 9

    assert pow_short(5, 1) == 5
    assert pow_short(5, 2) == 25
    assert pow_short(5, 3) == 125
    assert pow_short(5, 4) == 625
