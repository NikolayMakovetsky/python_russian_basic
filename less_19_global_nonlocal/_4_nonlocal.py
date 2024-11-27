"""
nonlocal говорит интерпретатору переходить сразу
к пространству имен enclosed

enclosed означает все пространство вложенностей,
или иначе все функции, которые вложены друг в друга

ОСОБЕННОСТЬ nonlocal:
В отличие от global, мы не можем с помощью этого ключевого слова переменную
в области nonlocal, что логично, ведь не понятно в какой именно ф-ии нужно
создавать переменную (вложенных ф-ий мб много)
"""

counter = 100


def increment():
    counter = 0

    def inner1():

        def inner():
            nonlocal counter  # используй counter из enclosed
            counter += 1
            print(counter)

        inner()
    inner1()


if __name__ == '__main__':
    increment()  # 100