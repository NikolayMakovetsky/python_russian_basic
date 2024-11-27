"""
Правило работы интерпретатора:
Если внутри ф-ии мы меняем переменную, то интерпретатор автоматически
считает, что эта переменная локальная,
и он будет искать в локальной области объявление данной переменной
"""

counter = 1

#  ЧАСТАЯ ОШИБКА
#  UnboundLocalError:
#  cannot access local variable 'counter' where it is not associated with a value
def increment():
    counter += 1
    print(counter)



if __name__ == '__main__':
    increment()
