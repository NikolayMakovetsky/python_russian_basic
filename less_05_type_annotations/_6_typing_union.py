from typing import List, Union


def calc(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """
    Функция может складывать либо int, либо float
    """
    return a + b


if __name__ == '__main__':
    print(calc(1.2, 3.3))
    print(calc(5, 9))
    print(calc(1.2, 10))
