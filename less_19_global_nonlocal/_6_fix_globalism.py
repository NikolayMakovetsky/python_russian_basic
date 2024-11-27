#  СОВЕТ: не используйте global (и тем более nonlocal)

counter = 100


def increment(value):
    """Данная ф-я универсальна, и всегда возвращает один и тот же результат
    Они не влияет ни на что вне себя
    Такую ф-ю легко тестировать и удобно использовать"""
    return value + 1


if __name__ == '__main__':
    counter = increment(counter)  # counter меняем явно
    print(counter)
