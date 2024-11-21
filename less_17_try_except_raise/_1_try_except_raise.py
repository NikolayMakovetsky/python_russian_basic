"""
Проблема try-except в том,
что пользователь может не видеть логи, в которые мы записываем сообщения об ошибках...
Также он может не понимать, почему функция возвращает не ожидаемое значение, а
нуль или например пустую строку...
ДА, КОНЕЧНО, МЫ МОЖЕМ УКАЗАТЬ АННОТАЦИИ ТИПОВ, И PYCHARM ПОДСКАЖЕТ НАМ,
ГДЕ ТОНКИЕ МЕСТА, НО ДРУГАЯ IDE МОЖЕТ НЕ ДАВАТЬ ТАКОЙ ИНФОРМАЦИИ
Аннотации - это рекомендации, а не требования...
Код все равно будет запускаться...

Чтобы избежать проблем, можно использовать явные проверки
RAISE
Таким образом мы выбрасываем исключения
А отлавливать и обрабатывать их можно в отдельном классе например
(Чтобы с одной стороны программы продолжала работать,
а с другой пользователь точно увидел что именно идет не так,
и мог исправить ошибку)
"""


def divide(a, b):
    return a // b


def divide2(a, b):
    try:
        return a // b  # когда интерпретатор выбросит исключение
        # он увидит что есть перехватчик, и воспользуется им
        # Интерпретатор передает управление перехватчику
    except ZeroDivisionError:
        print("ZeroDivisionError!")
        return 0  # цель перехвата в том, чтобы программа продолжила корректную работу
    except TypeError:
        print("TypeError!")
        return ""


def divide3(a: int, b: int) -> int:
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Аргументы должны быть целыми числами")
    if b == 0:
        raise ValueError("Делитель не может быть равен нулю")
    return a // b


if __name__ == '__main__':
    print("=== no try-except = problem")
    print(divide(4, 2))
    # print(divide(4, 0)) # ZeroDivisionError: integer division or modulo by zero

    print("=== try-except")
    print(divide2(4, 0))

    print("=== if we put '0' to param: b")
    print(divide2(4, '0'))  # TypeError: unsupported operand type(s) for //: 'int' and 'str'

    print("=== raise")
    print(divide3(4, 0))
    print(divide3(4, '0'))

