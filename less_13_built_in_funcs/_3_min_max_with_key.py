a_list = ['aaa', 'bb', 'cc', 'd']


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat({self.name=}, {self.age=})"


if __name__ == '__main__':
    print(max(a_list))
    print(max(a_list, key=len))

    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Bob', 5)]
    print(max(cats, key=lambda cat: cat.name))
    print(max(cats, key=lambda cat: cat.age))

