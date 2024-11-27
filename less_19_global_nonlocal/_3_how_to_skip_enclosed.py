"""
global, nonlocal нужны только для изменения значений переменных

РАССМОТРИМ ОДНО ИСКЛЮЧЕНИЕ ИЗ ЭТОГО ПРАВИЛА:
В случаях крайней необходимости можно использовать
global, чтобы "обмануть" legb-rule
"""


counter = 100

def increment():
    counter = 0

    def inner():
        global counter  # "перескочи" nonlocal, используй сразу global
        print(counter)

    inner()

if __name__ == '__main__':
    increment()  # 100