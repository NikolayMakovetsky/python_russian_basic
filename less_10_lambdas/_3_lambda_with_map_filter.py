def is_even(x):
    return x % 2 == 0

def second(x):  # замена для lambda
    return x[1]


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat {self.name}, age is {self.age}"

if __name__ == '__main__':
    print(is_even(2))
    print(is_even(3))

    print("========= working with list")
    ints = list(range(10))
    print(list(map(lambda y: y ** 2, filter(lambda x: x % 2 == 0, ints))))

    print("========= sorting dict")
    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}
    print(sorted(a_dict.items(), key=lambda x: x[0]))
    print(sorted(a_dict.items(), key=lambda x: x[1]))

    print("========= sorting cats")
    cats = [Cat('Tom',4), Cat('Angela',5)]
    print(sorted(cats, key=lambda cat: cat.name))
    print(sorted(cats, key=lambda cat: cat.age))
