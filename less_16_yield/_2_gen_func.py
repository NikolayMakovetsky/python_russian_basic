# yield показывает что ф-я является генератором (т.е. возвращает она генератор)
# внутри ф-ии генератора могут содержаться и return-ы
# генератор ленивый (lazy)
# Когда генератор исчерпан, он бросает StopIteration (но в цикле for этого не видно)
# for сам обрабатывает StopIteration
# Генератор мб использован ТОЛЬКО ОДИН РАЗ!


def square2():
    print("Generator working...")
    for e in range(0, 11, 2):
        yield e ** 2


if __name__ == '__main__':
    gen = square2()
    print(gen)

    for i in gen:  # Generator working... будет распечатано перед выдачей первого значения
        print(i)
