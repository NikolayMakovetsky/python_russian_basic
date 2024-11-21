squares = [e * e for e in range(10) if e % 2 == 0]  # фильтрация и преобразование


squares2 = []
for e in range(10):
    if e % 2 == 0:
        squares2.append(e * e)


text = 'hello world'
words = [word.capitalize() for word in text.split()]  # только преобразование

ints = [-1, -2, 0, 3, -4]
positives = [e for e in ints if e > 0]  # только фильтрация

if __name__ == '__main__':
    print("=== squares")
    print(squares)
    print(squares2)

    print("=== words")
    print(words)

    print("=== positives")
    print(positives)
