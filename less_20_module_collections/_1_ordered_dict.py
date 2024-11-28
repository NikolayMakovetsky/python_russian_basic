"""
Несмотря на то, что начиная с Python 3.7+
dict - упорядоченная коллекция,
в OrderedDict реализованы полезные методы, которых нет во встроенном словаре!

За удобство мы платим памятью
OrderedDict занимает в 2 раза больше места на диске, чем dict
"""

from collections import OrderedDict

if __name__ == '__main__':

    first = {1:1, 2:2, 3: 3}
    second = {2:2, 1:1, 3:3}

    order1 = OrderedDict(first)
    order2 = OrderedDict(second)

    print("\n=== Сравнение работы dict и OrderedDict")
    print(first == second)
    print(order1 == order2)  # здесь учитывается порядок элементов!

    print("\n=== dict УМЕЕТ ВОЗВРАЩАТЬ ТОЛЬКО последний добавленный элемент")
    print(first, second)
    print(first.popitem())  # 3:3 (вернул именно последний добавленный элемент)
                            # т.е. встроенный словарь хранит порядок


    print("\n=== OrderedDict УМЕЕТ ВОЗВРАЩАТЬ НАЧАЛЬНЫЙ элемент")
    print(order1)
    print(order1.popitem(last=False))  # вернул начальный элемент

    print("\n=== OrderedDict УМЕЕТ СДВИГАТЬ ЭЛЕМЕНТЫ (в начало/в конец)")
    print(order1)
    order1.move_to_end(2)  # сдвить элемент 2 в конец
    print(order1)
    order1.move_to_end(2, last=False)  # сдвить элемент 2 В НАЧАЛО!
    print(order1)
