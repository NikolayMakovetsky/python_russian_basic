"""
Lambda-functions часто используются в:
1. сортировках
2. внутри функции map
3. просто в коде, где их удобно использовать
"""


def square(x):
    return x ** 2


square2 = lambda x: x ** 2  # square2 - это переменная, а не имя функции
even_odd = lambda x: 'EVEN' if x % 2 == 0 else 'ODD'  # тернарный оператор можно использовать

# здесь мы просим lambda при вызове вернуть значение переменной abracadabra
# удобство в том, что мы можем создать lambda до того, как abracadabra существует
any_ = lambda: abracadabra  # lambda не выполняется до вызова!

# здесь мы просим lambda при вызове вернуть значение функции square
any2 = lambda: square(use(it))  # lambda не выполняется до вызова!

if __name__ == '__main__':
    print("==========even, odd")
    print(square(2))
    print(square2(3))
    print("==========even, odd")
    print(even_odd(5))
    print(even_odd(6))
    print("==========abracadabra, square")
    print(any_)
    print(any2)
    print("==========abracadabra=100")
    abracadabra=100
    print(any_())
