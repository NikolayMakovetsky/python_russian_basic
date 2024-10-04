"""
typing содержит множество полезных функцию: Bool, Callable, None...
"""
from typing import List


def calc(a: int, b: int) -> int:
    return a + b

# def to_int(a_list) -> list[int]:  # python 3.9
def to_int(a_list) -> List[int]:  # Используем тип из модуля typing
    return [int(e) for e in a_list]


if __name__ == '__main__':
    print(to_int(['1', '2']))
    to_int(['1', '2'])[0].upper()  # PyCharm УВИДЕЛ ОШИБКУ
