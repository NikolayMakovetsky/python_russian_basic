# finally выполняется всегда (даже если ничего не упадет)


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
        print(ext)  # ОБЯЗАТЕЛЬНО СООБЩАЙТЕ ПОЛЬЗОВАТЕЛЮ ЧТО ПРОИЗОШЛО ИСКЛЮЧЕНИЕ !!!
    finally:
        # в блоке finally тоже могут падать исключения!
        # print(res)  # NameError: name 'res' is not defined
        print("Finish")
