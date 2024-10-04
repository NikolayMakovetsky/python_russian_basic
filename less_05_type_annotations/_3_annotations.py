def calc(a: int, b: int) -> int:
    return a + b


def to_int(a_list) -> list:  # мы не указали какие элементы допустимы внутри передаваемого списка
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(to_int(['1', '2']))
    to_int(['1', '2'])[0].upper()  # PyCharm не видит ошибки
