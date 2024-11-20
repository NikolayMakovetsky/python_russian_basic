from operator import itemgetter, attrgetter


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat {self.name}, age is {self.age}"


if __name__ == '__main__':
    print("========= working with list")
    ints = list(range(10))
    print([i ** 2 for i in ints if i % 2 == 0])

    print("========= sorting dict")
    # в питоне 3.8+ itemgetter работает быстрее, чем lambda!
    a_dict = {'a': 3, 'b': 2, 'd': 1, 'c': 4}
    print(sorted(a_dict.items(), key=itemgetter(0)))
    print(sorted(a_dict.items(), key=itemgetter(1)))

    print("========= sorting cats")
    cats = [Cat('Tom', 4), Cat('Angela', 5)]
    print(sorted(cats, key=attrgetter('name')))
    print(sorted(cats, key=attrgetter('age')))
