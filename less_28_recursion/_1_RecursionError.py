def inc(x):
    print(x)
    return inc(x + 1)


if __name__ == '__main__':
    inc(0)  # 996 + RecursionError: maximum recursion depth exceeded while calling a Python object
