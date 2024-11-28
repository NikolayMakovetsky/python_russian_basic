"""
Named tuple
позволяет работать с ним как с кортежем, он также неизменяемый,
но при этом в нем есть возожность добавить имя кортежа и имена свойств...
По сути мы получаем что-то вроде класса в зачаточном состоянии...

Начиная с питон 3.8 обращение к атрибуту в Named tuple
быстрее чем к атрибуту класса!
"""

from collections import namedtuple
import csv

tuple_tom = ('Tom', 4, 'yellow')  # неудобно, т.к. нужно помнить номера свойств
Cat = namedtuple('Cat', 'name age color')
Point = namedtuple('Point', 'x y')


if __name__ == '__main__':

    print("\n=== tuple")
    print(tuple_tom)

    print("\n=== named tuple")
    tom = Cat('Tom', 4, 'yellow')
    print(tom)
    print(tom[0], tom[1], tom[2])
    print(tom.name, tom.age, tom.color)

    print("\n=== working with file")
    with open('files\points.csv') as file:
        for line in csv.reader(file):
            point = Point._make(line)
            print(point)
