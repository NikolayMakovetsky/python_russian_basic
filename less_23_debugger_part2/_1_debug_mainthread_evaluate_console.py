def one(x, y):
    result = x + y
    return two(result)


def two(result):
    result = f'{result}!!'
    return three(result)


def three(result):
    return 100 / result.count("!")  # "?"


if __name__ == '__main__':
    print(one(1, 2))
