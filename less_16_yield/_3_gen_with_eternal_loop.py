def pause():
    print("Generator working...")
    while True:
        print(f"global {a=}")
        yield a  # здесь генератор в прямом смысле ставится на паузу
        # он помнит значения всех переменных, которые тут используются
        # Он будет работать пока не выбросится StopIteration


if __name__ == '__main__':
    a = 10
    gen = pause()
    print(gen)
    print(next(gen))
    a = 20
    print(next(gen))
