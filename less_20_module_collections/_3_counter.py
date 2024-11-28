"""
Counter
принимает iterable или словарь (hashable - объекты)
т.к. он под капотом преобразует все объекты в словарь,
а ключи в словаре должны быть строго хэшируемые


ДЗ: посчитать 5 самых частых слов в каком-нибудь тексте (книга марка луца)
Частотный анализ текста достаточно частая задача 
"""

from collections import Counter

counter = Counter('hello')  # принимает iterable или словарь (hashable - объекты)

if __name__ == '__main__':
    print("\n=== Counter works with hashable objects")
    print(counter)  # найти какие буквы встречаются в слове больше всего
    counter.update('world')
    print(counter)

    print("\n=== Counter.most_common")
    print(counter.most_common(1)) # вывести самый частый элемент
    print(counter.most_common(3))