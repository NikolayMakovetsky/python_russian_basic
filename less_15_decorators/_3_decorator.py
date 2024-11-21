def summ(a, b):
    return a + b


def logger(func):
    def wrapper(a, b):
        """Мы добавили логирование к нашей ф-ии func"""
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} finished')
        return result

    return wrapper


if __name__ == '__main__':
    function = logger(summ)
    print(function)
    print(function(2, 3))

    print(logger(summ)(4, 5))  # запись в одну строку

    summ = logger(summ)  # переопределили функцию
    print(summ(1, 2))
