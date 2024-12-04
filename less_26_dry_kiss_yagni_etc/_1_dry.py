def func():
    """Код дублируется"""
    # some code
    with open('test.txt') as file:
        result = file.readlines()
    return result


def two():
    """Код дублируется"""
    # some code
    with open('test2.txt') as file:
        result = file.readlines()
    return result


def read_from_file(name):
    """Хорошая функция"""
    with open(name) as file:
        result = file.readlines()
    return result


