def pow_(base):
    def inner(value):
        return value ** base

    return inner


if __name__ == '__main__':
    pow__ = pow_(2)

    print("\n=== pow with base 2")
    print(pow__(5))
    print(pow__(6))
    print(pow__(7))

    pow_2 = pow_(3)

    print("\n=== pow with base 3")
    print(pow_2(5))
    print(pow_2(6))
    print(pow_2(7))