"""
ВОПРОС НА СОБЕСЕДОВАНИИ: tuple можно положить в словарь или в сет?
Можно, но только если он содержит все хешируемые элементы
ТО ЕСТЬ
TUPLE СТАНОВИТСЯ ХЕШИРУЕМЫМ ТОЛЬКО ЕСЛИ У НЕГО ВСЕ ЭЛЕМЕНТЫ ХЕШИРУЕМЫЕ!!
(при попытке записи все элементы будут проверены питоном)
"""


a_tuple = (1,2,3)  # a_tuple = (1,2,3, []) упадет ошибка
a_set = {a_tuple}

if __name__ == '__main__':
    print(a_set)