"""
print(int()) = 0

Как работает defaultdict?
Если в нем нет какого-то элемента, а мы к нему обращаемся, то
он вызывает ту функцию, которую мы передали.
Примеры передаваемых ф-ий:
- создание списка
- создание целого числа

СУТЬ В ТОМ, ЧТО ЗНАЧЕНИЕ ПОДСТАВЛЯЕТСЯ ИМЕННО В МОМЕНТ
КОГДА МЫ ОБРАЩАЕМСЯ К КЛЮЧУ
"""

from collections import defaultdict


def item_factory():
    return "default_value"


a_dict = defaultdict(int)
b_dict = defaultdict(list)
c_dict = defaultdict(item_factory)

if __name__ == '__main__':
    print("\n=== int() returns 0 !")
    print(int())

    print("\n=== Добавление нового ключа со значением по умолчанию")
    print(a_dict["vfvnhgggmvbvnvcbcv"])

    print("\n=== Проверка на наличие ключа")
    print(1 in a_dict)

    print("\n=== Добавление пар ключ:значение в цикле")
    for char in 'hello':
        a_dict[char] += 1  # сделали аналог Counter=)
        # Если char не существует, то вызывается int(), которая возвращает 0 и мы делаем +1
        # Если char уже существует, то счетчик просто увеличиваестся +1

    print(a_dict)
    print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))

    print("\n=== Добавление существующего ключа (перезапись значения)")
    a_dict['l'] = 999
    print(a_dict)

    print("\n=== defaultdict(list) -> получим мультисловарь")
    for char in 'hello':
        b_dict[char].append(char)

    print(b_dict)

    print("\n=== defaultdict with own func as a factory")
    c_dict[1]
    c_dict[2]
    print(c_dict)