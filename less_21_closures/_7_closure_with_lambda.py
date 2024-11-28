"""
ЭТО ТОЖЕ ЗАМЫКАНИЕ !!!
"""

def pow_(base):
    return lambda value: value ** base


if __name__ == '__main__':
    p = pow_(2)

    print("\n=== pow with base 2")
    print(p(5))
