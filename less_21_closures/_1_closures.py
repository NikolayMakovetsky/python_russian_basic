"""
Когда интерпретатор создал объект ф-ии inner
(не выполнил ее, а пока только создал объект)
он увидел, что она использует переменную из внешнего scope
(пространства имен)
и он добавил к ней ссылку на на список all_names
Теперь у ф-ии inner есть ссылка на all_names
А по правилу работы питона, объект не удаляется пока на него существует ссылка!

ЗАМЫКАНИЕ
это внутренняя ф-я, кот возвращатся из внешней ф-ии, имеющая доступ
к переменным из внешнего пространства имен
"""


def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner

if __name__ == '__main__':
    students = names()  # ф-я names() вызывается только один раз

    print("\n=== students")
    print(students('Vasya'))
    print(students('Petya'))
    print(students('Dimas'))