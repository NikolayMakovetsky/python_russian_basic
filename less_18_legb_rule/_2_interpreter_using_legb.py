"""
Когда интерпретатор видит название какой-то функции или переменной
он не идет сразу во встроенные функции и не вызывает ее!
Он начинает искать встроенную ф-ю также по правилу LEGB !!!
И если именем встроенной ф-ии назвали по невнимательности пользовательский объект,
то интерпретатор вернет ссылку на этот пользовательский объект
"""

max = 10

if __name__ == '__main__':
    print(max([1, 2, 3]))  # TypeError: 'int' object is not subscriptable