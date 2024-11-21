def my_print1(a, *args):
    print(a, args)


def my_print2(*args):
    print(args)


def my_print3(*args, number: int | float = 2):
    lst = [el * number for el in args]
    print(lst)


def my_print4(*args, **kwargs):
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


def my_print5(*args, **kwargs):
    lst = [el * kwargs["number"] for el in args]
    print(*lst, sep=kwargs["sep"])


def my_print6(*args, **kwargs):
    print(*args, **kwargs)


if __name__ == '__main__':
    print("=== my_print1")
    my_print1(1, 2, 3, 4, 5)  # получили int, tuple

    print("=== my_print2")
    my_print2(6, 7, 8, 9)

    print("=== my_print3")
    my_print3(6, 7, 8, 9, number=1.5)
    my_print3(6, 7, 8, 9)

    print("=== my_print4")
    my_print4(3, 4, 5, "erer", flag=True, DB="pg")

    print("=== my_print5")
    my_print5(1, 2, 3, number=3, sep="-//-")

    # print("=== my_print6")
    # my_print6(1, 2, 3, number=3, sep="-//-")  # TypeError:
    # # 'number' is an invalid keyword argument for print()
    # ЕСЛИ БЫ print() СОДЕРЖАЛ **kwargs, ТО ОН БЫ ПРИНИМАЛ ЛЮБЫЕ ИМЕНОВАННЫЕ АРГУМЕНТЫ !!!

    print("=== оператор ** внутри принта")
    print(1, 2, **{'sep': "/", 'end': "!!!"})
    print("")
    print(1, 2, sep="/", end="!!!")  # аналог строки выше
    print("")
