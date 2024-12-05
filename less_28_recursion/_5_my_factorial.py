def my_factorial(value: int) -> int:
    if value == 0:
        return 1
    return value * my_factorial(value-1)

fact_short = lambda val: 1 if val == 0 else val * fact_short(val-1)


if __name__ == '__main__':
    assert my_factorial(0) == 1
    assert my_factorial(1) == 1
    assert my_factorial(2) == 2
    assert my_factorial(3) == 6
    assert my_factorial(4) == 24
    assert my_factorial(5) == 120

    assert fact_short(0) == 1
    assert fact_short(1) == 1
    assert fact_short(2) == 2
    assert fact_short(3) == 6
    assert fact_short(4) == 24
    assert fact_short(5) == 120