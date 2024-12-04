from timeit import timeit

if __name__ == '__main__':
    a_list = list(range(10_000))
    a_set = set(a_list)
    a_dict = {e: None for e in a_list}

    in_list = timeit("5_000 in a_list", "from __main__ import a_list", number=100)
    in_set = timeit("5_000 in a_set", "from __main__ import a_set", number=100)
    in_dict = timeit("5_000 in a_dict", "from __main__ import a_dict", number=100)

    print(f'{in_list:.6f}')  # 0.004325 время поиска значения 5_000 в списке
    print(f'{in_set:.6f}')  # 0.000006 время поиска значения 5_000 в множестве!
    print(f'{in_dict:.6f}')  # 0.000006 время поиска значения 5_000 в словаре!