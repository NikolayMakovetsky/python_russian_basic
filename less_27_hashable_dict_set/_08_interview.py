"""
ВОПРОС НА СОБЕСЕДОВАНИИ:
А можно ли сет или словарь положить в сет или словарь?
НЕТ.
И словарь и сет хранят в себе только хешируемые объекты,
но сами они не являются таковыми!

Более полный ответ
1. сет и дикт МОЖНО В КАЧЕСТВЕ ЗНАЧЕНИЯ положить в словарь
2. FROZENSET можно положить и в сет, и в дикт в качестве ключа
"""


a_set = {1,2,3}
a_fr_set = frozenset(a_set)
dct = {}

if __name__ == '__main__':
    dct[a_fr_set] = 2
    a_set.add(a_fr_set)
    print(dct)
    print(a_set)