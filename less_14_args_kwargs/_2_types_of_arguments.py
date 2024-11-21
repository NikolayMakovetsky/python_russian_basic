# args - позиционные аргументы (всегда идут вначале)
# kwargs - именованные(ключевые) аргументы

def example(a, b, c):
    print(a, b, c)


if __name__ == '__main__':
    example(1, 2, 3)
    example(1, c=88, b=77)
    example(b=2, a=9, c=3)
    # example(a=3, 6, c=8)  # ОШИБКА! Сначала нужно указывать все позиц аргументы