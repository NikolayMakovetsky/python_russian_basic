"""
Список содержит целые числа и списки целых чисел.
Напишите рекурсивную функцию, которая возвращает список целых чисел
"""


def my_fixed_list(value: list) -> list:
    if not value:
        return []
    full_res, res1, res2 = [], [], []
    if isinstance(value[0], int):
        res1 = [value[0]]
        res1.extend(my_fixed_list(value[1:]))
    elif isinstance(value[0], list):
        res2 = value[0]
        res2.extend(my_fixed_list(value[1:]))

    full_res.extend(res1)
    full_res.extend(res2)
    return full_res


if __name__ == '__main__':
    assert my_fixed_list([]) == []
    assert my_fixed_list([[]]) == []
    assert my_fixed_list([[], [], []]) == []

    assert my_fixed_list([0]) == [0]
    assert my_fixed_list([1, 2, 3]) == [1, 2, 3]

    assert my_fixed_list([[1], [2], 3]) == [1, 2, 3]
    assert my_fixed_list([1, [2], 3]) == [1, 2, 3]
    assert my_fixed_list([1, 2, [3]]) == [1, 2, 3]
    assert my_fixed_list([[1, 2], 3]) == [1, 2, 3]
