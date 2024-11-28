if __name__ == '__main__':
    print("\n=== old python version")
    first = {1:1, 2:2}
    second = {3: 3, 4: 4}
    third = {5:5, 4:100}
    first.update(second)
    print(first)
    print({**first, **second, **third})  # Объединение словарей

    print("\n=== python 3.9")
    first = {1:1, 2:2}
    second = {3: 3, 4: 4}
    first |= second  # first = first | second  # обновление словаря
    print(first)
    print(first | second | third)  # Объединение словарей

    print("\n=== ЕСТЬ ChainMap - логическое, а не физическое объединение словарей!")