def calc(a, b):
    return a + b


if __name__ == '__main__':
    print(calc(2, 2))

    # Хотя в коде есть ошибки, PyCharm без аннотаций не может о них заранее просигнализировать
    calc(2, 3).upper()  # у типа int нет метода upper()
    calc('2', 3)  # в python складывать стоку с числом нельзя
