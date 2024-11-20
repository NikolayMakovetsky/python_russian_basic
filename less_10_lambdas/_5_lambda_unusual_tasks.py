"""
Task 1:
Как с помощью lambda-функции и рекурсии написать факториал?
(Обычные функции использовать нельзя)

Task 2:
Как реализовать for или while циклы при помощи lambda и рекурсии?

Task 3:
Как с помощью lambda написать конструкцию if, elif, else?
"""

if __name__ == '__main__':
    print("=== task 1")
    task1 = lambda x: 1 if x == 1 or x == 0 else x * task1(x - 1)
    print(f"0! = {task1(0)}")
    print(f"1! = {task1(1)}")
    print(f"2! = {task1(2)}")
    print(f"3! = {task1(3)}")
    print(f"4! = {task1(4)}")
    print(f"5! = {task1(5)}")

    print("=== task 2")
    task2 = lambda x, a: 0 if x == 0 else a + task2(x - 1, a)
    print(task2(5, 5))
    print(task2(9, 9))

    print("=== task 3")
    task3 = lambda x: "x > 5" if x > 5 else ("x < 0" if x < 0 else "0 < x < 5")
    print(task3(-3))
    print(task3(3))
    print(task3(10))
