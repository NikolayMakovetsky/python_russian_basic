def my_sum(a_list: list) -> int:
    """Условие: написать функцию без использования циклов"""
    if not a_list:
        return 0
    if len(a_list) == 1:
        return a_list[0]
    return a_list[0] + my_sum(a_list[1:])  # кстати, рекурсивных вызовов мб несколько


sum_short = lambda lst: 0 if not lst else lst[0] if len(lst) == 1 else lst[0] + sum_short(lst[1:])


if __name__ == '__main__':
    # сначала пишем asserts, а потом уже реализацию самой функции
    assert my_sum([]) == 0
    assert my_sum([1]) == 1
    assert my_sum([-1]) == -1
    assert my_sum([2, 2]) == 4
    assert my_sum([1, 2, 3]) == 6

    assert sum_short([]) == 0
    assert sum_short([1]) == 1
    assert sum_short([-1]) == -1
    assert sum_short([2, 2]) == 4
    assert sum_short([1, 2, 3]) == 6