

def cycle(value):
    even_squares = [e ** 2 for e in range(10) if e % 2 == 0]
    for e in range(6):
        value += e
        print(value)
        # some more actions
    return value


if __name__ == '__main__':
    print(one(1, 2))
    cycle(50)