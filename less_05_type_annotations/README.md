### Польза аннотаций:

1. Код становится читабельнее и понятнее
2. PyCharm нам подскажет заранее о возможных ошибках и проблемах
3. Если мы используем библиотеку ```mypy``` мы можем увидеть где мы что неправильно передаем в программе

Зачастую функции, которые мы используем в программе находятся где-то глубоко, и просто импортируются в наш проект. Мы этих функций не видим, но пользуемся ими. Благодаря аннотациям PyCharm подсказывает нам, если мы пытаемся передать в функцию значение не того типа, или хотим выполнить с результатом выполнения функции недопустимое действие.

```
ВАЖНО !!! Все аннотации типов это только РЕКОМЕНДАЦИИ И ПОДСКАЗКИ
НИЧТО НЕ ПОМЕШАЕТ ВАМ ЗАПУСТИТЬ КОД И ПЕРЕДАТЬ НЕВЕРНЫЕ АРГУМЕНТЫ
```
Если функция ничего не возвращает, то не нужно писать ```-> None:```
Это и так понятно. Писать так, излишне:

```def calc(a: int, b: int) -> None:```

mypy — это инструмент для проверки типов во время компиляции для Python.
Он анализирует код по аннотациям типов и выявляет потенциальные ошибки.

Установка mypy происходит через pip:

```pip install mypy```

Запустить инструмент можно по команде:

```python -m mypy <путь до файла или директории>```

Использование подсказок типов в сочетании с mypy может помочь уменьшить количество ошибок, возникающих из-за неправильного использования функций, методов и классов. Также полезно добавить mypy в конвейер CI (конвейер непрерывной интеграции), чтобы проверять типизацию перед слиянием или развёртыванием кода.