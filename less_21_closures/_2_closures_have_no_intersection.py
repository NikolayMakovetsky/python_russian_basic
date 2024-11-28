"""
Замыкания не пересекаются друг с другом
Каждое замыкание хранит ТОЛЬКО свое состояние!
"""

def names():
    all_names = []

    def inner(name: str) -> list:
        all_names.append(name)
        return all_names

    return inner

if __name__ == '__main__':
    boys = names()
    girls = names()

    print("\n=== closures have no intersection")
    print("\n=== boys")
    print(boys('Vasya'))
    print(boys('Petya'))
    print(boys('Dimas'))

    print("\n=== girls")
    print(girls('Tanya'))
    print(girls('Sveta'))
    print(girls('Olyga'))