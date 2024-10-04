## Imports in Python

### Absolute import (full path to module)
We write full path to the function from the root of our project

ex1: ```from less_03_imports.utils import multi```

It's a good way of import!
However if after that we replace our files to module, that is situated deep inside our project,
the length of import string will be too long. That isn't useful.

ex2: ```from less_03_imports.second.third.utils import multi```

### Relative import
If we replace our two modules together then we don't need to change them inside.
Everything will work.

ex.3: ```from .utils import multi```

```
The problem:
Traceback (most recent call last):
  File "C:\DISK_D\_17_python_russian_basic\less_03_imports\works.py", line 21, in <module>
    from .utils import multi
ImportError: attempted relative import with no known parent package
```

Why did we get this result?

In a row: //```if __name__ == '__main__':```// current module takes name '__main__' and after that
it already doesn't know the package name where it saved.

How to fix this problem?
1. Use ABSOLUTE IMPORT IN runner.py OR main.py as an entry point of our program. ```[BEST]```
2. Temporarily set ```__package__``` var to make it possible to debug current file using // if __name__ == '__main__'://

ex.4: ```__package__ = 'less_03_imports.second.third'  # just for testing```
'''
