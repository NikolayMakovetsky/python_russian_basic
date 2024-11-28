"""
Механизм замыкания позволяет работать с состоянием объекта
без прибегания к global, что бывает принципиально
"""

def average():
    values = []

    def inner(value: int) -> float:
        values.append(value)
        print("added value =", value, end=" / current result = ")
        return sum(values) / len(values)

    return inner


if __name__ == '__main__':
    avg = average()

    print("\n=== fing average")
    print(avg(10))
    print(avg(20))
    print(avg(30))

