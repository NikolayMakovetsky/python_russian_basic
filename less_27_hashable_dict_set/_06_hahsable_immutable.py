"""
ВНИМАНИЕ! hashable и immutable ЭТО РАЗНЫЕ ТЕРМИНЫ!

Путаница в том, что для встроенных классов питона Неизменяемые типы они же и хешируемые!

Однако для пользовательских классов это может быть совершенно не так!

immutable означает, что нас класс или объект не изменяемый
hashable означает, что объект имеет дандер-метод hash

А СЛОВАРЬ и МНОЖЕСТВО РАБОТАЮТ ТОЛЬКО С HASHABLE-объектами!

"""