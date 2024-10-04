from typing import Union, Optional, Any


def calc(a: Union[int, float], b: Optional[int]) -> Any:
    """
    Аргумент a может принять int, либо float
    Аргумент b может принять None, либо int
    Функция может вернуть любой тип (Any)

    ВАЖНО !!! Все аннотации типов это только РЕКОМЕНДАЦИИ И ПОДСКАЗКИ
    НИЧТО НЕ ПОМЕШАЕТ ВАМ ЗАПУСТИТЬ КОД И ПЕРЕДАТЬ НЕВЕРНЫЕ АРГУМЕНТЫ
    """
    if b is None:
        return a
    return a + b


if __name__ == '__main__':
    print(calc(3.3, None))
    # print(calc(3.3))  # TypeError: calc() missing 1 required positional argument: 'b'
    print(calc(5, 9))
