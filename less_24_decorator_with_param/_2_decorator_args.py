def typed(type_):
    def real_decorator(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    raise ValueError(f"Тип должен быть {type_}")
            return func(*args)

        return wrapper

    return real_decorator


@typed(str)  # real_decorator
def convert(a: str, b: str) -> str:
    """ф-я для работы со строками"""
    # logic
    return a + b


if __name__ == '__main__':
    # convert = typed(int)(convert)
    # typed(int)(convert)('Hello, ', 'world!') -> convert('Hello, ', 'world!')
    print(convert('Hello, ', 'world!'))
