print("\n---if")

# Bad code
# if x == True and y == True:
#     pass

x, y = 1, 1
if x and y:  # if bool(x) and bool(y):
    print(x, y)

print("\n---Truthy, Falsy value (beginners mistake)")
word = 'NO'
if word == 'YES' or 'yes' or 'Yes':  # Каждая часть условия проверяется по частям (Truthy, Falsy value)
    print('YES')
else:
    print('NO')

print("\n---Truthy, Falsy value (let's fix it)")
word = 'NO'
if word == 'YES' or word == 'yes' or word == 'Yes':
    print('YES')
else:
    print('NO')

print("\n---Truthy, Falsy value (best variant)")
word = 'NO'
if word in ('YES', 'yes', 'Yes'):
    print('YES')
else:
    print('NO')
