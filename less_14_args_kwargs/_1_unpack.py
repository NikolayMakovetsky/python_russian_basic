

a, b, c = 1, 2, 3  # распаковка
d, e = "ab"
f, g = [88, 99]
h, *i = (5, 6, 7, 8)  # * заворачивает все что осталось в список
j, *k = 'abbbb'  # * заворачивает все что осталось в список
*l, m = 'ccccd'  # * заворачивает все что осталось в список
n, *_, p = 11, 77, 88, 99, 22

if __name__ == '__main__':
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')
    print(f'{d=}')
    print(f'{e=}')
    print(f'{f=}')
    print(f'{g=}')
    print(f'{h=}')
    print(f'{i=}')
    print(f'{j=}')
    print(f'{k=}')
    print(f'{l=}')
    print(f'{m=}')
    print(f'{n=}')
    print(f'{p=}')

    print(*[1, 2, 3])
    print(1, 2, 3)  # аналог записи выше (получаем удобный вывод)
