"""
count можно менять только используя метод counter()
т.е. объект count с важными нам данными защищен!
Фактически, мы добавляем к объекту специальный публичный метод для работы с ним!

NAMED TUPLE - ПЕРВЫЙ ШАК К ООП (Мы можем создавать объект с атрибутами)
ЗАМЫКАНИЕ - ВТОРОЙ ШАГ К ООП (Мы добавляем к объекту метод для работы с ним)
"""


def counter():
    count = 0

    def inner(val: int) -> int:
        nonlocal count
        count += val
        return count

    return inner


if __name__ == '__main__':
    count = counter()
    print(count(1))
    print(count(1))
    print(count(1))
    print(count(-3))
