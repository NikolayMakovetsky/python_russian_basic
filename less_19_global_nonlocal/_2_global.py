"""
global, nonlocal НЕ НУЖНЫ ДЛЯ ПЕЧАТИ ПЕРЕМЕННЫХ
Их следует использовать если мы будем менять значения переменных

ОСОБЕННОСТЬ global:
МЫ МОЖЕМ СОЗДАТЬ ПЕРЕМЕННУЮ ВНУТРИ Ф-ИИ, НО ПРИ ЭТОМ
СРАЗУ ПОМЕСТИТЬ ЕЕ В ГЛОБАЛЬНОЕ ПРОСТРАНСТВО ИМЕН (global scope)

"""

counter = 1


def increment():
    global counter  # начни поиск с ГЛОБАЛЬНОГО пространства имен
    global temp  # создай переменую в глобальном пространстве имен (НЕ ДЕЛАЙ ТАК)
    temp = 100
    counter += 1
    print(counter, temp)



if __name__ == '__main__':
    increment()
    print(f"{counter=}")
    print(f"{temp=}")