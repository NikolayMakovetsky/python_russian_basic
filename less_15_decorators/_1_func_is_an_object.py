# decorator - паттерн программирования, кот. исп-ся во многих языках
# цель изменить поведение ф-ии, не меняя ее реализации

# Функция - полноправный объект

def summ(a, b):
    return a + b


def example(func):
    print(f"{func.__name__}")


if __name__ == '__main__':
    function = summ
    print(summ)
    print(function)

    example(summ)
    example(function)
