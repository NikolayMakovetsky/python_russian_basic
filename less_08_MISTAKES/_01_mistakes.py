print("\n---Давайте понятные имена переменным и функциям")
# bad style
x = 1
s = 'text'
l = [1, 2, 3, 4]


def getPositives(ints: list) -> list:  # camelCase is a Java syntax, not Python
    return ints


# good style
value = 1
text = 'text'
integers = [1, 2, 3, 4]  # названия коллекций давай во множественном числе!
student = ['Петя Иванов', 22]


# Название функции должно кратно отражать то, что она конкретно делает (но не как именно)
def get_positives(ints: list) -> list:
    return ints


print("---Используйте английский язык")
zagolovok, zarplata = 1, 2

print("---Всегда используй f-строки и никогда не используй конкатенацию!")
first = 'hello'
second = 'world'
print(first + second)  # так не делай
print(f"{first}" + f"{second}")  # это тоже канкатенация! ошибка!

print("---Не делаем то, что происходит по-умолчанию")
# value = str(input())  # input и так вернет строку

a_dict = {1: 1, 2: 2}
value = a_dict.get(3, None)  # None тут излишне написан
value = a_dict.get(3)  # правильный вариант
print(value)

print("---Используем listcomps СТРОГО ЛИБО для преобразования, ЛИБО для фильтрации итерируемого объекта")
# ОШИБКА
integers = [e for e in range(10)]  # listcomps должен либо 1) преобразовывать числа, либо 2) их фильтровать. Все!
print(integers)

integers = [e ** 2 for e in range(10)]  # так норм
print(integers)

integers = [e for e in range(10) if e % 2 == 0]  # так норм
print(integers)

integers = [e ** 2 for e in range(10) if e % 2 == 0]  # так норм
print(integers)

integers = list(range(10))  # так хорошо
print(integers)

print("---Не зацикливайся на map(), filter(). Они не дают преимуществ перед listcomps")
integers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))  # list[квадраты четных чисел]
integers2 = [e ** 2 for e in range(10) if e % 2 == 0]  # так мы создаем сразу список (так гораздо лучше)
integers3 = (e ** 2 for e in range(10) if e % 2 == 0)  # так мы создаем итератор (тоже вариант)
print(integers)
print(integers2)
print(integers3)

print("---Используем СТРОГО конструкцию while True: для вечных циклов")

while 1 == 1:  # while True - общепринятое написание вечного цикла, и так будет быстрее
    break

while 0 == 0:  # while True - общепринятое написание вечного цикла, и так будет быстрее
    break

print("---По-возможности используй genexp вместо listcomps (когда не требуется создавать список в памяти)")
# Мы так привыкаем писать [] для listcomps, что мы начинаем писать их даже там, где они не нужны
sum([e for e in range(10) if e % 2 == 0])  # listcomps занимает память
# listcomps создает реальный список в памяти, а нам-то сумма нужна...убирай квадратные скобки и получай итератор
lst = sum(e for e in range(10) if e % 2 == 0)  # genexp не занимающий память
print(lst)

string = ''.join(str(e) for e in range(10) if e % 2 == 0)  # genexp не занимающий память
print(string)

print("---Не используем range(len(list)), если нужен индекс, то используем enumerate")
integers = [1, 2, 3]
for integer in range(len(integers)):
    print(integers[integer], end="/")

print()
for integer in integers:  # верный способ
    print(integer, end="*")

print()
for index, element in enumerate(integers):  # верный способ, 0 - стартовый номер
    print(f"{index}, {element}")

print()
for index, element in enumerate(integers, 1):  # верный способ, 1 - стартовый номер
    print(f"{index}, {element}")

print("---Используем if collection, чтобы проверить что она не пустая")
integers = [1, 2, 3]
if len(integers) > 0:  # Ошибка, так как производится лишнее действие
    pass

if integers:  # Если коллекция не пуста, то Truthy value вернет нам True, что нам и нужно
    pass

print("---Используй встроенные функции all(), any() и прочие")
# Хотим узнать все ли элементы положительные
integers = [1, 2, 3, -1]

flag = True
for integer in integers:
    if integer < 0:
        flag = False
        break
print(flag)

print(all(e>0 for e in integers))  # так короче и быстрее

print("---Ловим конкретные исключения (используем  try-except-except-...-finally), пишем инфу в ветке except")
integers = [1, 2, 3, -1]

# такой код проглотит ошибку!!
try:
    int('a')
except:
    pass  # здесь всегда должен быть вывод сообщения! СТРОГО!

# хороший стиль
try:
    int('a')
except ValueError as e:  # ловим конкретное исключение
    print(e)  # выводим стандартное сообщение об исключении
    print('Error')  # выводим свое сообщение
