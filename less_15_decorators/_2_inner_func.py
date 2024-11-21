# Внутренняя ф-я можут захватывать переменные из внешней


def example(a):
    def inner(b):
        print(a+b)

    inner(3)  # мы вызвали одну ф-ю внутри другой


if __name__ == '__main__':
    example(2)