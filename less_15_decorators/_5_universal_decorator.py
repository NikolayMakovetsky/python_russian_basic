def logger_number(log_num):
    def logger(func):
        def wrapper(*args, **kwargs):
            """Мы добавили логирование к нашей ф-ии func"""
            print(f'{func.__name__} started. {log_num=}')
            result = func(*args, **kwargs)
            print(f'{func.__name__} finished. {log_num=}')
            return result

        return wrapper
    return logger

@logger_number(5)
def calc(a, b, sign='+'):
    action = {"+": lambda a, b: a + b,
              "-": lambda a, b: a - b,
              "*": lambda a, b: a * b,
              "/": lambda a, b: a / b
              }
    return action[sign](a, b)


if __name__ == '__main__':
    print(calc(2, 3))
    print(calc(2, 3, sign="+"))
    print(calc(2, 3, sign="-"))
    print(calc(2, 3, sign="*"))
    print(calc(2, 3, sign="/"))
