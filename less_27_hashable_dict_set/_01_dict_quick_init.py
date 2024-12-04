import dis
from timeit import timeit

if __name__ == '__main__':
    x = timeit("dict()")
    y = timeit("{}")  #  Такой способ создания пустого словаря БЫСТРЕЕ !
    print(x)
    print(y)
    print(dis.dis("dict()"))
    print(dis.dis("{}"))  # байт-код этой команды содержит МЕНЬШЕ строк