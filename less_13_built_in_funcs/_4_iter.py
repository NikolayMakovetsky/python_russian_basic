class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat({self.name=}, {self.age=})"


words = ['sdf', 'hg', 'cvb', 'NONE', 'www']
idx = -1


def get_word():
    global words
    global idx
    if idx == len(words):
        return "NONE"
    idx += 1
    return words[idx]


if __name__ == '__main__':
    cats = [Cat('Tom', 3), Cat('Angela', 4), Cat('Bob', 5)]
    for cat in iter(cats):
        print(cat)

    # print("=== ввод пользователем пока он что-то не введет")
    # print("Введите слово (end - выход):")
    # for word in iter(input, 'end'):
    #     print(word.upper())

    print("===")
    for word in iter(get_word, 'NONE'):
        print(word)
    # iter запрашивает функцию без параметров
    # пока ее результат не будет -> 'NONE'
    # def iter(source, sentinel=None), sentinel - ограничитель
