"""
1. Аннотации типов

"""
from typing import List


def to_str(integers: List[int]) -> List[str]:
    return [str(elem) for elem in integers]


def to_str2(integers: list[int]) -> list[str]:
    """в python 3.9
    можно использовать встроенные типы list, tuble, dict...
    и убрать импорт из typing!
    Однако,
    Any, Optional, Union... по-прежнему работают через typing"""
    return [str(elem) for elem in integers]


if __name__ == '__main__':
    print(to_str([1, 2, 3]))
