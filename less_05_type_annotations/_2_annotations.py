def calc(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    print(calc(2, 2))

    calc(2, 3).upper()  # теперь видим подсказку среды
    calc('2', 3)  # теперь видим подсказку среды
    # Теперь чтобы получить основную информацию о функции достаточно навести на нее мышь
