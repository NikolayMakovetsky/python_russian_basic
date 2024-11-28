"""
ChainMap нужен для логического объединения нескольких словарей

Очень удобно 'закинуть' словари в ChainMap
Объединение это чисто логическое, никакого реального копирования не происходит
И далее, можно во всех этих словарях сразу поискать ключ, и найти его значение

ВАЖНО!
chain имеет все те же методы, что и обычный словарь,
но если выполнять методы chain-а, они будут применяться
ТОЛЬКО К ПЕРВОМУ СЛОВАРЮ В ПОСЛЕДОВАТЕЛЬНОСТИ!!!

Поэтому ЛУЧШЕ ИСПОЛЬЗОВАТЬ ЕГО ТОЛЬКО ДЛЯ ЧТЕНИЯ
"""

from collections import ChainMap

first = {1: 11, 2: 22, 3: 33}
second = {4: 44, 5: 55}

chain = ChainMap(first, second)

if __name__ == '__main__':
    print("\n=== ChainMap inheritance")
    print(chain)

    print("\n=== ChainMap is like a union of dicts")
    print("1 in chain = ", 1 in chain)
    print("5 in chain = ", 5 in chain)

    print("\n=== get value from ChainMap")
    print(chain[1])
    print(chain[5])

    print("\n=== lets change value in one of dicts")
    first[1] = 1111
    print(f"{first[1]=}")
    print(chain)

    print("\n=== !!! USE CHAINMAP ONLY FOR READING !!!")
    chain[1] = 'hello'
    print(chain)
    chain[5] = 'world'
    print(chain)  # it doesn't change second dict as we logically want !!!
    first.pop(5)
    second[5] = 'world'
    print(chain)

