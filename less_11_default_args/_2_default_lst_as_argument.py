def calc(time_=[]):
    time_.append(1)
    return time_


def calc2(time_=None):
    if time_ is None:
        time_ = []
    time_.append(1)
    return time_


if __name__ == '__main__':
    print("=== looks like OK")
    print(calc([]))
    print(calc([]))
    print(calc([]))

    print("=== but we have a problem")
    print(calc())
    print(calc())
    print(calc())  # сохраняется ссылка на один и тот же список

    print("=== fixed")
    print(calc2())
    print(calc2())
    print(calc2())
