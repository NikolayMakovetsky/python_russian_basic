"""
Если аргумент не передается, то будет использовано значение по-умолчанию
"""
from time import time, sleep


def print_n_times(value: str, n: int = 3):
    for _ in range(n):
        print(value)


def calc(time_=time()):  # аргумент по-умолчанию создается только один раз
    print(time_)


def some_func():
    print("\nSOME FUNC CALLED !!! (only once) \n")
    return 1


def calc2(var=some_func()):
    print(var)


if __name__ == '__main__':
    print("=== basic usage of default value")
    print_n_times('hello')
    print_n_times("hi", n=2)

    print("==== working with time as default value in function")
    calc()
    calc()
    sleep(2)
    calc()

    print("==== working with default value as result of other func (SOME FUNC CALLED ABOVE)")
    calc2()
    calc2()
    calc2()
