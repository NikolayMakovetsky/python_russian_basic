from time import sleep

ints = [8, -1, -2, 0, 3, -4, 5]
positives_gen = (e for e in ints if e > 0)

# приятно то, что память не выделяется сразу под все число
# по факту память не выделяется ни для одного элемента
# значения будут генерироваться на лету
positives_gen2 = (e for e in range(10_000_000_000_000_000_000) if e > 0)


def some_source():
    """
    Данная функция будет выполнена при формировании genexp!
    И произойдет задержка на 3 секунды !!!
    Т.е. ХОТЯ ГЕНЕРАТОР И ЛЕНИВЫЙ, НО ИСТОЧНИК ОН ПРОВЕРИТ СРАЗУ ПРИ СОЗДАНИИ
    """
    print("!!!")
    # open db
    # read file
    # calculate
    sleep(3)
    return [1, 2, 3]

if __name__ == '__main__':
    print(positives_gen)
    print(next(positives_gen))
    print("=")

    for e in positives_gen:
        print(e)

    print("=== work with big int")
    print(next(positives_gen2))
    print(next(positives_gen2))
    print(next(positives_gen2))
    print(next(positives_gen2))

    print("=== some_source")
    gen = (e for e in some_source())