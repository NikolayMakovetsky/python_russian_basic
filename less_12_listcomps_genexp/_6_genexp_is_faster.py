from time import sleep


def some_source():
    return 1, 2, 3

def some_filter(x):
    sleep(1)
    return True

def some_mapping(x):
    sleep(1)
    return x

if __name__ == '__main__':
    # it = [some_mapping(e) for e in some_source() if some_filter(e)]
    # print(it[0])  # 6 sec to get the result !!!

    it2 = (some_mapping(e) for e in some_source() if some_filter(e))
    print(next(it2)) # 2 sec to get the result !!!
