# Обычно данные классы лежат в отдельном модуле
# Exceptions или Errors
# Это удобно, когда выброс типового исключения не дает ясности
# пользователю в чем же все-таки проблема


class ArgumentEqualZeroError(Exception):
    """Выбрасывается когда делитель равен нулю"""
    pass


class ArgumentIsNotIntegerError(Exception):
    """Выбрасывается если аргумент не целое число"""
    pass


def divide(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ArgumentIsNotIntegerError("Аргументы должны быть целыми числами")
    if b == 0:
        raise ArgumentEqualZeroError("Делитель не может быть равен нулю")
    return a // b


if __name__ == '__main__':
    try:
        res = divide(4, 0)
    except (ArgumentIsNotIntegerError, ArgumentEqualZeroError) as ext:
        print(ext)
        raise   # если без аргументов указать то бросается ОТРАБОТАВШЕЕ ИСКЛЮЧЕНИЕ

