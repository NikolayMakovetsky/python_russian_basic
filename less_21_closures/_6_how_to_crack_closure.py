def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner


if __name__ == '__main__':
    boys = names()

    print("\n=== how to crack closure")
    boys('Vasya')
    print(boys.__closure__[0].cell_contents)
