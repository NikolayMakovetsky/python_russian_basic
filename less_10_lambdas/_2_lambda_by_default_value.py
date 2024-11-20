if __name__ == '__main__':
    x = 2
    result = lambda: x ** 2
    x = 3
    result2 = lambda: x ** 2
    print(result())  # 9
    print(result2())  # 9

    x = 4
    result = lambda n=x: n ** 2  # задаем значение по-умолчанию
    x = 5
    result2 = lambda n=x: n ** 2  # задаем значение по-умолчанию
    print(result())  # 16
    print(result2())  # 25
    print(result(1))  # 1  (т.к. наше значение перегрузило знач по-умолчанию)
    print(result2(2))  # 4 (т.к. наше значение перегрузило знач по-умолчанию)


