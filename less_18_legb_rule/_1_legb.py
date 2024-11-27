# LEGB - rule  (Порядок поиска интерпретатором переменных)
# L - local
# E - enclosed
# G - global
# B - builtins

import builtins

builtins.scope = 'builtins'  # Так лучше не писать, это для демонстрации

# scope = 'global'

def outer():
    # scope = 'enclosed'

    def inner():
        # scope = 'local'
        print(scope)

    inner()

if __name__ == '__main__':
    outer()  # 'local'
             # if we will comment line with scope = 'local' the result will be 'enclosed'
             # if we will comment line with scope = 'enclosed' the result will be 'global'
             # if we will comment line with scope = 'global' the result will be 'builtins'
             # if we will comment line with scope = 'builtins' the result will be NameError!