def logger(func):
    def wrapper(a, b):
        """Мы добавили логирование к нашей ф-ии func"""
        print(f'{func.__name__} started')
        result = func(a, b)
        print(f'{func.__name__} finished')
        return result

    return wrapper


@logger
def summ(a, b):
    return a + b


if __name__ == '__main__':
    print(summ(2, 3))
    print(summ)
