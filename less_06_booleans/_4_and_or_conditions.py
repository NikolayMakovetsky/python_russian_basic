"""
Операторы and и or
Операндами операторов and и or, как и в случае с not, могут быть объекты любых типов данных.
По аналогии с оператором not можно предположить,
что результатом работы логических операторов and и or также является значение True или False.
Однако на самом деле данные операторы возвращают один из своих операндов!!!
Какой именно — зависит от самого оператора.
"""

MAIN_RULE = "___'И' ЛОМАЕТСЯ НА ЛЖИ, A 'ИЛИ' ИЩЕТ ПРАВДУ___"
print(f"\n---{MAIN_RULE=}")

# И ЛОМАЕТСЯ НА ЛЖИ И ВОЗВРАЩАЕТ объект ЕСЛИ bool(объект)==False, ЛИБО ВОЗВРАЩАЕТ ПОСЛЕДНИЙ объект
# ИЛИ ИЩЕТ ПРАВДУ И ВОЗВРАЩАЕТ объект ЕСЛИ bool(объект)==True, ЛИБО ВОЗВРАЩАЕТ ПОСЛЕДНИЙ объект

print("\n---'И' возвращает x при bool(x)==False или последний x из списка сравнения")
print(None and 10)  # None
print(5 and 0.0)  # 0.0
print('beegeek' and {})  # {}
print([1, 2, 3] and [6, 9])  # [6,9]
print('habr' and 0 and {'one': 1})  # 0
print(10 and [6, 9] and [])  # []

print("\n---'ИЛИ' возвращает x при bool(x)==True или последний x из списка сравнения")
print(None or 0)  # 0
print(0 or 5)  # 5
print('beegeek' or None)  # beegeek
print([1, 2, 3] or [6, 9])  # [1, 2, 3]
print(1 or 'beegeek' or None)  # 1
print(0.0 or 'habr' or {'one': 1})  # habr
print(0 or '' or [6, 9])  # [6, 9]
print(0 or '' or [])  # []
print(0 or '' or [] or {})  # {}


def check(x) -> bool:
    """Функция возвращающая True при x > 0, и False при x < 0"""
    print(f'{x}>0 is {bool(x > 0)}')
    return x > 0


print("\n---'И' ЛОМАЕТСЯ НА ЛЖИ, и внутрь не заходит!...check(0) == False ")
if check(1) and check(0) and check(2) and check(3):
    print('CONGRATULATIONS! THE DOOR IS OPEN. YOU ARE INSIDE.')
else:
    print("Checking was stopped...")

print("\n---'И' ЛОМАЕТСЯ НА ЛЖИ, и внутрь не заходит!...все условия == True ")
if check(1) and check(5) and check(2) and check(3):  # YES
    print('CONGRATULATIONS! THE DOOR IS OPEN. YOU ARE INSIDE.')
else:
    print("Checking was stopped...")

print("\n---'ИЛИ' ИЩЕТ ПРАВДУ, и найдя её заходит внутрь!...check(5) == True ")
if check(-1) or check(5) or check(-2) or check(-3):  # YES
    print('CONGRATULATIONS! THE DOOR IS OPEN. YOU ARE INSIDE.')
else:
    print("Checking was stopped...")

print("\n---'ИЛИ' ИЩЕТ ПРАВДУ, и найдя её заходит внутрь!...все условия == False ")
if check(-1) or check(-5) or check(-2) or check(-3):  # YES
    print('CONGRATULATIONS! THE DOOR IS OPEN. YOU ARE INSIDE.')
else:
    print("Checking was stopped...")
