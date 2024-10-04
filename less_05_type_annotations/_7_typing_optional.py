from typing import Union, Optional


def calc(a: Union[int, float], b: Optional[int]) -> Union[int, float]:
    """
    Аргумент b может принять None, либо int
    """
    if b is None:
        return a
    return a + b


if __name__ == '__main__':
    print(calc(3.3, None))
    # print(calc(3.3))  # TypeError: calc() missing 1 required positional argument: 'b'
    print(calc(5, 9))
