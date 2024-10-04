print("\n---Всё пустое и ничего не содержащее вернет False")
falsy = [None, False, 0, 0.0, [], {}, set(), tuple(), range(0), '']

for e in falsy:
    print(bool(e), end=" ")

print("\n---Экземпляр класса вернет True (если не менять внутреннюю логику)")


class Cat:
    pass


cat = Cat()
print(bool(cat))

print("\n---Как заставить экземпляр класса вернуть False?")


class Dog:
    def __len__(self):
        return 0


dog = Dog()
print(bool(dog))


print("\n---")