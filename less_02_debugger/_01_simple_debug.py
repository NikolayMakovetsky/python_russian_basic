
'''
Ошибка при вводе нуля:
Traceback (most recent call last):
  File "C:\DISK_D\_17_python_russian_basic\less_02_debugger\_01_simple_debug.py", line 10, in <module>
    print(get(val).upper())
AttributeError: 'NoneType' object has no attribute 'upper'
'''

def get(value):
    if value > 0:
        return "Positive"
    if value < 0:
        return "Negative"


if __name__ == '__main__':
    val = int(input("Input number: "))
    print(get(val).upper())

