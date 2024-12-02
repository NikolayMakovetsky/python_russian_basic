def typed_int(func):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int):
                raise ValueError("Тип должен быть int")
        return func(*args)

    return wrapper


@typed_int
def calculate(a, b, c):
    # logic
    return a + b + c


if __name__ == '__main__':
    # calculate = typed_int(calculate)
    # typed_int(calculate)(1, 2, 3) -> (calculate)(1, 2, 3)
    print(calculate(1, 2, 3))
